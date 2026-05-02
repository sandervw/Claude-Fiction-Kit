# Creative Writing Toolkit — Implementation Plan

A set of Claude skills designed to combat LLM pattern-repetition in creative
writing. Intended to compose with the user's existing creative writing skills
(scene-writer, voice-revision, literary-revision, stratguide-scribe,
character-analysis, scene-idea-generator, story-idea-generator,
folklore-generator, etc.).

---

## 1. Context (for the implementing LLM)

### The user

Data engineer with extensive original worldbuilding (two settings: *Time of
Dying*, a dark fantasy "road of graves" world; *CorpLore*, a modern corporate
dark fantasy). Has built a substantial library of personal Claude skills under
`/mnt/skills/user/` that follow a consistent pattern: SKILL.md at the root,
optional `assets/` subfolder for scripts/data, modular reference files for
multi-mode skills.

### The problem these skills solve

LLM creative writing collapses into pattern-repetition even across
superficially different scenes. The user provided a concrete example: two
scenes from the same story, different settings and antagonists, but sharing:

- Identical simile cadence: `X like Y` constructions where Y is always
  domestic/mundane (`like old fruit leather`, `like dry kindling`,
  `like dice thrown on a table`, `like ripped parchment`)
- Repeated sensory beats (visor fogging inside helm, breath inside armor)
- Repeated staccato list cadence (`throat, chest, chest, skull`)
- Identical antagonist voice (clinical-curious, asks "what does it feel like"
  questions)
- Identical protagonist dialogue register (stoic-terse: "None of that.",
  "Be quiet.", "Come on then.")

The mechanism: when given negative constraints ("don't do X"), the model
shifts to the next-highest-probability mode and camps there. The probability
distribution doesn't broaden, the basin just relocates. Instructions like
"be more varied" fail by their nature — they ask the thing the model can't
do unprompted.

### The principle

**Force variety upstream of drafting.** Once prose generation begins, the
distribution is already collapsed. The fix is hard, specific constraints
locked in *before* the writing agent sees the scene — preferably with
randomness in the loop so the model can't bias selection toward its
defaults.

### Architectural decisions (already settled)

1. **Hard contracts.** Cards are not recommendations. The writing agent
   treats them as inviolable rules.
2. **Per-scene scope.** No cross-scene state tracking in v1.
3. **Subagent composition.** Each card-producing skill runs as a subagent.
   The main writing agent never loads these skill files into its context —
   it receives only the finished cards.
4. **Randomized selection where applicable.** Three of the four skills use
   a sampling script + JSON array pattern to roll choices, removing the
   model's ability to gravitate toward defaults during selection.

---

## 2. Architecture

### Subagent pattern

```
main agent (orchestrator + writer)
   │
   ├─ subagent: scene-parameters    → parameter card
   ├─ subagent: forbidden-patterns  → blacklist card  (predictive mode)
   ├─ subagent: source-imprint      → imprint profile + source paragraphs
   ├─ subagent: speech-rules        → speech card (per character)
   │
   ├─ drafts scene using cards (skill files NEVER enter this context)
   │
   └─ subagent: forbidden-patterns  → audit report   (verification mode)
```

The main agent's context contains only: scene context (provided by user) +
the cards returned by subagents. Skill instructions, sampling logic, and
JSON pools stay confined to the subagent that needs them.

### Sampling pattern

Three of the four skills (`scene-parameters`, `forbidden-patterns` in
predictive mode, `speech-rules`) use the same pattern:

```
{skill-name}/
├── SKILL.md
└── assets/
    ├── sampling.py          # unchanged copy of user's existing script
    └── vocabulary.json      # skill-specific arrays
```

`sampling.py` (provided by user) reads `vocabulary.json` from its own
directory and prints randomly-sampled elements from a named array:

```
python sampling.py <array_name> [n]
```

Each skill curates its own `vocabulary.json` with arrays appropriate to its
domain. The script is identical across skills; only the JSON differs.

**Why randomness:** The model cannot bias `random.sample()` toward its
defaults. Asked to "pick a sentence rhythm," the model will pick the same
one repeatedly. Forced to roll, it can't.

### Card format

Cards are JSON or markdown (skill-author's choice; markdown preferred per
user style). Each card includes:

