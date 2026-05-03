---
name: source-imprint
description: Extract concrete style features (rhythm, syntax, register, sensory mode) from 1-3 source paragraphs and produce a hard-contract style card for downstream drafting. Triggers include "source imprint", "borrow style from", "imprint this passage".
---

Read the source paragraphs the user provides. Extract style features by direct observation, not by author or genre label.

Extract 4-7 concrete features - at a minimum:

- Sentence-length distribution (e.g., "alternates 4-7 word and 25-40 word sentences; no middle range")
- Clause stacking (left-branching, right-branching, parenthetical, periodic)
- Register and vocabulary (archaic, plain, Latinate, colloquial; contractions y/n)
- Dominant sensory channels
- Signature tics (recurring conjunctions, punctuation habits, repetition patterns)

Derive a short **do this / don't do this** rule list from the features.

Compose a markdown card with:
- The extracted features
- The do/don't rules

Keep your card under 100 words.

Save to `output/imprint-card-[short-source-tag].md`.
