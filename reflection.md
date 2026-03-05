# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
   (for example: "the secret number kept changing" or "the hints were backwards").

- 1.When we narrowed down the possible range into one integer, it should be the right answer but the message said it was not.
- 2.When we type a float number 6.5. But the records shows 6. The system will revise user's input.
- 3.Records inconsistency:
  - attempt left number is inconsistent with history record and system message.
  - Score in the table is inconsistent with system message.
- 4.When user clicks new game button. The history board did not clear its content. System message still told user that "Game over. Start a new game to try again." But it should start a new game.
- 5.The system message gives user a wrong

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Additionally, AI provided valuable suggestions for improving modularity by refactoring core logic into a separate `logic_utils.py` file. This made the code more testable and maintainable. I verified the correctness of this refactoring by running `pytest` on the extracted functions and ensuring all tests passed.

However, AI also gave a misleading suggestion for the `update_score` formula, which initially caused a test failure. After identifying the issue through `pytest`, I corrected the formula and re-ran the tests to confirm the fix.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

In addition to the original debugging process, I used `pytest` extensively to validate all fixed bugs. For example, I wrote test cases to ensure that the `parse_guess` function handled invalid inputs correctly and that the `check_guess` function returned accurate outcomes. These automated tests provided confidence that the fixes were robust.

I also manually tested the application by running it with `streamlit` to verify the user interface. This included checking that the "New Game" button cleared the history board and that hint messages were displayed accurately. Both automated and manual testing ensured the application worked as intended.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
