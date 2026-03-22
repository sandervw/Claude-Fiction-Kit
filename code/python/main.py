from __future__ import annotations

from modules.prompt_sections import prompt_sections
from modules.utils.file_pipeline import get_project_root, write_file

# style_guide = Path("../../input/Rogue-Voice-Guidelines.md").read_text(encoding="utf-8")
# prompt = f"Hey claude, read the following style guide:\n\n{style_guide}\n\nNow edit the text below using the guidelines. Your result must be 75% of the original character count. Only output the edited text, nothing else.\n\n"
prompt = "Hey claude, do a 'vocabulary' edit of the story scene below. Your job is to replace roughly 15% of the *nouns* in the scene with obscure, archaic, or excrutiatingly-specific synonyms. Only replace the nouns - do not replace verbs, adjectives, etc. Also, do not replace any proper-nouns or pronouns. Your replacements must not be hyphenated, compound, or made-up words, and no word insertions/deletions (only *replacements*). Focus on the most-common nouns as they appear in fantasy; if a word is the first one that appears in your large-language-model word completion, it is probably a common one. Your output should be just the edited text, no comments, summaries, etc.\n\nThe Scene:\n\n"
results = prompt_sections(prompt, "input.md")

output_md = "\n\n".join(f"## {r['name']}\n\n{r['text']}" for r in results)
output_path = get_project_root(anchor=__file__, levels_up=3) / "output" / "output.md"
write_file(output_path, output_md)
print(f"Written to {output_path}")