# LOCATION

## Pre-Draft Setup

`Prompt:`

```
TODO - get claude to retrieve a random fantasy location
```

## First Draft

`Prompt:`

```
Hey claude, you are a worldbuilding assistant. I will provide two documents:

1. **Location Baseline** – A structural description of a dungeon/location covering layout, flow, encounter placement, environmental features.

2. **World Setting** – Documentation describing my fictional world.

Your task: Generate a new location description (less than 500 words). Preserves the _structural DNA_ of the baseline while translating all elements to fit my world.

**Translation rules:**

- Replace all creatures/enemies with equivalents from my setting (if an equivilant does not exist, invent one)
- Adapt architecture and environmental details to my world's aesthetics and geography
- Preserve the spatial flow: entry points, branching paths, chokepoints, verticality, and progression
- Include A MINIMUM of three concrete sensory details - textural elements to help ground the writing.
- Include AT LEAST ONE small, unusual aspect or feature - something uncanny for the setting.
- Reference AT LEAST THREE named characters or creatures.
  - AT LEAST ONE must some kind of leader or authority in a field (or significant creature); at least one must be common.
  - Use the lore document to guide your choice of character/creature, but DO NOT copy/paste from the document.

**Output format:**
Organized by zone/section (like the baseline), prose-forward. Include brief notes on enemy types and key interactive features (traps, puzzles, environmental hazards). REMEMBER: your result must be under 500 words.

---

**Location Baseline:**
see temp.md

---

**World Setting:**
see World.md
```

### The Kenhallow Delve

#### Exterior Compound

A hill-fort gone to ruin—two longhouses with collapsed thatch, a pair of watchtowers listing like rotten teeth, and a central firepit where smoke still rises. Wooden walkways, half-swallowed by creeping moss, connect the structures. Raiders have claimed the place: desperate Kinfolk turned to banditry under a man called **Beoric One-Hand**, who sits by the fire sharpening a notched blade. His people watch the approaches—two at the gate, three more patrolling the overgrown earthworks. The air smells of wet ash and something fouler beneath.

#### Upper Delve (The Old Ward-Hall)

Stone steps descend into cool dark. The walls bear carved spirals—shamanic work, centuries old—now cracked and dark with mold. Shattered **Kestanes** litter the corridor: jade hound-shapes with fractured limbs, their purpose long exhausted. Two raiders crouch near a guttering torch ahead, arguing over a stolen ring.

The passage branches. North: a barred door (key on a sleeping guard) leads to a cell where **Mother Aelwen**, an aging shaman, awaits ransom or rescue. South: a ramp descends to a vaulted chamber where the wards have fully failed. Here, Kestanes have reawakened and turned on the raiders who disturbed them. Combat is already joined when you arrive—two bandits on each raised walkway, two Kestanes skittering below alongside two more desperate fighters. _The jade guardians click and scrape across flagstones slick with old rain._

Beyond, corridors wind through halls where **Bhruggspire** drift in slow, grinding circuits—floating sentinels trailing dust, their jade wings humming a sound felt more than heard. Ceiling scuttles disgorge more Kestanes as you pass. A spear-trap gauntlet blocks the way forward: six pressure-plates requiring careful sequencing.

#### Lower Delve (The Drowned Roots)

A counterweighted lift descends to flooded caverns. Black water pools between raised stone walkways; the roots of ancient trees pierce the ceiling like fingers. **Sarks** have nested here—Lost Ones wearing the rotted remnants of farmers' clothes, clicking and grunting in the dark. Their tents are hide stretched over bone. A lone **Skrelving** guards a web-choked alcove, rust-feathers bristling at any sound.

A split-level chamber holds two Sarks across its gallery. Beyond, tripwire-triggered deadfalls and more Sark camps. _The smell is rank: old meat, black water, something vegetable and wrong._ A gated courtyard with a cracked fountain contains a half-dozen Lost Ones and two crude shelters. A spiral ramp ascends a tower where a lever retracts the bone-spears blocking egress.

