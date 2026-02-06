import { readFileSync, writeFileSync } from "fs";
import { llmPrompt } from "./javascript/llmPrompt.js";
import { markdownToBlobs } from "./javascript/markdownToBlobs.js";

const inputStory = readFileSync("./Input/temp.md", "utf-8");
const revisionGuide = readFileSync("./Input/Revision-Guide.md", "utf-8");

const { 'blob-groups': blobGroups } = markdownToBlobs(inputStory, 1);

const revisedGroups = [];
for (const group of blobGroups) {
  const prompt = `Hey claude, here is a section of a fiction story:\n\n${JSON.stringify(group)}\n\nPlease revise this section according to the following revision guide:\n\n${revisionGuide}\n\nOutput the revised section only, as markdown text, with each blob distinguished by a header like '## Blob X', and blobs separated by '---'.`;
  const response = await llmPrompt(prompt);
  revisedGroups.push(response);
  console.log(`Revised group ${revisedGroups.length} of ${blobGroups.length}`);

}

const result = revisedGroups.join('\n\n---\n\n');

writeFileSync(`./Output/llmresult.md`, result);