---
name: scene-parameters
description: Lock scene-level stylistic axes before drafting, by rolling random selections from a vocabulary file. Triggers include "scene parameters", "lock parameters", "scene fingerprint".
---

Read the scene context the user provides. Note any user-locked axes (e.g., "POV must be close") and skip the roll for those.

For each unlocked axis, run `assets/sampling.py`:

```
python assets/sampling.py senses 3
python assets/sampling.py rhythms 2
python assets/sampling.py pov_distances 1
python assets/sampling.py time_handling 1
python assets/sampling.py scene_shapes 1
```

Compose a markdown card with the locked rolled parameters and one short rationale sentence per axis tying the choice to the scene.

Keep your card under 100 words.

Save to `output/scene-params-[scene-tag].md`.
