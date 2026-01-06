# Description Mode Reference

Generate physical description of a character based on source material. Focus exclusively on sensory details — what can be seen, heard, smelled, touched. Do NOT include personality, tone, or internal states.

## Phase 1: Gather Sources

Prioritize direct source text. The ideal case is a verbatim character description from the original work.

**Primary search targets:**
1. Wiki pages with "Appearance" or "Physical Description" sections
2. Direct quotes from the source material
3. Official character profiles or art descriptions

**Search queries:**
- `"[character] appearance"` or `"[character] physical description"`
- `"[character] [work title] wiki"` (then web_fetch, look for Appearance section)
- `"[character] described as"` (finds quoted descriptions)
- `"[work title] [character] what does [character] look like"`

**For visual media (games, films, animation):**
- `"[character] character design"` or `"[character] concept art description"`
- `"[character] [work title] model viewer"` or `"[character] in-game appearance"`

Use `web_fetch` on wiki pages and look specifically for:
- Dedicated "Appearance" sections
- Quoted passages from source text
- Detailed physical breakdowns

If direct source text is unavailable, compile from multiple secondary sources but note the limitation.

## Phase 2: Synthesize

Compile findings into the description template fields.

**Strict rules:**
- Only fill fields with directly stated or clearly visible information
- Do NOT infer unstated details (e.g., don't guess smell if not mentioned)
- Exception: `symbolic_animal` should always be filled — infer a best-guess if not explicit

**For the Full Description:**
- If source text is 250-500 words: use verbatim (mark with quotes)
- If source text is shorter: include quoted source text, then augment with other research to reach 250 words minimum
- If source text is longer: include most relevant quoted passages, summarize remainder

## Phase 3: Generate Output

Create both output files:

1. **Markdown output**: Copy template from `assets/Description-Template.md`, fill in all applicable fields
2. **JSON output**: Copy template from `assets/description-template.json`, fill in all applicable fields

**Field guidelines:**

| Field | Notes |
|-------|-------|
| symbolic_animal | Always include — infer if not stated |
| gender, rough_age | Only if stated or unambiguous |
| height/build/stance | Physical frame and posture |
| skin_tone | Only if described |
| hands | Calluses, scars, nail condition, etc. |
| hair | Style, color, condition, length |
| face | Nose shape, mouth, brow, jaw |
| eyes | Color, shape, notable features |
| expression | Resting expression or common look |
| voice | Pitch, texture, accent, speech patterns |
| movement | Gait, gestures, mannerisms |
| sound | Sounds caused by movement, gear, breathing |
| smell | Only if explicitly mentioned |
| scars_marks_tattoos | Visible marks, wounds, body modifications |
| equipment | Categorized list with specific materials |

**Save as:**
- `[Character]-Description.md`
- `[Character]-Description.json`
