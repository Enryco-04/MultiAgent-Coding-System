"""
llm_agent/analyzer.py
---------------------
AnalyzerAgent: turns failure signals into actionable hints for the Coder.

The analyzer receives full failure details including expected/actual values.
Its output goes directly to the Coder with no truncation or filtering.
"""

import re


class AnalyzerAgent:
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

Rules:
- FAILED_TESTS should say compilation failed and quote only the most important compiler errors.
- ROOT_CAUSE must be short and direct.
- TARGETED_CHANGES must be 1-4 short imperative lines.
- In TARGETED_CHANGES you should say things like:
  - replace X with Y
  - use long instead of int
  - sort before processing
  - compute A from B instead of simulating
  - change the condition from X to Y
- Do not write full Java code.
- Do not output vague advice like "review the logic" or "check syntax".
- Keep the whole diagnosis concise and action-oriented.

ERRORS:
{compile_errors}

CODE:
{self._strip_imports(code)}

DIAGNOSIS:
"""
        )
        raw = self.llm.generate_response(prompt, temperature=0.2).strip()
        return self._normalize_diagnosis(raw, "compilation failed")

    def analyze_test_failures(self, code: str, failures: list[str]) -> str:
        failure_text = "\n".join(f"- {f}" for f in failures) or "(no details)"
        prompt = (
            "Java JUnit tests failed. Produce a short structured diagnosis for the coder.\n"
            "No markdown fences. No JSON. No full code blocks. Use exactly these section headers:\n"
            "FAILED_TESTS:\nROOT_CAUSE:\nTARGETED_CHANGES:\n\n"
            "Rules:\n"
            "- FAILED_TESTS must list only the important failing tests and the shared expected/actual pattern.\n"
            "- ROOT_CAUSE must infer the logical bug in 1-2 direct sentences.\n"
            "- TARGETED_CHANGES must be 1-4 short imperative lines tied to the bug.\n"
            "- TARGETED_CHANGES should explicitly suggest replacements such as replace formula X with Y, use a safe upper bound, sort before processing, deduplicate first, or use long instead of int.\n"
            "- You may mention exact variables, formulas, boundary conditions, and data types.\n"
            "- Do not write full Java code.\n"
            "- If several failures share one pattern, identify the shared broken condition, formula, or data type.\n"
            "- Keep the whole diagnosis concise, direct, and action-oriented.\n\n"
            f"FAILED TESTS (with expected vs actual):\n{failure_text}\n\n"
            f"CODE:\n{self._strip_imports(code)}\n\n"
            "DIAGNOSIS:\n"
        )
        raw = self.llm.generate_response(prompt, temperature=0.2).strip()
        return self._normalize_diagnosis(raw, "tests failed")

    def analyze_sonar(self, code: str, metrics: dict, issues: list) -> str:
        key_metrics = {k: metrics.get(k, "N/A") for k in ("bugs", "code_smells", "complexity")}
        top_issues  = "; ".join(
            f"line {i.get('line','?')}: {i.get('message','?')}" for i in issues[:3]
        ) or "none"
        prompt = (
            "Java code quality issues below. Produce a short structured diagnosis for the coder.\n"
            "No markdown fences. No JSON. No full code blocks. Use exactly these section headers:\n"
            "FAILED_TESTS:\nROOT_CAUSE:\nTARGETED_CHANGES:\n\n"
            "Rules:\n"
            "- FAILED_TESTS should summarize the quality gate failure, not JUnit tests.\n"
            "- ROOT_CAUSE must explain the quality problem briefly and directly.\n"
            "- TARGETED_CHANGES must be 1-4 short imperative refactoring actions.\n"
            "- TARGETED_CHANGES may suggest extracting a helper, simplifying nested branches, removing duplication, or replacing a verbose pattern with a simpler one.\n"
            "- Do not write full Java code.\n"
            "- Keep the whole diagnosis concise and action-oriented.\n\n"
            f"METRICS: {key_metrics}\n"
            f"ISSUES: {top_issues}\n\n"
            f"CODE:\n{self._strip_imports(code)}\n\n"
            "DIAGNOSIS:\n"
        )
        raw = self.llm.generate_response(prompt, temperature=0.2).strip()
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

        if not failed:
            failed = failed_default
        if not root:
            root = "A logic or boundary condition in the implementation does not match expected behavior."
        if not targeted:
            targeted = (
                "Re-check the core formula against expected outputs.\n"
                "Fix boundary conditions and data types used in that formula."
            )

        return (
            f"FAILED_TESTS:\n{failed}\n\n"
            f"ROOT_CAUSE:\n{root}\n\n"
            f"TARGETED_CHANGES:\n{targeted}"
        )
