"""
services/docker_runner.py
-------------------------
Owns Docker command execution for the project:
  - runs JUnit inside the already-running `java_tester` container
  - runs the Sonar scanner container when requested by SonarService
"""

import os
import subprocess
import time


class DockerRunner:
    JAVA_TESTER_CONTAINER = "java_tester"
    SONAR_CONTAINER = "sonarsource/sonar-scanner-cli"
    TIMEOUT = 120
    SONAR_TIMEOUT = 120

    def run_command(self, cmd: list[str], timeout: int | None = None) -> subprocess.CompletedProcess:
        """Execute one Docker command and return the completed process."""
        return subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout or self.TIMEOUT,
        )

    def run_java_tester(
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
            "docker", "exec", self.JAVA_TESTER_CONTAINER,
            "/app/run_tests.sh",
            iter_dir,
            impl_class,
            test_class,
        ]

        print(f"  [docker] exec: {' '.join(cmd)}")
        proc = self.run_command(cmd, timeout=self.TIMEOUT)

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

    def run_sonar_scanner(self, source_folder: str, project_key: str, token: str) -> subprocess.CompletedProcess:
        """Run sonar-scanner-cli in Docker for one source folder."""
        abs_folder = os.path.abspath(source_folder)
        cmd = [
            "docker", "run", "--rm",
            "-v", f"{abs_folder}:/usr/src",
            self.SONAR_CONTAINER,
            f"-Dsonar.projectKey={project_key}",
            "-Dsonar.sources=/usr/src",
            "-Dsonar.java.binaries=/usr/src/bin",
            "-Dsonar.host.url=http://host.docker.internal:9000",
            f"-Dsonar.login={token}",
            "-Dsonar.scm.disabled=true",
            "-Dsonar.exclusions=**/*Test.java",
            "-Dsonar.issue.ignore.multicriteria=e1",
            "-Dsonar.issue.ignore.multicriteria.e1.ruleKey=java:S1220",
            "-Dsonar.issue.ignore.multicriteria.e1.resourceKey=**/*.java",
        ]
        print(f"  [docker] run: {' '.join(cmd)}")
        return self.run_command(cmd, timeout=self.SONAR_TIMEOUT)
