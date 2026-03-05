# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- 1.When we narrowed down the possible range into one integer, it should be the right answer but the message said it was not.
- 2.When we type a float number 6.5. But the records shows 6. The system will revise user's input.
- 3.Records inconsistency:
  - attempt left number is inconsistent with history record and system message.
  - Score in the table is inconsistent with system message.
- 4.When user clicks new game button. The history board did not clear its content. System message still told user that "Game over. Start a new game to try again." But it should start a new game.
- 5.The system message gives user a wrong

---

## 2. How did you use AI as a teammate?

Additionally, AI provided valuable suggestions for improving modularity by refactoring core logic into a separate `logic_utils.py` file. This made the code more testable and maintainable. I verified the correctness of this refactoring by running `pytest` on the extracted functions and ensuring all tests passed.

However, AI also gave a misleading suggestion for the `update_score` formula, which initially caused a test failure. After identifying the issue through `pytest`, I corrected the formula and re-ran the tests to confirm the fix.

---

## 3. Debugging and testing your fixes

In addition to the original debugging process, I used `pytest` extensively to validate all fixed bugs. For example, I wrote test cases to ensure that the `parse_guess` function handled invalid inputs correctly and that the `check_guess` function returned accurate outcomes. These automated tests provided confidence that the fixes were robust.

I also manually tested the application by running it with `streamlit` to verify the user interface. This included checking that the "New Game" button cleared the history board and that hint messages were displayed accurately. Both automated and manual testing ensured the application worked as intended.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script from top to bottom whenever a user interacts with the app, which can lead to unexpected behavior if session state is not managed properly. For example, the secret number kept changing because it was being reinitialized on every rerun. I learned that using `st.session_state` allows you to persist variables across reruns, ensuring stability. By initializing the secret number only when it is not already in `st.session_state`, I was able to fix this issue and make the game behave predictably.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing automated tests for every bug fix. This practice helped me ensure that the fixes were robust and prevented regressions. Additionally, I found that breaking down tasks into smaller, testable units (like refactoring logic into `logic_utils.py`) made debugging and testing much easier.

Next time I work with AI, I will be more cautious about verifying its suggestions. For example, AI suggested an incorrect formula for `update_score`, which caused a test failure. While the suggestion was helpful as a starting point, I had to adjust it to meet the requirements. This project taught me to treat AI as a collaborator rather than a perfect solution provider, and to always validate its output through testing.
