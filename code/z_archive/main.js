import { readFileSync, writeFileSync } from "fs";
import { llmPrompt } from "./modules/llmPrompt.js";

const inputFile = readFileSync("../input/input.md", "utf-8");

const prompt = `Write prompt here with input file = ${inputFile}`;
const response = await llmPrompt(prompt);
console.log(response);

writeFileSync(`../output/llmresult.md`, response);