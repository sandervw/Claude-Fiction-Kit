import Anthropic from '@anthropic-ai/sdk';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Model configuration
// Use 'claude-sonnet-4-5-20250929' for speed/cost balance
// Use 'claude-opus-4-5-20251101' for highest quality
const MODEL = 'claude-sonnet-4-5-20250929';

/**
 * Select random actions from fullActionsArray without repeats
 * @param {string[]} characterActions - Actions already chosen
 * @param {string[]} fullActionsArray - All available actions
 * @param {number} actionsPerSelection - Number of actions to pick
 * @returns {string[]} - Array of randomly selected actions
 */
function selectWithoutRepeats(characterActions, fullActionsArray, actionsPerSelection) {
  // Filter out actions already used
  const availableActions = fullActionsArray.filter(
    action => !characterActions.includes(action)
  );

  // Shuffle and pick
  const shuffled = [...availableActions].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, actionsPerSelection);
}

/**
 * Call Claude API to pick the best next action
 * @param {Anthropic} client - Anthropic client
 * @param {string} characterDescription - Description of the character
 * @param {string[]} precedingActions - Most recent actions taken
 * @param {number} currentAction - Current action number (1-indexed)
 * @param {number} totalCharacterActions - Total actions in the arc
 * @param {string[]} tempPickedArray - Candidate actions to choose from
 * @param {string} genre - Story genre
 * @returns {Promise<string>} - The chosen action
 */
async function pickActionLLM(
  client,
  characterDescription,
  precedingActions,
  currentAction,
  totalCharacterActions,
  tempPickedArray,
  genre
) {
  const precedingActionsText = precedingActions.length > 0
    ? precedingActions.map((a, i) => `${i + 1}. ${a}`).join('\n')
    : '(No actions yet - this is the first action)';

  const candidateActionsText = tempPickedArray
    .map((a, i) => `${i + 1}. ${a}`)
    .join('\n');

  const prompt = `You are writing a character collaboratively in a ${genre} story.

The only context you have of the character is the following:

1. CHARACTER DESCRIPTION:
${characterDescription}

2. MOST RECENT CHARACTER ACTIONS IN STORY:
${precedingActionsText}

3. TOTAL ACTIONS the character must take in the story: ${totalCharacterActions}

4. THE NEXT ACTION NUMBER: ${currentAction}

You are given the following list of random possible next actions the character could take:
${candidateActionsText}

Given your known context, your task is to pick the single best action from that list, given the goal of writing a satisfying character arc.

Remember, you are picking action number ${currentAction} in the sequential list of ${totalCharacterActions} character actions. Follow general ${genre} pacing when making your selection.

IMPORTANT: Consider narrative pacing. For example:
- Do not select 'character dies' as action 2/10 in the story
- Early actions should establish character and situation
- Middle actions should develop conflict and growth
- Later actions should build toward climax and resolution

Return ONLY the single chosen action as your output, exactly as it appears in the list above. No explanation, no quotes, just the action text.`;

  // If only one candidate, just return it directly (no need to call LLM)
  if (tempPickedArray.length === 1) {
    return tempPickedArray[0];
  }

  const message = await client.messages.create({
    model: MODEL,
    max_tokens: 256,
    messages: [{ role: 'user', content: prompt }]
  });

  // Extract text from response
  const responseText = message.content[0].text.trim();

  // Validate response is one of the candidates (handle LLM refusal/explanation)
  const matchedAction = tempPickedArray.find(
    action => responseText.includes(action) || action.includes(responseText)
  );

  if (matchedAction) {
    return matchedAction;
  }

  // Fallback: if LLM gave explanation instead of action, pick first candidate
  console.log('  (LLM gave explanation, falling back to first candidate)');
  return tempPickedArray[0];
}

/**
 * Main function to generate character action arc
 */
async function generateCharacterActions() {
  // Load config
  const configPath = path.join(__dirname, 'generate-actions-config.json');
  if (!fs.existsSync(configPath)) {
    console.error('Error: generate-actions-config.json not found in project root');
    process.exit(1);
  }

  const config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
  const {
    characterDescription,
    fullActionsArray: actionsFilePath,
    totalCharacterActions,
    actionsPerSelection,
    genre
  } = config;

  // Load actions array
  const fullActionsPath = path.resolve(__dirname, actionsFilePath);
  if (!fs.existsSync(fullActionsPath)) {
    console.error(`Error: Actions file not found at ${fullActionsPath}`);
    process.exit(1);
  }

  const actionsFile = JSON.parse(fs.readFileSync(fullActionsPath, 'utf-8'));
  // Support both { tags: [...] } format and plain array
  const fullActionsArray = actionsFile.tags || actionsFile;

  if (!Array.isArray(fullActionsArray)) {
    console.error('Error: Actions file must contain an array or { tags: [...] }');
    process.exit(1);
  }

  console.log(`Generating ${totalCharacterActions} character actions...`);
  console.log(`Character: ${characterDescription}`);
  console.log(`Genre: ${genre}`);
  console.log(`Actions pool: ${fullActionsArray.length} available actions`);
  console.log(`Candidates per selection: ${actionsPerSelection}`);
  console.log('---');

  // Initialize Anthropic client
  const client = new Anthropic();

  // Build character actions array
  const characterActions = [];

  for (let i = 0; i < totalCharacterActions; i++) {
    const currentAction = i + 1;
    console.log(`\nSelecting action ${currentAction}/${totalCharacterActions}...`);

    // Get random candidate actions
    const tempPickedArray = selectWithoutRepeats(
      characterActions,
      fullActionsArray,
      actionsPerSelection
    );

    if (tempPickedArray.length === 0) {
      console.error('Error: No more available actions to choose from');
      break;
    }

    console.log('Candidates:', tempPickedArray);

    // Get most recent 4 actions
    const precedingActions = characterActions.slice(-4);

    // Call LLM to pick best action
    const nextAction = await pickActionLLM(
      client,
      characterDescription,
      precedingActions,
      currentAction,
      totalCharacterActions,
      tempPickedArray,
      genre
    );

    console.log(`Selected: ${nextAction}`);
    characterActions.push(nextAction);
  }

  // Save output
  const outputPath = path.join(__dirname, 'Output', 'character-actions.json');
  const output = {
    characterDescription,
    genre,
    totalActions: totalCharacterActions,
    generatedAt: new Date().toISOString(),
    actions: characterActions
  };

  fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));
  console.log(`\n---\nSaved ${characterActions.length} actions to ${outputPath}`);

  return characterActions;
}

// Run
generateCharacterActions().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});
