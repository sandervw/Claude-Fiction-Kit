# Actions Mode Reference

Generate a list of significant quotes, proverbs, or statements made by a character. Focus exclusively on **character-defining quotes**, the words that represent the character's core beliefs. Do NOT include quotes jsut because they are memorable.

## Phase 1: Gather Sources

Prioritize source material when available. **ALL QUOTES MUST BE VERBATIM FROM THE SOURCE**.

**Primary search targets:**
1. Direct quotes from the source material
2. Wiki pages with "Quotes" or "Dialogue"
3. Blog posts of character analysis

**Search queries:**
- `"[character] [work title] quotes"`
- `"[character] [work title] dialogue"`
- `"[character] [work title] gutenberg"`

**For visual media (tv, films, animation):**
- `"[character] quotes"` or `"[character] dialogue"`
- `"[character] [work title] quotes.net"` or `"[character] [work title] wikiquote"`

Use `web_fetch` on **2-3 pages max**, look specifically for:
- "Quotes" or "Dialogue" sections
- Passages from source

## Phase 2: Synthesize

Build chronological list of *significant* quotes spoken by the character. Distinguish the phrases that define the character's *core*, not just their *most memorable* sayings.

## Phase 3: Generate Output

**Quote criteria:**
- `30 words maximum`, each.
- `10 total quotes maximum`
- `Significant`: character-defining, or pivotal-decisions

**Include:**
- Quotes expressing core beliefs
- Quotes involving key story decision
- Key statements made to other people
- Turning point or moral decision quotes

**Exclude:**
- Quotes by other characters *about* the character
- Internal thoughts or beliefs without spoken words
- Popular quotes that do not define the character

**Format:**
Copy template from `assets/Quotes-Template.md` to working directory, then fill in list items as: 
1. [Quote, 1-30 words]
2. [Quote, 1-30 words]
...

Save as: `[Character]-Quotes.md`
