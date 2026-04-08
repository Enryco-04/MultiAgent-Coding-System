"""
llm_agent/analyzer.py
---------------------
AnalyzerAgent: turns failure signals into actionable hints for the Coder.

The analyzer receives full failure details including expected/actual values.
Its output goes directly to the Coder with no truncation or filtering.
"""

import re


class AnalyzerAgent:
    SYSTEM_PROMPT = (
        "You are an analyzer agent for Java code iterations.\n"
        "Provide concise, high-signal repair guidance.\n"
        "Always follow requested output headers exactly.\n"
        "Prefer concrete minimal fixes over rewrites.\n"
        "Avoid vague advice and avoid full code snippets."
    )

    def __init__(self, llm):
        self.llm = llm

    def analyze_compile_errors(self, code: str, compile_errors: str) -> str:
        prompt = (
            f"""
Java compile errors below. Produce a short structured diagnosis for the coder.

No markdown fences. No JSON. No full code blocks.
Use exactly these section headers:

FAILED_TESTS:
ROOT_CAUSE:
TARGETED_CHANGES:
CHECK_AFTER_FIX:

Rules:
- FAILED_TESTS should say compilation failed and quote only the most important compiler errors.
- ROOT_CAUSE must be short and direct.
- TARGETED_CHANGES must be 1-2 short imperative lines.
- Prefer smallest possible edits.
- Do not write full Java code.
- CHECK_AFTER_FIX must be 1-2 concrete checks.

ERRORS:
{compile_errors}

CODE:
{self._strip_imports(code)}

DIAGNOSIS:
"""
        )
        raw = self.llm.generate_response(
            prompt,
            temperature=0.3,
            system_prompt=self.SYSTEM_PROMPT,
        ).strip()
        return self._normalize_diagnosis(raw, "compilation failed")

    def analyze_test_failures(self, code: str, failures: list[str]) -> str:
        failure_text = "\n".join(f"- {f}" for f in failures) or "(no details)"
        prompt = (
            "Java JUnit tests failed. Produce a short structured diagnosis for the coder.\n"
            "No markdown fences. No JSON. No full code blocks. Use exactly these section headers:\n"
            "FAILED_TESTS:\nROOT_CAUSE:\nTARGETED_CHANGES:\nCHECK_AFTER_FIX:\n\n"
            "Rules:\n"
            "- FAILED_TESTS must list only the important failing tests and the shared expected/actual pattern.\n"
            "- ROOT_CAUSE must infer the logical bug in 1-2 direct sentences.\n"
            "- TARGETED_CHANGES must be 1-2 short imperative lines tied to the bug.\n"
            "- Prefer minimal edits; do not suggest rewrites unless unavoidable.\n"
            "- Do not write full Java code.\n"
            "- CHECK_AFTER_FIX must be 1-2 concrete checks.\n\n"
            f"FAILED TESTS (with expected vs actual):\n{failure_text}\n\n"
            f"CODE:\n{self._strip_imports(code)}\n\n"
            "DIAGNOSIS:\n"
        )
        raw = self.llm.generate_response(
            prompt,
            temperature=0.3,
            system_prompt=self.SYSTEM_PROMPT,
        ).strip()
        return self._normalize_diagnosis(raw, "tests failed")

    def analyze_sonar(self, code: str, metrics: dict, issues: list) -> str:
        key_metrics = {k: metrics.get(k, "N/A") for k in ("bugs", "code_smells", "complexity")}
        top_issues  = "; ".join(
            f"line {i.get('line','?')}: {i.get('message','?')}" for i in issues[:3]
        ) or "none"
        prompt = (
            "Java code quality issues below. Produce a short structured diagnosis for the coder.\n"
            "No markdown fences. No JSON. No full code blocks. Use exactly these section headers:\n"
            "FAILED_TESTS:\nROOT_CAUSE:\nTARGETED_CHANGES:\nCHECK_AFTER_FIX:\n\n"
            "Rules:\n"
            "- FAILED_TESTS should summarize the quality gate failure, not JUnit tests.\n"
            "- ROOT_CAUSE must explain the quality problem briefly and directly.\n"
            "- TARGETED_CHANGES must be 1-2 short imperative actions.\n"
            "- TARGETED_CHANGES must prioritize issues explicitly present in ISSUES (rule/line/message), not generic cleanup.\n"
            "- Prefer minimal local edits over architecture rewrites.\n"
            "- Do not write full Java code.\n"
            "- CHECK_AFTER_FIX must be 1-2 measurable checks tied to Sonar.\n\n"
            f"METRICS: {key_metrics}\n"
            f"ISSUES: {top_issues}\n\n"
            f"CODE:\n{self._strip_imports(code)}\n\n"
            "DIAGNOSIS:\n"
        )
        raw = self.llm.generate_response(
            prompt,
            temperature=0.3,
            system_prompt=self.SYSTEM_PROMPT,
        ).strip()
        return self._normalize_diagnosis(raw, "quality gate failed")

    @staticmethod
    def _strip_imports(code: str) -> str:
        return "\n".join(
            line for line in code.splitlines()
            if not line.strip().startswith("import ")
        ).strip()

    @staticmethod
    def _normalize_diagnosis(text: str, failed_default: str) -> str:
        # Keep only plain text and enforce the four required sections in a compact form.
        clean = re.sub(r"```(?:\w+)?", "", text)
        clean = clean.replace("```", "").strip()

        def extract(name: str) -> str:
            m = re.search(
                rf"(?is)\b{name}\s*:\s*(.*?)(?=\n[A-Z_]+\s*:|\Z)",
                clean,
            )
            return (m.group(1).strip() if m else "")

        def compact_lines(block: str, max_lines: int, max_chars: int) -> str:
            if not block:
                return ""
            lines = []
            for raw_line in block.splitlines():
                line = raw_line.strip()
                line = re.sub(r"^[-*]\s*", "", line)
                if not line:
                    continue
                lines.append(line)
                if len(lines) >= max_lines:
                    break
            merged = "\n".join(lines)
            if len(merged) > max_chars:
                merged = merged[: max_chars - 3].rstrip() + "..."
            return merged

        failed = compact_lines(extract("FAILED_TESTS"), max_lines=3, max_chars=280)
        root = compact_lines(extract("ROOT_CAUSE"), max_lines=2, max_chars=320)
        targeted = compact_lines(extract("TARGETED_CHANGES"), max_lines=4, max_chars=420)
        checks = compact_lines(extract("CHECK_AFTER_FIX"), max_lines=3, max_chars=260)

        if not failed:
            failed = failed_default
        if not root:
            root = "A logic or boundary condition in the implementation does not match expected behavior."
        if not targeted:
            targeted = (
                "Re-check the core formula against expected outputs.\n"
                "Fix boundary conditions and data types used in that formula."
            )
        if not checks:
            checks = (
                "Re-run tests related to the reported failure.\n"
                "Confirm the specific failing pattern no longer appears."
            )

        return (
            f"FAILED_TESTS:\n{failed}\n\n"
            f"ROOT_CAUSE:\n{root}\n\n"
            f"TARGETED_CHANGES:\n{targeted}\n\n"
            f"CHECK_AFTER_FIX:\n{checks}"
        )
