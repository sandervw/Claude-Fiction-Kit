# Prompt

Hey claude, I want to create a new python module/script which extends the @code/python/modules/llm_prompt.py. Basically, the extended script would ave the following form:

Input:
- a json array where each object has a 'name' and 'text' field, both strings

logic:
- for each string in the array, call llm prompt (not in sequence; individually)
- Capture the array of returned text in a new json object

Output:
- a new json object, same form as the original, but now the 'text' fields are replaced by the output of llm_prompt

Does this make sense? any questions?

---

Great. Now lets create another helper script with a different function. Read @input/input.md This is the general form of a markdown file which the script will recieve, and the script would do the following logic:

Input:
- The relative path of the markdown file, always in @input/ - you may be able to use @code/python/modules/utls/file_pipeline.py for relative path resolution

logic:
- Split out the markdown file based on the 2nd header-level elements

Output:
- a json array of objects, of the 'name'/'text' form, where each name is the header, and each text is the text below it (newlines included)

No need to call llm_prompt/batch (yet). Any questions?

---