#### The Warden's Rest (Boss Chamber)

A **Grundkholm** stands dormant in a stone alcove—twice a man's height, carved from red-veined jade, its eyes dark pits. It wakes when you cross the threshold. Mid-fight, a Gravelform may descend from above. Raised platforms offer retreat; a lever lowers spears guarding a chest.

A sealed gate bears spiral carvings and a keyhole shaped like no modern lock. _Those who press their ear to the stone hear something breathing on the other side—slow, vast, patient._

An exit lift returns to the surface, emerging west of the ruined compound beneath a sky that seems somehow darker than when you entered.

---

**Key Interactive Features:** Spear-trap sequencing puzzle (Upper Delve); tripwire deadfalls (Lower Delve); boss-arena lever; sealed Vormakhian gate requiring a shamanic key-item.

## Revised Prose

`Prompt:`

```
Hey claude, can you revise the attached markdown doc describing a location in a fantasy setting I'm working on? Revise it with the following goals:
* Cut explanatory scaffolding. If a sentence tells the reader what to feel ("The horror is..."), remove it or replace it with imagery that evokes that feeling.
* Vary sentence rhythm. Break long sentences into fragments where impact warrants. Combine choppy sequences into longer rolling clauses where atmosphere warrants.
* Replace generic phrasing with specific, tactile language.
* Add one aphorism as an inline quoted phrase that crystallizes a theme.
* Your revised version must not exceed the original in total letter/character.
```

### The Kenhallow Delve

#### Exterior Compound

A hill-fort gone to ruin—two longhouses with collapsed thatch, watchtowers listing like rotten teeth, a central firepit trailing smoke. Wooden walkways, half-swallowed by creeping moss, bridge the structures. Raiders have claimed the place: desperate Kinfolk turned bandit under **Beoric One-Hand**, who sits by the fire working a notched blade with his remaining fingers. His people watch the approaches—two at the gate, three more on the overgrown earthworks. Wet ash on the wind. Something fouler beneath.

#### Upper Delve (The Old Ward-Hall)

Stone steps descend into cool dark. The walls bear carved spirals—shamanic work, centuries old—now cracked and black with mold. Shattered **Kestanes** litter the corridor: jade hound-shapes with fractured limbs. Two raiders crouch near a guttering torch, arguing over a stolen ring.

The passage branches. North: a barred door (key on a sleeping guard) leads to a cell where **Mother Aelwen**, an aging shaman, awaits ransom or rescue. South: a ramp descends to a vaulted chamber where the wards have bled dry. Kestanes have reawakened and turned on the raiders who disturbed them. Two bandits hold each raised walkway; two jade guardians click and scrape across flagstones slick with old rain, two more fighters already bleeding below.

Beyond, corridors wind through halls where **Bhruggspire** drift in slow, grinding circuits—floating sentinels trailing dust, jade wings humming a sound felt in the teeth. Ceiling scuttles disgorge more Kestanes as you pass. A spear-trap gauntlet blocks the way forward: six pressure-plates requiring careful sequencing.

#### Lower Delve (The Drowned Roots)

A counterweighted lift descends to flooded caverns. Black water pools between raised stone walkways; roots of ancient trees pierce the ceiling like grasping fingers. **Sarks** have nested here—Lost Ones wearing rotted remnants of farmers' clothes, clicking in the dark. Their tents are hide stretched over bone. A lone **Skrelving** guards a web-choked alcove, rust-feathers bristling.

A split-level chamber holds two Sarks across its gallery. Beyond, tripwire deadfalls and more Sark camps. Old meat. Black water. Something vegetable and wrong. A gated courtyard with a cracked fountain contains a half-dozen Lost Ones and two crude shelters. _"What falls to ruin invites new tenants."_ A spiral ramp ascends a tower where a lever retracts the bone-spears blocking egress.

