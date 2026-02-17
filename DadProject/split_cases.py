import json

with open("IA-ENT-npi-filtered.json", "r") as f:
    data = json.load(f)

no_cases = []
has_cases = []

for result in data["results"]:
    if result["cases-involved"]:
        has_cases.append(result)
    else:
        no_cases.append(result)

base = {k: v for k, v in data.items() if k != "results"}

no_cases_out = {**base, "total_filtered_results": len(no_cases), "results": no_cases}
has_cases_out = {**base, "total_filtered_results": len(has_cases), "results": has_cases}

with open("IA-ENT-npi-no-cases.json", "w") as f:
    json.dump(no_cases_out, f, indent=2)

with open("IA-ENT-npi-cases.json", "w") as f:
    json.dump(has_cases_out, f, indent=2)

print(f"Done: {len(no_cases)} with no cases, {len(has_cases)} with cases")
