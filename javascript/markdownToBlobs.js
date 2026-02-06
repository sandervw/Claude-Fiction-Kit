/**
 * Parses a markdown document of blob sections into a grouped JSON object.
 *
 * @param {string} markdown - The raw markdown string containing ## Blob N: sections separated by ---
 * @param {number} groupSize - How many blobs per group
 * @returns {object} Grouped blob object
 */
function markdownToBlobs(markdown, groupSize) {
  const sections = markdown.split(/^---$/m);

  const blobs = [];

  for (const section of sections) {
    const headerMatch = section.match(/^##\s*Blob\s+(\d+)\s*/m);
    if (!headerMatch) continue;

    const blobNum = parseInt(headerMatch[1], 10);

    // Strip the header line, then clean up the text
    const text = section
      .replace(/^##\s*Blob\s+\d+\s*:.*$/m, '') // remove header
      .split('\n')
      .map(line => line.trim())
      .filter(line => line.length > 0)
      .join('\n');

    blobs.push({ num: blobNum, text });
  }

  const blobGroups = [];

  for (let i = 0; i < blobs.length; i += groupSize) {
    const group = {};
    const chunk = blobs.slice(i, i + groupSize);

    for (const blob of chunk) {
      group[`blob${blob.num}`] = blob.text;
    }

    blobGroups.push(group);
  }

  return { 'blob-groups': blobGroups };
}

export { markdownToBlobs };
