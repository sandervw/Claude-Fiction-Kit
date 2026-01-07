---
name: character-generalizer
description: Generalize character elements (actions, quotes, descriptions) from specific fictional sources.. Use when asked to "generalize [elements]", make elements "more general" or "setting-agnostic", create "reusable" or "generic" templates. Triggers include "generalize [filename]", "make [character] generic", "strip [element] details".
---

# Character Generalizer

Transform setting-specific character elements into portable, reusable templates for worldbuilding.

## Mode Detection

Determine mode from user request:

**Actions mode**:
- Triggers: "generic actions", "generalize actions", "list of generic actions"
- **Read**: `references/actions-reference.md`

**Quotes mode**:
- Triggers: "generic quotes", "generalize quotes", "generate quote structure"
- **Read**: `references/quotes-reference.md`

If ambiguous, ask user which mode.

## Workflow

1. Detect mode from triggers above
2. Read the appropriate reference doc for that mode
3. Follow the workflow in that reference doc
4. Present completed file(s) to user