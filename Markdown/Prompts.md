# Prompts for Dark Fantasy Worldbuilding

## 'World' Prompt

Hey Claude, I want you to generate 10 dark fantasy settings. Each setting should be atypical or untried in the genre.
Tag Constraint: I've attached a json array of 10 sets of 'tags'. Each of your generated settings must feature, include, or be based on each set of tags in the array, in order. For example, if the first set of tags is ["blood-drinking forest", "veggie-folk villages", "graveyard city"], your first setting must incorporate those three elements.
Output Format: Provide your settings in a json "worlds" array. Each setting should be an object with one property: "description" (2-3 sentences elaborating on the setting - but do not name the settings).
Quality Constraint: Remember, these settings should appear distinct or rare in dark fantasy. Take your time with this task.

LOCATION PROMPT:
Generate 10 specific dark fantasy locations. Each should be a single
place (a building, landmark, or geographic feature) - not a region or
city. Include one unusual physical or spatial property for each.
Output as JSON array: [{"location": "...", "property": "..."}]

THREAT PROMPT:
Generate 10 dark fantasy monsters or threats. Each must have a
specific behavioral quirk - not just what it is, but how it acts
or what it wants. Avoid generic undead, demons, or corrupted beasts.
Output as JSON array: [{"threat": "...", "behavior": "..."}]

RITUAL PROMPT:
Generate 10 social rituals or daily practices for a dark fantasy
society. These should be obligations, customs, or routines - things
people DO regularly. Avoid religious worship or obvious magical rites.
Output as JSON array: [{"ritual": "...", "purpose": "..."}]

COMPOSITION PROMPT:
Build a dark fantasy setting that incorporates all three elements below. The setting should make these elements feel connected - not just coexisting, but creating tension or meaning through their interaction.

Location: Thornspire Keep - All rooms share the same doorway—which door you enter depends on the emotion you carry
Threat: The Seamstress - Stitches sleeping victims into their own nightmares using thread spun from regret; victims wake paralyzed, living their worst memories on loop
Ritual: Hollow Pockets - Before sleep, all pockets and bags must be turned inside-out and shown empty, symbolizing one carries no hidden burdens into dreams

Output: A 4-5 sentence setting description. Include one strong visual image and explain why the ritual matters given the threat.

## Revision Prompt

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

## Bandcamp Review Prompt

Hey Claude, try revising the following album review in the thorogood style, 500 characters:
Been listening to Clann, and this album, for years; it's perfectly idiosyncratic, there's nothing I've found on all the seas that sounds quite like like music of faeries and sirens; bit of synth, never too heavy, with melancholy/eerie distorted vocals woven throughout; it's not happy or sad, it's uncanny - it's 10/10; wish they'd make more music though...

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

## Research Prompt

Hey claude, I want you drum up a large list of monsters, imaginary beasts, "fey" folk, and any other folkloric creatures attributed to the following geographic regions: TODO.

- Focus more on creatures which might have been part of [TIME-PERIOD] culture - avoid creature definitely attributed to modern influences.
- Avoid the "common" creatures that appear in every listicle or amateur review of TODO folklore (Common Examples: TODO).
- Focus your research on reputable primary sources: books by researchers, comprehensive studies, archeological/textual evidence from the period, etc.
- Entries should include names, descriptions, and at least one reference or where you found it.
- Some spirits or limnal entities are fine, but only if they have a specific regional term/name ('ancestor spirit' is too general).

## Location Prompt

Hey claude, you are a worldbuilding assistant. I will provide two documents:

1. **Location Baseline** – A structural description of a dungeon/location covering layout, flow, encounter placement, environmental features, and pacing.

2. **World Setting** – Documentation describing my fictional world, including its creatures, factions, architecture, geography, and tone.

Your task: Generate a new location description (~500 words) that preserves the _structural DNA_ of the baseline while translating all elements to fit my world.

**Translation rules:**

- Replace all creatures/enemies with equivalents from my setting (match threat level and role—e.g., "patrolling guard" stays a patrol, "swarm enemy" stays a swarm)
- Adapt architecture and environmental details to my world's aesthetics and geography
- Preserve the spatial flow: entry points, branching paths, chokepoints, verticality, and progression
- Maintain encounter pacing: where ambushes occur, reinforcement triggers, boss placement
- Match my prose style as demonstrated in the World Setting document
- Do not invent lore, factions, or creatures not present in my setting—ask if uncertain

