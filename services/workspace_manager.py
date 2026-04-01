"""
services/workspace_manager.py
------------------------------
Manages the shared workspace/ directory mounted into the tester container.

The container writes three plain-text files per iteration:
  compile_ok.txt   — "true" or "false"
  compile_out.txt  — raw javac output
  junit_out.txt    — raw JUnit ConsoleLauncher output

Failure parsing strategy:
  JUnit --details verbose emits one block per test method. Each block contains
  a "caught:" line with the full exception message when the test fails.
  We build a map of {method_name -> caught_message} in a single pass, then
  read the summary counts from the footer lines.
"""

import os
import re


class WorkspaceManager:
    def __init__(self, base_dir: str = "workspace"):
        self.base_dir = base_dir
        self.problem_id = None
        os.makedirs(self.base_dir, exist_ok=True)

    def set_problem(self, problem_id: str) -> None:
        self.problem_id = problem_id
        os.makedirs(self.problem_root(), exist_ok=True)

    def problem_root(self) -> str:
        if not self.problem_id:
            raise ValueError("Workspace problem_id is not set.")
        return os.path.join(self.base_dir, self.problem_id)

    def iteration_relpath(self, iteration: int) -> str:
        if not self.problem_id:
            raise ValueError("Workspace problem_id is not set.")
        return f"{self.problem_id}/iteration_{iteration}"

    def iteration_path(self, iteration: int) -> str:
        return os.path.join(self.base_dir, self.iteration_relpath(iteration))

    def create_iteration_folder(self, iteration: int) -> str:
        path = self.iteration_path(iteration)
        os.makedirs(path, exist_ok=True)
        return path

    def write_java(self, code: str, class_name: str, iteration: int) -> str:
        folder = self.create_iteration_folder(iteration)
        path   = os.path.join(folder, f"{class_name}.java")
        with open(path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"  [workspace] wrote {path}")
        return path

    def read_result(self, iteration: int) -> dict | None:
        folder          = self.iteration_path(iteration)
        compile_ok_path = os.path.join(folder, "compile_ok.txt")
        if not os.path.isfile(compile_ok_path):
            return None

        compile_ok  = open(compile_ok_path,  encoding="utf-8").read().strip() == "true"
        compile_out = open(os.path.join(folder, "compile_out.txt"), encoding="utf-8").read().strip()
        junit_path  = os.path.join(folder, "junit_out.txt")
        junit_out   = open(junit_path, encoding="utf-8").read() if os.path.isfile(junit_path) else ""

        if not compile_ok:
            return {
                "success":              False,
                "compile_ok":           False,
                "compile_errors":       compile_out,
                "tests_run":            0,
                "tests_passed":         0,
                "tests_failed":         0,
                "failures_with_values": [],
                "raw_output":           compile_out,
            }

        passed, failed, failures = self._parse_junit(junit_out)
        return {
            "success":              failed == 0 and (passed + failed) > 0,
            "compile_ok":           True,
            "compile_errors":       None,
            "tests_run":            passed + failed,
            "tests_passed":         passed,
            "tests_failed":         failed,
            "failures_with_values": failures,
            "raw_output":           junit_out,
        }

    def clear_result(self, iteration: int) -> None:
        folder = self.iteration_path(iteration)
        for name in ("compile_ok.txt", "compile_out.txt", "junit_out.txt"):
            path = os.path.join(folder, name)
            if os.path.isfile(path):\
                os.remove(path)

    @staticmethod
    def _parse_junit(output: str) -> tuple[int, int, list[str]]:
        """
        Parse JUnit ConsoleLauncher --details verbose output.

        The verbose format emits one block per test, each containing:
          │  ├─ methodName()
          │  │     source: MethodSource [... methodName ...]
          │  │     caught: <ExceptionClass>: <message>   ← only on failure
          │  │     status: ✔ SUCCESSFUL  |  ✘ FAILED

        Strategy: single-pass scan.  Track the "current method" whenever we
        see a source line, record the caught message if present, emit a
        failure entry whenever we see a ✘ status line.
        """
        # Strip ANSI escape codes so regex patterns are clean
        clean = re.sub(r'\x1b\[[0-9;]*m', '', output)

        # ── summary counts from footer ────────────────────────────────────────
        passed = 0
        failed = 0
        m = re.search(r'\[\s*(\d+)\s+tests?\s+successful', clean)
        if m:
            passed = int(m.group(1))
        m = re.search(r'\[\s*(\d+)\s+tests?\s+failed', clean)
        if m:
            failed = int(m.group(1))

        # ── per-test failure details ──────────────────────────────────────────
        failures      = []
        current_method = None
        current_caught = None

        for line in clean.splitlines():
            # "source: MethodSource [className = '...', methodName = 'foo', ...]"
            src = re.search(r'methodName\s*=\s*[\'"]?(\w+)[\'"]?', line)
            if src:
                current_method = src.group(1) + "()"
                current_caught = None
                continue

            # "caught: org.opentest4j.AssertionFailedError: expected: <3> but was: <-1>"
            caught = re.search(r'caught:\s*(.+)', line)
            if caught:
                msg = caught.group(1).strip()
                # shorten package-qualified exception names
                msg = re.sub(r'[\w.]+\.(\w+(?:Error|Exception)):', r'\1:', msg)
                current_caught = msg
                continue

            # "status: ✘ FAILED"
            if re.search(r'status:.*[✘✗]|status:.*FAIL', line):
                if current_method:
                    entry = current_method
                    if current_caught:
                        entry += ": " + current_caught
                    failures.append(entry)
                current_method = None
                current_caught = None

        return passed, failed, failures
