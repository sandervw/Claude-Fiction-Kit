import { readFileSync, writeFileSync } from "fs";
import { llmPrompt } from "./Javascript/llmPrompt.js";
import { markdownToBlobs } from "./Javascript/markdownToBlobs.js";

const inputStory = readFileSync("./Input/temp.md", "utf-8");
const revisionGuide = readFileSync("./Input/Revision-Guide.md", "utf-8");

const { 'blob-groups': blobGroups } = markdownToBlobs(inputStory, 1);

const revisedGroups = [];
for (const group of blobGroups) {
  const prompt = `Hey claude, here is a section of a fiction story:\n\n${JSON.stringify(group)}\n\nThis text is in a nearly finished state. I want you to suggest between 1 and 4 final revisions to this text. Focus on bringing it into a polished final state. Focus on cutting redundant sentences/words, minor re-ordering of sentences/words for better flow, or substituting more specific, better-sounding words. Do not suggest additions, unless they greatly enhance the flow of the text. Your revision's character count MUST BE less than the original. Output your result in the following format\n\n${revisionGuide}`;
  const response = await llmPrompt(prompt);
  revisedGroups.push(response);
  console.log(`Revised group ${revisedGroups.length} of ${blobGroups.length}`);

}

const result = revisedGroups.join('\n\n---\n\n');

writeFileSync(`./Output/llmresult.md`, result);