---
name: scene-parameters
description: Lock scene-level stylistic axes (sensory palette, sentence rhythm, POV distance, time handling, scene shape) before drafting, by rolling random selections from a vocabulary file. Use at the start of every new scene to give it a unique fingerprint by construction. Triggers include "scene parameters", "lock parameters", "scene fingerprint".
---

Read the scene context the user provides. Note any user-locked axes (e.g., "POV must be close") and skip the roll for those.

For each unlocked axis, run `assets/sampling.py` against `assets/vocabulary.json`:

```
python assets/sampling.py senses 3
python assets/sampling.py rhythms 2
python assets/sampling.py pov_distances 1
python assets/sampling.py time_handling 1
python assets/sampling.py scene_shapes 1
```

Accept the rolls. The point of randomness is to surface combinations the model wouldn't pick. Only cull a roll if it is genuinely incompatible with the scene context.

Compose a markdown card with the locked parameters and one short rationale sentence per axis tying the choice to the scene. End with a one-line note: *"The writing agent treats every parameter above as a hard contract."*

Save to `output/scene-params-[scene-tag].md`.