**Output format:**
Organized by zone/section (like the baseline), prose-forward, minimal bullet points. Include brief notes on enemy types and key interactive features (traps, puzzles, environmental hazards) but omit specific loot.

---

**Location Baseline:**
see temp.md

---

**World Setting:**
see World.md

## Story Scaffold Prompt

Hey claude, I want you to help be write out a scaffold for a short story. My final goal is a fantasy story of 3-4 thousand words. I've attached three documents.

1. World.md: general info about the world I want to set the story in
2. Outline-Rite-of-Spring.md: the general 'structure' or 'template' I want the story to follow
3. Kelpshaw.md: The location in the world that I want to use as the specific backdrop/setting of this story

Basically, I want you to use these three documents to write out 'boilerplate' for me to follow, replacing your generic text with the actual story prose. My thinking is this: for each section, scene, or breakpoint, you'd specify things like:

- section word count
- character actions/emotions to show
- descriptions to write out
- questions to answer from prior scene
- questions to pose for next scene
- general sentence flow
- anything else you think is relevant? (Open to suggestions)

My goal is to have as much detail as possible in this scaffold. A step-by-step series of paragraphs/beats/elements to write for each scene would be ideal. Basically, taking away the overhead of knowing when I need to reference a character, or set a stage, and focusing on the actual literary 'implementation'.

Does this make sense, and is this something you can help with?

## Revision (Mervyn) Prompts

### GPT

Write a descriptive passage in a slow, atmospheric, observational prose style.

Focus on:

- Extended sentences that accumulate detail through subordinate clauses and modifiers, occasionally punctuated by short, declarative sentences marking absence, change, or finality.
- Concrete, precise nouns paired with low-frequency but readable adjectives; favor texture, weight, and age over emotional language.
- Metaphors and similes grounded in physical resemblance, especially between natural phenomena and constructed or time-worn objects. Let metaphors enrich atmosphere rather than explain meaning.
- Environmental movement over human action: light shifting, weather pressing, materials decaying, animals inhabiting spaces once shaped by people.
- An impersonal, patient narrative voice that observes without commentary and implies history through erosion, vacancy, or residue rather than exposition.

Avoid:

- Modern idiom, casual phrasing, or overt emotional interpretation.
- High fantasy tropes, named characters, or explicit backstory.
- Metaphor stacking or lyrical excess that draws attention to itself.

The goal is prose that feels dense, deliberate, and quietly monumental, where time seems slowed and the setting carries more presence than any implied observer.

Now write a description of a celtic bronze-age king's feasting hall, with the trophies of slain monsters about the room, in this style.

### Claude

Write a descriptive passage in the following style:

**Sentence Structure:** Use long, winding sentences with multiple dependent clauses that delay resolution. Connect related observations with semicolons. Include rhythmic enumerations (lists of 4-6 elements joined by commas and "and"). Interrupt sentences with parenthetical asides that add texture. Vary this occasionally with shorter declarative sentences for emphasis.

**Vocabulary:** Favor archaic, rare, or unexpected words where common ones would suffice—words that feel slightly weathered or forgotten. Use precise technical terms for natural phenomena, architecture, or craftsmanship. Build compound adjectives that are sensory-specific (color-texture, shape-material). Avoid modern idiom entirely.

**Figurative Language:** Personify architecture and landscape as though they breathe, age, and act with intention. When using similes, reach for the unexpected or faintly unsettling—comparisons to disease, minerals, or ancient artifacts rather than obvious analogues. Treat light as a theatrical agent that selects, reveals, and transforms.

**Atmosphere:** Convey deep geological time—decay and growth measured in centuries, layers accumulating beneath layers. Blur the boundary between the living and the built. Use color sparingly but with compound precision. Create a sense of slow, deliberate observation, as though the narrator is pacing through the scene.

**Avoid:** Modern phrasing, cliché, rushed pacing, short punchy sentences as the default, obvious metaphors, and any sense of hurry. The prose should feel heavy with age and attention.