#### The Warden's Rest (Boss Chamber)

A **Grundkholm** stands dormant in a stone alcove—twice a man's height, carved from red-veined jade, its eyes dark pits. It wakes when you cross the threshold. Mid-fight, a Gravelform may descend from above. Raised platforms offer retreat; a lever lowers spears guarding a chest.

A sealed gate bears spiral carvings and a keyhole shaped like no modern lock. Press your ear to the stone: something breathing on the other side. Slow. Vast. Patient.

An exit lift returns to the surface, emerging west of the compound beneath a sky darker than when you entered.

---

**Key Interactive Features:** Spear-trap sequencing puzzle (Upper Delve); tripwire deadfalls (Lower Delve); boss-arena lever; sealed Vormakhian gate requiring a shamanic key-item.

## Renamed Characters

`Prompt:`

```
Hey claude, take a look at the description for a dark fantasy location I've attached as a markdown file.  need you to revise this so that any proper character or location names are pulled randomly from the attached json doc. Don't update creature or location 'types', just any proper names. To make sure your choice is random, write a quick python script to randomly select from each list of names (male, female, or location) as appropriate.
```

### The Kelpshaw Delve

#### Exterior Compound

A hill-fort gone to ruin—two longhouses with collapsed thatch, watchtowers listing like rotten teeth, a central firepit trailing smoke. Wooden walkways, half-swallowed by creeping moss, bridge the structures. Raiders have claimed the place: desperate Kinfolk turned bandit under **Moldrick One-Hand**, who sits by the fire working a notched blade with his remaining fingers. His people watch the approaches—two at the gate, three more on the overgrown earthworks. Wet ash on the wind. Something fouler beneath.

#### Upper Delve (The Old Ward-Hall)

Stone steps descend into cool dark. The walls bear carved spirals—shamanic work, centuries old—now cracked and black with mold. Shattered **Kestanes** litter the corridor: jade hound-shapes with fractured limbs. Two raiders crouch near a guttering torch, arguing over a stolen ring.

The passage branches. North: a barred door (key on a sleeping guard) leads to a cell where **Mother Drelvi**, an aging shaman, awaits ransom or rescue. South: a ramp descends to a vaulted chamber where the wards have bled dry. Kestanes have reawakened and turned on the raiders who disturbed them. Two bandits hold each raised walkway; two jade guardians click and scrape across flagstones slick with old rain, two more fighters already bleeding below.

Beyond, corridors wind through halls where **Bhruggspire** drift in slow, grinding circuits—floating sentinels trailing dust, jade wings humming a sound felt in the teeth. Ceiling scuttles disgorge more Kestanes as you pass. A spear-trap gauntlet blocks the way forward: six pressure-plates requiring careful sequencing.

#### Lower Delve (The Drowned Roots)

A counterweighted lift descends to flooded caverns. Black water pools between raised stone walkways; roots of ancient trees pierce the ceiling like grasping fingers. **Sarks** have nested here—Lost Ones wearing rotted remnants of farmers' clothes, clicking in the dark. Their tents are hide stretched over bone. A lone **Skrelving** guards a web-choked alcove, rust-feathers bristling.

A split-level chamber holds two Sarks across its gallery. Beyond, tripwire deadfalls and more Sark camps. Old meat. Black water. Something vegetable and wrong. A gated courtyard with a cracked fountain contains a half-dozen Lost Ones and two crude shelters. _"What falls to ruin invites new tenants."_ A spiral ramp ascends a tower where a lever retracts the bone-spears blocking egress.

#### The Warden's Rest (Boss Chamber)

A **Grundkholm** stands dormant in a stone alcove—twice a man's height, carved from red-veined jade, its eyes dark pits. It wakes when you cross the threshold. Mid-fight, a Gravelform may descend from above. Raised platforms offer retreat; a lever lowers spears guarding a chest.

