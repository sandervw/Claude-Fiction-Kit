---
name: forbidden-patterns
description: Per-scene blacklist of LLM prose tells. Predictive mode rolls a sampled blacklist before drafting; audit mode scans a draft against an existing blacklist and flags violations. Triggers include "forbidden patterns", "ban patterns", "audit draft", "scene blacklist".
---

Two modes. Detect from the request.

- **Predictive** — user asks for bans/blacklist before drafting, or provides scene context without a draft. Default.
- **Audit** — user provides a draft plus an existing blacklist card and asks for a check.

## Predictive

Roll bans from `assets/vocabulary.json` using `assets/sampling.py`:

```
python assets/sampling.py simile_bans 2
python assets/sampling.py cadence_bans 2
python assets/sampling.py syntactic_bans 1
python assets/sampling.py imagery_bans 2
python assets/sampling.py register_bans 1
```

Use the rolled rules verbatim. Do not paraphrase or soften. If the user supplies additional bans, append them.

Compose a markdown card with categorized bans and a one-line note: *"The writing agent treats every ban above as a hard contract."* Save to `output/blacklist-[scene-tag].md`.

## Audit

Read the draft and the existing blacklist card. Scan systematically — one ban at a time.

For each violation report: paragraph or line reference, the offending text quoted, and the rule it broke.

Do NOT rewrite. Output a violation report only. Save to `output/audit-[scene-tag].md`.
