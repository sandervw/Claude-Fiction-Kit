# High-Originality LLM Creative Output: Working Methodology

A practical guide for generating fiction prose that escapes statistical averaging.

---

## Method 1: Cross-Model Anti-Pattern Identification

**Goal:** Build a project-specific list of tropes/beats to constrain against.

### Phase 1: Generate Baseline Output

- Prompt Model A for 10 scene ideas (or character concepts, settings, etc.)
- Use minimal constraints — let it produce its "default" output
- Save raw output

### Phase 2: Pattern Extraction

- Pass output to Model B with prompt:

```
Analyze these scene concepts. Identify:
1. Recurring structural beats (e.g., "revelation interrupted," "must face fear")
2. Familiar genre tropes being invoked
3. Predictable cause-effect patterns
4. Emotional beats that feel "expected"

Be specific. Name the pattern, not just "cliché."
```

- Repeat 2-3 times with different seed generations

### Phase 3: Consolidation

- Compile all identified patterns into one list
- Pass to Model C:

```
From this list of identified patterns, extract the 5-10 most frequently recurring.
For each, provide:
- Pattern name (2-4 words)
- Brief description
- Why it feels predictable
```

### Output

A reusable "ANTI-PATTERN CONSTRAINTS" block for your project:

```
AVOID THESE PATTERNS:
- [Pattern 1]: [description]
- [Pattern 2]: [description]
...
```

---

## Method 2: Random Seed Constraints

**Goal:** Force divergent paths by requiring incorporation of arbitrary elements.

### Setup: Build Seed Pools

Create category-specific word pools. Examples:

**Objects:** moth wing, broken thermometer, salt crust, wax seal, copper wire, dried fig, chalk dust, glass eye, iron filings, leather cord

**Sensory Details:** metallic taste, subsonic hum, smell of wet stone, pins-and-needles numbness, pressure behind eyes

**Mundane Interruptions:** needs to urinate, stomach growling, itchy fabric, forgot someone's name, awkward silence

**Emotional Micro-States:** secondhand embarrassment, anticipatory regret, relief that curdles into guilt, boredom masking fear

### Implementation

For each generation request:

1. Randomly select 2-3 seeds from different pools
2. Add to prompt as hard constraints:

```
REQUIRED ELEMENTS (must appear meaningfully, not as throwaway mentions):
- [Random Object]
- [Random Sensory Detail]
- [Random Emotional Micro-State]
```

### Variation

For scene generation specifically, add a **structural seed**:

- "Scene must begin mid-action, no setup"
- "Scene ends before resolution"
- "POV character is wrong about what's happening"
- "The dramatic moment already happened; this is the aftermath"

---

## Method 3: Cross-Model Iteration

**Goal:** Use model differences to break out of single-model convergence.

### Workflow

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

---

## Method 4: Emotional Register Shifting

**Goal:** Request underrepresented emotional tones that LLMs rarely default to.

### The Problem

LLM training data over-represents: tension, revelation, triumph, grief, rage, fear. These are the "loud" emotions that drive published fiction.

### Underrepresented Registers

Request scenes built around:

- **Tedium** — waiting, repetition, nothing happening
- **Anticlimax** — the expected drama doesn't materialize
- **Secondhand embarrassment** — witnessing someone else's failure
- **Quiet wrongness** — something is off but unnameable
- **Obligation without meaning** — doing a task because it must be done
- **Recognition without understanding** — knowing something matters, not why
- **Exhaustion that precedes decision** — too tired to feel the weight

### Implementation

Add to prompt:

```
EMOTIONAL REGISTER: [specific underrepresented tone]
The scene should NOT build toward dramatic release.
The tension, if any, should remain unresolved and low-grade.
```

---

## Method 5: Structural Subversion (Scenes Between Scenes)

**Goal:** Request the moments stories typically skip.

### The Problem

LLMs optimize for "story-shaped" output — scenes with setup, escalation, climax. These are what training data rewards.

### Request Instead

- "The morning after he breaks someone's jaw"
- "Waiting for the meeting that will change everything — the waiting, not the meeting"
- "The walk back from the revelation, before processing begins"
- "The task that must be completed despite the crisis"
- "Two characters who should talk about it, choosing not to"

### Implementation

```
STRUCTURAL CONSTRAINT: This scene takes place [before/after/during] the dramatic beat, not at its peak.

The [revelation/confrontation/disaster] has [already happened / not yet happened / is happening elsewhere].

Focus on: [mundane action], [suppressed reaction], [displacement behavior].
```

---

## Recommended Testing Workflow

### Session 1: Build Anti-Pattern List

- Run Method 1 for your specific genre/project
- Output: Reusable constraint block

### Session 2: Build Seed Pools

- Generate or curate word pools for Method 2
- Test random selection mechanism
- Output: Category pools + selection process

### Session 3: Test Single Method

- Generate 5 scenes using Method 2 alone
- Evaluate: Which feel least predictable?

### Session 4: Test Combination

- Generate 5 scenes using Methods 1 + 2 + 4
- Compare against Session 3

### Session 5: Test Cross-Model

- Run Method 3 on best outputs from Session 4
- Evaluate: Does revision improve or homogenize?

### Session 6: Full Pipeline

- Combine all methods
- Document which combinations work for your style

---

## Quick Reference: Prompt Structure

```markdown
## ANTI-PATTERN CONSTRAINTS

[From Method 1 output]

## REQUIRED ELEMENTS

[From Method 2 random selection]

## EMOTIONAL REGISTER

[From Method 4 selection]

## STRUCTURAL CONSTRAINT

[From Method 5 selection]

## CONTEXT

[Existing prose from project, if available]

## TASK

[Specific generation request]
[Note: Output will be used as draft material, not final prose]
```

---

## Notes

- **Document everything.** Track which constraints produce interesting results.
- **Failure is data.** Boring output tells you what to constrain against next time.
- **Don't over-constrain initially.** Start with 2-3 methods, add complexity as needed.
- **The goal is seeds, not finished prose.** Extract fragments worth keeping; discard the rest.
