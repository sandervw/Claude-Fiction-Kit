import { readFileSync } from "fs";

const allTemplates = JSON.parse(readFileSync("./Elements/paragraph-templates.json", "utf-8"));

/**
 * Selects random templates (without replacement) from a given category.
 * @param {string} type - Exact top-level key, e.g. "action-paragraphs"
 * @param {number} number - Max number of templates to select
 * @returns {Array} Array of template objects
 */
export function selectTemplates(type, number) {
  const pool = allTemplates[type];
  if (!pool) {
    throw new Error(`Unknown template type: "${type}". Valid types: ${Object.keys(allTemplates).join(", ")}`);
  }

  const count = Math.min(number, pool.length);
  const indices = Array.from({ length: pool.length }, (_, i) => i);

  // Fisher-Yates shuffle, then take the first `count`
  for (let i = indices.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [indices[i], indices[j]] = [indices[j], indices[i]];
  }

  return indices.slice(0, count).map(i => pool[i]);
}
