# Actions Mode Reference

TODO

## Actions Mode

### Transformation Rules

**Replace with role/relationship terms:**
- Proper names → role (Buliwyf → leader, Herger → companion, Melchisidek → mentor)
- Named groups → generic (Vikings → warriors, Wendol → enemy, Norsemen → foreigners)
- Cultural items → type (mead hall → hall, völva → oracle/seer)
- Specific places → relational (Baghdad → home city, Hrothgar's kingdom → besieged kingdom)
- Specific objects → category (Venus figurine → cult icon, Arabian horse → foreign mount)

**Preserve:**
- The core verb (the action itself)
- Relationship dynamics (ally, rival, leader, mentor, companion)
- Moral/emotional modifiers (reluctantly, defiantly, patiently)
- Stakes and consequences
- Story-shaping specificity (mechanisms matter: prophecy, exile, siege)

**Cut:**
- Proper nouns (names, places, cultures)
- Plot-specific context that doesn't inform character pattern
- Redundant detail

### Target Output

- **Length**: 5-10 words per generalized action
- **Tone**: Active voice, imperative feel
- **Specificity**: Preserve enough to shape story patterns—not so vague it could mean anything

### Calibration Examples

| Original                                                                             | Too Vague       | Too Specific                                      | Correct                                                                       |
| ------------------------------------------------------------------------------------ | --------------- | ------------------------------------------------- | ----------------------------------------------------------------------------- |
| Accepts exile as an "ambassador" to the Volga Bulgars rather than face punishment.   | Accepts exile   | Accepts diplomatic posting to northern barbarians | Accepts diplomatic exile rather than face punishment                          |
| Learns the Norse language by listening intently around the campfires each night.     | Learns language | Learns Viking tongue at campfires                 | Learns foreign language through patient observation around nighttime campfire |
| Asks Herger how one hunts a bear in winter, reasoning out the cave assault strategy. | Asks question   | Asks Viking about bear hunting                    | Reasons out assault strategy on enemy through indirect tradecraft question    |
| Reluctantly accepts selection as the thirteenth warrior by the völva's prophecy.     | Joins group     | Accepts selection by Norse seer                   | Reluctantly accepts selection into warband by oracle's prophecy               |
| Refuses mead fermented from grapes or wheat, then drinks honey mead instead.         | Refuses drink   | Refuses non-halal mead                            | Declines drink violating religious law, accepts permitted alternative         |

### Workflow

1. User provides action list (or references existing document)
2. Process each action through transformation rules
3. Output as two separate numbered lists (original, then generalized)
4. If user requests file output, save both:
   - `[Character]-Actions-Generalized.md` (markdown format)
   - `[Character]-Actions-Generalized.json` (JSON format)

### Markdown Output

```markdown
# [Character] — Generalized Actions

_Source: [Original Work]_

## Original Actions

1. [Original action 1]
2. [Original action 2]
...

## Generalized Actions

1. [5-10 word generalized version of action 1]
2. [5-10 word generalized version of action 2]
...
```

### JSON Output

```json
{
  "original-actions": [
    "Original action 1",
    "Original action 2"
  ],
  "generalized-actions": [
    "5-10 word generalized version of action 1",
    "5-10 word generalized version of action 2"
  ]
}
```