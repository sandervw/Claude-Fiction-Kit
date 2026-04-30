# CLAUDE.md

## Project Overview

LLMAppDocs is a toolkit and research repository for LLM-assisted fiction writing.

## Repository Structure

```
Claude-Fiction-Kit/
├── .claude/
├── code/
├── documentation/           # Project docs, prompt archives, research templates
├── fiction/
├── input/
├── output/
├── sources/
├── CLAUDE.md
└── README.md
```

## Rules

- Always write results to markdown or JSON files unless instructed otherwise
- Always write generated results to `output/` unless instructed otherwise
- Use `input/` for scratch/working files
- Literary source texts live in `sources/literature/` (public domain) and `sources/derivative/` (game/RPG lore)
- Do not modify files in `sources/` unless asked
- Skills follow a consistent structure: `SKILL.md` (instructions), `assets/` (resources), `references/` (information)
- Node.js code uses ES modules (`"type": "module"` in package.json) and the Anthropic SDK
- When running JS code, `cd` into `code/` first
