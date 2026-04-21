# Table Mode

Write Table blobs for a numbered breakdown. Produce only Table-style blobs, preserving original numbers.

## Voice

Structural, not narrative. No POV, no "you." Each cell is a self-contained reference entry: factual, evocative, and terse.

## Hard Rules

### Dimensions

1. Use only these configurations:

| Cells | Rows | Columns |
|-------|------|---------|
| 2     | 1    | 2       |
| 3     | 1    | 3       |
| 4     | 2    | 2       |
| 6     | 3    | 2       |
| 8     | 4    | 2       |
| 9     | 3    | 3       |
| 12    | 4    | 3       |

2. The breakdown header specifies cell count: `## TABLE (4)` means 4 cells (2 rows x 2 columns).

### Word Limits

3. Per cell: 70 words maximum.
4. Per table: 200 words maximum. This is a ceiling, not a target. Do not pad cells.
5. Vary cell lengths deliberately. Mix short punches (8-15 words) with longer entries (30-60 words). Let content dictate length.
6. Vary totals across tables. Some tables should be lean (60-100 words), others fuller.

### Structure

7. No column headers. Data starts immediately.
8. Cell format: `**Title** Explanatory text.`
9. Bold title, one space, then description.

### Formatting

10. Single-row tables (2 or 3 cells): compact format, separator row immediately follows content.
11. Multi-row tables (4+ cells): expanded format with full separator line.

### Content

12. Binary choices (left/right, yes/no, take/leave) always use a 2-cell table.

## What Table Blobs Cover

Content a player would screenshot or reference:
- **Items**: Loot, equipment, consumables, cursed objects
- **Locations**: Rooms, hiding spots, landmarks, dungeon areas
- **Choices**: Binary decisions, branching paths, risk/reward forks
- **Traps**: Hazards, environmental dangers, trigger mechanisms
- **NPCs**: Character rosters, enemy types, ally catalogs
- **Quests**: Objectives, tasks, optional goals

If the content is not something a player would consult like a reference card, it is not a Table blob.

## Tone

Concrete and evocative. Each cell should feel like a discoverable game object with weight, history, or consequence. Not clinical inventory text, not flowery prose. Atmospheric brevity.

Avoid:
- Generic descriptions ("a useful item", "a dangerous place")
- Mechanical stats without flavor ("deals 10 damage")
- Sentences starting with "This is" or "There is"
- Questions

## Workflow

1. Read the full breakdown to understand scene arc and Table blob placement.
2. Identify each Table blob: note size in parentheses and bullet points.
3. Determine dimensions from Hard Rule 1 using cell count.
4. Draft cells: bold title + description, each under 70 words.
5. Add header only if brief context is essential, using `### Header Title` above the table.
6. Format correctly: single-row = compact, multi-row = expanded.
7. Validate: correct cell count, word limits, no column headers, bold titles.

## Output Format

```markdown
# [Scene Title] — Table Blobs

## 3. TABLE (3)

| **Title A** Description text. | **Title B** Description text. | **Title C** Description text. |
| --- | --- | --- |

## 7. TABLE (4)

### Optional Header

| **Title A** Description text. | **Title B** Description text. |
| ----------------------------- | ----------------------------- |
| **Title C** Description text. | **Title D** Description text. |

## 12. TABLE (2)

| **Title A** Description text. | **Title B** Description text. |
| --- | --- |
```

Output file: `[Scene-Title]-Table-Blobs.md`.

**CRITICAL:** Output only Table blobs. Do not write other blob styles. Do not renumber — preserve exact numbers from input.

## Examples

### Example 1: 3-cell NPC table (single-row)

## 5. TABLE (3)

| **Man with Sheep's Wool** A coarse beard of curly white wool covers half of this cursed man's face. | **The Broom Woman** She holds one. If you touch the fading handle, some of the flaking paint will slip into your skin. | **Time-Eyes** The paint of his eyes alone has fallen away, leaving two pupils like clock hands. No matter how long you stare, the hands refuse to move. |
| --- | --- | --- |

### Example 2: 4-cell location table with header (multi-row)

## 8. TABLE (4)

### Places to Hide

| **Ald Medas Shrine** In this tall chamber of The Heather Vault, you crouch among the splintered piles of ten thousand exhausted magical wands. | **Big Eye's Cave** Seven ivory eggs encased in amber stud the ceiling. |
| --- | --- |
| **Selgon** This pillared corridor reminds you of an apprentice knight you once escorted through a similar sepulcher. | **Index Chamber** A snake of yellow light slithers constantly through the air between two pilons. The shifting illumination makes this a surprisingly good place to hide. |

### Example 3: 2-cell binary choice (single-row)

## 11. TABLE (2)

| **Right** The slope, in buckles and gnarls, rises gradually. Branches burst up like volcanic mushrooms. The little branch-trees thicken into a thicket; the tunnels shrink and shrink. | **Left** Your branch opens onto a wide, flat ledge. The light looks brighter this way. A place for your Blue Lady to catch her breath. |
| --- | --- |
