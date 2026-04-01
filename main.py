"""
main.py
-------
Entry point. Runs all problems through the evaluation pipeline.

Usage:
  python main.py                      # run all problems
  python main.py sliding_window_max   # run one problem by id

Environment variables (set in .env):
  OPENAI_API_KEY   - required for CodexClient
  SONAR_TOKEN      - required for SonarQube
  SONAR_PROJECT_KEY
  SONAR_HOST_URL   - default http://localhost:9000
"""

import os
import re
import sys
import json
from dotenv import load_dotenv

load_dotenv(override=True)

from config.llm_client           import OllamaClient, CodexClient         # swap to OllamaClient for local dev
from llm_agent.coder             import CoderAgent
from llm_agent.analyzer          import AnalyzerAgent
from services.workspace_manager  import WorkspaceManager
from services.docker_runner       import DockerRunner
from services.sonar_service       import SonarService
from orchestrator.loop            import EvaluationLoop
from problems.problem_bank        import PROBLEMS, get_problem


def _format_detailed_results(results: list[dict]) -> list[dict]:
    detailed = []
    for r in results:
        iterations = []
        for a in r.get("attempt_history", []):
            jr = a.get("junit") or {}
            passed = jr.get("tests_passed", 0)
            run = jr.get("tests_run", 0)
            iterations.append(
                {
                    "iterazione": a.get("iteration"),
                    "stato": a.get("status"),
                    "test_passati": f"{passed}/{run}",
                    "test_totali": run,
                    "test_falliti_numero": jr.get("tests_failed", 0),
                    "quali_test_sono_falliti": jr.get("failures_with_values", []),
                    "compile_ok": jr.get("compile_ok", False),
                    "compile_errors": jr.get("compile_errors"),
                    "sonar_metrics": a.get("sonar_metrics", {}),
                    "sonar_issue_count": len(a.get("sonar_issues", [])),
                    "sonar_issues": a.get("sonar_issues", []),
                    "analyzer_hints": a.get("analyzer_hints"),
                }
            )

        final_jr = r.get("junit_result") or {}
        detailed.append(
            {
                "problema": r.get("problem_id"),
                "titolo": r.get("title"),
                "stato_finale": r.get("status"),
                "migliore_iterazione": r.get("attempts"),
                "miglior_test_passati": f"{final_jr.get('tests_passed', 0)}/{final_jr.get('tests_run', 0)}",
                "iterazioni": iterations,
                "sonar_metrics_finali": r.get("sonar_metrics", {}),
                "sonar_issue_count_finale": len(r.get("sonar_issues", [])),
                "sonar_issues_finali": r.get("sonar_issues", []),
            }
        )
    return detailed


def build_components():
    llm = CodexClient(model="gpt-5-nano")

    coder    = CoderAgent(llm)
    analyzer = AnalyzerAgent(llm)
    workspace = WorkspaceManager(base_dir="workspace")
    runner   = DockerRunner()

    sonar = None
    token = os.getenv("SONAR_TOKEN")
    key   = os.getenv("SONAR_PROJECT_KEY")
    host  = os.getenv("SONAR_HOST_URL", "http://localhost:9000")
    if token and key:
        sonar = SonarService(token=token, project_key=key, host=host)

    loop = EvaluationLoop(coder, analyzer, workspace, runner, sonar)
    return loop


def main():
    loop = build_components()

    # Which problems to run
    if len(sys.argv) > 1:
        problems = [get_problem(pid) for pid in sys.argv[1:]]
    else:
        problems = PROBLEMS

    results = []
    for problem in problems:
        result = loop.run(problem)
        results.append(result)

    # ── Summary ──────────────────────────────────────────────────────────────
    print("\n\n" + "═"*60)
    print("  SUMMARY")
    print("═"*60)
    for r in results:
        icon = "✅" if r["status"] == "PASS" else "❌"
        jr   = r.get("junit_result") or {}
        p    = jr.get("tests_passed", 0)
        t    = jr.get("tests_run",    0)
        print(f"{icon}  [{r['status']:4}]  {r['title']:<35}  {p}/{t} tests  (attempt {r['attempts']})")

    # Save full results — strip ANSI escape codes from raw_output so the
    # JSON is human-readable and doesn't break some parsers.
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')

    def _clean(obj):
        if isinstance(obj, str):
            return ansi_escape.sub('', obj)
        if isinstance(obj, dict):
            return {k: _clean(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [_clean(v) for v in obj]
        return obj

    with open("results.json", "w", encoding="utf-8") as f:
        clean_results = [{k: _clean(v) for k, v in r.items() if k != "final_code"} for r in results]
        detailed = _format_detailed_results(clean_results)
        json.dump(detailed, f, indent=2, ensure_ascii=False)
    print("\nFull results saved to results.json")


if __name__ == "__main__":
    main()
