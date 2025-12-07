1. Adjusted Original Prompt (for distinct setting names):

Hey claud, I want you to generate 20 dark fantasy settings. Each setting should be less typical or never-tried in the genre. Each setting must include at least 3 of these elements:
**Decaying/Ruined World**
**Gothic Architecture**
**Subterranean/Underground Spaces**
**Castle/Fortress as Central Location**
**Hostile/Cursed Wilderness**
**World Under Dead/Dying God**
**Post-Apocalyptic Elements**
Tag Constraint: I've attached a json array of 20 sets of 'tags'. Each of your generated settings must feature, include, or be based on each set of tags in the array, in order. For example, if the first set of tags is ["blood-drinking forest", "veggie-folk villages", "graveyard city"], your first setting must incorporate those three elements.
Naming constraint: Names should raise questions, not answer them. Use unexplained proper nouns (Lordran, Yharnam), single evocative words (The Pale, Overmire), or unexpected pairings. Avoid patterns like [Thematic Adjective] + [Geographic Feature]—no "Bleeding Glacier" or "Cursed Swamp." If the name explains the setting, rename it.
Output Format: Provide your settings in a json array. Each setting should be an object with two properties: "name" (the generated name) and "description" (a brief paragraph describing the setting and how it incorporates the required elements).
Remember - these settings should appear distinct or rare in dark fantasy. Take your time with this task.
Do you have any questions before you start?

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
