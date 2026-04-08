from __future__ import annotations

from modules.prompt_sections import prompt_sections
from modules.utils.file_pipeline import get_project_root, write_file

# input_path = get_project_root(anchor=__file__, levels_up=3) / "input" / "Rogue-Voice-Guidelines.md"
# style_guide = input_path.read_text(encoding="utf-8")
prompt = f"Hey claude, do a general prose review of the text below. Your job is to find logical inconsistencies, use of common fiction tropes, repeated beats - anything that seems 'rough' or 'unpolished' in the prose. Your output should be a brief list of any identified issues, along with suggested fixes. Your output must be less than 200 words.\n\nThe Prose:\n\n"
results = prompt_sections(prompt, "input.md")

output_md = "\n\n".join(f"## {r['name']}\n\n{r['text']}" for r in results)
output_path = get_project_root(anchor=__file__, levels_up=3) / "output" / "output.md"
write_file(output_path, output_md)
print(f"Written to {output_path}")