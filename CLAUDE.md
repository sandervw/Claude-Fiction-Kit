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

### Prose Revision
Use the `literary-revision` skill for prose revision in specific styles (Thorogood, Howard, Peake, etc.). Style references are maintained in `.claude/skills/literary-revision/references/`.

### Tag Quality Guidelines
Good tags: brief (1-3 words), evocative, transferable ("black palace", "ashen ruins")
Bad tags: proper names, verbose descriptions, overly specific

## Output Formats

- JSON for LLM-processable data
- Markdown for human-readable content and web display
