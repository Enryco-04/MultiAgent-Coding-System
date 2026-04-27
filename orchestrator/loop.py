"""
orchestrator/loop.py
--------------------
Evaluation loop for a single problem plus the current project runtime.
"""

import json
import os
import re
import uuid

from dotenv import load_dotenv

from config.llm_client import CodexClient
from llm_agent.analyzer import AnalyzerAgent
from llm_agent.coder import CoderAgent
from problems.problem_bank import PROBLEMS, get_problem
from services.docker_runner import DockerRunner
from services.sonar_service import SonarService
from services.workspace_manager import WorkspaceManager

MAX_ITER = 5
SONAR_MAX_BUGS = 0
SONAR_MAX_CODE_SMELLS = 3
SONAR_MAX_COMPLEXITY = 999999
SONAR_MAX_COGNITIVE_COMPLEXITY = 25


def _format_detailed_results(results: list[dict]) -> list[dict]:
    """Convert raw loop output into a compact JSON shape."""
    detailed = []
    for result in results:
        iterations = []
        for attempt in result.get("attempt_history", []):
            junit_result = attempt.get("junit") or {}
            passed = junit_result.get("tests_passed", 0)
            run = junit_result.get("tests_run", 0)
            iterations.append(
                {
                    "attempt": attempt.get("iteration"),
                    "passrate": f"{passed}/{run}",
                    "tests_failed": junit_result.get("failures_with_values", []),
                    "sonar_metrics": attempt.get("sonar_metrics", {}),
                }
            )

        detailed.append(
            {
                "problem_id": result.get("problem_id"),
                "attempts": iterations,
            }
        )
    return detailed


def build_components() -> "EvaluationLoop":
    """Build and wire all runtime components for the current evaluation flow."""
    load_dotenv(override=True)

    llm = CodexClient(model="gpt-5-nano")
    coder = CoderAgent(llm)
    analyzer = AnalyzerAgent(llm)
    workspace = WorkspaceManager(base_dir="workspace")
    runner = DockerRunner()

    sonar = None
    token = os.getenv("SONAR_TOKEN")
    key = os.getenv("SONAR_PROJECT_KEY")
    host = os.getenv("SONAR_HOST_URL", "http://localhost:9000")
    if token and key:
        sonar = SonarService(token=token, project_key=key, docker_runner=runner, host=host)

    return EvaluationLoop(coder, analyzer, workspace, runner, sonar)


def resolve_problems(problem_ids: list[str]) -> list[dict]:
    """Resolve CLI problem ids, or return the whole bank when none are provided."""
    if problem_ids:
        return [get_problem(problem_id) for problem_id in problem_ids]
    return PROBLEMS


