# LLMAppDocs

A toolkit for LLM-assisted fiction writing, built around Claude Code's skills and agents system. Feed in literary source material and worldbuilding docs, get structured prose generation, style revision, and character analysis out.

## What This Is

This repository is part research lab, part writing workbench. It contains:

- **Custom Claude Code skills** for scene writing, prose revision, character analysis, folklore generation, and more
- **Custom Claude Code agents** for draft editing, tag extraction, and document compression
- **A dark fantasy setting** (Whyneland) with bestiary, world lore, and etymology guides
- **Literary source texts** from Howard, Peake, Eddison, Vance, Homer, and others -- used for style analysis and emulation
- **JSON element libraries** for procedural character generation, scene tagging, and template selection
- **Node.js utilities** that interface with the Claude API for automated prose revision

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code)
- An Anthropic API key (for the Node.js scripts)

### Setup

```bash
npm install
```

### Usage

**With Claude Code (primary workflow):**

Open the repo in Claude Code. The 8 skills and 3 agents are automatically available. Use them via slash commands (e.g., `/scene-writer`, `/literary-revision`) or by asking Claude to invoke them.

**With Node.js scripts:**

```bash
# Revise prose via Claude API
# Place input text in Input/temp.md, then:
node main.js

# Generate a character from templates
npm run generate-character
```

## Skills

| Skill                   | What It Does                                                                            |
| ----------------------- | --------------------------------------------------------------------------------------- |
| `scene-writer`          | Writes complete prose scenes from an outline and story context                          |
| `literary-revision`     | Revises prose in literary styles (Howard, Peake, Eddison, Thorogood)                    |
| `voice-revision`        | Rewrites prose in character voices (Freeman, Cugel, Gittes, Dagoth Ur, Solaire)         |
| `story-idea-generator`  | Generates story ideas by colliding two unrelated elements (bisociation)                 |
| `character-analysis`    | Analyzes fictional characters across four modes (profile, description, actions, quotes) |
| `character-abstraction` | Strips setting details from character elements into portable templates                  |
| `fiction-abstraction`   | Abstracts paragraphs and dialogue into reusable, generic templates                      |
| `folklore-generator`    | Generates culturally-plausible folklore for objects or phenomena                        |

## Agents

| Agent            | What It Does                                                       |
| ---------------- | ------------------------------------------------------------------ |
| `draft-editor`   | Three-phase prose review: analyze, report, revise                  |
| `fiction-tagger` | Extracts concrete tags from fictional sources into structured JSON |
| `text-trimmer`   | Compresses documents to ~70% token count while preserving clarity  |

## Repository Layout

```
├── .claude/skills/      # 8 custom Claude Code skills with reference docs
├── .claude/agents/      # 3 specialized agents
├── Elements/            # JSON data (names, tags, actions, templates, encyclopedia)
├── Input/               # Working input files and revision guides
├── javascript/          # Node.js utilities for generation and parsing
├── Markdown/            # Prompts, worldbuilding, writing guides
├── Output/              # Generated prose and story ideas
├── Sources/
│   ├── OriginalWorks/   # Full literary texts for style analysis
│   └── Derivative/      # Game/RPG lore for tag extraction
├── main.js              # Entry point for LLM-powered prose revision
└── package.json
```

## Tech Stack

- **Claude Code** -- skills, agents, and interactive writing workflows
- **Node.js** -- automation scripts and Claude API integration
- **@anthropic-ai/sdk** -- Claude API client
- **Python** -- utility scripts (tag randomization)
