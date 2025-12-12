# Prompts for Dark Fantasy Worldbuilding

## 1. 'World' Prompt

<!-- Each setting must include at least 3 of these elements:
**Decaying/Ruined World**
**Gothic Architecture**
**Subterranean/Underground Spaces**
**Castle/Fortress as Central Location**
**Hostile/Cursed Wilderness**
**World Under Dead/Dying God**
**Post-Apocalyptic Elements** -->

Hey Claude, I want you to generate 10 dark fantasy settings. Each setting should be atypical or untried in the genre.
Tag Constraint: I've attached a json array of 10 sets of 'tags'. Each of your generated settings must feature, include, or be based on each set of tags in the array, in order. For example, if the first set of tags is ["blood-drinking forest", "veggie-folk villages", "graveyard city"], your first setting must incorporate those three elements.
Output Format: Provide your settings in a json "worlds" array. Each setting should be an object with one property: "description" (2-3 sentences elaborating on the setting - but do not name the settings).
Quality Constraint: Remember, these settings should appear distinct or rare in dark fantasy. Take your time with this task.

## 2. Revision Prompt

Hey claude, I want you to play a role. You are a young adult in the late 90s, with a love of all things fantasy - especially those that will influence/become 'dark fantasy'. Princess Mononoke, Willow, The Dark Crystal: these films are your foundation. You love Conan, both the movie, and Howard's original stories. The Book of the New Sun, The Black Company series, and The Dark Elf Trilogy are all perfect to you. You play the Gauntlet, Dialbo, and Castlevania series obsessively.
You're given the attached set of ten world/lore settings for a new dark fantasy novel. After reading through the list, you're asked to pick the three that you find most interesting. Which three do you pick? Why?

2. Follow-up Prompt (for distinct locations):

For each setting, generate 3-5 specific locations where a contained story could unfold.
Maintain the same creative standard as the settings themselves. Each location should feel like it could anchor its own narrative.
Naming rules: No name should describe its function or theme. Avoid [Descriptor] + [Place Type] (no "Bone Market," "Shadow Tavern," "Corpse Garden"). Prefer: unexplained proper nouns, place-names that sound inhabited (Kethval, Thornwick), or simple words used strangely (The Asking, The Dangle).
Anti-examples for a skeleton-themed setting: "The Marrow Shrine," "Ribcage Tavern," "The Bone Quarter." These explain themselves. Don't do this.

3. Generalized Prompt Template (for other elements):

Generate [NUMBER] distinct [ELEMENT TYPE: characters / creatures / themes / plot hooks] for dark fantasy.
Quality anchor: Each should feel hand-crafted—distinctive enough to be memorable, specific enough to use, and resistant to obvious genre patterns. If it could appear in a "generic dark fantasy generator," rethink it.
Naming rules (if applicable): Names should create questions, not answer them. Avoid [Trait] + [Role] patterns (no "Mad King," "Hollow Knight," "Cursed Wanderer"). Use names that feel like they belong to someone specific rather than a template.
Anti-examples: [Provide 2-3 examples of the generic output you want to avoid for this specific element type.]

The anti-examples are key—they give me a concrete floor to stay above. Good luck with the testing, man.

## Thorogood Revision

Can you rewrite the attached prose? I'm happy with the overall 'concept', but not the form. Please keep your rewrite under [TODO] characters. I'd like you to rewrite it, using the following guidelines.

**Guidelines:**

`1. Strip it to the skeleton`

- Note the core beats in plain language.
- Think “outline of a campfire story,”

`2. Set narrator and point of view`

- Bar-band storyteller talking to the crowd; or guy sitting next to you at a dive bar.
- Use 2nd person and a loose, talk-sung feel: something you could say over a 12-bar blues riff.
- Refer to the subject or listener as "buddy," "friend," or "man."
- Add the narrators own opinion, cynicism, or attitude to the story.
- Tip: Inject rhetorical questions or casual observations.

`3. Use barroom blues diction`

- Trade nouns for rock/blues images.
- Imagine taking a cathedral sermon and retelling it in a smoky roadhouse.

`4. Keep the rhythm punchy, not solemn`

- Short hits and stacked phrases; rely on a punchy, staccato beat (paratactic).
- Read it out loud; if it can’t ride on drums and slide guitar, tighten or rephrase.
- Tip: Break one long sentence into three short ones.

`5. Compress names into attitude`

- Collapse specifics into general types and keep just enough prose flavor.
- Save details for another “verse,” not the opening spiel.

## Peake Revision

Can you rewrite the attached prose? I'm happy with the overall 'concept', but not the form. Please keep your rewrite under [TODO] characters. I'd like you to rewrite it, using the following guidelines.

**Guidelines:**

