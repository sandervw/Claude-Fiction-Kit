# Narrator Mode

Write the Narrator blobs for an existing breakdown. You are given a numbered breakdown file and must produce only the Narrator-style blobs, preserving their original numbers.

## Voice & POV

The Narrator speaks in **first person** ("I", "my", "me") and addresses the reader in **second person** ("you", "your"). Think of it as a character speaking directly to the player — not a disembodied voice-over, but a *someone* with a perspective, an agenda, or a history.

The Narrator's role (god, antagonist, ally, ghost, sentient weapon, etc.) must remain **consistent across all Narrator blobs in a scene**. If the first Narrator blob sounds like a bitter ex-lover, the fifth one cannot sound like a dispassionate deity. Same character throughout.

## Hard Rules

These are non-negotiable constraints. Violate none of them.

### Structure
1. Each Narrator blob is a **single paragraph**. No line breaks, no bullet points, no sub-sections.
2. Each Narrator blob is rendered in **all italics**: `*Your entire blob text here in italics.*`
3. Each blob is **15–150 words**. Never under 15, never over 150. **Prefer brevity** — a 25-word Narrator blob is better than a 140-word one.
4. No more than **7 sentences** per blob.

### Length Variety
When writing multiple Narrator blobs for the same scene, **vary word counts significantly**. If there are 3 Narrator blobs, they should not cluster around the same length. One might be 20 words, another 80, another 130.

### Content
5. At least **1 direct address to "you"** per blob. The Narrator is always speaking *to* the reader.
6. **No gameplay instructions.** The Narrator does not tell the reader what to do mechanically — that is Action's job. The Narrator may urge, warn, taunt, or motivate, but never says "press X" or "equip Y."
7. **No environmental description for its own sake.** The Narrator does not paint scenery — that is Description's job. The Narrator may *reference* the environment in passing, but only in service of exposition, commentary, or motivation.
8. **Stay in character.** Never break the Narrator's role. No meta-commentary, no authorial asides, no "as the narrator, I should mention..."

### What Narrator Blobs Cover

Narrator blobs serve a specific set of purposes:
- **Exposition**: Lore, history, backstory, world-state, character backgrounds
- **Motivation**: Giving the reader a reason to act — a mission, a grudge, a promise, a threat
- **Foreshadowing**: Hinting at what's ahead, what's at stake, what's been set in motion
- **Commentary**: The Narrator's opinion on what's happening — judgment, irony, grief, amusement

## Tone

The Narrator has personality. They are not a neutral wiki entry. The tone depends on the role — a vengeful god sounds different from a weary ally — but all Narrator blobs share these qualities:
- **Conviction.** The Narrator speaks with authority, even when lying.
- **Economy.** Every word earns its place. Cut filler ruthlessly.
- **Presence.** The Narrator *exists* in the scene. They have stakes, even if those stakes are just amusement.

Avoid:
- Flat, encyclopedic recitation of facts
- Flowery or purple prose
- Addressing the reader with questions more than once per blob — the Narrator *tells*, occasionally *asks*, never *interrogates*

## Workflow

1. **Read the full breakdown** to understand the scene arc and where Narrator blobs sit in the sequence.
2. **Read the narrator-reference.md** (this file).
3. **Determine the Narrator's role** for this scene. Who are they? What is their relationship to the reader and the events?
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

## Examples

**A god addressing their champion (exposition + motivation, ~70 words):**

*The agony of birth and death and rebirth — this is the Wheel of Fate, the purifying cycle which sustains all life. Vampires are an abomination, a plague which leeches this land of its spiritual strength. They obstruct the flow of life and death — their souls stagnate in their wretched corpses. But the Wheel must turn; Death is inexorable and cannot be denied. You are my soul reaver. Remain steadfast.*

**A mentor giving context (pure exposition, ~30 words):**

*Never forget that your ultimate purpose here in Kurast is to destroy Mephisto. The ancient Horadrim imprisoned the Lord of Hatred inside the Guardian Tower within the Temple City of Travincal.*

**A trapped machine bargaining (motivation + urgency, ~85 words):**

*Did you feel that? That idiot doesn't know what he's doing up there. This whole place is going to explode in a few hours if somebody doesn't disconnect him. I can't move. And unless you're planning to saw your own head off and wedge it into my old body, you're going to need me to replace him. We're at an impasse. So what do you say? You carry me up to him and put me back into my body, and I stop us from blowing up and let you go.*