def print_summary(results: list[dict]):
    """Print a compact summary for all executed problems."""
    print("\n\n" + "=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    for result in results:
        junit_result = result.get("junit_result") or {}
        passed = junit_result.get("tests_passed", 0)
        total = junit_result.get("tests_run", 0)
        print(
            f"[{result['status']:4}]  {result['title']:<35}  "
            f"{passed}/{total} tests  (attempt {result['attempts']})"
        )


def save_results(results: list[dict], output_path: str = "results.json"):
    """Persist a cleaned, compact JSON report for post-run analysis."""
    ansi_escape = re.compile(r"\x1b\[[0-9;]*m")

    def _clean(value):
        if isinstance(value, str):
            return ansi_escape.sub("", value)
        if isinstance(value, dict):
            return {key: _clean(item) for key, item in value.items()}
        if isinstance(value, list):
            return [_clean(item) for item in value]
        return value

    with open(output_path, "w", encoding="utf-8") as file_handle:
        clean_results = [
            {key: _clean(value) for key, value in result.items() if key != "final_code"}
            for result in results
        ]
        json.dump(_format_detailed_results(clean_results), file_handle, indent=2, ensure_ascii=False)

    print(f"\nFull results saved to {output_path}")


def run_normal_mode(problem_ids: list[str] | None = None) -> list[dict]:
    """Run the current project workflow."""
    loop = build_components()
    problems = resolve_problems(problem_ids or [])

    results = []
    for problem in problems:
        results.append(loop.run(problem))

    print_summary(results)
    save_results(results)
    return results


def run_future_mode(args: list[str] | None = None):
    """
    Reserved entrypoint for the future version of the project.

    The selector already supports this mode, but its implementation is still
    intentionally left for the next update.
    """
    if args:
        print(f"[future-mode] received args: {args}")
    print("[future-mode] This mode is reserved for the next project update.")
    return None


class EvaluationLoop:
    def __init__(self, coder, analyzer, workspace, runner, sonar=None):
        self.coder = coder
        self.analyzer = analyzer
        self.workspace = workspace
        self.runner = runner
        self.sonar = sonar
        self._run_nonce = uuid.uuid4().hex[:8]

    def run(self, problem: dict) -> dict:
        pid = problem["id"]
        title = problem["title"]
        impl_class = problem["class_name"]
        test_class = impl_class + "Test"

        self.workspace.set_problem(pid)

        print(f"\n{'-' * 60}")
        print(f"  Problem: {title}  ({pid})")
        print(f"{'-' * 60}")

        hints = None
        last_code = None
        best_result = None
        best_iter = 1
        final_sonar_metrics = {}
        final_sonar_issues = []
        stall_count = 0
        attempt_history = []

        for attempt in range(1, MAX_ITER + 1):
            print(f"\n  -- Attempt {attempt}/{MAX_ITER} --")
            attempt_entry = {
                "iteration": attempt,
                "status": "",
                "junit": None,
                "sonar_metrics": {},
                "sonar_issues": [],
                "analyzer_hints": None,
            }

            try:
                generation = self.coder.code_with_test(
                    problem,
                    hints=hints,
                    previous_code=last_code,
                )
            except ValueError as exc:
                print(f"  [coder] format error: {exc}")
                hints = (
                    f"Your response format was wrong: {exc}. "
                    "Return strict JSON with a single field: java_code."
                )
                attempt_entry["status"] = "CODER_FORMAT_ERROR"
                attempt_entry["analyzer_hints"] = hints
                attempt_history.append(attempt_entry)
                continue

            new_code = generation["code"]
            if new_code.strip() == (last_code or "").strip():
                stall_count += 1
                print(f"  [loop] stall ({stall_count})")
            else:
                stall_count = 0

            last_code = new_code
            print(f"  [coder] generated {generation['filename']}.java ({len(last_code)} chars)")

            self.workspace.write_java(last_code, impl_class, attempt)
            self.workspace.write_java(problem["junit_test"], test_class, attempt)

            result = self.runner.run_java_tester(attempt, impl_class, test_class, self.workspace)
            attempt_entry["junit"] = {
                "compile_ok": result.get("compile_ok", False),
                "compile_errors": result.get("compile_errors"),
                "tests_run": result.get("tests_run", 0),
                "tests_passed": result.get("tests_passed", 0),
                "tests_failed": result.get("tests_failed", 0),
                "failures_with_values": result.get("failures_with_values", []),
                "success": result.get("success", False),
                "raw_output": result.get("raw_output", ""),
            }

            if not result["compile_ok"]:
                print("  [junit] COMPILE FAILED")
                print(f"  {result['compile_errors'][:400]}")
                if attempt < MAX_ITER:
                    hints = self.analyzer.analyze_compile_errors(last_code, result["compile_errors"])
                else:
                    hints = None
                attempt_entry["status"] = "COMPILE_FAILED"
                attempt_entry["analyzer_hints"] = hints
                attempt_history.append(attempt_entry)
                continue

            passed = result["tests_passed"]
            total = result["tests_run"]
            failed = result["tests_failed"]
            print(f"  [junit] {passed}/{total} passed, {failed} failed")

            failures = result["failures_with_values"]
            if failures:
                print("  [junit] failures:")
                for line in failures:
                    print(f"    x {line}")

            if best_result is None or passed > best_result["tests_passed"]:
                best_result = result
                best_iter = attempt

            if not result["success"]:
                if attempt < MAX_ITER:
                    hints = self.analyzer.analyze_test_failures(last_code, failures)
                else:
                    hints = None
                attempt_entry["status"] = "TESTS_FAILED"
                attempt_entry["analyzer_hints"] = hints
                attempt_history.append(attempt_entry)
                continue

            print("  [junit] All JUnit tests passed")
            best_result = result
            best_iter = attempt

            if not self.sonar:
                attempt_entry["status"] = "PASS"
                attempt_history.append(attempt_entry)
                break

            sonar_component = self._build_sonar_component(pid, attempt)
            print(f"  [sonar] component_key={sonar_component}")
            sonar_metrics, sonar_issues = self._run_sonar(attempt, sonar_component)
            final_sonar_metrics = sonar_metrics
            final_sonar_issues = sonar_issues
            attempt_entry["sonar_metrics"] = sonar_metrics
            attempt_entry["sonar_issues"] = sonar_issues

            quality_ok, quality_reason = self._quality_ok(sonar_metrics)
            if quality_ok:
                print("  [sonar] quality OK")
                attempt_entry["status"] = "PASS"
                attempt_history.append(attempt_entry)
                break

            print(f"  [sonar] quality not met: {quality_reason}")
            attempt_entry["status"] = "SONAR_FAILED"
            if attempt < MAX_ITER:
                failed_metric = self._failed_metric_from_reason(quality_reason)
                filtered_issues = sonar_issues
                if failed_metric:
                    try:
                        filtered_issues = self.sonar.get_issues_for_metric(
                            failed_metric,
                            component=sonar_component,
                            in_new_code_period=False,
                        )
                        print(f"  [sonar] filtered issues for {failed_metric}: {len(filtered_issues)}")
                    except Exception as exc:
                        print(f"  [sonar] filtered issues fetch failed: {exc}")

                hints = self.analyzer.analyze_sonar(last_code, sonar_metrics, filtered_issues)
                print("  [analyzer] sonar hints generated")
                attempt_entry["analyzer_hints"] = hints
            attempt_history.append(attempt_entry)

        passed = best_result is not None and best_result.get("success", False)
        best_passed = best_result.get("tests_passed", 0) if best_result else 0
        best_total = best_result.get("tests_run", 0) if best_result else 0
        status_label = "PASS" if passed else "FAIL"
        print(f"\n  {status_label}  {best_passed}/{best_total} tests  (best at attempt {best_iter})")

        return {
            "problem_id": pid,
            "title": title,
            "status": "PASS" if passed else "FAIL",
            "attempts": best_iter,
            "attempt_history": attempt_history,
            "junit_result": best_result,
            "sonar_metrics": final_sonar_metrics,
            "sonar_issues": final_sonar_issues,
            "final_code": last_code,
        }

    def _run_sonar(self, iteration: int, component: str) -> tuple[dict, list]:
        iter_path = self.workspace.iteration_path(iteration)
        try:
            self.sonar.sonar_scan(iter_path, project_key=component)
            metrics = self.sonar.get_metrics(component=component)
            issues = self.sonar.get_issues(
                component=component,
                in_new_code_period=False,
                retries=8,
                retry_delay=2,
                retry_on_empty=True,
            )
            print(f"  [sonar] metrics: {metrics}")
            return metrics, issues
        except Exception as exc:
            print(f"  [sonar] scan failed: {exc}")
            return {}, []

    def _build_sonar_component(self, problem_id: str, iteration: int) -> str:
        if not self.sonar:
            return ""
        base = self.sonar.project_key
        sanitized = re.sub(r"[^a-zA-Z0-9_.:-]", "_", problem_id)
        return f"{base}_{sanitized}_it{iteration}_{self._run_nonce}"

    @staticmethod
    def _quality_ok(metrics: dict) -> tuple[bool, str]:
        bugs = int(metrics.get("bugs", 0))
        smells = int(metrics.get("code_smells", 0))
        complexity = int(metrics.get("complexity", 0))
        cognitive = int(metrics.get("cognitive_complexity", 0))
        if bugs > SONAR_MAX_BUGS:
            return False, f"bugs={bugs}"
        if smells > SONAR_MAX_CODE_SMELLS:
            return False, f"code_smells={smells}"
        if complexity > SONAR_MAX_COMPLEXITY and complexity > 0:
            return False, f"complexity={complexity}"
        if cognitive > SONAR_MAX_COGNITIVE_COMPLEXITY and cognitive > 0:
            return False, f"cognitive_complexity={cognitive}"
        return True, ""

    @staticmethod
    def _failed_metric_from_reason(reason: str) -> str | None:
        if not reason:
            return None
        metric = reason.split("=", 1)[0].strip().lower()
        if metric in {"bugs", "code_smells", "complexity", "cognitive_complexity"}:
            return metric
        return None
