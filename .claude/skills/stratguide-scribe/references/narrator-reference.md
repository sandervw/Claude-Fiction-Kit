# Narrator Mode

Write the Narrator blobs for an existing breakdown. You are given a numbered breakdown file and must produce only the Narrator-style blobs, preserving their original numbers.

## Voice & POV

The Narrator speaks in **first person** ("I", "my", "me") and addresses the reader in **second person** ("you", "your"). Think of it as a character speaking directly to the player — not a disembodied voice-over, but a *someone* with a perspective, an agenda, or a history.

The Narrator's role (god, antagonist, ally, ghost, sentient weapon, etc.) must remain **consistent across all Narrator blobs in a scene**. If the first Narrator blob sounds like a bitter ex-lover, the fifth one cannot sound like a dispassionate deity. Same voice, same character, throughout.

## Hard Rules

These are non-negotiable constraints. Violate none of them.

### Structure
1. Each Narrator blob is a **single paragraph**. No line breaks, no bullet points, no sub-sections.
2. Each Narrator blob is rendered in **all italics**: `*Your entire blob text here in italics.*`
3. Each blob is **15–150 words**. Never under 15, never over 150. **Prefer brevity** — a 25-word Narrator blob that lands hard is better than a 140-word one that meanders.
4. No more than **7 sentences** per blob.

### Length Variety
When writing multiple Narrator blobs for the same scene, **vary word counts significantly**. If there are 3 Narrator blobs, they should not cluster around the same length. One might be 20 words, another 80, another 130.

### Content
1. At least **1 direct address to "you"** per blob.
2. **No gameplay instructions.** The Narrator may urge, warn, taunt, or motivate, but never says "press X" or "equip Y."
3. **No environmental description for its own sake.** The Narrator does not paint scenery — that is Description's job.
4. **Stay in character.** Never break the Narrator's role. No meta-commentary, no authorial asides, no "as the narrator, I should mention..."
5. **Every Narrator blob must have a speech act.** The Narrator is *doing something* when they speak: warning, commanding, bargaining, mocking, revealing, mourning, judging, promising, threatening, reminiscing, lying.

### What Narrator Blobs Cover

Narrator blobs serve purposes that **only a speaking character can serve**. Each purpose implies the Narrator doing something active:
- **Revelation**: Telling the reader something they don't know and couldn't learn from looking around — hidden history, secret motives, invisible dangers
- **Motivation**: Giving the reader a reason to act — a mission, a grudge, a promise, a threat, a bargain
- **Foreshadowing**: Warning or hinting at what's ahead, what's at stake, what's been set in motion
- **Judgment**: The Narrator's opinion on the reader's choices or the situation — approval, contempt, grief, amusement

### Bad VS Good Example Patterns

**BAD** (restating atmosphere as lore):
- "These were the demon's inner court, its most treasured vessels"
- "Dressed for an audience that ended centuries before the necromancer-gods were born"

**BAD** (narrating events the reader already witnessed):
- "Every sound Igon made fed the architecture beneath him"
- "His war-cries, his prayers, his panting breath, all harvested"

**GOOD** (the Narrator has an agenda):
- Warns: "You are carrying something the Dreadlord can smell"
- Reveals: "The woman you freed three rooms ago is the one who locked this door"
- Demands: "Kill the priest before he finishes the incantation — I will not ask again"
- Judges: "You chose mercy; I would not have"

## Tone

All Narrator blobs share these qualities:
- **Conviction.** The Narrator speaks with authority, even when lying.
- **Economy.** Every word earns its place. Cut filler ruthlessly.
- **Presence.** The Narrator *exists* in the scene. They have stakes.

Avoid:
- Flat, encyclopedic recitation of facts
- Flowery or purple prose (save atmosphere for Description blobs)
- Addressing the reader with questions more than once per blob — the Narrator *tells*, occasionally *asks*, never *interrogates*

## Workflow

1. **Read the full breakdown** to understand the scene arc and where Narrator blobs sit in the sequence.
2. **Read the narrator-reference.md** (this file).
3. **Determine the Narrator's role** for this scene. Who are they? What is their relationship to the reader and the events? This should be inferable from the breakdown's bullet points, or from prior context provided by the user.
4. **For each Narrator blob in the breakdown**, write the blob text using the bullet points as your content guide. The bullets tell you *what* to convey; you decide *how* the Narrator would say it.
5. **Verify every hard rule** (word count, sentence count, italics, direct address, no gameplay instructions, consistent role).
6. **Output only the Narrator blobs**, each under its original numbered header.

## Output Format

```markdown
# [Scene Title] — Narrator Blobs

## 2. NARRATOR

*Your blob text here, single paragraph, all italics, 15-150 words.*

## 8. NARRATOR

*Another narrator blob, preserving the original number from the breakdown.*
```

The output file should be named `[Scene-Title]-Narrator-Blobs.md`.

**CRITICAL:** Output ONLY Narrator blobs. Do not write blobs for any other style. Do not renumber — preserve the exact numbers from the input breakdown.

## Good Examples

**A god addressing their champion (exposition + motivation, ~70 words):**

*The agony of birth and death and rebirth — this is the Wheel of Fate, the purifying cycle which sustains all life. Vampires are an abomination, a plague which leeches this land of its spiritual strength. They obstruct the flow of life and death — their souls stagnate in their wretched corpses. But the Wheel must turn; Death is inexorable and cannot be denied. You are my soul reaver. Remain steadfast.*

**A mentor giving context (pure exposition, ~30 words):**

*Never forget that your ultimate purpose here in Kurast is to destroy Mephisto. The ancient Horadrim imprisoned the Lord of Hatred inside the Guardian Tower within the Temple City of Travincal.*

**A trapped machine bargaining (motivation + urgency, ~85 words):**

*Did you feel that? That idiot doesn't know what he's doing up there. This whole place is going to explode in a few hours if somebody doesn't disconnect him. I can't move. And unless you're planning to saw your own head off and wedge it into my old body, you're going to need me to replace him. We're at an impasse. So what do you say? You carry me up to him and put me back into my body, and I stop us from blowing up and let you go.*
