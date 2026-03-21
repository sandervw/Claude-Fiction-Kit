from __future__ import annotations

from modules.prompt_sections import prompt_sections
from modules.utils.file_pipeline import get_project_root, write_file

# style_guide = Path("../../input/Rogue-Voice-Guidelines.md").read_text(encoding="utf-8")
# prompt = f"Hey claude, read the following style guide:\n\n{style_guide}\n\nNow edit the text below using the guidelines. Your result must be 75% of the original character count. Only output the edited text, nothing else.\n\n"
prompt = "Hey claude, do a general prose review of the text below. Your job is to find logical inconsistencies, use of common fiction tropes, repeated beats - anything that seems 'rough' or 'unpolished' in the prose. Your output should be a a brief list of any identified issues, along with suggested fixes. Your output must be less than 200 words.\n\nThe Prose:\n\n"
results = prompt_sections(prompt, "input.md")

output_md = "\n\n".join(f"## {r['name']}\n\n{r['text']}" for r in results)
output_path = get_project_root(anchor=__file__, levels_up=3) / "output" / "output.md"
write_file(output_path, output_md)
print(f"Written to {output_path}")