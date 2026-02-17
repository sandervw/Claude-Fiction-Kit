/**
 * Fetch all Iowa Otolaryngology providers from the NPPES NPI Registry API.
 *
 * Usage:  npm start
 * Output: iowa_otolaryngology_npi.json (in current directory)
 *
 * API docs: https://npiregistry.cms.hhs.gov/api-page
 * ZIP geocoding: https://api-ninjas.com/api/zipcode
 * No dependencies beyond Node.js built-ins.
 */

//const https = require("https");
import https from "https";
import fs from "fs";
//const { URL, URLSearchParams } = require("url");
import { URL, URLSearchParams } from "url";

const API_URL = "https://npiregistry.cms.hhs.gov/api/";
const ZIPCODE_API = "https://api.api-ninjas.com/v1/zipcode";
const NINJA_API_KEY = "Oxw4Qz0wYcn5RklZqfN058b6NE1qd0mmTQ6ppNod";
const WASHINGTON_IA_ZIP = "52353";
const LIMIT = 200;
const OUTPUT_FILE = "iowa_otolaryngology_npi.json";

const BASE_PARAMS = {
  version: "2.1",
  taxonomy_description: "Otolaryngology",
  state: "IA",

  limit: LIMIT,
};

function fetchPage(skip) {
  return new Promise((resolve, reject) => {
    const params = new URLSearchParams({ ...BASE_PARAMS, skip });
    const url = `${API_URL}?${params}`;

    https
      .get(url, (res) => {
        let body = "";
        res.on("data", (chunk) => (body += chunk));
        res.on("end", () => {
          if (res.statusCode !== 200) {
            return reject(new Error(`HTTP ${res.statusCode}: ${body}`));
          }
          try {
            resolve(JSON.parse(body));
          } catch (e) {
            reject(new Error(`Failed to parse JSON: ${e.message}`));
          }
        });
      })
      .on("error", reject);
  });
}

function fetchZipCoords(zip) {
  return new Promise((resolve, reject) => {
    const url = `${ZIPCODE_API}?zip=${zip}`;
    const options = {
      headers: { "X-Api-Key": NINJA_API_KEY },
    };

    https
      .get(url, options, (res) => {
        let body = "";
        res.on("data", (chunk) => (body += chunk));
        res.on("end", () => {
          if (res.statusCode !== 200) {
            return reject(new Error(`ZIP API HTTP ${res.statusCode}: ${body}`));
          }
          try {
            const data = JSON.parse(body);
            if (data.length === 0) return resolve(null);
            resolve({ lat: data[0].lat, lon: data[0].lon });
          } catch (e) {
            reject(new Error(`Failed to parse ZIP JSON: ${e.message}`));
          }
        });
      })
      .on("error", reject);
  });
}

function haversineDistanceMiles(lat1, lon1, lat2, lon2) {
  const toRad = (deg) => (deg * Math.PI) / 180;
  const R = 3958.8; // Earth radius in miles
  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);
  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) ** 2;
  return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function fetchAll() {
  const allResults = [];
  let skip = 0;

  while (true) {
    console.log(`Fetching records ${skip} to ${skip + LIMIT}...`);

    const data = await fetchPage(skip);
    const results = data.results || [];

    if (results.length === 0) break;

    allResults.push(...results);
    console.log(`  Got ${results.length} records (total so far: ${allResults.length})`);

    if (results.length < LIMIT) break;

    skip += LIMIT;
    await sleep(1000);
  }

  return allResults;
}

async function main() {
  console.log("Querying NPPES for Otolaryngology providers in Iowa...\n");

  const results = await fetchAll();

  const otoOnly = results.filter((r) =>
    r.taxonomies.some((t) => t.primary && t.desc.includes("Otolaryngology"))
  );

  const filtered = otoOnly.map((r) => {
    const address =
      r.addresses.find((a) => a.address_purpose === "LOCATION") ||
      r.addresses.find((a) => a.address_purpose === "MAILING") ||
      r.addresses[0];
    return {
      npi: r.number,
      basic: r.basic,
      address,
    };
  });

  // Look up Washington, IA coordinates
  console.log("\nLooking up Washington, IA coordinates...");
  const washCoords = await fetchZipCoords(WASHINGTON_IA_ZIP);
  if (!washCoords) throw new Error("Could not geocode Washington, IA ZIP");

  // Collect unique ZIP codes, then batch-lookup coords with a cache
  const uniqueZips = [...new Set(filtered.map((r) => r.address.postal_code.slice(0, 5)))];
  console.log(`Looking up coordinates for ${uniqueZips.length} unique ZIP codes...`);

  const zipCache = {};
  for (const zip of uniqueZips) {
    zipCache[zip] = await fetchZipCoords(zip);
    await sleep(100); // be polite to the API
  }

  // Attach distance to each provider
  for (const r of filtered) {
    const zip5 = r.address.postal_code.slice(0, 5);
    const coords = zipCache[zip5];
    if (coords) {
      const dist = haversineDistanceMiles(washCoords.lat, washCoords.lon, coords.lat, coords.lon);
      r["distance_washington_iowa_miles"] = Math.round(dist * 10) / 10;
    } else {
      r["distance_washington_iowa_miles"] = null;
    }
  }

  const output = {
    query: {
      taxonomy_description: "Otolaryngology",
      state: "IA",
      distance_from: "Washington, IA 52353",
    },
    total_results: filtered.length,
    results: filtered,
  };

  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(output, null, 2));
  console.log(`\nDone! Saved ${filtered.length} records to ${OUTPUT_FILE}`);
}

main().catch((err) => {
  console.error("Error:", err.message);
  process.exit(1);
});