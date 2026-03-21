from __future__ import annotations

from modules.md_splitter import split_md_by_h2
from modules.llm_batch import llm_batch


def prompt_sections(prompt: str, filename: str) -> list[dict]:
    """Split a markdown file by ## headers and run each section through the LLM.

    Each section's text is prefixed with the prompt string before being sent.
    Returns [{name, text}] where text is the LLM response for that section.
    """

    sections = split_md_by_h2(filename)

    prompted = [
        {"name": s["name"], "text": prompt + "\n" + s["text"]}
        for s in sections
    ]

    return llm_batch(prompted)
