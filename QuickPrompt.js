import Anthropic from "@anthropic-ai/sdk";
import { readFileSync, writeFileSync } from "fs";

const client = new Anthropic();

const guidelines = readFileSync("./Output/DescriptionGuidelines.md", "utf-8");
const character = readFileSync("./Output/temp.md", "utf-8");
// Use 'claude-sonnet-4-5-20250929' for speed/cost balance
// Use 'claude-opus-4-5-20251101' for highest quality
const MODEL = 'claude-opus-4-5-20251101';

//console.log(markdownContent);


const response = await client.messages.create({
  model: MODEL,
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: `Hey claude, write a full description of a dark fantasy character, based on the rough, generic physical traits I've included here:\n\n${character}\n\n Use these guidelines to shape your description. Keep your description under 120 words.\n\n${guidelines}\n.`,
    },
  ],
});

writeFileSync("./Output/Description.txt", response.content[0].text.trim());
console.log(response.content[0].text.trim());