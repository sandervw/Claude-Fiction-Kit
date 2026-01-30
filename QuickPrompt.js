import Anthropic from "@anthropic-ai/sdk";
import { readFileSync, writeFileSync } from "fs";

const client = new Anthropic();

const contextNotes = readFileSync("./Input/Context-Notes.md", "utf-8");
const templates = readFileSync("./Input/Templates.json", "utf-8");
const paragraphNumber = 19;


// Use 'claude-sonnet-4-5-20250929' for speed/cost balance
// Use 'claude-opus-4-5-20251101' for highest quality
const MODEL = 'claude-opus-4-5-20251101';
const response = await client.messages.create({
  model: MODEL,
  max_tokens: 20000,
  messages: [
    {
      role: "user",
      content: `Hey claude, take a look at ${contextNotes}. This is the only context you have for a fiction story. I want you to write just paragraph ${paragraphNumber} into a full piece of third person, past-tense prose. You must pick one of the paragraph templates from ${templates} , and write your paragraph to the form of that template. Pick the most fitting template. Output your paragraph as markdown, along the number of the template you used and a brief explanation of how you applied at the top.\nFocus particularly on writing with less-used or uncommon nouns, verbs, and adjectives.`,
    },
  ],
});

writeFileSync(`./Output/paragraph-${paragraphNumber}.md`, response.content[0].text.trim());