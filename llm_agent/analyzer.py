"""
llm_agent/analyzer.py
---------------------
AnalyzerAgent: turns compile/test/sonar signals into concise repair hints.
"""

import json


class AnalyzerAgent:
    SYSTEM_PROMPT = (
        "You are an analyzer agent for Java iterations.\n"
        "Return strict JSON matching the provided schema.\n"
        "Keep guidance concise, concrete, and patch-oriented.\n"
        "Do not output code blocks."
    )

    DIAG_JSON_SCHEMA = {
        "name": "diagnosis",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "failed_tests": {"type": "string"},
                "root_cause": {"type": "string"},
                "targeted_changes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 1,
                    "maxItems": 3,
                },
                "check_after_fix": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 1,
                    "maxItems": 3,
                },
            },
            "required": ["failed_tests", "root_cause", "targeted_changes", "check_after_fix"],
            "additionalProperties": False,
        },
    }

    def __init__(self, llm):
        self.llm = llm

    def analyze_compile_errors(self, code: str, compile_errors: str) -> str:
        return self._analyze(
            context=(
                "Context: Java compilation failed.\n"
                f"ERRORS:\n{compile_errors}\n\n"
                f"CODE:\n{code}\n"
            ),
            failed_default="compilation failed",
        )

    def analyze_test_failures(self, code: str, failures: list[str]) -> str:
        failure_text = "\n".join(f"- {f}" for f in failures) or "(no details)"
        return self._analyze(
            context=(
                "Context: JUnit tests failed.\n"
                f"FAILED TESTS (expected vs actual):\n{failure_text}\n\n"
                f"CODE:\n{code}\n"
            ),
            failed_default="tests failed",
        )

    def analyze_sonar(self, code: str, metrics: dict, issues: list) -> str:
        key_metrics = {
            k: metrics.get(k, "N/A")
            for k in ("bugs", "code_smells", "complexity", "cognitive_complexity")
        }
        def _flow_summary(issue: dict) -> str:
            flows = issue.get("flows") or []
            points = []
            for flow in flows[:3]:
                for loc in (flow.get("locations") or [])[:1]:
                    rng = loc.get("textRange") or {}
                    line = rng.get("startLine", "?")
                    delta = loc.get("msg", "?")
                    points.append(f"L{line}:{delta}")
            return ", ".join(points) if points else "no-flow-details"

        top_issues = "; ".join(
            (
                f"line {i.get('line', '?')} "
                f"[rule={i.get('rule', '?')}]: {i.get('message', '?')} "
                f"| flows: {_flow_summary(i)}"
            )
            for i in issues[:3]
        ) or "none"
        return self._analyze(
            context=(
                "Context: Sonar quality gate failed.\n"
                f"METRICS: {key_metrics}\n"
                f"ISSUES: {top_issues}\n\n"
                f"CODE:\n{code}\n"
            ),
            failed_default="quality gate failed",
        )

    def _analyze(self, context: str, failed_default: str) -> str:
        prompt = (
            "Produce a diagnosis JSON with fields:\n"
            "failed_tests, root_cause, targeted_changes, check_after_fix.\n"
            "Rules:\n"
            "- root_cause: 1-2 short sentences.\n"
            "- targeted_changes: 1-3 short imperative actions.\n"
            "- check_after_fix: 1-3 concrete validations.\n\n"
            f"{context}"
        )
        raw = self.llm.generate_response(
            prompt,
            temperature=0.3,
            system_prompt=self.SYSTEM_PROMPT,
            json_schema=self.DIAG_JSON_SCHEMA,
        ).strip()
        return self._json_to_text(raw, failed_default)



    @staticmethod
    def _json_to_text(raw: str, failed_default: str) -> str:
        payload = json.loads(raw)
        failed = str(payload.get("failed_tests", "")).strip() or failed_default
        root = str(payload.get("root_cause", "")).strip()
        targeted = "\n".join(str(x).strip() for x in payload.get("targeted_changes", []))
        checks = "\n".join(str(x).strip() for x in payload.get("check_after_fix", []))
        return (
            f"FAILED_TESTS:\n{failed}\n\n"
            f"ROOT_CAUSE:\n{root}\n\n"
            f"TARGETED_CHANGES:\n{targeted}\n\n"
            f"CHECK_AFTER_FIX:\n{checks}"
        )
