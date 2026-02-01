import Anthropic from "@anthropic-ai/sdk";
import { readFileSync, writeFileSync } from "fs";
import { selectTemplates } from "./templateSelector.js";

const client = new Anthropic();

const contextNotes = readFileSync("./Input/Context-Notes.md", "utf-8");
const paragraphNumber = 29;
// => array of 3 random action paragraph template objects
const templates = JSON.stringify(selectTemplates("exposition-paragraphs", 3));

// \nThis time you have an additional challenge: I want you to write this 'paragraph' in the form of an 'exchange'. this should be a dialogue between two or more individuals, as described in the context notes. You'll need to adapt the template you choose to dialogue, so take that into consideration when picking a template.\n

// Use 'claude-sonnet-4-5-20250929' for speed/cost balance
// Use 'claude-opus-4-5-20251101' for highest quality
const MODEL = 'claude-opus-4-5-20251101';
const response = await client.messages.create({
  model: MODEL,
  max_tokens: 20000,
  messages: [
    {
      role: "user",
      content: `Hey claude, take a look at ${contextNotes}. This is the only context you have for a fiction story. I want you to write just paragraph ${paragraphNumber} into a full piece of third person, past-tense prose. You must pick one of the paragraph templates from ${templates} , and write your paragraph to the form of that template. Pick the most fitting template. *You must remain within the template's word count.*\nOutput your paragraph as markdown, along the template you used (provide the 'respecification seed'), your word-count, and a brief explanation of how you applied at the top.\n**Focus particularly on writing with less-used or uncommon nouns, verbs, and adjectives.**`,
    },
  ],
});

writeFileSync(`./Output/paragraph-${paragraphNumber}.md`, response.content[0].text.trim());