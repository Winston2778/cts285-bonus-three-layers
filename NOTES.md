# NOTES: Three Layers

Your name: Latoya Winston

Fill each TODO. Write plain, short sentences. Do not delete the headings.

## Part 1. Predict, then find [S1]

Write your prediction before you open any code. Then search. In the last column, write each file the search finds and what that file does.

| Action | Search word | My prediction (file) | Files found and what each does |
|---|---|---|---|
| Prints "Not yet. Try again." | `Not yet` | app.py| it prints out what the user sees|
| Decides that the second miss shows the answer | `reveal` | dataman/logic.py | dataman/logic.py: decides to reveal; app.py: prints the answer; tests/test_logic.py: checks the rule works |
| Saves one attempt | `save_attempt` | dataman/store.py | dataman/store.py: does the saving; dataman/logic.py: asks the store to save |
|Refuses the 11th problem | `SetFull` | dataman/logic.py | dataman/logic.py: raises SetFull to refuse; app.py: catches it and shows a message; tests/test_logic.py: checks the rule works; exercise/bank.py and exercise/test_bank.py: practice exercise for later |

Search command: `grep -rn "SEARCH WORD" --include=*.py .`

## Part 2. What the program remembered [S1]

After the restart, what did the program remember? It remebered my first attempt (55,wrong) so it output said  try 2

Which file made that possible? dataman/store.py

## Part 3. The interface change [S1]

Why did no test need to change? to test check the rules in logic.py, not the words app.py prints. I only needed to changed the words, so the rules and results stayed the same.

## Part 4. The rule in the real library [S2]

The same 10-problem rule exists in the real library. Write the file and the function name. 

## Part 5. The red test [S2]

With the rule removed from the library, what did the screen show? 

With the rule removed, which test failed? 

## Part 6. The data swap [S2]

A real database would replace which file? 

Which file holds the rules and does not change when the database changes? 

## Reflection [S2]

Write 3 to 5 sentences. Pick one layer. Say what you changed in it. Say what stayed the same in the other two layers. 

## Beta feedback (optional)

This bonus is a beta test. Which step took longer than its time? What confused you? Write it here. Your answer helps the next class.
