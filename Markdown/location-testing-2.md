# Crannóg Teile

## First Draft

`Prompt:`

```
Hey claude, take a look at the attached lore document for a dark-fantasy world I'm working on. I want you to generate a concrete location in this setting. Ideally, this is a lore-appropriate settlement or distinctive geographical feature. I want this settlement to serve as a background or location for a short story. Your description should meet the following constraints:
1. A few-paragraph description, NO MORE THAN 400 words.
2. Include A MINIMUM of three concrete sensory details - textural elements to help ground the writing.
3. Inlude AT LEAST ONE small, unusual aspect or feature - something uncanny for the setting.
4. Reference AT LEAST THREE named characters or creatures.
  a. AT LEAST ONE must some kind of leader or authority in a field (or significant creature); at least one must be common.
  b. Use the lore document to guide your choice of character/creature, but DO NOT copy/paste anything directly from the document.
```

**Crannóg Teile**

The settlement clings to a limestone islet in the middle of Loch Mórann, accessible only by a causeway of rotting timber that surfaces at low tide. The water is black and still, tasting of peat and old iron when the wind lifts spray to your lips. Seventeen souls remain—down from forty-three when the warlord Brennach mac Coire first declared this place a refuge, six winters past.

Brennach rules from a roundhouse whose thatch has gone grey with damp. He is a thick-armed man who once led raids on the mainland; now he spends his days reinforcing the causeway timbers and rationing grain. His axe hangs above the hearthfire, untouched for two seasons. There is nothing left worth raiding, and no one comes to trade.

The druid Síle keeps the names. Each evening before the communal meal, she recites the lineages of every resident—a wavering litany that takes longer each month, as she must now speak for the dead as well as the living. Her fingers are stained black from the oak-gall ink she uses to mark genealogies onto scraped hide. She insists the children listen. She insists they repeat. The youngest, a boy called Faolán, mouths the words but his eyes slide toward the water, watching something none of the adults acknowledge.

The uncanny thing: the fish have stopped coming. Not scarce—gone. The loch surface lies mirror-flat most days, undisturbed by fin or ripple. Yet each morning, Cáit the net-mender finds her lines heavy with something. Waterlogged cloth. A leather shoe. Once, a carved wooden figure so worn by the black water that its features had smoothed to nothing. She buries these finds behind the roundhouse and speaks of them to no one, though Síle has noticed the fresh-turned earth and says nothing either.

At night, the wind carries sounds from the mainland shore—clicks and low hoots that might be owls, or might be the Sarks who have claimed the abandoned village there. On clear evenings, you can see the glow of their fires through the trees. They remember fire, at least. Brennach posts a watch until dawn, though everyone knows the Lost Ones fear the water.

What no one mentions is that the causeway timbers are rotting faster than they can be replaced. By spring, the path may sink entirely. Whether that makes the crannóg a fortress or a tomb depends on what remains when the last plank goes under.

## Revised Prose

`Prompt:`

```
Hey claude, can you revise the attached markdown doc describing a location in a fantasy setting I'm working on? Revise it with the following goals:
* Cut explanatory scaffolding. If a sentence tells the reader what to feel ("The horror is..."), remove it or replace it with imagery that evokes that feeling.
* Compress bullet lists. Keep only the most vivid 3-4 points. Trust implication.
* Vary sentence rhythm. Break long sentences into fragments where impact warrants. Combine choppy sequences into longer rolling clauses where atmosphere warrants.
* Replace generic phrasing with specific, tactile language. "The sea encroaches" → "The sea swallows the coast in fingerwidths."
* Add aphorisms as inline quoted phrases that crystallize themes.
* Your revised version must not exceed the original in total letter/character.
```

**Crannóg Teile**

The settlement clings to a limestone islet in Loch Mórann, reached only by a causeway of rotting timber that surfaces at low tide. The water lies black and still. It tastes of peat and old iron when the wind lifts spray to your lips.

Seventeen souls remain—down from forty-three when the warlord Brennach mac Coire declared this place a refuge, six winters past. He rules from a roundhouse whose thatch has gone grey with damp, a thick-armed man who once led raids on the mainland. Now he reinforces timbers and rations grain. His axe hangs above the hearthfire, untouched two seasons. "What cannot be taken cannot be kept."

The druid Síle keeps the names. Each evening she recites every lineage—a wavering litany growing longer each month, for she must now speak for the dead as well as the living. Her fingers are stained black from oak-gall ink. She insists the children listen. Repeat. The youngest, Faolán, mouths the words but his eyes slide toward the water, watching something none of the adults acknowledge.

The fish have stopped coming. Not scarce—gone. The loch surface lies mirror-flat, undisturbed by fin or ripple. Yet each morning, Cáit the net-mender finds her lines heavy. Waterlogged cloth. A leather shoe. Once, a carved figure so worn by the black water its features had smoothed to nothing. She buries these finds behind the roundhouse and speaks of them to no one.

