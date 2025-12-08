# Project Description

A web app that generates a dynamic, multiple-choice story, using a mix of input parameters (genre, choice of generated character, etc) and random chance. This web app would display the story text and options, possibly with auto-generated styling, images, and music as well. Basically, CYAA, but random, with no going back.

## User Flows

User Login:

- The user is confronted by a black screen, then a guard, or unknown narrator, speaks
- If the user has tokens, the guard lets them in, saying they are recognized
- Otherwise, the guard asks for name and password
- User has option to say "I'm new" - go through sign-up flow

Home Screen:

- User is presented with a stylized display of their stories - the ones they've already 'heard'
  - How to display? Book covers? Glyphs? Needs to look good, while still conforming to Sparse
- Option to start a new story

Story Generation:

- QUESTION THROUGHOUT: How much user choice/input, vs randomness/fate?
- QUESTION THROUGHOUT: How much can you "pre-load" the story, to avoid user wait?
- QUESTION THROUGHOUT: How do you make the AI output "good"?
- Start by asking for Main genre, user must select from one of five options
  - Behind the scenes, pick random secondary genre
  - From these two, generate uncommons settings/locations, and uncommon protagonists
- Ask user to pick from generated options
- Behind the scenes, generate a rough outline/pivot points for the story
- User opens the first 'screen' - the story begins

Replay Stories:

- NOTICE: The user cannot make different choices, only 'relive' the same story

## Story Structure

`Genre`, `Setting`, and `Character` choice - entry point to a story

Generate your `Location` or `Setting` (uncommon to genre)

Generate uncommon `Protagonists`: Dwarves, Machines/Automatons, Veg-folk (but not ents)

- Need to be specific to setting

Possible requirement - every story is generated like a video game guidebook (Vermis, Baldur's Gate Strategy Guide, etc)

- Mix of description, action, lists, and "In-game dialogue/snippets"

Predetermined `Outline` - the structure, plot, or outline is roughly determined beforehand

- Made up of a series of `pivots` - moments in the story which form the vertebrae
- User's choices matter for direct consequences and succeeded text, but not for the overall 'arc'
- The user doesn't see/know this
- Use your existing story outlines (music outlines) as the first set to test with
- `Theme` is hidden too

### Genres

Somewhat randomly generated, somewhat picked from list

NOTICE: Every story should have a Main sub-genre and Secondary one - blending genre's is where magic happens

Possible requirement - all `choices` must have unique names:

1. 'In the Deep' = Dungeon (Dark) Fantasy (_Your Genre_)
2. 'Of the Backworldsmen' = Mythic (High) Fantasy
3. 'Those Pinholes of Light' = Science Fiction
4. 'Of Foulness' = Horror
5. 'Goldeneye' = Spy Thriller? TODO = Alternate History?
   a. Possibly have historic period be a `Setting`, not a genre
   b. What to do for genre 5?

Folklore: - Fairy Tales (specifically Japanese, Russian, European, Native American), Don't Starve - Myth: The Odyssey, Beowulf, Dark Souls (Again...), Zelda, King Arthur - Ghost Stories: The Woman in Black, Kaidan,

Alternate/Period History:

- Japan (Muromachi and Edo): Seven Samurai, 13 Assassins, Samurai Champloo
- Ancient Greek: The Odyssey, 300
- Bronze/Stone/Iron-age Europe (druids, early settlements): Drova... The Bard's Tale? and not much else (**HERE LIES OPPORTUNITY**)
- Medieval Europe: A Knight's Tale, Crusader King's 3: Mount and Blade
- Victorian: Penny Dreadful, Dickens,
- Norse: Vikings, The 13th Warrior
- Mesoamerican (Maya, Inca): Curse of the Dead Gods (**HERE LIES MORE OPPORTUNITY**)
- Golden Age of Exploration (Late 19th, early 20th): Indiana Jones
- World War 1 (The Great War): 1917

#### Dark Fantasy

Exemplars: **Dark Souls**, Vermis, Lunacid, Castlevania, The Black Company, The Dark Elf Trilogy, Mork Borg, Pan's Labyrinth, The Dark Crystal, Darkest Dungeon, Pillars of Eternity

Subgenres: Dungeon (Crawl, Synth), Gothic, Apocalyptic, Sword-and-Sorcery

Character Archtypes:

Locations/Settings:

Theme:

Tone:

Plot Structure/Patterns:

Conflic Type:

**Motifs (Super Important):**

Stakes/Scope:

Resolution:

#### High Fantasy

    - Gaslamp/Steampunk Fantasy: Howl's Moving Castle, Castle in the Sky, Torchlight
    - High Fantasy: The Hobbit, Morrowind (Elder Scrolls), Wildermyth, Dungeon Siege, Fable

Exemplars:

Subgenres:

Character Archtypes:

Locations/Settings:

Theme:

Tone:

Plot Structure/Patterns:

Conflic Type:

**Motifs (Super Important):**

Stakes/Scope:

Resolution:

#### Science Fiction

- Science Fiction:
  - Space Western: Firefly, Cowboy BeBop, The Mandalorian, Borderlands, Faster Than Light, Void Bastards
  - Cyberpunk: Neuromancer, Deus Ex, Blade Runner

Exemplars:

Subgenres:

Character Archtypes:

Locations/Settings:

Theme:

Tone:

Plot Structure/Patterns:

Conflic Type:

**Motifs (Super Important):**

Stakes/Scope:

Resolution:

#### Horror

- Horror:
  - Exemplars: The House on the Borderland, The Thing, H.P. Lovecraft's stories, Carnacki the Ghost-Finder, The Cabinet of Dr. Caligari
  - Subgenres: Cosmic/Lovecraftian, Monster, Gothic
  - Monster: Dracula, The Mummy, Frankenstein, etc

Exemplars:

Subgenres:

Character Archtypes:

Locations/Settings:

Theme:

Tone:

Plot Structure/Patterns:

Conflic Type:

**Motifs (Super Important):**

Stakes/Scope:

Resolution:

#### TODO Genre

Exemplars:

Subgenres:

Character Archtypes:

Locations/Settings:

Theme:

Tone:

Plot Structure/Patterns:

Conflic Type:

**Motifs (Super Important):**

Stakes/Scope:

Resolution:

## Method

Step 1: Start by getting one complete story, pseudo-random, with the LLM (not automated through your app)

- Focus on the text (if it can't do that to your standard, the rest is pointless)
- Then images, based on the text
- Then soundtrack

Step 2: Figure out the pseudo-random structure

- How do you keep a story going to its satisfying, inevitable conclusion, while still allowing some choice/agency?

Step 3: Design your screens

- Use excalidraw - no actual coding yet

Step 4: Backend API

- Copy over user-auth API, converted to your new DB if needed
- Possibly, convert from Node to Bun?) unified tool?)
- Next work on text API, then image and sound if separate

