import json
import re
import sys


def strip_case_name(filename):
    """Strip 'case-' prefix and '.txt' suffix from case filenames."""
    name = filename
    if name.startswith("case-"):
        name = name[5:]
    if name.endswith(".txt"):
        name = name[:-4]
    return name


def title_case_name(name):
    """Convert 'BRUCE' to 'Bruce'."""
    return name.strip().title()


def build_markdown(data):
    lines = ["# Doctors Involved in Work Comp Cases\n"]

    sorted_results = sorted(data["results"], key=lambda d: d["distance_washington_iowa_miles"])

    for doc in sorted_results:
        full_name = f"{title_case_name(doc['first_name'])} {title_case_name(doc['last_name'])}"
        lines.append(f"## {full_name} - {doc['credentials']}\n")

        lines.append(f"**Address:** {doc['address']}\n")
        lines.append(f"**Distance from Washington, IA:** {doc['distance_washington_iowa_miles']} miles\n")
        lines.append(f"**NPI #:** {doc['npi']}\n")

        # Parse contact info
        phone = None
        fax = None
        for item in doc.get("contact-info", []):
            if item.lower().startswith("fax:"):
                fax = item[4:].strip()
            else:
                phone = item.strip()

        lines.append("**Contact Info:**")
        if phone:
            lines.append(f"- Phone: {phone}")
        if fax:
            lines.append(f"- Fax: {fax}")
        lines.append("")

    return "\n".join(lines)


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "IA-ENT-npi-no-cases.json"
    output_file = input_file.replace(".json", ".md")

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    md = build_markdown(data)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Wrote {output_file}")


if __name__ == "__main__":
    main()
