import json
from llm_client import LLMClient


SYSTEM_PROMPT = """
You are an operations documentation review assistant.

Your job is to review an operator log entry against retrieved reference material.

You must not determine compliance.
You must not invent facts.
You must identify potentially relevant references, possible missing information,
suggested follow-up questions, and a human-review note.

Return valid JSON only.
"""

def format_retrieved_context(references: list[dict]) -> str:
    formatted_sections = []

    for index, reference in enumerate(references, start=1):
        formatted_sections.append(
            f"""
Reference {index}
Title: {reference.get("title", "Unknown")}
Source: {reference.get("source_file", "Unknown")}
Content:
{reference.get("content", "")}
"""
        )

    return "\n".join(formatted_sections)


def build_review_prompt(log_entry: dict, retrieved_references: list[dict]) -> str:
    context = format_retrieved_context(retrieved_references)

    return f"""
Review the following operator log entry using only the retrieved reference material.

Operator Log:
{json.dumps(log_entry, indent=2)}

Retrieved Reference Material:
{context}

Return JSON in this structure:
{{
  "log_id": "...",
  "summary": "...",
  "relevant_references": [
    {{
      "title": "...",
      "source_file": "...",
      "why_relevant": "..."
    }}
  ],
  "possible_missing_information": ["..."],
  "suggested_follow_up_questions": ["..."],
  "review_note": "..."
}}
"""


class LogReviewer:

    def __init__(self, llm_client: LLMClient) -> None:
        self.llm_client = llm_client

    def review_log_entry(self, log: str, retrieved_references: list[dict]) -> dict:
        user_prompt = build_review_prompt(log, retrieved_references)
        response = self.llm_client.query_model(system_prompt = SYSTEM_PROMPT, user_prompt = user_prompt)
        return json.loads(response)
