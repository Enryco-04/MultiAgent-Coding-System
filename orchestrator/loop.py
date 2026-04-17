"""
orchestrator/loop.py
--------------------
Evaluation loop for a single problem.

Flow per attempt:
  compile fail → analyzer(code, errors)          → hints → coder
  junit fail   → analyzer(code, failures+values) → hints → coder
  junit pass   → sonar scan 
  sonar fail   → analyzer(code, metrics, issues) → hints → coder

"""

from llm_agent.coder            import CoderAgent
from llm_agent.analyzer         import AnalyzerAgent
from services.workspace_manager import WorkspaceManager
from services.docker_runner     import DockerRunner
from services.sonar_service     import SonarService
import re
import uuid

MAX_ITER             = 5
SONAR_MAX_BUGS        = 0
SONAR_MAX_CODE_SMELLS = 3
# Cyclomatic complexity todo

SONAR_MAX_COMPLEXITY  = 999999
#Variabile 
SONAR_MAX_COGNITIVE_COMPLEXITY = 25


class EvaluationLoop:
    def __init__(self, coder, analyzer, workspace, runner, sonar=None):
        # The loop orchestrates the collaboration:
        # coder produces code, analyzer produces repair hints, runner validates.
        self.coder     = coder
        self.analyzer  = analyzer
        self.workspace = workspace
        self.runner    = runner
        self.sonar     = sonar
        # Per-process nonce used to isolate Sonar projects across different runs.
        self._run_nonce = uuid.uuid4().hex[:8]

    def run(self, problem: dict) -> dict:
        pid        = problem["id"]
        title      = problem["title"]
        impl_class = problem["class_name"]
        test_class = impl_class + "Test"

        self.workspace.set_problem(pid)

        print(f"\n{'─'*60}")
        print(f"  Problem: {title}  ({pid})")
        print(f"{'─'*60}")

        # `hints`: analyzer feedback passed to coder at next attempt.
        hints       = None
        # `last_code`: most recent generated source for current problem.
        last_code   = None
        # `best_result`: best JUnit outcome seen so far (by passed tests).
        best_result = None
        best_iter   = 1
        final_sonar_metrics = {}
        final_sonar_issues  = []
        stall_count = 0
        # Full per-attempt trace persisted into results.json for later analysis.
        attempt_history = []

        #Loop entry point
        for attempt in range(1, MAX_ITER + 1):
            print(f"\n  ── Attempt {attempt}/{MAX_ITER} ──")
            # Attempt-local record (later appended to attempt_history).
            attempt_entry = {
                "iteration": attempt,
                "status": "",
                "junit": None,
                "sonar_metrics": {},
                "sonar_issues": [],
                "analyzer_hints": None,
            }

            # ── Step 1: generate code ─────────────────────────────────────────
            try:
                gen = self.coder.code_with_test(
                    problem,
                    hints=hints, # will be None at the first iteration
                    previous_code=last_code, # will be none at the first iteraction
                )
            except ValueError as exc:
                print(f"  [coder] format error: {exc}")
                # If we get formatting errors, we ask for strict JSON again.
                hints = (
                    f"Your response format was wrong: {exc}. "
                    "Return strict JSON with a single field: java_code."
                )
                attempt_entry["status"] = "CODER_FORMAT_ERROR"
                attempt_entry["analyzer_hints"] = hints
                attempt_history.append(attempt_entry)
                continue

            new_code = gen["code"]
            if new_code.strip() == (last_code or "").strip():
                stall_count += 1
                
                print(f"  [loop] stall ({stall_count})")
                # NOTE: stalling means the model repeated almost identical code.
                # This is legacy as it does not happen with longer solutions, but still needed


            else:
                stall_count = 0
            last_code = new_code
            print(f"  [coder] generated {gen['filename']}.java ({len(last_code)} chars)")

            # ── Step 2: write sources ─────────────────────────────────────────
            self.workspace.write_java(last_code,             impl_class, attempt)
            self.workspace.write_java(problem["junit_test"], test_class,  attempt)

            # ── Step 3: compile + run ─────────────────────────────────────────
            result = self.runner.run(attempt, impl_class, test_class, self.workspace)
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

            # ── Step 4: compile failure ───────────────────────────────────────
            if not result["compile_ok"]:
                print(f"  [junit] COMPILE FAILED")
                print(f"  {result['compile_errors'][:400]}")
                if attempt < MAX_ITER:
                    # Generate actionable guidance only if another retry exists.
                    hints = self.analyzer.analyze_compile_errors(
                        last_code, result["compile_errors"]
                    )
                else:
                    # Last attempt: skip analyzer to avoid unnecessary token usage.
                    hints = None
                attempt_entry["status"] = "COMPILE_FAILED"
                attempt_entry["analyzer_hints"] = hints
                attempt_history.append(attempt_entry)
                continue

            # ── Step 5: JUnit results ─────────────────────────────────────────
            p = result["tests_passed"]
            t = result["tests_run"]
            f = result["tests_failed"]
            print(f"  [junit] {p}/{t} passed, {f} failed")

            failures = result["failures_with_values"]
            if failures:
                print("  [junit] failures:")
                for line in failures:
                    print(f"    ✘ {line}")

            if best_result is None or p > best_result["tests_passed"]:
                best_result = result
                best_iter   = attempt

            if not result["success"]:
                if attempt < MAX_ITER:
                    # Generate test-failure diagnosis only if we can still retry.
                    hints = self.analyzer.analyze_test_failures(last_code, failures)
                else:
                    # Last attempt: skip analyzer to avoid unnecessary token usage.
                    hints = None
                attempt_entry["status"] = "TESTS_FAILED"
                attempt_entry["analyzer_hints"] = hints
                attempt_history.append(attempt_entry)
                continue

            # ── All tests passed ──────────────────────────────────────────────
            print(f"  ✅  All JUnit tests passed")
            best_result = result
            best_iter   = attempt

            if not self.sonar:
                # Sonar is optional: if disabled, green JUnit is enough to stop.
                attempt_entry["status"] = "PASS"
                attempt_history.append(attempt_entry)
                break

            # Sonar project key is unique per (problem, attempt, run),
            # so metrics/issues refer to this exact iteration only.
            sonar_component = self._build_sonar_component(pid, attempt)
            print(f"  [DEBUG][sonar] component_key={sonar_component}")
            sonar_metrics, sonar_issues = self._run_sonar(attempt, sonar_component)
            final_sonar_metrics = sonar_metrics
            final_sonar_issues  = sonar_issues
            attempt_entry["sonar_metrics"] = sonar_metrics
            attempt_entry["sonar_issues"] = sonar_issues
            print(
                f"  [DEBUG][sonar] attempt={attempt} "
                f"metrics={sonar_metrics} issues_count={len(sonar_issues)}"
            )

            quality_ok, quality_reason = self._quality_ok(sonar_metrics)
            if quality_ok:
                print(f"  ✅  Sonar quality OK")
                attempt_entry["status"] = "PASS"
                attempt_history.append(attempt_entry)
                break

            # Sonar failed: keep this attempt and (if possible) prepare hints.
            print(f"  [sonar] quality not met: {quality_reason}")
            attempt_entry["status"] = "SONAR_FAILED"
            if attempt < MAX_ITER:
                # Focus analyzer on the specific metric that violated the threshold.
                failed_metric = self._failed_metric_from_reason(quality_reason)
                filtered_issues = sonar_issues
                print(
                    f"  [DEBUG][sonar] quality_reason={quality_reason} "
                    f"failed_metric={failed_metric}"
                )
                if failed_metric:
                    try:
                        # Pull metric-specific issues (e.g., BUG / CODE_SMELL).
                        filtered_issues = self.sonar.get_issues_for_metric(
                            failed_metric,
                            component=sonar_component,
                            in_new_code_period=False,
                        )
                        print(
                            f"  [sonar] filtered issues for {failed_metric}: "
                            f"{len(filtered_issues)}"
                        )
                    except Exception as exc:
                        print(f"  [sonar] filtered issues fetch failed: {exc}")

                preview = [
                    {
                        "type": i.get("type", "?"),
                        "severity": i.get("severity", "?"),
                        "line": i.get("line", "?"),
                        "message": i.get("message", "?"),
                    }
                    for i in filtered_issues[:3]
                ]
                print(
                    f"  [DEBUG][sonar] analyzer_payload "
                    f"issues_count={len(filtered_issues)} preview={preview}"
                )
                # Analyzer receives code + metrics + focused issues.
                hints = self.analyzer.analyze_sonar(last_code, sonar_metrics, filtered_issues)
                print(f"  [analyzer] sonar hints generated")
                attempt_entry["analyzer_hints"] = hints
            attempt_history.append(attempt_entry)

        # ── Final summary ─────────────────────────────────────────────────────
        passed = best_result is not None and best_result.get("success", False)
        bp = best_result.get("tests_passed", 0) if best_result else 0
        bt = best_result.get("tests_run",    0) if best_result else 0
        print(f"\n  {'✅ PASS' if passed else '❌ FAIL'}  {bp}/{bt} tests  (best at attempt {best_iter})")

        return {
            "problem_id":    pid,
            "title":         title,
            "status":        "PASS" if passed else "FAIL",
            "attempts":      best_iter,
            "attempt_history": attempt_history,
            "junit_result":  best_result,
            "sonar_metrics": final_sonar_metrics,
            "sonar_issues":  final_sonar_issues,
            "final_code":    last_code,
        }

    def _run_sonar(self, iteration: int, component: str) -> tuple[dict, list]:
        # Run scanner and read metrics/issues for a specific component key.
        iter_path = self.workspace.iteration_path(iteration)
        try:
            self.sonar.scan(iter_path, iteration, project_key=component)
            metrics = self.sonar.get_metrics(component=component)
            issues  = self.sonar.get_issues(
                component=component,
                in_new_code_period=False,
                # Retry because Sonar issues may appear a few seconds after metrics.
                retries=8,
                retry_delay=2,
                retry_on_empty=True,
            )
            print(f"  [sonar] metrics: {metrics}")
            print(f"  [DEBUG][sonar] _run_sonar fetched issues_count={len(issues)}")
            return metrics, issues
        except Exception as exc:
            print(f"  [sonar] scan failed: {exc}")
            return {}, []

    def _build_sonar_component(self, problem_id: str, iteration: int) -> str:
        # Compose a Sonar key safe for API usage and unique for this iteration.
        if not self.sonar:
            return ""
        base = self.sonar.project_key
        sanitized = re.sub(r"[^a-zA-Z0-9_.:-]", "_", problem_id)
        return f"{base}_{sanitized}_it{iteration}_{self._run_nonce}"

    @staticmethod
    def _quality_ok(metrics: dict) -> tuple[bool, str]:
        # Quality gate used by the loop.
        bugs       = int(metrics.get("bugs",        0))
        smells     = int(metrics.get("code_smells", 0))
        complexity = int(metrics.get("complexity",  0))
        cognitive  = int(metrics.get("cognitive_complexity", 0))
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
