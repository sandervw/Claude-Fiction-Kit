# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LLMAppDocs is a toolkit and research repository for LLM-assisted fiction writing. Think of it as a workbench: literary source material goes in, and structured writing tools, prompts, and generated prose come out. The project focuses on:

- Dark fantasy worldbuilding (Whyneland setting, bestiary, folklore)
- LLM prompt engineering for prose generation and revision
- Tag/trait extraction from fictional source material
- Literary style emulation (Howard, Peake, Eddison, Vance, etc.)
- Claude Code skills and agents for structured creative workflows

## Repository Structure

```
LLMAppDocs/
├── .claude/
│   ├── agents/          # Specialized agents (draft-editor, fiction-tagger, text-trimmer)
│   └── skills/          # 8 custom skills (see Skills section below)
├── Elements/            # JSON data libraries (names, tags, actions, templates, encyclopedia)
├── Input/               # Working input files, revision guides, context notes
├── Images/              # Image assets
├── javascript/          # Node.js utilities (character gen, template selection, markdown parsing)
├── Markdown/            # Prompts, worldbuilding docs, writing guides, BRD
├── Output/              # Generated prose, dialogue, story ideas
├── Sources/
│   ├── OriginalWorks/   # Literary source texts (Peake, Howard, Eddison, Homer, etc.)
│   └── Derivative/      # Game/RPG lore (Dark Souls, Hollow Knight, Malazan, etc.)
├── main.js              # Entry point: reads Input/temp.md, revises via Claude, outputs to Output/
├── package.json         # Node.js config, depends on @anthropic-ai/sdk
└── CLAUDE.md
```

## Skills (`.claude/skills/`)

| Skill                     | Purpose                                                                        |
| ------------------------- | ------------------------------------------------------------------------------ |
| **scene-writer**          | Write complete prose scenes from outline + story context                       |
| **literary-revision**     | Revise prose in specific literary styles (Howard, Peake, Eddison, Thorogood)   |
| **voice-revision**        | Rewrite prose in character voices (Freeman, Cugel, Gittes, Dagoth Ur, Solaire) |
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

- **Worldbuilding setting**: Whyneland (regressive dark fantasy). Key docs: `Markdown/World.md`, `Markdown/Bestiary.md`
- **Prompts reference**: `Markdown/Prompts.md` contains scene-writing, revision, and generation prompts
- **Story files**: Stories live in a `Stories/` folder structure with TODO-driven scene tracking
- **Literary sources**: Full texts in `Sources/OriginalWorks/` are used for style analysis and tag extraction
- **JSON element libraries** in `Elements/` power character generation and template selection
- **Node.js entry point**: `main.js` reads from `Input/temp.md`, applies LLM revision, writes to `Output/llmresult.md`

## Working With This Repo

- When writing scenes, always check the TODO file for current scene priorities and placement
- When revising prose, reference the appropriate style/voice skill rather than improvising
- Prefer reading existing source material and worldbuilding docs before generating new content
- The `Elements/*.json` files are structured data -- modify via scripts or careful manual editing
- Story context files (setting, lore, character docs) should be read before scene writing to maintain consistency
