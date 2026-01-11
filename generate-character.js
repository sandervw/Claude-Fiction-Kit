import Anthropic from '@anthropic-ai/sdk';
import fs from 'fs';
import path from 'path';
import { json } from 'stream/consumers';
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
  // Filter out items already used (stringify for object comparison)
  const chosenStrings = chosenItems.map(item => JSON.stringify(item));
  const availableItems = fullItemsArray.filter(
    item => !chosenStrings.includes(JSON.stringify(item))
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
  // Helper to display items (stringify objects, leave strings as-is)
  const displayItem = (item) => typeof item === 'object' ? JSON.stringify(item, null, 2) : item;

  const precedingItemsText = precedingItems.length > 0
    ? precedingItems.map((a, i) => `${i + 1}. ${displayItem(a)}`).join('\n')
    : `(No ${itemType} yet - this is the first ${itemType})`;
  const candidateItemsText = candidateItems
    .map((a, i) => `${i + 1}. ${displayItem(a)}`)
    .join('\n');

  return `You are writing a character collaboratively in a story. The only context you have of the character is the following:

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
  prompt
) {

  const message = await client.messages.create({
    model: MODEL,
    max_tokens: 256,
    messages: [{ role: 'user', content: prompt }]
  });

  // Extract text from response
  const responseText = message.content[0].text.trim();
  return responseText;
}

/**
 * Main function to add a list of 'items' (actions, quotes, etc) to a character
 */
async function addCharacterList(configFilePath) {
  // Load config
  const configPath = path.join(__dirname, configFilePath);
  if (!fs.existsSync(configPath)) {
    console.error(`Error: config file not found at ${configPath}`);
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
  const fullItemsArray = itemsFile[itemType] || itemsFile[Object.keys(itemsFile)[0]] || itemsFile;
  if (!Array.isArray(fullItemsArray)) {
    console.error('Error: Items file must contain an array or { "[items]": [...] }');
    process.exit(1);
  }

  // Load character context if file path provided
  const contextPath = path.resolve(__dirname, context);
  if (!fs.existsSync(contextPath)) {
    console.error(`Error: context file not found at ${contextPath}`);
    process.exit(1);
  }
  const contextFile = JSON.parse(fs.readFileSync(contextPath, 'utf-8'));
  const characterContext = JSON.stringify(contextFile);

  console.log(`Generating ${totalItems} character ${itemType}...`);
  console.log(`Character: ${characterContext}`);
  console.log(`Pool: ${fullItemsArray.length} available`);
  console.log(`Candidates per selection: ${itemsPerSelection}`);
  console.log('---');

  // Initialize Anthropic client
  const client = new Anthropic();

  // Build character items array
  const characterItems = [];
  let firstPromptResponse = null;
  let lastPromptResponse = null;

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

    // console.log('Candidates:', tempPickedArray);

    // Get most recent 3 items
    const precedingItems = characterItems.slice(-3);

    const prompt = createPrompt(
      characterContext,
      itemType,
      precedingItems,
      currentItem,
      totalItems,
      tempPickedArray,
      objectiveText
    );

    // console.log(prompt);

    // Call LLM to pick best item
    const nextItem = await pickItemLLM(
      client,
      prompt
    );

    // console.log(`response: ${nextItem}`);
    characterItems.push(nextItem);

    // Track first and last prompt+response for logging
    const promptResponse = { prompt, response: nextItem };
    if (i === 0) {
      firstPromptResponse = promptResponse;
    }
    lastPromptResponse = promptResponse;
  }

  // Save output
  const outputPath = path.join(__dirname, 'Output', 'character.json');
  const output = {
    character: JSON.parse(characterContext),
    itemType,
    totalItems,
    generatedAt: new Date().toISOString(),
    [`${itemType}s`]: characterItems
  };

  fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));
  console.log(`\n---\nSaved ${characterItems.length} ${itemType} to ${outputPath}`);

  // Write first and last prompt+response to log file
  if (firstPromptResponse && lastPromptResponse) {
    const logPath = path.join(__dirname, 'Output', 'character-generation.log');
    const logContent = `=== Character Generation Log ===
Generated: ${new Date().toISOString()}
Item Type: ${itemType}
Total Items: ${totalItems}

================================================================================
FIRST PROMPT:
================================================================================
${firstPromptResponse.prompt}

================================================================================
FIRST RESPONSE:
================================================================================
${firstPromptResponse.response}

================================================================================
LAST PROMPT:
================================================================================
${lastPromptResponse.prompt}

================================================================================
LAST RESPONSE:
================================================================================
${lastPromptResponse.response}
`;
    fs.writeFileSync(logPath, logContent);
    console.log(`Saved prompt/response log to ${logPath}`);
  }

  return characterItems;
}

// Run
addCharacterList('generate-quotes-config.json').catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});