At night, the wind carries sounds from the mainland—clicks and low hoots that might be owls, or might be the Sarks who have claimed the abandoned village there. On clear evenings, their fires glow through the trees. They remember fire, at least. Brennach posts a watch until dawn, though everyone knows the Lost Ones fear the water.

The causeway rots faster than it can be replaced. By spring, the path may sink entirely. "A wall that holds nothing out holds everything in."

## Renamed Characters

`Prompt:`

```
Hey claude, take a look at the description for a dark fantasy location I've attached as a markdown file.  need you to update this so that any proper character names are pulled randomly from the attached json doc. Don't update creatures or locations, just the actual people-names. To make sure your choice is random, write a quick python script to randomly select from each list of names (male or female) as appropriate.
```

**Crannóg Teile**

The settlement clings to a limestone islet in Loch Mórànn, reached only by a causeway of rotting timber that surfaces at low tide. The water lies black and still. It tastes of peat and old iron when the wind lifts spray to your lips.

Seventeen souls remain—down from forty-three when the warlord Vardrek declared this place a refuge, six winters past. He rules from a roundhouse whose thatch has gone grey with damp, a thick-armed man who once led raids on the mainland. Now he reinforces timbers and rations grain. His axe hangs above the hearthfire, untouched two seasons. "What cannot be taken cannot be kept."

The druid Gellandrixa keeps the names. Each evening she recites every lineage—a wavering litany growing longer each month, for she must now speak for the dead as well as the living. Her fingers are stained black from oak-gall ink. She insists the children listen. Repeat. The youngest, Grundvik from Lowmire, mouths the words but his eyes slide toward the water, watching something none of the adults acknowledge.

The fish have stopped coming. Not scarce—gone. The loch surface lies mirror-flat, undisturbed by fin or ripple. Yet each morning, Phollimbra Dess the net-mender finds her lines heavy. Waterlogged cloth. A leather shoe. Once, a carved figure so worn by the black water its features had smoothed to nothing. She buries these finds behind the roundhouse and speaks of them to no one.

At night, the wind carries sounds from the mainland—clicks and low hoots that might be owls, or might be the Sarks who have claimed the abandoned village there. On clear evenings, their fires glow through the trees. They remember fire, at least. Vardrek posts a watch until dawn, though everyone knows the Lost Ones fear the water.

The causeway rots faster than it can be replaced. By spring, the path may sink entirely. "A wall that holds nothing out holds everything in."

## Reworded (Final Draft?)

`Prompt:`

```
Hey claude, take a look at the description for a dark fantasy location I've attached as a markdown file.  need you to update this so that the words used (both for proper-named places, and for regular nouns) mix in my setting-specific words defined in the attached json document. Substitute setting vocabulary sparingly. Convert proper nouns. Choose ONE key term to anchor the location's identity and use it no more than twice. Reserve other specialized words for moments of mystery, ritual, or deep antiquity—places where strangeness belongs. Leave generic words wherever they're doing navigational or functional work.
```

**Krannogg Teile**

The settlement clings to a limestone islet in Lake Dremling, reached only by a causeway of rotting timber that surfaces at low tide. The water lies black and still. It tastes of peat and old iron when the wind lifts spray to your lips.

Seventeen souls remain, down from forty-three when the warlord Vardrek declared this krannogg a refuge, six winters past. He rules from a rhundhaus whose thatch has gone grey with damp, a thick-armed man who once led raids on the mainland. Now he reinforces timbers and rations grain. His axe hangs above the hearthfire, untouched two seasons.

The druid Gellandrixa keeps the names. Each evening she recites every lineage—a wavering litany growing longer each month, for she must now speak for the dead as well as the living. Her fingers are stained black from oak-gall ink. She insists the children listen. Repeat. The youngest, Grundvik from Dhallmire, mouths the words but his eyes slide toward the water, watching something none of the adults acknowledge.

The fish have stopped coming. Not scarce, gone. The lake surface lies mirror-flat, undisturbed by fin or ripple. Yet each morning, Phollimbra Dess the net-mender finds her lines heavy. Waterlogged cloth. A leather shoe. Once, a figure carved from the stone of some passaj grav, so worn by the black water its features had smoothed to nothing. She buries these finds behind the rhundhaus and speaks of them to no one.

At night, the wind carries sounds from the mainland—clicks and low hoots that might be owls, or might be the Sarks who have claimed the abandoned balli there. On clear evenings, their fires glow through the trees. They remember fire, at least. Vardrek posts a watch until dawn, though everyone knows the Lost Ones fear the water.

The causeway rots faster than it can be replaced. By spring, the path may sink entirely. "A wall that holds nothing out holds everything in."
