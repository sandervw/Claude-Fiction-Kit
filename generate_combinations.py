import json
import random
import argparse
import sys
from pathlib import Path


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate random combinations from JSON arrays')
    parser.add_argument('input_file', help='Input JSON file in JSONInput folder (e.g., settings.json)')
    parser.add_argument('listSize', type=int, help='Number of elements in each combination')
    parser.add_argument('listNumber', type=int, help='Number of combinations to generate')

    args = parser.parse_args()

    # Construct input file path
    input_path = Path('JSONInput') / args.input_file

    # Check if input file exists
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found", file=sys.stderr)
        sys.exit(1)

    # Read input JSON
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON from '{input_path}': {e}", file=sys.stderr)
        sys.exit(1)

    # Get the first (and should be only) array from the JSON
    if not isinstance(data, dict) or len(data) != 1:
        print(f"Error: Expected JSON file to contain exactly one top-level key with an array", file=sys.stderr)
        sys.exit(1)

    array_name = list(data.keys())[0]
    array_data = data[array_name]

    if not isinstance(array_data, list):
        print(f"Error: Expected '{array_name}' to be an array", file=sys.stderr)
        sys.exit(1)

    # Check if listSize is valid
    if args.listSize > len(array_data):
        print(f"Error: listSize ({args.listSize}) is larger than the number of available elements ({len(array_data)})", file=sys.stderr)
        sys.exit(1)

    if args.listSize < 1:
        print(f"Error: listSize must be at least 1", file=sys.stderr)
        sys.exit(1)

    if args.listNumber < 1:
        print(f"Error: listNumber must be at least 1", file=sys.stderr)
        sys.exit(1)

    # Generate combinations
    combinations = {}
    for i in range(1, args.listNumber + 1):
        # Sample without replacement
        combo = random.sample(array_data, args.listSize)
        key = f"{i:02d}-{array_name}"
        combinations[key] = combo

    # Create output structure
    output_key = f"{array_name}-lists"
    output_data = {output_key: combinations}

    # Ensure JSONOutput directory exists
    output_dir = Path('JSONOutput')
    output_dir.mkdir(exist_ok=True)

    # Create output filename based on input filename
    input_filename = Path(args.input_file).stem
    output_path = output_dir / f"{input_filename}-combinations.json"

    # Write output JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated {args.listNumber} combinations of {args.listSize} elements")
    print(f"Output written to: {output_path}")


if __name__ == '__main__':
    main()
