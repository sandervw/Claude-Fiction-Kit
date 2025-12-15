# Working Doc for Creative Writing Tests

## Method 1: Cross-Model Anti-Pattern Identification

### Prompts

```
Do me a favor. I've got this attached outline for a story setting/character. I need to come up some ideas for potential, specific scenes in a story involving this character. Think you could give me a list of 10 or so 2-3 sentence scene ideas for this character, for a story taking place in my hanging-fortress world?
```

```
Analyze these scene concepts. Identify:
1. Recurring structural beats (e.g., "revelation interrupted," "must face fear")
2. Familiar genre tropes being invoked
3. Predictable cause-effect patterns
4. Emotional beats that feel "expected"

Be specific. Name the pattern, not just "cliché."
Output your results as a json array of objects, with a 'pattern-name', 'description' (be brief), and 'explanation' of why it's predictable.
```

### First Tropes

Generated 3 batches of 10 scenes w. Claude, GPT judged, Gemini grabbed the most common.

AVOID THESE SCENE PATTERNS:

- **Trauma-Triggered Outburst**: A protagonist suffering from PTSD or conditioning involuntarily reacts with violence or panic to a benign sensory trigger, such as a sound or touch.
- **The Interrupted Revelation**: A witness or ally is on the verge of revealing the truth but is silenced by an alarm, injury, or sudden danger before they can speak.
- **Sabotage Discovered via Duty**: The protagonist performs a dangerous or hated task and conveniently finds physical proof of tampering.
- **Institutional Gaslighting**: Authority figures or experts nervous about the "official story" use disciplinary meetings or soft warnings to intimidate the protagonist and hide the truth.
- **The Corrupted Artifact**: A sacred, ceremonial, or innocent object (such as a gift or research cache) is revealed to be a weapon, evidence of guilt, or a sign of moral rot.
- **Public Social Exile**: A public ceremony is disrupted by the protagonist, turning the community against them and forcing them to investigate alone.

### Second Tropes (TODO)

Generated 3 batches of 10 scenes w. GPT, Gemini judged, Claude grabbed the most common.

## Method 2:

Have claude call random_tags.py in Elements folder, randomly grab 3 tags from SCENE list, incorporate into scene

## Method 3:

Have claude call random_tags.py in Elements folder, randomly grab 3 tags from EMOTION list, incorporate into scene

Add to prompt:

```
EMOTIONAL REGISTER: [specific underrepresented tone]
The scene should NOT build toward dramatic release.
The tension, if any, should remain unresolved and low-grade.
```

## Method 4:

```
[Model A: Draft] → [Model B: Revise] → [Optional: Model A: Polish]
```

### Phase 1: Generation (Model A)

- Include all constraints (anti-patterns, random seeds, style parameters)
- Request raw draft, not polished output
- Specify: "Prioritize unexpected choices over polish"

### Phase 2: Revision (Model B)

- Provide original constraints + Model A's draft
- Prompt:

```
Revise this draft. Preserve any genuinely unexpected elements.

Your revision should:
1. Identify and cut any moments that resolve too neatly
2. Find places where the prose explains too much — leave gaps
3. Replace any phrasing that feels like "default LLM voice"
4. Maintain the required elements from the original constraints

Do not smooth over weirdness. Amplify it.
```

### Phase 3: Polish (Optional, Model A)

- Return to original model for final pass
- Focus on line-level prose, not structure
- Constraint: "Do not add new plot beats or revelations"
