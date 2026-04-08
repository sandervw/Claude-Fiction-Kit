from __future__ import annotations

from modules.prompt_sections import prompt_sections
from modules.utils.file_pipeline import get_project_root, write_file

# input_path = get_project_root(anchor=__file__, levels_up=3) / "input" / "Rogue-Voice-Guidelines.md"
# style_guide = input_path.read_text(encoding="utf-8")
prompt = f"Hey claude, do a 'vocabulary' edit of the story scene below. Your job is to replace roughly 15% of the *nouns* in the scene with archaic, or excrutiatingly-specific synonyms. Only replace nouns - no verbs, adjectives, Do not replace any proper-nouns or pronouns. Your replacements must not be hyphenated, compound, or made-up words, and no word insertions/deletions (only *replacements*). If a noun is the first one that appears in your large-language-model word completion, it is too common. Your output should be just the edited text, no comments, summaries, etc.\n\nThe Scene:\n\n"
results = prompt_sections(prompt, "input.md")

output_md = "\n\n".join(f"## {r['name']}\n\n{r['text']}" for r in results)
output_path = get_project_root(anchor=__file__, levels_up=3) / "output" / "output.md"
write_file(output_path, output_md)
print(f"Written to {output_path}")