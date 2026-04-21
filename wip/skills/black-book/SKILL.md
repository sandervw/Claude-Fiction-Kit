---
name: black-book
description: Break down story scenes into structured "blob" sequences in a 'black book' style, and write individual blob styles from existing breakdowns. Use when the user mentions "black book", "necromancer story", "grimiore", "black book outline", or "black book blobs". Also trigger when the user asks to write or revise content in any individual blob style ('verse', 'essay', 'interview', 'epitaph', or 'lemma' blobs) for an existing breakdown.
---

# Black Book

Structure stories and scenes as sequences of typed "blobs" — short text blocks in one of five distinct styles, arranged like entries in a necromancer's grimiore, or "Black Book".

## Blob Styles (quick reference)

| Style | Voice / POV | One-liner |
|---|---|---|
| **Verse** | 3rd person, action scrawls | Like a string of action-focused texts from a scholarly, eloquent necromancer. |
| **Essay** | discursive first person | Like a serious nonfiction essay, but describes/argues a specific fiction element.  |
| **interview** | 2nd person, prose fiction | Regular fiction prose, but "you" is the protagonist. |
| **epitaph** | 3rd person character speech | Four short bullet-point lines from a single NPC. Never the main character. |
| **lemma** | Structured list | Items, locations, choices, traps — any game mechanic. Sizes: 2, 3, 4, 9, 12. |

## Mode Detection

**STOP:** This is a branching skill. The modes below are mutually exclusive. Read ONLY the ONE reference file for the detected mode. NEVER read any other files.

Determine mode from user request:

**Breakdown mode**:
- Triggers: "break down", "breakdown", "blob outline", "structure this scene", "stratguide", "guidebook", "game guide book", or any request to outline/plan a scene as a blob sequence
- **Read**: `references/breakdown-reference.md`

**Action mode**:
- Triggers: "write the action blobs", "action mode", "action style", or user provides a breakdown and asks for Action blobs to be written
- **Read**: `references/action-reference.md`

**Narrator mode**:
- Triggers: "write the narrator blobs", "narrator mode", "narrator style", or user provides a breakdown and asks for Narrator blobs to be written
- **Read**: `references/narrator-reference.md`

**Description mode**:
- Triggers: "write the description blobs", "description mode", "description style", or user provides a breakdown and asks for Description blobs to be written
- **Read**: `references/description-reference.md`

**Dialogue mode**:
- Triggers: "write the dialogue blobs", "dialogue mode", "dialogue style", or user provides a breakdown and asks for Dialogue blobs to be written
- **Read**: `references/dialogue-reference.md`

**Table mode**:
- Triggers: "write the table blobs", "table mode", "table style", or user provides a breakdown and asks for Table blobs to be written
- **Read**: `references/table-reference.md`

If ambiguous, ask user which mode.

**REMINDER:** Each mode is a SEPARATE BRANCH. Read ONLY the single reference file listed for the detected mode. Do NOT read files for other modes.

## Workflow

1. Detect mode from triggers above
2. Read the appropriate reference doc for that mode
3. Follow the workflow in that reference doc
4. Present completed output to user