- The locked parameters/constraints
- A short rationale tying choices to scene context
- Explicit "this is a hard contract" framing

Cards travel with the scene context to the writing agent.

### Skill file conventions

Match the user's existing skill conventions:

```
{skill-name}/
├── SKILL.md                 # YAML frontmatter + instructions
├── assets/                  # (optional) scripts and data
└── reference/               # (optional) modular reference files
```

`SKILL.md` opens with YAML frontmatter:

```yaml
---
name: skill-name
description: When to invoke this skill. Triggers include...
---
```

Followed by markdown instructions. For multi-mode skills, follow the
`stratguide-scribe` pattern: brief mode descriptions in SKILL.md, full
instructions in `reference/{mode}.md`.

---

## 3. Skill specifications

### 3.1 scene-parameters

**Purpose.** Lock scene-level stylistic axes before drafting, so each scene
has a different fingerprint by construction.

**When to invoke.** At the start of every new scene, before scene-writer or
any drafting skill.

**Inputs.**
- Scene context (premise, characters present, location, beat purpose)
- Optional: user-locked axes (e.g., "POV must be close")

**Output (card).** A markdown card with:
- **Sensory palette** — 2-3 senses from the rolled options
- **Sentence rhythm** — dominant + secondary
- **POV distance** — close / mid / distant
- **Time handling** — real-time / summary / scene-into-summary / fractured
- **Scene shape** — escalation / reversal / accumulation / deflation
- Brief rationale (one sentence per choice) tying it to the scene context

**Mechanism.**
1. Read scene context.
2. For each axis, run `sampling.py` on the matching array in
   `vocabulary.json`. User-locked axes skip the roll and use the locked
   value.
3. Cull obviously incompatible combinations only if necessary; otherwise
   accept the roll. The point of randomness is to surface combinations the
   model wouldn't pick.
4. Compose the card with rationale.

**vocabulary.json arrays (suggested seed; user will expand):**
- `senses`: sight, sound, smell, taste, touch, proprioception, temperature,
  kinaesthetic, balance, pain
- `rhythms`: long-coordinated, fragmented, paratactic, periodic, balanced,
  cumulative, periodic-with-interruptions, run-on
- `pov_distances`: close, mid, distant, sliding-close-to-distant,
  sliding-distant-to-close
- `time_handling`: real-time, summary, scene-into-summary, fractured,
  retrospective, anticipatory
- `scene_shapes`: escalation, reversal, accumulation, deflation, circular,
  parallel-thread

**Sampling calls:**
```
python sampling.py senses 3
python sampling.py rhythms 2
python sampling.py pov_distances 1
python sampling.py time_handling 1
python sampling.py scene_shapes 1
```

---

### 3.2 forbidden-patterns

**Purpose.** Per-scene blacklist of constructions the writing agent is
banned from using. Two modes: **predictive** (pre-writing, rolled from a
pool of common LLM tells) and **audit** (post-writing, scans a draft
against the blacklist and flags violations).

**When to invoke.**
- Predictive: before drafting, alongside scene-parameters.
- Audit: after a draft exists, as a verification pass.

**Inputs.**
- Predictive mode: scene context, optional user-specified additional bans
- Audit mode: draft text + the blacklist card from predictive mode

**Output (card).**

*Predictive mode:* markdown card with categorized bans. Categories
(matching the rolled subset):
- Simile/metaphor constructions banned
- Sentence cadences banned
- Syntactic tics banned
- Pet imagery banned
- Register slips banned

Each ban must be specific. Not "vary your similes" but "no similes
comparing decaying things to food." Not "fewer fragments" but "no isolated
fragment sentences."

*Audit mode:* markdown report listing each violation with line reference,
the offending text, and the rule it broke.

**Mechanism (predictive).**
1. Read scene context.
2. Roll subset (e.g., 5-8 items) from `vocabulary.json` arrays of common
   LLM tells.
3. Compose blacklist card. Treat as inviolable.

**Mechanism (audit).**
1. Read draft + blacklist card.
2. Scan systematically for each banned pattern.
3. Output report; do NOT rewrite. The main agent decides what to revise.