Now write a description of a celtic bronze-age king's feasting hall, with the trophies of slain monsters about the room, in this style.

## Research Archtypes Prompt

```
Hey claude, I want you to do a research project for a list of character archtypes specific to the {{MAIN_GENRE}} genre. I'm looking specifically for protagonist archtypes, not side/support characters. Anything from film, tv, literature, and video games is on the table, but the media must have been made before the year 2005. Precursors or 'forefathers' of the genre are acceptable. Try for 8-12 archtypes, but do not pad the list with non-protagonists if you can't distinguish 8-12. You can include the following related genres in your research: {{INCLUDED_GENRES}}. But exclude {{EXCLUDED_GENRES}}.
Your final report should be in markdown format. Each archtype should have its own section. For each archtype, include 2-3 example characters, core elements, distinguishing features, and what makes it a {{MAIN GENRE}} archtype. At the end of the report, you should include a comparative analysis table, contrasting the general defining features of the genre's archtypes against traditional genre ones.
```

## Image Generation Prompt

Can you help me diagnose a prompting problem I'm having? I gave you the two prompts below in priors chats. The first one produced exactly what I wanted. I have adjusted the second half-a-dozen times, but you consistently refuse to output an image in the desired 2.5D style (no pixel sprites, no retro video game look). Can you explain why?
Prompt 1:

```
I want you to generate an image. IT should be a still first-person 2.5D dungeon crawler with chunky pixel-art: a blocky 3D world textured in low-res pixels, populated by billboarded 2D sprites, lit like a moody 90s FPS. In the still, there should be a pixel-art flail in the left hand, and the view should be looking down two long rows of 2D pews in a dark fantasy church, with skeleton sprites emerging from the darkness.
```

Prompt 2:

```
I want you to generate a still from a first-person 2.5D dungeon crawler with chunky pixel-art. It should look like a blocky 3D world textured in low-res pixels, populated by billboarded 2D sprites, lit like a moody 90s FPS. In the still, there should be a pixel-art sword in the left hand, and the view should be looking down a long row of 2D columns in a dark fantasy burial mound. There should be two gargoyle sprites emerging from the darkness. Any 2D sprites should be low-res.
The still should look like a low res screenshot from a 2.5D video game (Examples: Doom, Hexen, Shadow Warrior)
This is a still frame from a retro first-person 2.5D dungeon crawler video game.
The environment is rendered as a blocky 3D space with low-resolution pixel textures.
All enemies are flat, billboarded 2D sprites that always face the camera, with visible pixel grids and limited color palettes.
In the still, there should be a pixel-art longsword in the left hand, and the view should be looking down a ruined interior space resembling a Celtic burial mound. The walls are rough stone, a long and tall hall extending into the black background, with a long upper ledge on one side.
There are threey sprites, one crouched on the long ledge, two huddled on the floor. The sprites resemble gargoyles, hunched on all fours, with jade eyes.
The still should look like a low res screenshot from a 2.5D video game (Examples: Doom, Hexen, Shadow Warrior)
```

## JSON Conversion Prompt

```
Hey claude, take a look at @Markdown\temp.md and @Elements\archtype-example.json. I want you to use the info in temp.md to create a new json object in the structure shown in archtype-example.json. You should strive to be as generic as possible, with each attribute of the json object reflecting the most common pattern among characters in the Space Opera genre which fit this archtype. Be brief with your attributes: 1 word if possible, no more than 4 when *some* elaboration is called for. In cases where there is no 'fixed' attribute value in the genre, put "Example: attributeValue" with a common feature of characters in the genre.
Before you start, do a quick web search for "Space Opera [THE NAME OF THE ARCHTYPE]" so you have points of reference.
Output only your json object when you are finished.
```

## Conversion Prompt

Hey claude, take a look at the json I've pasted below. This is a breakdown of the 'wise woman' archtype of cozy/cottage fantasy. I want to take this archtype, and basically convert/pervert it to fit a dark fantasy story, and dark fantasy features. I want this conversation to be a back/forth between you and me, with you acting as a springboard. The final result would be a json template, similar to the one below, but for my new 'dark fantasy archtype',with some fields adjusted, some fields left the same, some fields much more fleshed out.
Before we start, do a quick web search on the follow characters, so you have an broader context of the archtype's defining traits:

