# Description Mode Reference

Generate physical description of a character based on source material. Focus exclusively on sensory details — what can be seen, heard, smelled, touched. Do NOT include personality, tone, or internal states.

## Phase 1: Gather Sources

Prioritize source text. The ideal description is verbatim from the original work.

**Primary search targets:**
1. Wiki pages with "Appearance" or "Description"
2. Direct quotes from the source material
3. Official character profiles or art descriptions

**Search queries:**
- `"[character] [work title] appearance"`
- `"[character] [work title] description"`
- `"[character] [work title] wiki"` (then web_fetch, look for Appearance section)

**For visual media (games, films, animation):**
- `"[character] character design"` or `"[character] concept art description"`
- `"[character] [work title] model viewer"` or `"[character] in-game appearance"`

Use `web_fetch` on **2 wiki pages max**, look specifically for:
- "Appearance" sections
- Quoted passages from source
- Detailed physical breakdowns

If direct source text is unavailable, compile from multiple secondary sources.

## Phase 2: Synthesize

Compile findings into the description template fields.

**Strict rules:**
- Only fill fields with directly stated or clearly visible information
- Do NOT infer unstated details (e.g., don't guess smell if not mentioned)
- Exception: `symbolic_animal` should always be filled — infer a best-guess if not explicit
- **DO NOT LIST NON-PHYSICAL DETAILS** such as mood, personality, occupation, etc

**For the Full Description:**
- If source text is 250-500 words: use verbatim (mark with quotes)
- If source text is shorter: **include quoted source text**, then augment with other research
- If source text is longer: **include most relevant quoted passages**
- `Reminder`: description must be 1-2 paragraphs long, 250-500 words

## Phase 3: Generate Output

Create both output files:

1. **Markdown output**: Copy template from `assets/Description-Template.md`, fill in ONLY applicable fields
2. **JSON output**: Copy template from `assets/description-template.json`, fill in ONLY applicable fields

**Save as:**
- `[Character]-Description.md`
- `[Character]-Description.json`
