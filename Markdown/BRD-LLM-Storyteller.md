# LLM Storyteller — Business Requirements Document

## Table of Contents

1. [Project Overview](#project-overview)
2. [User Flows](#user-flows)
3. [Story Structure](#story-structure)
   - Pivots, Arc Templates, Choice Mechanics
4. [Genres](#genres)
   - Dark Fantasy, High Fantasy, Sci-Fi, Horror, Folklore
5. [Implementation Roadmap](#implementation-roadmap)
6. [Data Models](#data-models)
7. [Technology Requirements](#technology-requirements)

---

## Project Overview

A web app that generates dynamic, multiple-choice stories using a mix of user input (genre, setting, character) and randomized fate. The app displays story text with options, auto-generated images, and optional music. Essentially: CYOA, but procedurally generated, with no going back.

**Core Concept:** Stories follow predetermined narrative arcs (hidden from the user), but player choices affect immediate consequences, tone, and flavor. The magic comes from blending genres—every story has a primary genre (user-selected) and secondary genre (fate-selected).

---

## User Flows

### 1. Login / The Threshold

The app establishes its tone immediately through a narrative login experience.

**The Narrator/Guard:**

- User sees a black screen; a narrator (the "guard") speaks
- The narrator is a consistent character throughout the app (not just login)

**Returning User:**

- If the user has valid auth tokens, the guard recognizes them: "You've been here before..."
- User proceeds to Home Screen

**New User:**

- Guard asks for credentials (name and password)
- User can say "I'm new" → sign-up flow
- Sign-up collects: username, password, email (email hidden in UI, used only for validation)

**Failed Login:**

- The guard speaks cryptically
- User can retry or go to sign-up

---

### 2. Home Screen / The Archive

The user sees their story history—the tales they've already "heard."

**Story Display:**
Recommendation: **Generated book covers** (not glyphs)

- Each completed story gets a procedurally generated cover image
- Cover reflects the story's genre blend and key imagery
- Covers displayed in a grid or shelf layout
- Conforms to Sparse CSS aesthetic (minimal, high-contrast)

**Elements:**

- Story covers with generated titles
- Completion status indicator
- "Start New Story" prominent option
- Story details on hover/click (genre, length, date)

---

### 3. Story Generation / The Beginning

User creates a new story through three selections:

**Step 1: Genre Selection**

- User picks from 5 genre options (displayed with their poetic names)
- System secretly selects a secondary genre for blending

**Step 2: Setting Selection**

- System generates 3 setting options based on genre blend
- Settings are "uncommon to genre" (using CSE tags as constraints)
- User selects one

**Step 3: Protagonist Selection**

- System generates 3 protagonist options specific to the chosen setting
- Includes non-human options: Dwarves, Machines/Automatons, Veg-folk (but not ents)
- User selects one

**Behind the Scenes (during selection):**

- System generates full Outline with Pivots
- Pre-loads first screen's content
- Begins generating choice branches for first decision

**Transition:**

- User clicks "Begin" → the story opens

---

### 4. Story Experience / The Journey

The main story loop:

**Screen Display:**

- Prose text (one or more Blobs)
- Optional image
- Optional ambient audio/music
- 2-3 choice options

**User Interaction:**

- User reads text
- User selects a choice
- Screen transitions to next (with loading state if needed)

**Pre-loading Strategy:**

- While user reads: system generates next 2-3 branches
- Loading states: subtle, thematic (not jarring spinners)
- Images/music may load slightly after text

**Completion:**

- Resolution screen marks the end
- User sees "The End" with story summary
- Option to return to Home Screen
- Story saved to user's archive

---

### 5. Replay / Reliving the Tale

Users can revisit completed stories, but cannot change choices.

**Replay Purpose:**

- Re-reading for appreciation (like re-reading a favorite book)
- Sharing with others (show them what happened)
- Comparing against new playthroughs of the same genre

**Replay Experience:**

- Same screens, same text, same choices
- Choices are pre-selected (shown as "what you chose")
- No new generation needed—purely retrieval
- Optional: different visual treatment to indicate replay mode

## Story Structure

### Overview

Every story follows a predetermined **Outline** composed of **Pivots**—narrative beats that form the story's spine. User choices affect immediate consequences and flavor, but not the overall arc. The user never sees the underlying structure.

### Entry Point

The user enters a story through three selections:

1. **Genre** (user picks from 5 options)
2. **Setting** (user picks from 3 generated options, constrained by genre)
3. **Protagonist** (user picks from 3 generated options, specific to setting)

Behind the scenes:

- System randomly selects a **Secondary Genre** to blend with the user's choice
- System generates settings and protagonists using genre-specific **CSE tags** as constraints
- Protagonists include non-human options: Dwarves, Machines/Automatons, Veg-folk (but not ents)
- Optional: may generate protagonists on the fly, not pre-generated like genre/setting

### Pivots

A **Pivot** is a predetermined story beat that the narrative must pass through regardless of player choices.

**Pivot Types:**

- **Opening**: Establishes setting, protagonist situation, initial tension
- **Inciting Incident**: The event that launches the story forward
- **Rising Action** (1-2 pivots): Complications, encounters, escalation
- **Midpoint Turn**: A revelation or shift that changes the story's direction
- **Crisis**: The lowest point or greatest challenge
- **Climax**: The decisive moment/confrontation
- **Resolution**: Consequences and closure

**Pivot Count:** 5-7 pivots for short-form stories (10-15 screens, ~15-20 minutes)

**Pivot Content:** Each pivot defines:

- Location (same, transition, or new)
- Event type (encounter, discovery, choice-consequence, environmental)
- Thematic beat (how this advances the hidden theme)
- Branching options (2-3 choices leading to next screens)

### Arc Templates

The system uses multiple story arc templates. An arc is selected based on genre-fit or randomized.

**Template 1: [PLACEHOLDER - Music Outline #1]**

- Description pending
- Pivot sequence pending

**Template 2: [PLACEHOLDER - Music Outline #2]**

- Description pending
- Pivot sequence pending

**Template 3: [PLACEHOLDER - Music Outline #3]**

- Description pending
- Pivot sequence pending

**Template 4: [PLACEHOLDER - Music Outline #4]**

- Description pending
- Pivot sequence pending

_TODO: These templates will be populated from existing music outline documents._

### Choice vs. Fate Mechanics

Three layers determine what happens in a story:

| Layer                   | Who Decides | Examples                                                                                 |
| ----------------------- | ----------- | ---------------------------------------------------------------------------------------- |
| **User Choice**         | Player      | Main genre, setting (from options), protagonist (from options), immediate action choices |
| **Fate/Random**         | System      | Secondary genre, specific pivot events, NPC behaviors, environmental details, item finds |
| **Fixed/Predetermined** | Outline     | Overall arc shape, pivot sequence, thematic resolution, hidden theme                     |

### Choice Consequence Model

User choices affect the story without altering the predetermined arc:

1. **Immediate Consequences**: Direct result of choice shown in next screen
2. **Accumulated Tone**: Choices shift tone/mood (darker/lighter, violent/diplomatic, curious/cautious)
3. **Character Memory**: NPCs reference past choices in dialogue
4. **Cosmetic Variance**: Same pivot, different flavor text based on accumulated choices
5. **Resource State**: Items, allies, or conditions gained/lost carry forward

### Pre-loading Strategy

To minimize user wait times:

| Phase                   | What Gets Generated                                                                         | When                            |
| ----------------------- | ------------------------------------------------------------------------------------------- | ------------------------------- |
| **Before story starts** | Full outline, all pivots (skeleton), protagonist details, setting description, hidden theme | During setup screen             |
| **One screen ahead**    | Next 2-3 choice branches, including prose and choice text                                   | While user reads current screen |
| **On-demand**           | Final prose polish, images, music                                                           | With loading states as fallback |

### Prose Style

Every story is generated in a specific prose style (Possibly like a video game guidebook - Vermis, Baldur's Gate Strategy Guide):

- Mix of description, action, lists, and "in-game dialogue/snippets"
- Genre-appropriate voice (see Writing Style Agents below)
- Hidden theme woven through imagery and word choice

### Future Enhancement: Variable Story Length

**MVP:** Short-form (10-15 screens, ~15-20 minutes)

**Future Tiers:**

- **Medium (25-40 screens)**: 30-60 min, more character development, additional pivot types, deeper branching
- **Long (50+ screens)**: Multi-session, save/resume required, expanded branching, multiple NPCs with memory

### Genres

Every story has a **Main Genre** (user-selected) and a **Secondary Genre** (system-selected). Blending genres is where the magic happens—uncommon combinations produce the most interesting stories.

**The Five Genres:**

| #   | Display Name              | Genre               | Notes                        |
| --- | ------------------------- | ------------------- | ---------------------------- |
| 1   | "In the Deep"             | Dark Fantasy        | Your core genre              |
| 2   | "Of the Backworldsmen"    | High Fantasy        | Mythic, heroic               |
| 3   | "Those Pinholes of Light" | Science Fiction     | Space Western + Cyberpunk    |
| 4   | "Of Foulness"             | Horror              | Cosmic, Monster, Gothic      |
| 5   | "Little Weaver Bird"      | Folklore/Fairy-Tale | Intimate, cultural, grounded |

**Historical Periods as Settings (not genres):**

Period settings can be layered onto any genre:

- Japan (Muromachi/Edo): Seven Samurai, 13 Assassins, Samurai Champloo
- Ancient Greek: The Odyssey, 300
- Bronze/Stone/Iron-age Europe: Drova, The Bard's Tale (**opportunity: underexplored**)
- Medieval Europe: A Knight's Tale, Crusader Kings 3, Mount and Blade
- Victorian: Penny Dreadful, Dickens
- Norse: Vikings, The 13th Warrior
- Mesoamerican (Maya, Inca): Curse of the Dead Gods (**opportunity: underexplored**)
- Golden Age of Exploration (late 19th/early 20th): Indiana Jones, Shackleton
- World War 1: 1917

---

#### 1. Dark Fantasy — "In the Deep"

**Exemplars:** Dark Souls, Vermis, Lunacid, Castlevania, The Black Company, The Dark Elf Trilogy, Mork Borg, Pan's Labyrinth, The Dark Crystal, Darkest Dungeon, Pillars of Eternity

**Subgenres:** Dungeon Crawl, Dungeon Synth, Gothic, Apocalyptic, Sword-and-Sorcery

**Character Archetypes:**

- The Cursed/Condemned Protagonist (marked, rejected, or damned before story begins)
- Fallen/Tragic Nobility (diminished gods, vampire queens, corrupted lords)
- The Crestfallen/Hollow (those who have lost purpose, teetering on edge)
- Morally Ambiguous Figures (mercenaries, complex villains, unreliable guides)
- The Divided Self (characters containing opposed aspects—light/dark, human/monster)
- Desperate/Fragile Heroes (expendable, already broken, surviving rather than thriving)

**Locations/Settings:**

- Decaying/Ruined Worlds (crumbling kingdoms, fallen ages, entropy as default)
- Gothic Architecture (cathedrals, impossible towers, sentient/hostile buildings)
- Subterranean Spaces (catacombs, great wells, underdark caverns)
- Castles/Fortresses as Central Locations (shapeshifting, corrupt, oversized)
- Hostile/Cursed Wilderness (blood-drinking forests, poisonous swamps, dead god's corpse)
- Post-Apocalyptic Remnants (surface ruins, survivors amid collapse)

**Theme:**

- Cycles/Entropy/Inevitable Decay (the world is ending or has already ended)
- Survival Against Hostile Odds (the world is trying to kill you)
- Moral Ambiguity (no clear good/evil; "evil is relative")
- Identity/Self-Discovery (purpose prevents hollowing; who are you apart from your curse?)
- Inherited Sin/Generational Burden (cleaning up ancestral crimes)
- Truth vs. Propaganda (divine lies exposed through exploration)

**Tone:**

- Melancholic and Contemplative (failure treated with empathy, not contempt)
- Dark Humor/Sardonic (soldiers joking amid atrocity; gallows wit)
- Gothic Atmosphere (European horror aesthetics, architectural menace)
- Reverent toward the fallen (dignity even in defeat)

**Plot Structure/Patterns:**

- Cyclical/Repetitive (the flame will fade again; the vampire will return)
- Descent/Journey Narrative (going down as spatial and moral metaphor)
- Fragmented/Environmental Storytelling (lore through items, architecture, implication)
- Coming-of-Age through Suffering (the protagonist is forged by ordeal)

**Conflict Type:**

- Man vs. Cosmic/Supernatural Forces (gods, cycles, elder things)
- Man vs. Self (hollowing, affliction, the Hunter persona, maintaining sanity)
- Man vs. Fate/Cycle/Doom (fighting predetermined patterns)
- Man vs. Society/Institution (escaping corrupt civilizations)

**Motifs (Super Important):**

- Light/Darkness/Fire (bonfires, torches, the First Flame, illumination vs. shadow)
- Blood (sacrifice, ritual, violence, menstruation, vampirism)
- Decay/Corpses/Bones/Undeath (skeletons, hollows, rot as visual vocabulary)
- Cycles/Wheels/Repetition (ages turning, resurrection, eternal recurrence)
- Transformation/Corruption of Self (hollowing, affliction, flesh mutation)
- Souls as Tangible Substance (currency, essence, transferable)
- Descent/Wells/Going Down (the journey into darkness)

**Stakes/Scope:**

- Cosmic/World-Ending (the age will end; the Heart will consume all)
- Personal Survival (staying alive is hard; permadeath is meaningful)
- Soul/Sanity at Risk (you might hollow, go mad, lose yourself)
- Small-Group/Found-Family (the Company, the party, the few who remain)

**Resolution:**

- Pyrrhic/Costly Victory (winning costs everything or changes nothing)
- Cyclical/Temporary (the threat will return; at best you delay)
- Ambiguous/Multiple Endings (the player decides, but no option is clean)
- Found Family as partial comfort (you survive together, reduced but continuing)

#### 2. High Fantasy — "Of the Backworldsmen"

**Exemplars:** The Hobbit, The Lord of the Rings, Morrowind (Elder Scrolls), Wildermyth, Dungeon Siege, Fable, Howl's Moving Castle, Castle in the Sky, Torchlight, The Odyssey, Beowulf, Legend of Zelda

**Subgenres:** Epic/Mythic Fantasy, Gaslamp/Steampunk Fantasy, Heroic Fantasy

TODO - research the rest of this genre after getting Dark Fantasy working in the app

#### 3. Science Fiction — "Those Pinholes of Light"

**Exemplars:** Firefly, Cowboy Bebop, The Mandalorian, Borderlands, Faster Than Light, Void Bastards, Neuromancer, Deus Ex, Blade Runner, Alien

**Subgenres:** Space Western, Cyberpunk, Survival Sci-Fi

TODO - research the rest of this genre after getting Dark Fantasy working in the app

#### 4. Horror — "Of Foulness"

**Exemplars:** The House on the Borderland, The Thing, H.P. Lovecraft's stories, Carnacki the Ghost-Finder, The Cabinet of Dr. Caligari, Dracula, Frankenstein, The Mummy, The Woman in Black, Kaidan (Japanese ghost stories), Alien

**Subgenres:** Cosmic/Lovecraftian Horror, Monster Horror, Gothic Horror, Ghost Stories

TODO - research the rest of this genre after getting Dark Fantasy working in the app

#### 5. Folklore/Fairy Tale — "What Was Spoken"

**Exemplars:** Don't Starve, Spirited Away, Pan's Labyrinth (crossover with Dark Fantasy), Over the Garden Wall, Original Grimm Tales, Russian Fairy Tales, Kaidan Collections, Princess Mononoke, Kwaidan

**Subgenres:** European (Grimm, Andersen), Japanese (kaidan, yokai), Slavic (Baba Yaga, firebirds), Native American, Dark Fairy Tale, Mythic/Legendary

TODO - research the rest of this genre after getting Dark Fantasy working in the app

## Implementation Roadmap

### Phase 1: Validate the Core — Manual Story Generation

**Goal:** Prove the text quality before building anything.

1. **Generate one complete story manually** (not automated)

   - Use LLM directly with prompts
   - Test pivot structure, genre blending, prose quality
   - If text quality isn't there, stop: the rest is pointless

2. **Test image generation**

   - Generate images based on the story text
   - Validate the visual style (2.5D pixel-art aesthetic)

3. **Test audio generation** (optional)
   - Explore ambient audio/music options
   - Lower priority than text and images

### Phase 2: Define the Pseudo-Random Structure

**Goal:** Solve the core design challenge.

- How do you keep a story moving toward its satisfying, inevitable conclusion while still allowing choice/agency?
- Document the Arc Templates (populate placeholders with your music outlines)
- Test different balances of User Choice vs. Fate vs. Fixed

### Phase 3: Design Screens

**Goal:** Visual design before code.

- Use Excalidraw or similar
- Design all screens: Login, Home, Story Generation, Story Experience, Replay
- Apply Sparse CSS aesthetic principles
- No coding yet

### Phase 4: Backend Development

**Goal:** Build the API layer.

1. User authentication (adapt existing auth patterns)
2. Text generation endpoints
3. Story/Outline/Screen management
4. Image generation integration
5. Audio integration (if implementing)

### Phase 5: Frontend Development

**Goal:** Build the user interface.

1. Implement designed screens
2. Connect to backend APIs
3. Handle pre-loading and loading states
4. Polish transitions and interactions

---

## Data Models

### Core Objects

#### CSE (Critical Story Element)

Tags extracted from exemplars, used to constrain LLM generation for consistency and quality.

**Purpose:** Provide the "vocabulary" that grounds generated content in genre conventions.

**Contains:**

- Tag text (1-3 words, evocative, transferable)
- Source (which exemplar it came from)
- Type (setting, character-trait, character-description, monster, weapon, magic, atmosphere)
- Genre association(s)

**Quality Guidelines:**

- Good tags: brief, evocative, transferable ("black palace", "ashen ruins", "hollow-eyed")
- Bad tags: proper names, verbose descriptions, overly specific

---

#### Outline

The predetermined story skeleton for a single playthrough.

**Purpose:** Provides the narrative structure that user choices cannot alter.

**Contains:**

- Arc template reference (which of the 4 templates)
- Array of Pivots (5-7 for short-form)
- Primary genre
- Secondary genre (randomly assigned)
- Hidden theme
- Setting summary
- Protagonist summary

---

#### Pivot

A single story beat within an Outline.

**Purpose:** Defines what must happen at this point in the story, regardless of player choices.

**Contains:**

- Pivot type (Opening, Inciting Incident, Rising Action, Midpoint Turn, Crisis, Climax, Resolution)
- Location (same, transition, or new location name)
- Event type (encounter, discovery, choice-consequence, environmental)
- Thematic beat (how this advances the hidden theme)
- Required story elements (what must be present)
- Branching options (2-3 Choice objects leading to next screens)

---

#### Blob

A generated section of text with metadata.

**Purpose:** The actual prose shown to the user, plus the context needed to regenerate or refine it.

**Contains:**

- Generated text (the prose)
- Generation prompt (what was sent to the LLM)
- CSEs used (which tags constrained generation)
- Pivot association (which pivot this serves)
- Accumulated tone state (at time of generation)
- Version history (if refined)

---

#### Screen

The rendered unit shown to the user.

**Purpose:** Everything needed to display one "page" of the story.

**Contains:**

- Array of Blobs (the text sections)
- Array of Choices (user options)
- Selected Choice (if already chosen, for replay)
- Picture reference (optional)
- Music Track reference (optional)
- Ambience Track reference (optional)
- Screen index (position in story)

---

#### Choice

A user-selectable option on a Screen.

**Purpose:** Presents the player's decision point.

**Contains:**

- Display text (what the user sees)
- Consequence hint (subtle indication of what might happen)
- Tone shift (how this affects accumulated tone: darker/lighter, violent/diplomatic, etc.)
- Target pivot (which pivot this choice leads toward)
- Resource effects (items/conditions gained or lost)

---

#### Story

A complete playthrough, owned by a User.

**Purpose:** The full record of a single story experience.

**Contains:**

- User reference
- Outline used
- Array of Screens (in order)
- Array of Choices made
- Completion status
- Timestamps (started, last played, completed)
- Display metadata (for home screen—generated title, cover image, etc.)

---

#### User

Account information.

**Purpose:** Authentication and story ownership.

**Contains:**

- Username
- Password (hashed)
- Email (for validation, hidden in UI)
- Auth tokens
- Array of Story references

---

#### Picture

An LLM-generated image.

**Purpose:** Visual illustration for a Screen or Story.

**Contains:**

- Image data/URL
- Generation prompt
- Style constraints (see Visual Style below)
- Associated Screen(s)

**Visual Style (concrete choice to ground the app):**
First-person 2.5D dungeon crawler with chunky pixel-art: a blocky 3D world textured in low-res pixels, populated by billboarded 2D sprites, lit like a moody 90s FPS.

---

#### Track

A piece of music or ambient audio.

**Purpose:** Audio accompaniment for a Screen.

**Contains:**

- Audio data/URL
- Type (music or ambience)
- Generation prompt (if AI-generated)
- Mood tags
- Associated Screen(s)

---

#### Modifier

Special modes that drastically alter story style.

**Purpose:** Easter eggs / special experiences for replayability.

**Examples:**

- "Birdland" — Every background song is just "Birdland" by Weather Report
- "Nyquil" — The story gets progressively sleepier

**Contains:**

- Modifier name
- Effect description
- Implementation rules

---

### Writing Style Agents

Different LLM configurations (or prompt personas) for distinct prose styles:

| Agent                        | Style                                        | Best For             |
| ---------------------------- | -------------------------------------------- | -------------------- |
| Dickens/Peake/Wilkie Collins | Baroque, atmospheric, labyrinthine sentences | Dark Fantasy, Horror |
| Tolkien/Lord Dunsany         | Mythic, archaic, reverent                    | High Fantasy         |
| Hammett/Chandler             | Hardboiled, terse, noir                      | Sci-Fi (Cyberpunk)   |
| Fairy-tale                   | Simple, rhythmic, moral clarity              | Folklore             |
| Howard/Hodgson/Lovecraft     | Pulpy, cosmic, purple prose                  | Horror, Dark Fantasy |
| H.G. Wells                   | Scientific romance, wonder and dread         | Sci-Fi               |

---

### Storage Requirements

**Structured Data (Users, Stories, Outlines, etc.):**

- Need efficient querying by user
- Need retrieval of story history
- Relationships between objects (User → Stories → Screens → Choices)

**Binary/Media (Images, Audio):**

- Need storage for generated images
- Need storage for audio tracks (if implemented)
- Consider separate media storage vs. same database

**Question for Implementation:** Same DB for all, or separate media storage?

---

## Technology Requirements

_Note: These are capability requirements, not specific tool choices._

### Text Generation Requirements

- Must support prose in multiple literary styles
- Must accept CSE tags as constraints
- Must handle context for multi-screen stories
- Must generate JSON-structured output for story elements
- Must generate Markdown for final prose display

### Image Generation Requirements

- Must support consistent visual style across a story
- Must accept text descriptions as prompts
- Must produce images suitable for web display
- Preferred style: chunky pixel-art, 2.5D dungeon crawler aesthetic

### Audio Generation Requirements (Future/Optional)

- Nice-to-have: ambient audio generation
- Nice-to-have: music generation
- Lower priority than text and images

### Quality Evaluation

- Need mechanism to check generated content quality
- Options: automated scoring, human review, self-critique prompts
- Quality anchors: "hand-crafted, distinctive, resistant to obvious genre patterns"

### Content Generation Strategy

- Ask LLM for "uncommon/unknown exemplars" (not just TV/Movies/Lit./VGs—also music, art, theater, web design)
- Separately ask what they have in common and what makes them distinct
- Use randomization to build uncommon combos of locations, characters, and items
- Output as JSON (for processing) or Markdown (for display)
