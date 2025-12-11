# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LLMAppDocs is a documentation and research repository for an LLM-powered dynamic storytelling web app. The project focuses on:
- Dark fantasy worldbuilding and genre analysis
- LLM prompt engineering for prose generation
- Tag/trait extraction from fictional source material
- Testing and refining prose revision techniques across different literary styles

## Repository Structure

```
LLMAppDocs/
├── Markdown/           # Core documentation and analysis
│   ├── BRD-LLM-Storyteller.md   # Business requirements document
│   ├── Dark-Fantasy-Analysis.md  # Genre anatomy of 11 dark fantasy works
│   ├── Prompts.md               # Worldbuilding prompt templates
│   └── Revision-Tests.md        # Prose revision experiments
├── JSONInput/          # Input data for LLM processing
│   └── setting-tags.json        # Curated setting tags
├── JSONOutput/         # Generated outputs from tag extraction
├── Elements/           # Story element definitions
│   └── worlds.json
├── .claude/agents/     # Custom Claude Code agents
│   ├── fiction-tagger.md        # Full tag extraction agent
│   └── fiction-tagger-mark2.md  # Lightweight tag extraction agent
└── generate_combinations.py     # Python utility for tag combinations
```

## Custom Agents

### fiction-tagger / fiction-tagger-mark2
Extract thematic tags from fictional sources (Dark Souls, The Black Company, etc.). Invoke with:
- Source name (the fictional work)
- Tag type (monster, setting, character trait, character description, weapon, magic, atmosphere)
- Number of tags to extract

Output goes to `JSONOutput/[source]-[type].json`

## Key Concepts

### Prose Revision Guidelines
The repository documents tested methods for rewriting prose in specific styles:

**Dark Souls Style** (Gemini method preferred):
1. Mythic Capitalization - capitalize common nouns as Proper Nouns
2. Passive Historic Voice - narrator as observer of fate
3. Contrast and Disparity - juxtapose opposing concepts rhythmically
4. Archaic/Somber Vocabulary - gothic over technical words
5. "The Turn" - history first, then immediate danger to the individual

**Robert E. Howard Style** (GPT method preferred):
1. Name places and give reputation
2. Physical, archaic nouns/verbs over neutral ones
3. Turn abstracts into three concrete images
4. Personify landscape as beast/titan
5. Rolling sentence chains with occasional short cuts
6. Concrete sensory language over explanation
7. Logic dressed in legend

**Mervyn Peake Style**:
1. Animism of the inanimate - buildings with agency
2. Juxtapose elegant and grotesque
3. Labyrinthine sentence structure with multiple clauses
4. Precise textural vocabulary
5. Focus on lighting and shadow
6. Auditory weight - sound as physical presence
7. Micro-focus on movement details

### Tag Quality Guidelines
Good tags: brief (1-3 words), evocative, transferable ("black palace", "ashen ruins")
Bad tags: proper names, verbose descriptions, overly specific

## Output Formats

- JSON for LLM-processable data
- Markdown for human-readable content and web display
