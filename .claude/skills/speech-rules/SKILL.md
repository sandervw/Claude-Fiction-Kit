---
name: speech-rules
description: Per-character speech card that forces positive specification (what the character actively does) plus default-banned dialogue tics. Run once per speaking character per scene with dialogue. Triggers include "speech rules", "character voice card", "dialogue rules".
---

Read the character (name, brief description, or profile if provided) and scene context. Note any source paragraphs of the character's speech the user supplies.

Roll the character's voice from using `assets/sampling.py`:

```
python assets/sampling.py positive_modes 1
python assets/sampling.py vocab_registers 1
python assets/sampling.py sentence_length_caps 1
python assets/sampling.py signature_constructions 1
```

If source paragraphs are provided, override rolled choices which conflict with concrete features extracted directly from the source.

Apply the **default-banned patterns** as constants (always banned, never rolled):
- Clinical or curious tone
- "What does it feel like" type questions
- Detached observational commentary on the protagonist
- Fragment-as-style (unless the rolled positive mode requires it)

Compose a markdown card per character with: positive mode, voice fingerprint (register, sentence-length cap, signature construction), default-banned patterns.

Keep your card under 100 words.

Save to `output/speech-card-[character]-[scene-tag].md`.
