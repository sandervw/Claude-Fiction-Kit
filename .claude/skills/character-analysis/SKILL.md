---
name: character-analysis
description: Analyze fictional characters using structured templates. Use when asked to analyze, break down, or create character profiles for fictional characters. Triggers include "analyze [character]", "character breakdown", "create character templates for", or requests for character analysis documents. Supports main characters (full analysis) and secondary characters (purpose only). Also supports Actions mode for listing concrete actions a character takes — triggers include "character actions", "list what [character] does", "action list for [character]".
---

# Character Analysis

Analyze fictional characters and output structured documents.

## Mode Detection

Determine mode from user request:

**Profile mode** (default):
→ Triggers: "analyze", "character breakdown", "character profile", "character template"
→ **Read**: `assets/profile-reference.md`

**Actions mode**:
→ Triggers: "character actions", "what does [character] do", "list of actions", "action list"
→ **Read**: `assets/actions-reference.md`

If ambiguous, ask user which mode.

## Workflow

1. Detect mode from triggers above
2. Read the appropriate reference doc for that mode
3. Follow the workflow in that reference doc
4. Present completed file(s) to user