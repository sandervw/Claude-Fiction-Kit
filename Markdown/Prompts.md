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

I want you to rewrite the following notes I have for an album review. I'd like you to keep your rewrite under 500 characters long. Rewrite it using the guidelines pasted below.
"review_text": "Porkchops instantly healing HP, the first castle you build out of cobblestone, that dog you tamed, the nether update - if you're late 20s/early-30s and this isn't the soundtrack to your chilhood, then I don't know what to tell you. You got the short end of the parent stick."

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
