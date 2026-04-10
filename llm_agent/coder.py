"""
llm_agent/coder.py
------------------
CoderAgent: generates a Java implementation from a problem spec.
"""

import json
import re


class CoderAgent:
    # Stable behavioral policy (high level). Dynamic task details stay in user prompt.
    SYSTEM_PROMPT = (
        "You are a Java coding agent.\n"
        "Non-negotiable rules:\n"
        "- Return only valid JSON matching the provided schema.\n"
        "- The java_code field must contain a complete compilable Java file.\n"
        "- Never add package declarations.\n"
        "- Preserve the required class name and method signature exactly.\n"
        "- On retries, apply minimal local edits only.\n"
        "- Do not regress passed tests."
    )

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
        """
        Produce one Java candidate for the current problem attempt.

        On retries, feed previous code + analyzer hints to request a minimal patch.
        Returns dict: {"filename": <class_name>, "code": <java_source>}.
        """
        class_name  = problem["class_name"]
        description = problem["description"]
        signature   = problem["signature"]

        cleaned_previous_code = self._clean(previous_code) if previous_code else None
        clean_hints = self._clean(hints) if hints else None

        desc_block = description

        if cleaned_previous_code and clean_hints:
            retry_block = (
                f"\nYour previous attempt failed:\n{cleaned_previous_code}\n\n"
                "Repair using analyzer diagnosis below.\n"
                "Treat TARGETED_CHANGES as required.\n"
                "Treat CHECK_AFTER_FIX as acceptance criteria.\n\n"
                f"{clean_hints}\n\n"
                "Patch policy:\n"
                "- Keep working logic unchanged.\n"
                "- Edit only what is needed for failing tests/issues.\n"
                "- Avoid rewrites and avoid new helpers unless necessary."
            )
        elif cleaned_previous_code:
            retry_block = (
                f"\nYour previous attempt failed:\n{cleaned_previous_code}\n\n"
                "Repair with minimal changes only.\n"
                "Preserve working logic and avoid full rewrites."
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

When retrying, prefer a minimal patch over a rewrite.
Do not break behavior that likely already passes tests.

Problem description:
{desc_block}

Method signature to implement:
{signature}
{retry_block}
"""
        # note: codex client does not support temperature, this is for retrocompatibility with OllamaClient.
        temperature = 0.4 if not cleaned_previous_code else 0.25
        response = self.llm.generate_response(
            prompt,
            temperature=temperature,
            json_schema=self.CODE_JSON_SCHEMA,
            system_prompt=self.SYSTEM_PROMPT,
        )
        code = self._extract_code_from_json(response)
        code = self._strip_package(code)
        return {"filename": class_name, "code": code}

    @staticmethod
    def _extract_code_from_json(text: str) -> str:
        """Parse strict JSON model output and extract java_code field."""
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
        """Defensive cleanup: remove package lines (tests expect default package)."""
        return "\n".join(
            line for line in code.splitlines()
            if not (line.strip().startswith("package ") and line.strip().endswith(";"))
        )

    @staticmethod

    def _clean(text: str) -> str:
        """This method is needed because ''' java markdowns in response"""
        text = re.sub(r'```(?:java)?\s*', '', text)
        text = re.sub(r'```', '', text)
        return text.strip()
