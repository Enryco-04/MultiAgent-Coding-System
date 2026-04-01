"""
services/docker_runner.py
--------------------------
Triggers test execution inside the already-running `java_tester` container.
Waits for run_tests.sh to finish, then asks WorkspaceManager to parse the
plain-text result files.
"""

import subprocess
import time


class DockerRunner:
    CONTAINER = "java_tester"
    TIMEOUT   = 120   

    def run(
        self,
        iteration: int,
        impl_class: str,
        test_class: str,
        workspace,
    ) -> dict:
        iter_dir = workspace.iteration_relpath(iteration)

        # Remove stale files from any previous attempt at this slot
        workspace.clear_result(iteration)

        cmd = [
            "docker", "exec", self.CONTAINER,
            "/app/run_tests.sh",
            iter_dir,
            impl_class,
            test_class,
        ]

        print(f"  [docker] exec: {' '.join(cmd)}")
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=self.TIMEOUT)

        if proc.stdout.strip():
            print(f"  {proc.stdout.strip()}")
        if proc.stderr.strip():
            print(f"  [docker stderr] {proc.stderr.strip()}")

        # Give the container a moment to flush writes to the volume
        time.sleep(0.3)

        result = workspace.read_result(iteration)
        if result is None:
            return {
                "success":        False,
                "compile_ok":     False,
                "compile_errors": f"No output files from container.\nstdout: {proc.stdout}\nstderr: {proc.stderr}",
                "tests_run":      0,
                "tests_passed":   0,
                "tests_failed":   0,
                "failures":       [],
                "raw_output":     proc.stdout + proc.stderr,
            }

        return result
