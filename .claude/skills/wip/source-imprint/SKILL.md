---
name: source-imprint
description: Extract concrete style features (rhythm, syntax, register, sensory mode) from 1-3 source paragraphs and produce a hard-contract style card for downstream drafting. Use when a scene needs deliberate stylistic borrowing from a specific source, especially across genre lines. Triggers include "source imprint", "borrow style from", "imprint this passage".
---

Read the source paragraphs the user provides. Extract style features by direct observation, not by author or genre label.

Extract 3-5 concrete features. Each feature must include a short quote from the source as evidence. Cover at minimum:

- Sentence-length distribution (e.g., "alternates 4-7 word and 25-40 word sentences; no middle range")
- Clause stacking (left-branching, right-branching, parenthetical, periodic)
- Register and vocabulary (archaic, plain, Latinate, colloquial; contractions y/n)
- Dominant sensory channels
- Signature tics (recurring conjunctions, punctuation habits, repetition patterns)

Derive a short **do this / don't do this** rule list (3-5 of each) from the features.

Compose a markdown card with:
- The source paragraphs verbatim (these ride with the card)
- The extracted features
- The do/don't rules
- A one-line note: *"The writing agent treats every rule above as a hard contract."*

Save to `output/imprint-card-[short-source-tag].md`.
