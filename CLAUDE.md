# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LLMAppDocs is a toolkit and research repository for LLM-assisted fiction writing. Think of it as a workbench: literary source material goes in, and structured writing tools, prompts, and generated prose come out. The project focuses on:

- Worldbuilding prompt and context engineering
- Prose generation and revision with Claude Code and Claude API
- Literary style emulation (Howard, Peake, Eddison, Vance, etc.)
- Character analysis and abstraction into reusable templates
- Story ideation via bisociation (colliding unrelated elements)
- Folklore and cultural worldbuilding generation

## Repository Structure

```
Claude-Fiction-Kit/
├── .claude/
│   ├── agents/              # Custom claude agents (draft-editor, fiction-tagger, text-trimmer)
│   └── skills/              # Custom claude skills (see Skills section below)
├── code/
│   ├── javascript/          # Node.js utilities (character gen, template selection, markdown parsing)
│   ├── python/              # Python utilities (Gutenberg HTML-to-MD converter, random tag selector)
│   ├── package.json         # Node project config (uses @anthropic-ai/sdk)
│   └── package-lock.json
├── documentation/           # Project docs, prompt archives, research templates
├── fiction/
│   ├── elements/            # JSON data files (names, words, scene tags, paragraph templates, etc.)
│   ├── images/              # Character/creature artwork (PNG)
│   └── whyneland/           # Whyneland setting: worldbuilding, bestiary, stories, drafts
├── input/                   # Working input files, context notes, revision guides, temp scratch
├── output/                  # Generated results (dialogue guidelines, story ideas, character JSON)
├── sources/
│   ├── literature/          # Public-domain literary texts (Howard, Peake, Eddison, Smith, Homer, etc.)
│   └── derivative/          # Game/RPG lore extracts (Dark Souls, Hollow Knight, Malazan, yokai, etc.)
├── CLAUDE.md
└── README.md
```

## Skills (`.claude/skills/`)

| Skill                     | Purpose                                                                        |
| ------------------------- | ------------------------------------------------------------------------------ |
| **scene-writer**          | Write complete prose scenes from outline + story context                       |
| **literary-revision**     | Revise prose in specific literary styles (Howard, Peake, Eddison)              |
| **voice-revision**        | Rewrite prose in character voices (Freeman, Paladin, Thorogood)                |
| **story-idea-generator**  | Generate story ideas via bisociation (colliding two unrelated elements)        |
| **character-analysis**    | Analyze fictional characters (profile, description, actions, quotes)           |
| **character-abstraction** | Strip setting-specific details from character elements into portable templates |
| **fiction-abstraction**   | Abstract paragraphs/dialogue into reusable, generic templates                  |
| **folklore-generator**    | Generate culturally-plausible folklore for objects or phenomena                |

## Agents (`.claude/agents/`)

| Agent              | Purpose                                                         |
| ------------------ | --------------------------------------------------------------- |
| **draft-editor**   | 3-phase prose review: analyze, report, revise                   |
| **fiction-tagger** | Extract 1-word concrete tags from fictional sources into JSON   |
| **text-trimmer**   | Compress documents to ~70% token count while preserving clarity |

## Key Conventions

- Always write results to markdown or JSON files unless instructed otherwise
- Output goes to the `output/` folder by default (see Working With This Repo)
- Literary source texts live in `sources/literature/` (public domain) and `sources/derivative/` (game/RPG lore)
- JSON data files (names, tags, templates) live in `fiction/elements/`
- Skills follow a consistent structure: `SKILL.md` (instructions), `assets/` (templates), `references/` (style guides)
- Node.js code uses ES modules (`"type": "module"` in package.json) and the Anthropic SDK

## Working With This Repo

- Always write generated results to `output/` unless instructed otherwise
- Use `input/` for scratch/working files (context notes, temp markdown, revision guides)
- When running JS code, `cd` into `code/` first (`npm` scripts expect that working directory)
- To convert a Gutenberg HTML book: `python code/python/convert-gutenberg.py <input.html> [output.md]`
- Source texts are reference material; do not modify files in `sources/` unless asked
- The `fiction/whyneland/` folder contains an active fiction project; treat drafts carefully
