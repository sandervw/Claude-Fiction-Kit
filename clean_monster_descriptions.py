#!/usr/bin/env python3
"""
Dungeon Siege Monster Description Cleaner
==========================================
Two-pass cleaning:
1. Regex strip: Remove table artifacts (stats, affiliations, damage/armor/exp data)
2. LLM condense: Use Claude API to distill into 1-2 sentence descriptions

Usage:
    python clean_monster_descriptions.py input.json output.json

Requirements:
    pip install anthropic --break-system-packages
    
Environment:
    ANTHROPIC_API_KEY=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
"""

import json
import re
import os
import sys
import time
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed.")
    print("Run: pip install anthropic --break-system-packages")
    sys.exit(1)


def regex_clean(description: str) -> str:
    """
    Pass 1: Strip table artifact garbage from descriptions.
    Removes stats blocks, affiliation headers, damage/armor/exp patterns.
    """
    # Remove stat blocks: "Damage h2h 14-16 lvl 5 Armor 57 Experience 40"
    # Handles variations: "Damage (as weapon)", "Damage (as spell)", etc.
    description = re.sub(
        r'(Regular|Veteran|Elite)\s+Damage\s+(\(as \w+\)\s*\+?\s*)?[\d\-,\s]*'
        r'(h2h\s+)?[\d\-,]*\s*lvl\s+\d+\s*Armor\s+[\d,]+\s*Experience\s+[\d,]+',
        '', description, flags=re.IGNORECASE
    )
    
    # Remove "Affiliations <stuff>" lines (up to next sentence or end)
    description = re.sub(
        r'Affiliations\s+[\w\s\'-]+?(?=\s+(?:Regular|Veteran|Elite|The|This|An?|They|It|[A-Z][a-z]+\s+is))',
        '', description, flags=re.IGNORECASE
    )
    
    # Catch remaining affiliation fragments
    description = re.sub(r'Affiliations\s+[\w\s\'-]+', '', description)
    
    # Remove "Race <word>" patterns
    description = re.sub(r'\bRace\s+\w+\s*', '', description)
    
    # Remove "Type Region" patterns (location entries that snuck in)
    description = re.sub(r'\bType\s+Region\s*', '', description)
    
    # Remove map upload requests
    description = re.sub(
        r'Map\s+Have a world map of this location\?\s+Then please upload it!\s*',
        '', description
    )
    
    # Remove standalone stat fragments that might remain
    description = re.sub(r'\blvl\s+\d+\b', '', description)
    description = re.sub(r'\bArmor\s+[\d,]+\b', '', description)
    description = re.sub(r'\bExperience\s+[\d,]+\b', '', description)
    
    # Clean up multiple spaces and leading/trailing whitespace
    description = re.sub(r'\s+', ' ', description).strip()
    
    return description


def condense_with_llm(client: anthropic.Anthropic, monsters: list[dict], batch_size: int = 10) -> list[dict]:
    """
    Pass 2: Use Claude to condense descriptions into 1-2 sentences.
    Processes in batches to reduce API calls.
    """
    results = []
    total = len(monsters)
    
    for i in range(0, total, batch_size):
        batch = monsters[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (total + batch_size - 1) // batch_size
        
        print(f"Processing batch {batch_num}/{total_batches} ({len(batch)} monsters)...")
        
        # Build the batch prompt
        monster_list = "\n".join([
            f'{idx + 1}. **{m["name"]}**: {m["description"]}'
            for idx, m in enumerate(batch)
        ])
        
        prompt = f"""Rewrite each monster description as a brief 1-2 sentence snippet.
Focus on: what the creature looks like + how it fights/behaves.
Remove: lore, locations, quest references, game mechanics (levels, spells names, damage numbers).
Keep the tone neutral and encyclopedic.

Respond with a JSON array of objects with "name" and "description" keys. No markdown, just raw JSON.

Monsters:
{monster_list}"""

        try:
            response = client.messages.create(
                model="claude-haiku-4-5",  # Fast and cheap
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Parse the response
            response_text = response.content[0].text.strip()
            
            # Handle potential markdown code blocks
            if response_text.startswith("```"):
                response_text = re.sub(r'^```(?:json)?\n?', '', response_text)
                response_text = re.sub(r'\n?```$', '', response_text)
            
            batch_results = json.loads(response_text)
            
            # Merge with original URLs
            for j, result in enumerate(batch_results):
                result["url"] = batch[j]["url"]
            
            results.extend(batch_results)
            
        except json.JSONDecodeError as e:
            print(f"  Warning: JSON parse error in batch {batch_num}: {e}")
            print(f"  Raw response: {response_text[:200]}...")
            # Fall back to regex-only versions for this batch
            for m in batch:
                results.append({
                    "name": m["name"],
                    "description": m["description"],  # Already regex-cleaned
                    "url": m["url"]
                })
        except anthropic.APIError as e:
            print(f"  API error in batch {batch_num}: {e}")
            # Fall back to regex-only versions
            for m in batch:
                results.append({
                    "name": m["name"],
                    "description": m["description"],
                    "url": m["url"]
                })
        
        # Rate limiting: small delay between batches
        if i + batch_size < total:
            time.sleep(0.5)
    
    return results


def main():
    if len(sys.argv) != 3:
        print("Usage: python clean_monster_descriptions.py <input.json> <output.json>")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    
    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Set it with: export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)
    
    # Load monsters
    print(f"Loading monsters from {input_path}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        monsters = json.load(f)
    
    print(f"Loaded {len(monsters)} monsters.")
    
    # Pass 1: Regex cleanup
    print("\nPass 1: Regex cleanup...")
    for monster in monsters:
        monster["description"] = regex_clean(monster["description"])
    
    # Pass 2: LLM condensing
    print("\nPass 2: LLM condensing...")
    client = anthropic.Anthropic(api_key=api_key)
    cleaned_monsters = condense_with_llm(client, monsters)
    
    # Save results
    print(f"\nSaving cleaned monsters to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_monsters, f, indent=2, ensure_ascii=False)
    
    print(f"Done! Processed {len(cleaned_monsters)} monsters.")


if __name__ == "__main__":
    main()
