---
name: black-book
description: Break down story scenes into structured "blob" sequences in a 'black book' style, and write individual blob styles from existing breakdowns. Use when the user mentions "black book", "necromancer story", "grimiore", "black book outline", or "black book blobs". Also trigger when the user asks to write or revise content in any individual blob style ('verse', 'essay', 'interview', 'epitaph', or 'lemma' blobs) for an existing breakdown.
---

# Black Book

Structure stories and scenes as sequences of typed "blobs" — short text blocks in one of five distinct styles, arranged like entries in a necromancer's grimiore, or "Black Book".

## Blob Styles (quick reference)

| Style | Voice / POV | One-liner |
|---|---|---|
| **Verse** | 3rd-person, action scrawls | Like a string of action-focused texts from a scholarly, eloquent necromancer. |
| **Essay** | discursive 1st-person | Like a serious nonfiction essay, but describes/argues a specific fiction element.  |
| **Interview** | candid, conversational 1st-person | A framed monologue where prompts stand in for the interviewer. |
| **Memorials** | formal, compressed 2nd/3rd-person | 2-4 epitaphs. Aimed at honoring the dead or addressing passers-by. |
| **Lemma** | 3rd-person omniscient | Encyclopedia entry for a fictional element: items, locations, monsters, etc. |

## Mode Detection

**STOP:** This is a branching skill. The modes below are mutually exclusive. Read ONLY the ONE reference file for the detected mode. NEVER read any other files.

Determine mode from user request:

**Breakdown mode**:
- Triggers: "break down", "breakdown", "blob outline", "structure this scene", or any request to outline/plan a scene as a blob sequence
- **Read**: `references/breakdown-reference.md`

**Verse mode**:
- Triggers: TODO
- **Read**: `TODO.md`

**Essay mode**:
- Triggers: TODO
- **Read**: `TODO.md`

**Interview mode**:
- Triggers: TODO
- **Read**: `TODO.md`

**Memorials mode**:
- Triggers: TODO
- **Read**: `TODO.md`

**Lemma mode**:
- Triggers: TODO
- **Read**: `TODO.md`

If ambiguous, ask user which mode.

**REMINDER:** Each mode is a SEPARATE BRANCH. Read ONLY the single reference file listed for the detected mode. Do NOT read files for other modes.

## Workflow

1. Detect mode from triggers above
2. Read the appropriate reference doc for that mode
3. Follow the workflow in that reference doc
4. Present completed output to user