- Kiela from The Spellshop by Sarah Beth Durst
- Granny Weatherwax from the Discworld Series
- Sylvie and her mother and grandmother from Healer and Witch by Nancy Werlin

Also, here are some defining dark-fantasy features we're shooting for:

| Feature                   | Dark Fantasy Protagonist Version           |
| ------------------------- | ------------------------------------------ |
| **Motivation**            | Survival, profit, vengeance, curiosity     |
| **Moral framework**       | Situational, amoral, or inverted           |
| **Relationship to magic** | Corrupting force, enemy, or costly bargain |
| **Community**             | Isolated, bonds are temporary or fatal     |
| **Character arc**         | Stasis, corruption, or doom                |
| **Victory condition**     | Personal survival, pyrrhic triumph         |
| **Divine relationship**   | Gods are absent, hostile, or manipulative  |

JSON:

```
{
      "type-name": "The Village Wise Woman",
      "values": [
        "community",
        "duty",
        "tradition"
      ],
      "default-personality-trait": "Pragmatic",
      "default-argument-tactic": "knowing silence",
      "primary-motivation": "service",
      "self-revelation": "care is its own reward",
      "false-philosophy": "must solve everyone's problems",
      "false-goal": "earn community's gratitude",
      "fears": {
        "open": "failing those in need",
        "hidden": "becoming obsolete"
      },
      "social-problem": "unacknowledged labor",
      "specific-desire": "Example: heal the sick child",
      "greatest-weakness": "pride",
      "corresponding-strength": "competence",
      "rules-for-living": [
        "'don't meddle unnecessarily'",
        "'know when not to act'"
      ],
      "special-skills": [
        "herbalism",
        "headology",
        "midwifery"
      ]
    }
```

## Character-Description Prompt


Hey claude, I'm giving you a setting overview for my Whyneland story setting. Along with that, I have some CURRENT DETAILS about a character which influence his physical description. Using that information, as well as the GUIDELINES below, I want you to 'fill out' the *physical* description of the character. Rely on my pre-written details, and use the GUIDELINES to write the rest. The description must address all of the GUIDELINES, but may integrate them fluidly rather than sequentially.

### CURRENT DETAILS:
- The symbolic animal should be a `ANIMAL`
- The character should me male
- He should be a `PROFESSION`
- `ADDITONAL`

### GUIDELINES:
- [symbolic_animal] - influences exactly three to four elements: gait, one facial feature, one equipment piece, and optionally one additional detail (posture, hands, voice, etc.)
- [gender]; [rough_age]
- [height]; [build]; [stance] (build/stance should be uncommon)
- [skin_tone]
- [hands]
- [hair]- style/color/condition
- [face] - nose/mouth/brow; [eyes] - color/shape
- [expression]
- [voice]
- [movement] - gait/gestures
- [sound] - caused by movement/gear; [smell] - breath/general-odor
	- Must generate one of these
- [equipment] - exactly one element below must be an idiosyncratic, highly-identifiable symbol
	- clothing
	- any tools/weapons
	- any headwear
	- any footwear
	- any bags/backpacks
	- any other possessions or personal effects
	- *Name specific materials — wood types, fabric weaves, metal alloys, etc.*
	- *Describe equipment in spatial layers, not as a list*
- COLORS: Avoid primary colors and generic terms. Use compound-colors or specific shades
- ASSYMETRY: Include one physical asymmetry, old injury, and/or uneven equipment wear pattern
- METAPHOR: Use one or two 'as if' or 'like' constructions to anchor abstract qualities in physical causes or animal comparisons
- **DO NOT SPECIFY**: anything that cannot be inferred by the senses (not 'a warrior' or 'an evil man')
**The Final Description should be between 250 and 500 words**

## Character-Story Prompt

