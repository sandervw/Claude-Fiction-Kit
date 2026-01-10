import Anthropic from '@anthropic-ai/sdk';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Model configuration
// Use 'claude-sonnet-4-5-20250929' for speed/cost balance
// Use 'claude-opus-4-5-20251101' for highest quality
const MODEL = 'claude-opus-4-5-20251101';

/**
 * Select random items from json array without repeats
 */
function selectWithoutRepeats(chosenItems, fullItemsArray, itemsPerSelection) {
  // Filter out items already used
  const availableItems = fullItemsArray.filter(
    item => !chosenItems.includes(item)
  );

  // Shuffle and pick
  const shuffled = [...availableItems].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, itemsPerSelection);
}

/**
 * Build the prompt for action selection
 * @param {object} context - json object with character context (description and genre minimum)
 * @param {string} itemType - The type of item being selected (quotes, actions, etc)
 * @param {object[]} precedingItems - List of items already chosen
 * @param {number} currentItem - Current item number (1-indexed)
 * @param {number} totalItems - Total items final output should have
 * @param {object[]} candidateItems - Candidate items to choose from
 * @param {string} objectiveText - Text describing the objective of the selection
 * @returns {string} - The formatted prompt
 */
function createPrompt(
  context,
  itemType,
  precedingItems,
  currentItem,
  totalItems,
  candidateItems,
  objectiveText
) {
  const precedingItemsText = precedingItems.length > 0
    ? precedingItems.map((a, i) => `${i + 1}. ${a}`).join('\n')
    : `(No ${itemType} yet - this is the first ${itemType})`;
  const candidateItemsText = candidateItems
    .map((a, i) => `${i + 1}. ${a}`)
    .join('\n');

  return `You are writing a character collaboratively in a story.

The only context you have of the character is the following:

1. BASE CONTEXT:
${context}

2. MOST RECENT ${itemType.toUpperCase()}s IN STORY:
${precedingItemsText}

3. TOTAL ${itemType.toUpperCase()}s the character must have in the story: ${totalItems}

4. THE NEXT ${itemType.toUpperCase()} NUMBER: ${currentItem}

You are given the following list of random possible next ${itemType}s:
${candidateItemsText}

Given your known context, ${objectiveText}`;
}

/**
 * Call Claude API to pick the best item from candidates
 * @param {Anthropic} client - Anthropic client
 * @param {string} prompt - The prompt to send to the LLM
 * @param {string[]} candidates - Array of candidate items to choose from (for validation)
 * @returns {Promise<string>} - The chosen item
 */
async function pickItemLLM(
  client,
  prompt,
  candidates
) {
  // If only one candidate, just return it directly (no need to call LLM)
  if (candidates.length === 1) {
    return candidates[0];
  }

  const message = await client.messages.create({
    model: MODEL,
    max_tokens: 256,
    messages: [{ role: 'user', content: prompt }]
  });

  // Extract text from response
  const responseText = message.content[0].text.trim();

  // Validate response is one of the candidates (handle LLM refusal/explanation)
  const matchedItem = candidates.find(
    item => responseText.includes(item) || item.includes(responseText)
  );

  if (matchedItem) {
    return matchedItem;
  }

  // Fallback: if LLM gave explanation instead of item, pick first candidate
  console.log('  (LLM gave explanation, falling back to first candidate)');
  return candidates[0];
}

/**
 * Main function to add a list of 'items' (actions, quotes, etc) to a character
 */
async function addCharacterList() {
  // Load config
  const configPath = path.join(__dirname, 'generate-character-config.json');
  if (!fs.existsSync(configPath)) {
    console.error('Error: generate-character-config.json not found in project root');
    process.exit(1);
  }

  const config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
  const {
    context,
    fullItemArray,
    itemType,
    objectiveText,
    totalItems,
    itemsPerSelection
  } = config;

  // Load actions array
  const fullItemPath = path.resolve(__dirname, fullItemArray);
  if (!fs.existsSync(fullItemPath)) {
    console.error(`Error: item list file not found at ${fullItemPath}`);
    process.exit(1);
  }

  const itemsFile = JSON.parse(fs.readFileSync(fullItemPath, 'utf-8'));
  // Support both generic { "[items]": [...] } format and plain array
  const fullItemsArray = itemsFile[itemType] || itemsFile[Object.keys(itemsFile)[0]] || itemsFile;

  if (!Array.isArray(fullItemsArray)) {
    console.error('Error: Items file must contain an array or { "[items]": [...] }');
    process.exit(1);
  }

  console.log(`Generating ${totalItems} character ${itemType}...`);
  console.log(`Character: ${context}`);
  console.log(`Pool: ${fullItemsArray.length} available`);
  console.log(`Candidates per selection: ${itemsPerSelection}`);
  console.log('---');

  // Initialize Anthropic client
  const client = new Anthropic();

  // Build character items array
  const characterItems = [];

  for (let i = 0; i < totalItems; i++) {
    const currentItem = i + 1;
    console.log(`\nSelecting ${itemType} ${currentItem}/${totalItems}...`);
    // Get random candidate items
    const tempPickedArray = selectWithoutRepeats(
      characterItems,
      fullItemsArray,
      itemsPerSelection
    );

    if (tempPickedArray.length === 0) {
      console.error(`Error: No more available ${itemType} to choose from`);
      break;
    }

    console.log('Candidates:', tempPickedArray);

    // Get most recent 3 items
    const precedingItems = characterItems.slice(-3);

    const prompt = createPrompt(
      context,
      itemType,
      precedingItems,
      currentItem,
      totalItems,
      tempPickedArray,
      objectiveText
    );

    // Call LLM to pick best item
    const nextItem = await pickItemLLM(
      client,
      prompt,
      tempPickedArray
    );

    console.log(`Selected: ${nextItem}`);
    characterItems.push(nextItem);
  }

  // Save output
  const outputPath = path.join(__dirname, 'Output', 'character.json');
  const output = {
    context,
    itemType,
    totalItems,
    generatedAt: new Date().toISOString(),
    items: characterItems
  };

  fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));
  console.log(`\n---\nSaved ${characterItems.length} ${itemType} to ${outputPath}`);

  return characterItems;
}

// Run
addCharacterList().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});