**vocabulary.json arrays (suggested seed; user will expand from observed
ruts):**
- `simile_bans`: "no `X like Y` similes where Y is domestic/food",
  "no similes comparing the dead to objects", "no `like a` constructions",
  "no extended metaphors longer than one sentence", ...
- `cadence_bans`: "no isolated fragment sentences", "no
  `not X, but Y` constructions", "no tricolon (rule of three) lists",
  "no staccato comma-list cadences (`throat, chest, skull`)", ...
- `syntactic_bans`: "no semicolons", "no em-dashes", "no parenthetical
  asides", "no negative-construction sentences (`he did not X`)", ...
- `imagery_bans`: "no visor-fogging or breath-in-helm imagery",
  "no glowbug/lantern-throwing-shadows imagery", "no
  dust-motes-in-light imagery", ...
- `register_bans`: "no clinical/scientific vocabulary in narration",
  "no archaic register if scene is modern", ...

The user should populate these from observed ruts. Seed values above are
illustrative.

**Sampling calls (predictive mode):**
```
python sampling.py simile_bans 2
python sampling.py cadence_bans 2
python sampling.py syntactic_bans 1
python sampling.py imagery_bans 2
python sampling.py register_bans 1
```

**Audit mode does not sample.** It scans against the existing card.

---

### 3.3 source-imprint

**Purpose.** Borrow rhythm, register, or syntactic shape from one or more
specific source paragraphs. Most powerful when the source is *outside the
genre being written* (e.g., imprinting Vance onto a corporate scene,
McCarthy onto a fantasy torture scene).

**When to invoke.** When a scene needs a deliberate stylistic break, or
when targeting a specific aesthetic that named-style skills (like
literary-revision) won't capture precisely.

**Inputs.**
- 1-3 source paragraphs (provided by user)
- Imprint scope: which features to borrow {rhythm, syntax, register,
  sensory mode, full}
- Scene to write or revise (optional at this stage; profile can be
  generated standalone)