A sealed gate bears spiral carvings and a keyhole shaped like no modern lock. Press your ear to the stone: something breathing on the other side. Slow. Vast. Patient.

An exit lift returns to the surface, emerging west of the compound beneath a sky darker than when you entered.

---

**Key Interactive Features:** Spear-trap sequencing puzzle (Upper Delve); tripwire deadfalls (Lower Delve); boss-arena lever; sealed Ghastenrian gate requiring a shamanic key-item.

## Reworded

`Prompt:`

```
Hey claude, take a look at the description for a dark fantasy location I've attached as a markdown file.  need you to update this so that the words used (both for proper-named places, and for regular nouns) mix in my setting-specific words defined in the attached json document. Substitute setting vocabulary sparingly. Convert proper nouns. Choose ONE key term to anchor the location's identity and use it no more than twice. Reserve other specialized words for moments of mystery, ritual, or deep antiquity—places where strangeness belongs. Leave generic words wherever they're doing navigational or functional work.
```

### The Kelpshaw Soutrenn

#### Exterior Compound

A rhath gone to ruin—two longhouses with collapsed thatch, watchtowers listing like rotten teeth, a central firepit trailing smoke. Wooden walkways, half-swallowed by creeping moss, bridge the structures. Raiders have claimed the place: desperate Kinfolk turned bandit under **Moldrick One-Hand**, who sits by the fire working a notched blade with his remaining fingers. His people watch the approaches—two at the gate, three more on the overgrown earthworks. Wet ash on the wind. Something fouler beneath.

#### Upper Soutrenn (The Old Ward-Hall)

Stone steps descend into cool dark. The walls bear carved spirals—shamanic work, centuries old—now cracked and black with mold. Shattered **Kestanes** litter the corridor: jade hound-shapes with fractured limbs. Two raiders crouch near a guttering torch, arguing over a stolen ring.

The passage branches. North: a barred door (key on a sleeping guard) leads to a cell where **Mother Drelvi**, an aging shaman, awaits ransom or rescue. South: a ramp descends to a vaulted chamber where the wards have bled dry. Kestanes have reawakened and turned on the raiders who disturbed them. Two bandits hold each raised walkway; two jade guardians click and scrape across flagstones slick with old rain, two more fighters already bleeding below.

Beyond, corridors wind through halls where **Bhruggspire** drift in slow, grinding circuits—floating sentinels trailing dust, jade wings humming a sound felt in the teeth. Ceiling scuttles disgorge more Kestanes as you pass. A spear-trap gauntlet blocks the way forward: six pressure-plates requiring careful sequencing.

#### Lower Depths (The Drowned Roots)

A counterweighted lift descends to flooded caverns. Black water pools between raised stone walkways; roots of ancient trees pierce the ceiling like grasping fingers. **Sarks** have nested here—Lost Ones wearing rotted remnants of farmers' clothes, clicking in the dark. Their tents are hide stretched over bone. A lone **Skrelving** guards a web-choked alcove, rust-feathers bristling.

A split-level chamber holds two Sarks across its gallery. Beyond, tripwire deadfalls and more Sark camps. Old meat. Black water. Something vegetable and wrong. A gated courtyard with a cracked fountain contains a half-dozen Lost Ones and two crude shelters. _"What falls to ruin invites new tenants."_ A spiral ramp ascends a tower where a lever retracts the bone-spears blocking egress.

#### The Warden's Rest (Boss Chamber)

A **Grundkholm** stands dormant in a stone alcove—twice a man's height, carved from red-veined jade, its eyes dark pits. It wakes when you cross the threshold. Mid-fight, a Gravelform may descend from above. Raised platforms offer retreat; a lever lowers spears guarding a chest.

A sealed gate bears spiral carvings and a keyhole shaped like no modern lock. Press your ear to the stone: something breathing on the other side. Slow. Vast. Patient.

An exit lift returns to the surface, emerging west of the compound beneath a sky darker than when you entered.

---

