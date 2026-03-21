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