**Output (card).** Markdown profile containing:
- The source paragraphs verbatim (travel with the card)
- 3-5 specific extracted features with concrete examples from the source:
  - Sentence-length distribution (e.g., "alternates 4-7 word sentences
    with 25-40 word sentences; no middle range")
  - Clause stacking patterns (e.g., "left-branching with parenthetical
    asides")
  - Register (e.g., "archaic, Latinate vocabulary; no contractions")
  - Dominant sensory channels
  - Signature tics (e.g., "frequent use of `even as`", "no semicolons,
    only commas and full stops")
- A short "do this / don't do this" derived rule list

**Mechanism.**
1. Read source paragraphs.
2. Extract features by direct observation, not by genre/author labels.
3. Compose profile.
4. Source paragraphs ride with the card into the writing agent's context.
   The writer references them directly.

**No sampling.** Source selection is intentional. (Possible future
enhancement: a curated `vocabulary.json` of pre-collected source
paragraphs by category, for a "surprise me" mode. Out of scope for v1.)

---

### 3.4 speech-rules

**Purpose.** Break dialogue ruts (the clinical-curious antagonist, the
stoic-terse protagonist) by forcing positive specification per character,
not just avoidance.

**When to invoke.** Per scene with dialogue, run once per speaking
character.

**Inputs.**
- Character (name, brief description; if a `character-analysis` profile
  exists, pass it through)
- Scene context
- Optional: source-imprint paragraphs of the character's speech (e.g.,
  Cugel dialogue corpus)

**Output (card).** Markdown card per character:
- **Positive mode** — what the character actively does (e.g., "speaks only
  in declaratives about the past", "answers every question with another
  question", "issues commands without justification", "speaks in
  third-person about themselves")
- **Default-banned patterns** — clinical curiosity, "what is it like
  to..." constructions, asking the protagonist about feelings, fragment-
  as-style. These are off by default and must be explicitly re-enabled if
  desired.
- **Voice fingerprint** — vocab register, sentence-length cap, signature
  constructions, prohibited words, contraction rules

**Mechanism.**
1. Read character + scene context.
2. Roll positive mode from `vocabulary.json`. Roll voice fingerprint
   axes.
3. Apply default-banned patterns (these are constants, not rolled).
4. If source paragraphs provided, override rolled choices with extracted
   features.
5. Compose card.

**vocabulary.json arrays (suggested seed):**
- `positive_modes`: "speaks only in declaratives about the past",
  "answers questions with questions", "issues commands without
  justification", "speaks in third-person of themselves", "uses only
  imperatives and questions, never declaratives", "quotes proverbs or
  texts instead of speaking directly", "describes their own actions in
  present tense as they speak", ...
- `vocab_registers`: archaic, plain-modern, formal-modern, colloquial,
  technical/jargon-heavy, child-simple, biblical-cadence, ...
- `sentence_length_caps`: 6, 10, 15, 20, no-cap-but-min-15
- `signature_constructions`: "begins every line with a preposition",
  "never uses the word `I`", "always names the person they're addressing",
  ...

**Constants (not sampled, always banned by default):**
- Clinical/curious tone
- "What does it feel like" type questions
- Detached observational commentary on the protagonist
- Fragment-as-style (unless the rolled positive mode requires it)

**Sampling calls:**
```
python sampling.py positive_modes 1
python sampling.py vocab_registers 1
python sampling.py sentence_length_caps 1
python sampling.py signature_constructions 1
```

---

## 4. Composition flow

```
[scene context from user]
        │
        ▼
┌──────────────────────────────────────┐
│ Pre-writing subagents (parallel)     │
│                                      │
│  scene-parameters    → params card   │
│  forbidden-patterns  → blacklist     │
│  source-imprint      → profile       │ (optional)
│  speech-rules × N    → speech cards  │ (one per character)
└──────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────┐
│ Main writing agent                   │
│                                      │
│  Inputs:                             │
│   • scene context                    │
│   • all cards                        │
│  Does NOT load skill files.          │
│                                      │
│  Output: scene draft                 │
└──────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────┐
│ forbidden-patterns subagent (audit)  │
│                                      │
│  Inputs: draft + blacklist card      │
│  Output: violation report            │
└──────────────────────────────────────┘
        │
        ▼
[user reviews; revises or accepts]
```

**Lightest useful pipeline:** `scene-parameters → scene-writer`. Maximum
variety enforcement uses all four pre-writing skills + audit.

**Composes with existing skills:**
- `scene-writer` is the natural drafting agent; it consumes the cards.
- `voice-revision`, `literary-revision` work as pre- or post-passes.
- `character-analysis` profiles feed into `speech-rules` as input.
- `stratguide-scribe` follows the same multi-mode pattern as
  `forbidden-patterns` (predictive + audit).

---

## 5. Build order

1. **source-imprint** — no sampling, simplest implementation, immediate
   variety lift. Validates the subagent + card pattern.
2. **forbidden-patterns** — introduces sampling. Both modes implemented
   together (single skill, two modes).
3. **scene-parameters** — most sampling-heavy; benefits from lessons
   learned in (2).
4. **speech-rules** — depends on conventions established by (2) and (3);
   integrates with character-analysis.

After each skill, run a test pass: same scene context, draft with and
without the skill, compare for the targeted rut.

---

## 6. Open decisions / flags for implementer

- **`vocabulary.json` seed content.** The arrays in section 3 are
  illustrative seeds. The user will expand them based on observed ruts in
  their own writing. Implementer should provide the seed arrays as a
  starting point; expansion is the user's ongoing job.

- **Card format (JSON vs. markdown).** Default to markdown for
  human-readability; user preference is markdown for documents. JSON only
  if a downstream skill needs to parse fields programmatically.

- **Audit mode rewrite policy.** Audit mode should NOT auto-rewrite. It
  reports; user decides. This preserves authorial control and avoids
  cascading edits.

- **Subagent invocation mechanism.** This plan assumes subagents are
  available in the user's environment (Claude Code Task tool or
  equivalent). If running in an environment without subagent support, the
  skills can be invoked sequentially by the same agent — context hygiene
  is reduced but the contracts still hold.

- **Skill file location.** Place under `/mnt/skills/user/` matching
  existing convention.

- **Sampling script.** The user's `sampling.py` (provided) is unchanged
  across all skills. Each skill's `assets/` contains its own copy plus
  its own `vocabulary.json`. Do not modify `sampling.py`.
