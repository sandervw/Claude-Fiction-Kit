from __future__ import annotations

from modules.prompt_sections import prompt_sections
from modules.utils.file_pipeline import get_project_root, write_file

input_path = get_project_root(anchor=__file__, levels_up=3) / "input" / "Rogue-Voice-Guidelines.md"
style_guide = input_path.read_text(encoding="utf-8")
prompt = f"Hey claude, read the following style guide:\n\n{style_guide}\n\nYour job is to edit dialogue and character-thoughts in the fiction scene pasted below using these guidelines. You are only editing the dialogue/thoughts of the character *Rafe*, no other characters. If you need to increase the length of Rafe's dialogue, do so by 'folding' surround exposition/description into the dialogue; reframe surrounding text as dialogue, do not simply repeat beats/thoughts. o prevent bloating, the total length in characters of your final output text must be less than or equal to the length of the original - count before and after. Your output should be just the edited text, no comments, summaries, etc.\n\nThe Scene:\n\n"
results = prompt_sections(prompt, "input.md")

output_md = "\n\n".join(f"## {r['name']}\n\n{r['text']}" for r in results)
output_path = get_project_root(anchor=__file__, levels_up=3) / "output" / "output.md"
write_file(output_path, output_md)
print(f"Written to {output_path}")