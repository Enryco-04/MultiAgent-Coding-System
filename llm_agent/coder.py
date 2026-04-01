"""
llm_agent/coder.py
------------------
CoderAgent: generates a Java implementation from a problem spec.
"""

import json
import re


class CoderAgent:
    CODE_JSON_SCHEMA = {
        "name": "java_solution",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "java_code": {"type": "string"},
            },
            "required": ["java_code"],
            "additionalProperties": False,
        },
    }

    def __init__(self, llm):
        self.llm = llm

    def code_with_test(
        self,
        problem:       dict,
        hints:         str | None = None,
        previous_code: str | None = None,
    ) -> dict:
        class_name  = problem["class_name"]
        description = problem["description"]
        signature   = problem["signature"]

        clean_prev = self._clean(previous_code) if previous_code else None
        clean_hints = self._compact_hints(hints) if hints else None

        # On retries, keep the objective visible but reduce prompt bloat.
        desc_block = description if not clean_prev else self._condense_description(description)

        if clean_prev and clean_hints:
            retry_block = (
                f"\nYour previous attempt failed:\n{clean_prev}\n\n"
                "Use this diagnosis from the analyzer to repair the code.\n"
                "Treat TARGETED_CHANGES as instructions, not optional suggestions.\n"
                "Pay special attention to FAILED_TESTS, ROOT_CAUSE, and TARGETED_CHANGES.\n\n"
                f"{clean_hints}\n\n"
                "Important repair policy:\n"
                "- Keep the existing solution structure unless the diagnosis proves it is fundamentally wrong.\n"
                "- Make the smallest set of code changes needed to fix the diagnosed bug.\n"
                "- Do not rewrite working parts just to make the code look different.\n"
                "- Preserve behavior that likely already passes tests.\n"
                "- If only one formula, bound, condition, or data type is wrong, change only that part.\n\n"
                "If TARGETED_CHANGES says to replace a formula, bound, condition, or data type, apply that change directly.\n"
                "Do not ignore TARGETED_CHANGES unless they clearly contradict the failing tests.\n\n"
                "Fix the implementation so the diagnosis is addressed directly."
            )
        elif clean_prev:
            retry_block = (
                f"\nYour previous attempt failed:\n{clean_prev}\n\n"
                "Repair it with minimal changes.\n"
                "Preserve working logic and avoid rewriting the whole solution unless necessary.\n"
                "Change only the smallest number of lines needed to fix the bug."
            )
        else:
            retry_block = ""

        prompt = f"""You generate Java code.

Return JSON only. Field:
- java_code: valid complete single-file Java source

Rules for java_code:
- Complete compilable Java file
- Class named exactly: {class_name}
- No package declaration, no main method, no JUnit imports
- All necessary imports at the top (java.util.* etc.)
- No markdown, no explanations

IMPORTANT: Read the description carefully. Do NOT assume this is a problem
you have seen before — the framing and constraints may differ from similar problems.

When retrying after a failed attempt, prefer a minimal targeted patch over a full rewrite.
Do not replace a mostly-correct solution with a completely different approach unless the prior approach is fundamentally incompatible with the problem.

Problem description:
{desc_block}

Method signature to implement:
{signature}
{retry_block}
"""

        response = self.llm.generate_response(
            prompt,
            temperature=0.8,
            json_schema=self.CODE_JSON_SCHEMA,
        )
        code = self._extract_code_from_json(response)
        code = self._strip_package(code)
        return {"filename": class_name, "code": code}

    @staticmethod
    def _extract_code_from_json(text: str) -> str:
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Model output is not valid JSON: {text[:500]}") from exc

        code = payload.get("java_code", "")
        if not isinstance(code, str):
            raise ValueError("Model JSON does not contain string field 'java_code'.")
        if not code:
            raise ValueError("Field 'java_code' is empty.")
        return code

    @staticmethod
    def _strip_package(code: str) -> str:
        return "\n".join(
            line for line in code.splitlines()
            if not (line.strip().startswith("package ") and line.strip().endswith(";"))
        )

    @staticmethod
    def _clean(text: str) -> str:
        text = re.sub(r'```(?:java)?\s*', '', text)
        text = re.sub(r'```', '', text)
        return text.strip()

    @staticmethod
    def _condense_description(description: str, max_lines: int = 24) -> str:
        lines = [line.rstrip() for line in description.splitlines()]
        non_empty = [line for line in lines if line.strip()]
        if len(non_empty) <= max_lines:
            return description
        head = "\n".join(non_empty[:max_lines]).strip()
        return (
            head
            + "\n...\n"
            + "Keep the same objective/constraints as above; only repair the implementation bug."
        )

    @staticmethod
    def _compact_hints(hints: str, max_chars: int = 1600) -> str:
        clean = CoderAgent._clean(hints)
        if len(clean) <= max_chars:
            return clean
        # Prefer keeping structured diagnosis headers if present.
        parts = []
        for name in ("FAILED_TESTS", "ROOT_CAUSE", "TARGETED_CHANGES", "CHECK_AFTER_FIX"):
            m = re.search(rf"(?is)\b{name}\s*:\s*(.*?)(?=\n[A-Z_]+\s*:|\Z)", clean)
            if m:
                body = m.group(1).strip()
                body = "\n".join(line.strip() for line in body.splitlines() if line.strip())
                parts.append(f"{name}:\n{body}")
        packed = "\n\n".join(parts).strip() or clean
        if len(packed) > max_chars:
            packed = packed[: max_chars - 3].rstrip() + "..."
        return packed
