"""
services/sonar_service.py
--------------------------
SonarQube client. Restored to the approach that worked in the original project:
  - sonar-scanner-cli runs as a Docker container
  - Uses host.docker.internal:9000 to reach SonarQube on Windows Docker Desktop
  - Basic auth: auth=(token, "") — works with SonarQube lts-community
  - After scan: polls /api/ce/component until SUCCESS instead of fixed sleep
"""

import json
import os
import re
import subprocess
import time

import requests


METRIC_KEYS = [
    "ncloc",
    "functions",
    "complexity",
    "cognitive_complexity",
    "bugs",
    "vulnerabilities",
    "code_smells",
    "duplicated_lines_density",
]


class SonarService:
    def __init__(self, token: str, project_key: str, host: str = "http://localhost:9000"):
        self.token       = token
        self.project_key = project_key
        self.host        = host
        self.api         = f"{host}/api"

    # ── Scanner ───────────────────────────────────────────────────────────────

    def scan(self, source_folder: str, iteration: int, project_key: str | None = None) -> None:
        """
        Run sonar-scanner-cli as a Docker container — same approach as the
        original working code.  host.docker.internal resolves to the host
        machine on Windows Docker Desktop, reaching SonarQube at port 9000.
        """
        abs_folder = os.path.abspath(source_folder)
        effective_project_key = project_key or self.project_key
        token_preview = self.token[:8] + "..." if self.token else "(empty!)"
        print(
            f"  [sonar] scanning {abs_folder} "
            f"(project_key={effective_project_key}, token: {token_preview}) ..."
        )

        cmd = [
            "docker", "run", "--rm",
            "-v", f"{abs_folder}:/usr/src",
            "sonarsource/sonar-scanner-cli",
            f"-Dsonar.projectKey={effective_project_key}",
            "-Dsonar.sources=/usr/src",
            "-Dsonar.java.binaries=/usr/src/bin",
            "-Dsonar.host.url=http://host.docker.internal:9000",
            f"-Dsonar.login={self.token}",
            "-Dsonar.scm.disabled=true",
            "-Dsonar.exclusions=**/*Test.java",
            "-Dsonar.issue.ignore.multicriteria=e1",
            "-Dsonar.issue.ignore.multicriteria.e1.ruleKey=java:S1220",
            "-Dsonar.issue.ignore.multicriteria.e1.resourceKey=**/*.java",
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"  [sonar] stderr: {result.stderr[-600:]}")
            raise RuntimeError("SonarQube scan failed")

        print("  [sonar] scan submitted — waiting for background task...")
        self._wait_for_analysis(component=effective_project_key)
        self._wait_for_measures(component=effective_project_key)

    # ── Wait for background task ──────────────────────────────────────────────

    def _wait_for_analysis(
        self,
        component: str | None = None,
        timeout: int = 60,
        poll_interval: int = 3,
    ) -> None:
        """
        Poll /api/ce/component until the background task reports SUCCESS.
        More reliable than a fixed sleep — proceeds as soon as data is ready.
        """
        url     = f"{self.api}/ce/component"
        component_key = component or self.project_key
        params  = {"component": component_key}
        elapsed = 0

        while elapsed < timeout:
            time.sleep(poll_interval)
            elapsed += poll_interval
            try:
                resp   = requests.get(url, params=params,
                                      auth=(self.token, ""), timeout=10)
                resp.raise_for_status()
                status = resp.json().get("current", {}).get("status", "")
                print(f"  [sonar] task status: {status} ({elapsed}s)")
                if status == "SUCCESS":
                    return
                if status in ("FAILED", "CANCELED"):
                    raise RuntimeError(f"SonarQube background task {status}")
            except requests.exceptions.RequestException as e:
                print(f"  [sonar] poll error: {e}")

        print(f"  [sonar] warning: timed out after {timeout}s, fetching anyway")

    def _wait_for_measures(
        self,
        component: str | None = None,
        timeout: int = 15,
        poll_interval: int = 1,
    ) -> None:
        """
        After CE reports SUCCESS, SonarQube may still need a brief moment before
        measures are queryable with the latest values. Poll the measures API
        instead of relying on a fixed sleep.
        """
        elapsed = 0
        while elapsed < timeout:
            time.sleep(poll_interval)
            elapsed += poll_interval
            try:
                metrics = self.get_metrics(component=component)
                if metrics:
                    print(f"  [sonar] measures ready ({elapsed}s)")
                    return
            except requests.exceptions.RequestException as e:
                print(f"  [sonar] measures poll error: {e}")

        print(f"  [sonar] warning: measures not confirmed after {timeout}s")

    # ── Metrics ───────────────────────────────────────────────────────────────

    def get_metrics(self, component: str | None = None, retries: int = 3, retry_delay: int = 1) -> dict:
        component = component or self.project_key
        url    = f"{self.api}/measures/component"
        params = {"component": component, "metricKeys": ",".join(METRIC_KEYS)}
        last_error = None

        for attempt in range(1, retries + 1):
            try:
                resp = requests.get(url, params=params, auth=(self.token, ""), timeout=15)
                resp.raise_for_status()
                measures = resp.json().get("component", {}).get("measures", [])
                if measures:
                    return {m["metric"]: m.get("value", "N/A") for m in measures}
            except requests.exceptions.RequestException as e:
                last_error = e

            if attempt < retries:
                time.sleep(retry_delay)

        if last_error:
            raise last_error
        return {}

    # ── Issues ────────────────────────────────────────────────────────────────

    def get_issues(
        self,
        component: str | None = None,
        issue_types: list[str] | None = None,
        tags: list[str] | None = None,
        in_new_code_period: bool = False,
        page_size: int = 100,
        retries: int = 3,
        retry_delay: int = 1,
        retry_on_empty: bool = False,
    ) -> list:
        component = component or self.project_key
        url    = f"{self.api}/issues/search"
        params = {
            "componentKeys": component,
            "statuses":      "OPEN",
            "ps":            page_size,
        }
        if issue_types:
            params["types"] = ",".join(issue_types)
        if tags:
            params["tags"] = ",".join(tags)
        if in_new_code_period:
            params["inNewCodePeriod"] = "true"
        print(f"  [DEBUG][sonar] get_issues params={params}")

        last_error = None
        for attempt in range(1, retries + 1):
            try:
                resp = requests.get(url, params=params, auth=(self.token, ""), timeout=15)
                resp.raise_for_status()
                issues = resp.json().get("issues", [])
                print(
                    f"  [DEBUG][sonar] get_issues result_count={len(issues)} "
                    f"(attempt={attempt}/{retries})"
                )
                if issues or not retry_on_empty or attempt == retries:
                    return issues
            except requests.exceptions.RequestException as e:
                last_error = e
                print(f"  [sonar] issues poll error: {e}")

            if attempt < retries:
                time.sleep(retry_delay)

        if last_error:
            raise last_error
        return []

    def get_issues_for_metric(
        self,
        metric: str,
        component: str | None = None,
        in_new_code_period: bool = True,
    ) -> list:
        metric_name = (metric or "").strip().lower()
        print(
            f"  [DEBUG][sonar] get_issues_for_metric metric={metric_name} "
            f"in_new_code_period={in_new_code_period}"
        )
        if metric_name == "bugs":
            return self.get_issues(
                component=component,
                issue_types=["BUG"],
                in_new_code_period=in_new_code_period,
            )

        if metric_name == "code_smells":
            return self.get_issues(
                component=component,
                issue_types=["CODE_SMELL"],
                in_new_code_period=in_new_code_period,
            )

        if metric_name == "complexity":
            smells = self.get_issues(
                component=component,
                issue_types=["CODE_SMELL"],
                in_new_code_period=in_new_code_period,
            )
            # Sonar does not expose a dedicated "complexity issue type":
            # keep complexity-related smells when possible.
            focused = []
            for i in smells:
                text = " ".join(
                    str(i.get(k, "")) for k in ("message", "rule", "cleanCodeAttribute")
                ).lower()
                if "complex" in text or "cognitive" in text:
                    focused.append(i)
            return focused or smells

        return self.get_issues(component=component, in_new_code_period=in_new_code_period)
