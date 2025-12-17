# Working Doc for Creative Writing Tests

## Outline

Start with world generation - get it to generate 5 worlds you like - focus on trope identification/removal

- Make sure to generate some monsters, magic/tech, etc
- IDEA: when ranking, ask LLM to guess which fraction of ideas were human-generated (even though all AI)

Next: work on character generation

## Worlds (no constraints)

```
I want you to generate 6 dark fantasy world descriptions for me to use as setting for short stories. Output Format: Provide your settings in a json "worlds" array. Each setting should be an object with two properties: "name" (a 1-3 word tag, no proper nouns/names) and "description" (2-3 sentences elaborating on the setting - but do not name the setting in the description either).
```

```
Analyze these dark fantasy setting/world ideas. Identify:
1. Recurring thematic elements (e.g., "corruption of the sacred," "monster within")
2. Familiar genre tropes being invoked
3. Predictable world features
4. lore or environments that feel "expected"

Be specific. Name the pattern, not just "cliché."
Output your results as a json array of objects, with a 'pattern-name' (1-4 words) and 'description' (be brief).
```

```
I want you to generate 6 dark fantasy setting descriptions that I'll use for short stories.
`Tag Constraint`: Each of your generated settings must feature, include, or be based on 3 tags from the attached tags.json file
`Theme Constraint`: Avoid the following themes/tropes:
- **Scavenger Economy**: Societies no longer produces, it surviving by harvesting grim resources from ruins, corpses, or catastrophe.
- **Vertical Class Stratification**: Society is physically stratified by height: the further down one goes, the more strange or threatening the world becomes.
- **Colossal Corpse Geography**: Giant dead things (gods, leviathans, trees) forming the literal terrain.
- **Perpetual Dimness**: Twilight, dying suns, failed light sources as default atmosphere.
- **Identity/Sanity Erosion**: Threats that attack selfhood rather than just bodies.
- **Absent Authority**: Gods, rulers, or creators are dead/missing, leaving broken systems.
`Output Format`: Provide your settings in a json "worlds" array. Each setting should be an object with these properties: "name" (a 1-3 word name, no proper nouns/names), "description" (2-3 sentences elaborating on the setting - but do not name the setting in the description either), and "tags" (an array).
```

## TODO

## Final Edits

Final prompt edit ideas:

- clean up unrealistic dialogue
- replace comon verbs/adjectives
- remove parallel construction

For next scene:

- Extract 1-2 sentence summary
- Extract questions
- Extract 1 character detail
- Extract 1 plot beat?
