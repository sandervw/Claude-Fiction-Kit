## Conversion Prompt

Hey claude, take a look at the json I've pasted below. This is a breakdown of the 'wise woman' archtype of cozy/cottage fantasy. I want to take this archtype, and basically convert/pervert it to fit a dark fantasy story, and dark fantasy features. I want this conversation to be a back/forth between you and me, with you acting as a springboard. The final result would be a json template, similar to the one below, but for my new 'dark fantasy archtype',with some fields adjusted, some fields left the same, some fields much more fleshed out.
Before we start, do a quick web search on the follow characters, so you have an broader context of the archtype's defining traits:

- Kiela from The Spellshop by Sarah Beth Durst
- Granny Weatherwax from the Discworld Series
- Sylvie and her mother and grandmother from Healer and Witch by Nancy Werlin

Also, here are some defining dark-fantasy features we're shooting for:

| Feature                   | Dark Fantasy Protagonist Version           |
| ------------------------- | ------------------------------------------ |
| **Motivation**            | Survival, profit, vengeance, curiosity     |
| **Moral framework**       | Situational, amoral, or inverted           |
| **Relationship to magic** | Corrupting force, enemy, or costly bargain |
| **Community**             | Isolated, bonds are temporary or fatal     |
| **Character arc**         | Stasis, corruption, or doom                |
| **Victory condition**     | Personal survival, pyrrhic triumph         |
| **Divine relationship**   | Gods are absent, hostile, or manipulative  |

JSON:

```
{
      "type-name": "The Village Wise Woman",
      "values": [
        "community",
        "duty",
        "tradition"
      ],
      "default-personality-trait": "Pragmatic",
      "default-argument-tactic": "knowing silence",
      "primary-motivation": "service",
      "self-revelation": "care is its own reward",
      "false-philosophy": "must solve everyone's problems",
      "false-goal": "earn community's gratitude",
      "fears": {
        "open": "failing those in need",
        "hidden": "becoming obsolete"
      },
      "social-problem": "unacknowledged labor",
      "specific-desire": "Example: heal the sick child",
      "greatest-weakness": "pride",
      "corresponding-strength": "competence",
      "rules-for-living": [
        "'don't meddle unnecessarily'",
        "'know when not to act'"
      ],
      "special-skills": [
        "herbalism",
        "headology",
        "midwifery"
      ]
    }
```
