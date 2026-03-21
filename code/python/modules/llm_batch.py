from __future__ import annotations

from modules.llm_prompt import llm_prompt


def llm_batch(items: list[dict]) -> list[dict]:
    """Process a JSON array of {name, text} objects through llm_prompt.

    Each item's 'text' is sent as a prompt, and the response replaces it.
    """

    results = []
    for item in items:
        response_text = llm_prompt(item["text"])
        results.append({"name": item["name"], "text": response_text})

    return results