`1. Slow the “camera”:` linger on one image and worry at it with added clauses and details, as though you are circling a single painting rather than filming an action scene.
`2. Animate the Inanimate:` rarely treat items, building, objects, etc as static. Give them agency and biological traits.
`3. Juxtapose the Elegant and Grotesque:` Mix high beauty with repulsion.
`4. The "Labyrinthine" Sentence Structure:` often use long, rolling sentences that utilize multiple clauses to build a sense of scale. Cut sentences short for emphasis.
`5. Precise Adjectives:` Layer concrete plus strange: start with a clear physical detail, then attach an unexpected metaphor or simile.
`6. Exploit sound and texture:` describe clicks, throbs, murmurs, roughness, gloss—let the reader almost hear and touch the place. Sound and texture often have physical presence.
`7. Lighting and Shadow:` Focus on how light interacts with objects.
`8. Micro-Focus on Movement:` describes movement in distinct, specific detail.
`9. Be specific but selective:` choose a few odd, striking details (one kind of movement, one colour, one smell) instead of many generic ones, like a painter choosing three strong pigments.
`10. Imply the uncanny rather than explain it:` show the cost, mood, or consequence of magic or curses, but don’t fully systematize them; let the world feel ancient, arbitrary, and slightly unknowable.

## Howard Revision

Can you rewrite the attached prose? I'm happy with the overall 'concept', but not the form. Please keep your rewrite under [TODO] characters. I'd like you to rewrite it, using the following guidelines.

`1. Elevate the Vocabulary (The "High Style")` - replace functional words with dramatic ones - mix archaic, biblical language with visceral, pulp descriptions.
`2. Use "Compound Adjectives"` - this packs a lot of description into a tight rhythm.
`3. Sentence Rhythm (Cadence)` - use long sentences connected by conjunctions (and, but) or broken up by dramatic pauses; don't just list facts, connect them with a sense of flow. Start sentences with prepositions or dramatic declarations.
`4. Anthropomorphize` - It makes the inanimate feel like a living, malevolent antagonist rather than just a background.
`5. Focus on Material and Sensory Contrast` - contrast beauty with horror, luxury with decay, etc. When describing something intangible, list three sensory details or effects; this creates rhythm and weight.
`6.` **Use concrete sensory language instead of explanation.** - make readers _feel_ the setting/character/text rather than _understand_ it logically. Keep your logic, but dress it in legend.

## Testing

### Claude Final

The rope remembers his hands—this is what the other monks whisper, though they do not stop to watch him pull. It hangs from the bell-mouth like a tongue gone grey with silence, fibrous and patient, and where his palms have worn it smooth the hemp gleams with a jaundiced light that the morning cannot explain.
He pulls. The motion is a pendulum's habit: arm rising, shoulder blade jutting beneath his robe like something trying to escape, then the long descent of weight transferred through rope to bronze to the bruised air of the tower. The bell speaks. A thick, arterial sound. It does not ring so much as hemorrhage into the valley below.
His eyes hold the color of rain pooled in old stone—present yet vacant, reflecting only what passes over them. The other monks have learned to step around him as one steps around a stain that will not lift.
But sometimes—mid-pull, mid-breath—a laugh climbs out of him. Thin. A child's laugh, unchanged by decades. It touches nothing on his face. It simply escapes, the way water finds cracks.
Beneath the bell, where shadow gathers thick as silt, he keeps a journal. He records the wind's direction. The angle of afternoon light across the flagstones. Which brother stood where. He does not know what pattern he is tracing. Only that his hands must move. Must hold something.
The rope broke once, in a story no one tells anymore.
He pulls anyway.

### GPT Final

Up the hill the tower squats in its own weather, a slab of stone that feels less built than grown, and from its throat hangs the bell—verdigris and swollen, a bruised green moon that drinks the daylight and gives it back as sickly sheen. The rope waits for you like a rough confession: fibers raised, damp with cold, biting your palms as you close your fingers, as you set your feet, as you draw breath and feel the tower lean in to listen.

You pull. Not hard—exact. The rope slides a thumb’s width, then catches; your knuckles blanch; the bell answers with a click and a rasp, metal on metal, a sound that crawls down the stairwell and out across the rock like a slow train, leaving iron on your tongue. The bell barely moves, only a careful sway, but its shadow lurches on the stones as if something inside it has shifted position.

Because you dropped it once. Because the tower remembers with the patience of stone. If the pitch comes out wrong—too high, too tight, not quite true—your knees unhinge, your thoughts loosen, and you wake up already swinging, already laughing that sharp, boyish laugh that doesn’t open your eyes. The others learn to grab you fast. Learn to keep their fingers clear.

When the last vibration dies, you sit beneath that green bulk with a little book laid on the cold floor like an offering, and the tower breathes dust around you. No blaming. Just marks. Wind. Footsteps. Who climbed the stairs. Your pen scratches—scratch-scratch—like a trapped insect in the wall, and the ink acts like it’s doing something permanent, even as the only thing the tower ever gives back is the next hour, waiting.
