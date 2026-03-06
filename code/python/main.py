from __future__ import annotations

from pathlib import Path

from modules.llm_prompt import llm_prompt

input_file = Path("../../input/input.md").read_text(encoding="utf-8")

prompt = f"Hey claude, summarize this file.\n\n{input_file}\n\nYour output should be 30% of the original character count."
response = llm_prompt(prompt)
print(response)

Path("../../output/output.md").write_text(response, encoding="utf-8")