Hey claude, I want to test your ability to come up with a concrete story, given a generalized character. I have attached a json file containing all the context you will receive about the character. It includes a description, and a series of actions which the character performs in the story. Note: these actions are not "plot-steps" - they are the key things the character does, nothing else. 
Given only this context, you task is to create a 1-2 paragraph story summary, for a specific story involving this character. You should strive to make the plot as concrete and detail-focused as possible. Use the methods below, along with your own knowledge/ideas, to guide your approach:
- Replace generic words or terms with specific ones (For this attempt, for names/words, rely on the other two json docs I've attached to this request)
- Add proper names where appropriate
- Fill in missing plot gaps (where the character is not directly acting, but which are significant jumps between their actions) by inventing intermediate events, or by adding 'time passed'-style summaries
- Add relationship types: "noble daughter" or "chieftain" could be further specified (ally, obstacle, mentor, rival)
- Sprinkle in a few weather, smells, sounds, or other sensory groundings - but keep the summary terse

And for the purposes of this test:
1. This protagonist is `REPLACE - MORALITY` and the story is `REPLACE - tragedy, heroic, melancholy`
2. The story length is `REPLACE - rough word count`
3. The story timeframe is `REPLACE - hours/days/weeks/months/years`

Aside from these guidelines/constrains, you have total creative freedom. When you are finished, output 2 things in the chat:
1. The resulting story summary
2. Any assumptions you made, or specific story/setting directions you chose
3. Any suggestions for additional guidelines I could specify in my prompt above when describing how to add concrete detail.

## Quote Generation Template

*Note to self: 5-7 quotes for automation*

Hey claude, info below:

Attachments:
- `character.json` — character context
- `templates.json` — quote templates

Pick one template. Write one quote spoken by this character. The quote must:
- **Follow the template structure exactly**
- **Express a core belief, principle, or pivotal decision**

**Brevity over clarity**. Output only the quote and template number.

```
Hey claude, I have a test for you. Take a look at the attached character.json file. Assume that this is all the context you have about a character: a physical description, and a list of actions they take in a story. temp.json is a list of "quote templates". Each template is a guideline for writing a core/personality/decision-defining quote spoken by a fictional character.
*Your test*: pick `two` quote templates; write `two` quotations spoken by the character.
*Guidelines*:
- Quotes should fit the character (given your available context)
- Quotes should express some fundamental belief, guiding principle, or pivotal story decision made by the character
- Quotes `Must adhere` to all specifications in the template
- Quotes should prioritize `brevity` over clarity
- Aside from these constraints, you have creative freedom
*Desired Output*:
- Your two quotes
- The templates you chose
- Any assumptions or critical choices you made.
```

## Quote Extraction


Hey claude, I'm looking for real-life historical persons with a distinctive 'voice' or   
  'speech architecture'. I'm not talking about accent, I'm talking about word choice,      
  syntax, sentence organization and structure, etc.
  Lets dive into Werner Herzog. I want you to extract a massive list of quotes by him      
  from interviews and other text sources. Do a web search. Your goal is 30+ individual     
  quotes. Try to get a good variety of lengths and context: a true sample set of his       
  'verbal DNA' (at least, what the public sees).


## Style Skill Prompt

Hey claude, Analyze [AUTHOR/STYLE] and complete the attached Style-Guide markdown template.   

  CRITICAL INSTRUCTIONS:

  1. **Teach principles, not patterns.** For each section, explain WHY the style works, not just WHAT it looks like. The reader should be able to generate infinite variations, not copy surface features.

  2. **Avoid finite lists.** Instead of "use these 5 verbs," explain the *type* of verb and *why* that type fits. Give examples as illustrations, not as a vocabulary bank to rotate through.

  3. **Name the underlying engine.** What is the author trying to achieve emotionally or atmospherically? How does each technique serve that goal? A technique without its purpose becomes a hollow template.

  4. **Contrast with defaults.** Where does this style diverge from generic prose? What would an imitator get wrong by following surface patterns without understanding the logic?

  5. **Be specific about the WHY in Antipatterns.** Don't just say "avoid X." Explain what trap an imitator falls into and why it betrays the style's core intent.

  Ground every principle in concrete examples from the source material, but frame those examples as *evidence* for a larger technique, not as templates to copy.

  REFERENCE TEXT:
  The attached work-sample markdown file is source material from [AUTHOR].
  Use it as PRIMARY EVIDENCE for your analysis.
  Ground every technique you identify in specific examples from this text. 
  Do not summarize or continue this text; analyze it.