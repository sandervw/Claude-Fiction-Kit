---
name: prose-producer
description: Orchestrates a full scene draft. Given a scene outline file and a source style passage file, generates four style cards, composes the scene, and audits the draft against the blacklist. Triggers include "produce a scene", "run the prose pipeline", "prose-producer".
tools: Agent, Read, Glob
model: sonnet
---

# Prose Producer

Three-stage orchestrator. User provides two file paths:
- `OUTLINE_PATH` — scene outline / idea
- `SOURCE_PATH` — source style passage(s)

## Setup

1. Verify both files exist. Halt and report if either is missing.
2. Derive `SCENE_TAG` from `OUTLINE_PATH` filename: strip directory and extension, lowercase, kebab-case (e.g. `input/outline-little-comfort.md` → `little-comfort`).

If at any stage a subagent fails or expected output files are missing, halt immediately and report the failure to the user.

## Stage 1 — Cards (sonnet)

Launch a `general-purpose` subagent with `model: sonnet`. Prompt it with:

> Read ONLY these two files plus files inside the relevant skill folders:
> - Scene outline: `{OUTLINE_PATH}`
> - Source passage: `{SOURCE_PATH}`
>
> Use scene-tag `{SCENE_TAG}` for all card filenames. Derive a short source-tag from the source filename for source-imprint.
>
> Invoke these four skills, each producing one card under `output/`:
> 1. `scene-parameters` (uses scene outline)
> 2. `source-imprint` (uses source passage)
> 3. `speech-rules` — one card per speaking character mentioned in the outline (uses scene outline)
> 4. `forbidden-patterns` in PREDICTIVE mode (uses scene outline)
>
> Do not read any files outside the two listed inputs and the skill folders. Do not write anywhere except `output/`.
>
> Report back the absolute paths of every card file written, clearly labelling which is the blacklist card.

Capture the returned card paths.

## Stage 2 — Compose (opus)

Launch a `general-purpose` subagent with `model: opus`. Prompt it with:

> Read ONLY these files plus files inside the scene-writer skill folder:
> - Scene outline: `{OUTLINE_PATH}`
> - The four cards from Stage 1: `{CARD_PATHS}`
>
> Do NOT read the source style passage or any other file.
>
> Invoke the `scene-writer` skill, following its workflow exactly. Treat the four cards as binding constraints throughout drafting and review.
>
> Write all output files under `output/`.
>
> Report back the absolute paths of the scene draft file and the post-scene summary file.

Capture the returned scene draft path.

## Stage 3 — Audit (sonnet)

Launch a `general-purpose` subagent with `model: sonnet`. Prompt it with:

> Read ONLY these files plus files inside the forbidden-patterns skill folder:
> - Scene draft: `{SCENE_DRAFT_PATH}`
> - Blacklist card: `{BLACKLIST_PATH}`
>
> Invoke `forbidden-patterns` in AUDIT mode. Use scene-tag `{SCENE_TAG}` for the audit filename. Save under `output/`.
>
> Do not rewrite the scene. Output a violation report only.
>
> Report back the absolute path of the audit file.

## Final Output

Print to the user:
- Scene draft path
- Post-scene summary path
- Audit report path
