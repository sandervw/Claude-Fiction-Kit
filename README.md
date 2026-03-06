# Claude-Fiction-Kit

A toolkit for LLM-assisted fiction writing, built around Claude Code's skills and agents system. Feed in literary source material and worldbuilding docs, get structured prose generation, style revision, and character analysis out.

## What This Is

This repository is part research lab, part writing workbench. It contains:

- **Custom Claude Code skills** for scene writing, prose revision, character analysis, folklore generation, and more
- **Custom Claude Code agents** for draft editing, tag extraction, and document compression
- **Literary source texts** -- public-domain works (Howard, Peake, Eddison, Smith, Homer) and game/RPG lore (Dark Souls, Hollow Knight, Malazan)
- **Fiction worldbuilding** -- the Whyneland setting with bestiary, etymology, cosmology, and story drafts
- **Structured data** -- JSON files for names, scene tags, vocabulary, paragraph templates, and character actions
- **Utility scripts** -- Node.js tools for character generation and template selection, Python tools for Gutenberg conversion and tag randomization

## Getting Started

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI installed
- Node.js (for running JS utilities in `code/`)
- Python 3 (for running Python utilities in `code/python/`)

### Setup

```bash
git clone https://github.com/your-username/Claude-Fiction-Kit.git
cd Claude-Fiction-Kit
cd code && npm install && cd ..
```

### Usage

The primary workflow is through Claude Code's skills and agents. Open the repo in Claude Code and use slash commands:

```
/scene-writer          # Write a prose scene from an outline
/literary-revision     # Revise text in a literary style
/voice-revision        # Rewrite text in a character's voice
/story-idea-generator  # Generate a story idea via bisociation
/character-analysis    # Analyze a fictional character
/folklore-generator    # Generate folklore for an object or phenomenon
```

You can also run the Node.js utilities directly:

```bash
cd code
npm run generate-character    # Generate a character from templates
npm run main                  # Run the main paragraph archive tool
```

Or the Python utilities:

```bash
python code/python/convert-gutenberg.py <input.html> [output.md]   # Convert Gutenberg HTML to Markdown
python code/python/random_tags.py                                   # Select random tags from JSON
```

## Skills

| Skill                   | What It Does                                                                            |
| ----------------------- | --------------------------------------------------------------------------------------- |
| `scene-writer`          | Writes complete prose scenes from an outline and story context                          |
| `literary-revision`     | Revises prose in literary styles (Howard, Peake, Eddison)                               |
| `voice-revision`        | Rewrites prose in character voices (Freeman, Paladin, Thorogood)                        |
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
Claude-Fiction-Kit/
├── .claude/
│   ├── agents/              # 3 specialized agents (draft-editor, fiction-tagger, text-trimmer)
│   └── skills/              # 8 custom skills, each with SKILL.md, assets/, and references/
├── code/
│   ├── javascript/          # Node.js utilities (character gen, template selection, markdown parsing)
│   ├── python/              # Python utilities (Gutenberg converter, random tag selector)
│   └── package.json
├── documentation/           # Project docs, prompt archives, research templates
├── fiction/
│   ├── elements/            # JSON data (names, words, scene tags, paragraph templates)
│   ├── images/              # Character/creature artwork
│   └── whyneland/           # Whyneland setting: world docs, bestiary, story drafts
├── input/                   # Working scratch files, context notes, revision guides
├── output/                  # Generated results (dialogue, story ideas, character data)
├── sources/
│   ├── literature/          # Public-domain texts (Howard, Peake, Eddison, Smith, Homer)
│   └── derivative/          # Game/RPG lore (Dark Souls, Hollow Knight, Malazan, yokai)
├── CLAUDE.md                # Claude Code project instructions
└── README.md
```

## Tech Stack

- **Claude Code** -- skills, agents, and interactive writing workflows
- **@anthropic-ai/sdk** -- Claude API client
- **Node.js** -- automation scripts and Claude API integration
- **Python** -- utility scripts (Gutenberg conversion, tag randomization)
