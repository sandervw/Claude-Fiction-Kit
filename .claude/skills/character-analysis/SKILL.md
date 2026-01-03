---
name: character-analysis
description: Analyze fictional characters using structured templates. Use when asked to analyze, break down, or create character profiles for fictional characters. Triggers include "analyze [character]", "character breakdown", "create character templates for", or requests for character analysis documents. Supports main characters (full analysis) and secondary characters (purpose only). Also supports Actions mode for listing concrete actions a character takes — triggers include "character actions", "list what [character] does", "action list for [character]".
---

# Character Analysis

Analyze fictional characters and output structured documents.

## Analysis Mode

Determine mode from user request:

**Profile mode** (default):
→ Triggers: "analyze", "character breakdown", "character profile", "character template"
→ Output: Markdown + JSON templates (Purpose/Believe/Care/Invest)

**Actions mode**:
→ Triggers: "character actions", "what does [character] do", "list of actions", "action list"
→ Output: Chronological actions list

If ambiguous, ask user which mode.

## Character Type (Profile mode only)

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

Research strategy differs by mode:

#### Profile Mode Sources

Use web_search to find substantive analysis:

1. Literary criticism and serious analysis of the character
2. Author/director/designer commentary on characterization techniques
3. Analysis of defining scenes

Example queries:
- `"[character] literary analysis"`
- `"[character] character study essay"`
- `"[author] characterization [character]"`
- `"[character] arc meaning symbolism"`

For secondary characters, 1-2 searches may suffice.

#### Actions Mode Sources

Search for comprehensive plot coverage:

1. Detailed plot summaries and synopses
2. Chapter/episode/book breakdowns
3. Wiki pages with chronological coverage
4. Timeline resources

Example queries:
- `"[character] [work title] plot summary"`
- `"[work title] chapter summary"` or `"[work title] book by book summary"`
- `"[character] wiki"` (then web_fetch the result)
- `"[work title] timeline events"`

For long works (epics, series), search by arc/section:
- `"[work title] book 1 summary"`, `"[work title] book 2 summary"`, etc.
- `"[character] [arc name] actions"`

Use `web_fetch` on detailed wiki pages or plot breakdowns to get comprehensive coverage.

### Phase 2: Synthesize

**Profile mode**: Cross-reference findings. Note where common interpretations diverge from textual evidence. Identify symbolic patterns, recurring imagery, authorial intent.

**Actions mode**: Build chronological list of significant actions. Distinguish what character *does* from what *happens to* them.

### Phase 3: Generate Output

#### Profile Mode Output

Copy templates from `assets/` to working directory, then fill:

1. **Markdown template** (`Character-Template.md`): Replace "Text" placeholders with concise answers (<8 words each)
2. **JSON template** (`character-template.json`): Fill values with single words where possible, short phrases only when necessary

Guidelines:
- Leave fields empty string if not applicable
- For arrays, use 4 items maximum
- Secondary characters: fill Purpose only, remove other sections
- **REMINDER**: DO NOT ADD SECTIONS/FIELDS TO THE TEMPLATE FILES (no "metadata", "Additional Analysis Notes", "Critical Reception", etc.)

Save as:
- `[Character]-Analysis.md`
- `[character]-analysis.json`

#### Actions Mode Output

Generate comprehensive list of significant character actions.

**Action criteria:**
- 5-15 words each, single sentence
- Active verb phrase (character as subject doing the action)
- Significant: plot-moving, character-defining, or pivotal choices
- Concrete and specific (not vague summaries)

**Include:**
- Major plot actions and decisions
- Defining moral choices
- Key interactions with other characters
- Turning points and pivotal moments

**Exclude:**
- Passive events (things done TO the character)
- Internal states without external action ("feels sad", "realizes truth")
- Trivial actions unless character-defining

**Format:**
```markdown
# [Character] — Actions

_[Work Title] by [Author/Creator]_

1. [Action in active voice, 5-15 words]
2. [Action in active voice, 5-15 words]
...
```

**Order:** Chronological within the narrative.

Save as: `[Character]-Actions.md`

## Output

Present completed file(s) to user.