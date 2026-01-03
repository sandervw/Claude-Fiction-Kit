---
name: character-analysis
description: Analyze fictional characters using structured templates. Use when asked to analyze, break down, or create character profiles for fictional characters. Triggers include "analyze [character]", "character breakdown", "create character templates for", or requests for character analysis documents. Supports main characters (full analysis) and secondary characters (purpose only).
---

# Character Analysis

Analyze fictional characters and output structured markdown and JSON templates.

## Character Type

Determine analysis depth based on character role:

**Main character**:
→ Fill ALL sections: Purpose, Believe, Care, Invest
→ DO NOT ADD SECTIONS/FIELDS TO THE TEMPLATE FILES

**Secondary character**:
→ Fill ONLY: Purpose
→ Remove other sections from the docs
→ DO NOT ADD SECTIONS/FIELDS TO THE TEMPLATE FILES

If unspecified, infer from character's narrative importance or ask user.

## Workflow

### Phase 1: Gather Sources

Use web_search to find substantive analysis:

1. Search for literary criticism and serious analysis of the character (not plot summaries)
2. Search for author/director/designer commentary on characterization techniques
3. Search for analysis of defining scenes

Example queries:

- `"[character] literary analysis"`
- `"[character] character study essay"`
- `"[author] characterization [character]"`
- `"[character] arc meaning symbolism"`

For secondary characters, 1-2 searches may suffice.

### Phase 2: Synthesize

1. Cross-reference findings
2. Note where common interpretations diverge from textual evidence
3. Identify symbolic patterns, recurring imagery, authorial intent

### Phase 3: Fill Templates

Copy templates from `assets/` to working directory, then fill:

1. **Markdown template** (`Character-Template.md`): Replace "Text" placeholders with concise answers (<8 words each)
2. **JSON template** (`character-template.json`): Fill values with single words where possible, short phrases only when necessary

Guidelines:

- Leave fields empty string if not applicable
- For arrays, use 4 items maximum
- Secondary characters: fill Purpose only, remove other sections
- **REMINDER**: DO NOT ADD SECTIONS/FIELDS TO THE TEMPLATE FILES (no "metadata", "Additional Analysis Notes", "Critical Reception", etc.)

## Output

Save completed templates as:

- `[Character]-Analysis.md`
- `[character]-analysis.json`

Present both files to user.