Step 5: Frontend

### Technology

**Frontend** - `React`, with your `Sparse CSS`

- Simpler than the backend
- Apply your Sparse.React laws
- You come up with the screens, general layout - claude agents do the code
- Question: How do you "pre-load" pictures, tracks, and text, before the user makes a choice (before the LLM generates them)? - Do You have placeholders? Loading screens? Do you always generate 1 level ahead?

**Backend** - `Express`

- Apply your Sparse.ts, Sparse.Express laws
- Switch to `Bun` if possible (faster, unified with frontend): https://bun.com/
- You come up with the data models, the endpoints, the logic for LLM requests - claude agents do the code
- Use your standard auth from Leaves (clean it up, make it conform to Sparse Laws)
- Question: What to use for the storage?
  - MongoDB w. Mongoose again? Or try out PostgreSQL?
  - Depends on easiest way to store music and sound alongside structured data
- Question: Which LLM API/SDK do you use?
  - Claude is better for code, decent at ideas
  - GPT does images, probably better at actual fiction prose than Claude
  - What about Gemini? What about image-specific, and sound-specific?

### Creating Stories

Start by testing prompts and randomization

- Ask LLM for 'uncommon/unknown exemplars'
  - Not just TV/Movies/Lit. /VGs- also check music, art, theater, web design
  - Then, separately, ask what they have in common, and what makes them distinct
- Use the randomization method to build uncommon combos of locations, characters, and items

Always output result as JSON (for AI) or MD (for final website content)

Objects/Models

- `Critical Story Element (CSE)` - these are the focus
  - use keyword extraction from your exemplars
- `User` - Name and password, gather email for validation, but keep hidden in UI
- `Blob` - A generated section of text
  - Probably not just a string - you will need to keep track of the original prompt, any further prompt refinements, any CSEs used to generate it, where it sits in the story, if it is a crucial `pivot` in the outline
- `Track` - Possibly a pieces of music, or ambient audio, that goes with a screen
- `Picture` - An LLM-generated image that illustrates a blob or set of blobs
  - Pick a concrete style (grounds your app) - 2.5D platformer?
  - first-person 2.5D dungeon crawler with chunky pixel-art: a blocky 3D world textured in low-res pixels, populated by billboarded 2D sprites, lit like a moody 90s FPS.
- `Screen` - Possibly an image, an array of blobs, an array of choices, a selected choice, a music Track, an ambience track, possibly an optional user text input
- `Modifiers` - Basically weights that drastically alter the story style
  - 'Birdland' - Every background song is just Birdland by _Weather Report_
  - 'Nyquil' - the story gets progressively sleepier

One idea: have different models (or, agents) with specific writing styles

- A dickens/Peake/Willkie Collins model
- A Tolkien/Lord Dunsany model
- A Hammett/Chandler model
- A Fairy-tale model
- A Howard/Hodgson/Lovecraft model
- An H. G. Welles model
