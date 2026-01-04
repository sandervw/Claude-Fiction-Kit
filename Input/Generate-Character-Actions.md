# Generate Character Action Arc

Chicken scratch code for generating a complete, ordered array of significant character actions in a fiction story.

## Main Method

Parameters:
- characterDescription (string)
- fullActionsArray (json string array)
- totalCharacterActions (number)
- actionsPerSelection (number)
- genre (string)

Steps:
1. new variable = characterActions [] (json string array)
2. while i = 0 < totalCharacterActions
   1. new variable tempPickedArray = Select Without Repeats (characterActions, fullActionsArray, actionsPerSelection)
   2. new variable precedingActions (string array) = most recent 3 actions in characterActions
   3. new variable currentAction (number) = i+1
   4. new variable nextAction (string) = Pick Action LLM Method (characterDescription, precedingActions, currentAction, totalCharacterActions, tempPickedArray, genre)
   5. append nextAction to characterActions
3. return characterActions

Output: Full string array of character actions in story, of size (totalCharacterActions)

## Select Without Repeats Method

Parameters:
- characterActions [] (json string array)
- fullActionsArray (json string array)
- actionsPerSelection (number)

Steps:
1. Pick actionsPerSelection actions randomly from fullActionsArray, with no duplicates, and with no actions already used in characterActions
2. Write results to string array
3. return results

Output: string array of size actionsPerSelection

## Pick Action LLM Method

Parameters:
- characterDescription (string)
- precedingActions (string array)
- currentAction (number)
- totalCharacterActions (number)
- tempPickedArray (string array)
- genre (string)

Steps:
1. new variable prompt (string) = something like "You are writing a character collaboratively in a [genre] story. The only context you have of the character is the following: 1 - Character Description > [characterDescription]. 2 - most recent character actions in story > [precedingActions]. 3 - total actions the character must take in the story > [totalCharacterActions]. 4 - the next action number > [currentAction] \n You are given the following list of random possible next actions the character could take > [tempPickedArray]. Given your known context, your goal is to pick the single best action from that list, given the goal of writing a satisfying character arc. Remember, you are picking action number [currentAction] in the sequential list of [totalCharacterActions] character actions. Follow general [genre] pacing when making your selection. (Anti-Example: do not select 'character dies' as action 2/10 in the story...) /n return only the single chosen action, as a string, as your output
2. new variable result = Call claude API with [prompt]
3. return result

Output: a single string > the best next action, chosen from tempPickedArray, in an order set of character actions in the story