import json

with open("iowa_otolaryngology_npi.json", "r") as f:
    data = json.load(f)

filtered = []
for record in data["results"]:
    dist = record.get("distance_washington_iowa_miles", 9999)
    if dist >= 100:
        continue

    basic = record.get("basic", {})
    addr = record.get("address", {})

    # Build full address
    parts = [addr.get("address_1", "")]
    if addr.get("address_2"):
        parts.append(addr["address_2"])
    parts.append(addr.get("city", ""))
    parts.append(addr.get("state", ""))
    postal = addr.get("postal_code", "")
    if len(postal) > 5:
        postal = postal[:5] + "-" + postal[5:]
    parts.append(postal)
    full_address = ", ".join(p for p in parts if p)

    # Contact info
    contact = []
    if addr.get("telephone_number"):
        contact.append(addr["telephone_number"])
    if addr.get("fax_number"):
        contact.append(f"fax: {addr['fax_number']}")

    # Handle individual vs organization records
    first_name = basic.get("first_name", "")
    last_name = basic.get("last_name", "")
    credential = basic.get("credential", "")

    # Organization records: use authorized official or org name
    if not first_name and not last_name:
        org_name = basic.get("organization_name", "")
        first_name = basic.get("authorized_official_first_name", "")
        last_name = basic.get("authorized_official_last_name", "")
        credential = basic.get("authorized_official_credential", "")
        if org_name:
            last_name = f"{last_name} ({org_name})"

    entry = {
        "npi": record["npi"],
        "first_name": first_name,
        "last_name": last_name,
        "credentials": credential,
        "address": full_address,
        "contact-info": contact,
        "distance_washington_iowa_miles": dist
    }
    filtered.append(entry)

# Sort by distance
filtered.sort(key=lambda x: x["distance_washington_iowa_miles"])

output = {
    "query": data["query"],
    "filter": "distance_washington_iowa_miles < 100",
    "total_filtered_results": len(filtered),
    "results": filtered
}

with open("IA-ENT-npi-filtered.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Filtered {len(filtered)} records (from {data['total_results']} total)")