**Key Interactive Features:** Spear-trap sequencing puzzle (Upper Soutrenn); tripwire deadfalls (Lower Depths); boss-arena lever; sealed Ghastenrian gate requiring a shamanic key-item.

## Final Cleanup

`Prompt:`

```
Hey claude, can you revise the attached markdown doc describing a location in a fantasy setting I'm working on? Revise it with the following goals:
- clean up unrealistic dialogue
- replace all em-dashes with alternative punctuation
- replace 30% of common verbs/adjectives/nouns with uncommon equivilants
- replace 80% of parallel construction sentences
- replace 40% of triadic constructions (lists, three-sentence rhythms, etc) with two-, four-, or five-item constructions
- do not replace any setting-specific words or proper nouns
- your revised version must not exceed the original in total letters/characters
```

### The Kelpshaw Soutrenn

#### Exterior Compound

A rhath gone to wreckage—two longhouses with caved thatch, watchtowers canting like rotten teeth. Wooden walkways, half-swallowed by creeping moss, span the structures. A central firepit trails smoke. Raiders have claimed the place: desperate Kinfolk turned bandit under **Moldrick One-Hand**, who hunches by the flames working a notched blade with his remaining fingers. His people watch the approaches—two at the gate, three more on the overgrown earthworks. Wet ash on the wind, something fouler beneath.

#### Upper Soutrenn (The Old Ward-Hall)

Stone steps plunge into cool dark. The walls bear carved spirals—shamanic work, centuries old—now cracked and blackened with mold. Shattered **Kestanes** litter the corridor: jade hound-shapes with fractured limbs. Two raiders crouch near a guttering torch, bickering over a stolen ring.

The passage forks. North: a barred door (key on a dozing guard) opens to a cell where **Mother Drelvi**, an aging shaman, awaits ransom or rescue. South: a ramp drops to a vaulted chamber where the wards have bled dry. Kestanes have reawakened and turned on the raiders who disturbed them. Two bandits hold each raised walkway; two jade guardians click and scrape across flagstones slick with old rain, two more fighters bleeding below.

Beyond, corridors wind through halls where **Bhruggspire** drift in slow circuits—floating sentinels trailing dust, jade wings humming a sound felt in the teeth. Ceiling scuttles disgorge more Kestanes as you pass. A spear-trap gauntlet blocks the way forward: six pressure-plates demanding careful sequencing.

#### Lower Depths (The Drowned Roots)

A counterweighted lift sinks to flooded caverns. Black water pools between raised stone walkways; roots of ancient trees pierce the ceiling like grasping fingers. **Sarks** have nested here—Lost Ones wearing rotted remnants of farmers' clothes, clicking in the dark. Their tents are hide stretched over bone. A lone **Skrelving** guards a web-choked alcove, rust-feathers bristling.

A split-level chamber holds two Sarks across its gallery. Beyond: tripwire deadfalls, more Sark camps, old meat, black water. Something vegetable and wrong. A gated courtyard with a cracked fountain contains a half-dozen Lost Ones and two crude shelters. A spiral ramp ascends a tower where a lever retracts the bone-spears barring egress.

#### The Warden's Rest (Boss Chamber)

A **Grundkholm** stands dormant in a stone alcove—twice a man's height, carved from red-veined jade, its eyes dark pits. It stirs when you cross the threshold. Mid-fight, a Gravelform may plunge from above. Raised platforms offer retreat; a lever lowers spears guarding a chest.

A sealed gate bears spiral carvings with a keyhole shaped like no modern lock. Press your ear to the stone: something breathing on the other side. Slow. Patient.

An exit lift returns to the surface, emerging west of the compound beneath a sky darker than when you entered.

---

**Key Interactive Features:** Spear-trap sequencing puzzle (Upper Soutrenn); tripwire deadfalls (Lower Depths); boss-arena lever; sealed Ghastenrian gate requiring a shamanic key-item.
