# 🐞 Bug Report: Glitchy Guesser

This document records all identified bugs in the "Glitchy Guesser" game, along with their root causes.

---

## 1. **Narrowed Range Incorrect Guess**

- **Description**: When the possible range is narrowed down to one integer, the guess should be correct, but the system says it is not.
- **Root Cause**: The `check_guess` function inconsistently handles type mismatches between `guess` (integer) and `secret` (string on even-numbered attempts). This leads to incorrect comparisons and wrong outcomes.

---

## 2. **Float Input Revised to Integer**

- **Description**: When a float number (e.g., `6.5`) is entered, the system revises it to an integer (e.g., `6`) without informing the user.
- **Root Cause**: The `parse_guess` function converts floats to integers using `int(float(raw))`, truncating the decimal part. This behavior is intentional but not communicated to the user, leading to confusion.

---

## 3. **Records Inconsistency**

- **Description**:
  - The "Attempts left" number is inconsistent with the history record and system message.
  - The score displayed in the table is inconsistent with the system message.
- **Root Cause**:
  - The "Attempts left" value is calculated before the `attempts` counter is incremented, causing an off-by-one error.
  - The score update logic occurs after the outcome is determined, leading to a delay in reflecting the correct score.
- **Status**: Fixed
- **Fix Details**:
  - Updated the "Attempts left" calculation to reflect the incremented attempts.
  - Ensured the score is updated before displaying the message.

---

## 4. **New Game Does Not Clear History**

- **Description**: When the "New Game" button is clicked, the history board is not cleared, and the system message still says "Game over. Start a new game to try again."
- **Root Cause**:
  - The `st.session_state.history` variable is not reset when starting a new game.
  - The `st.session_state.status` variable is not reset to "playing," causing the system to display the old game state.

---

## 5. **Wrong Hint Messages**

- **Description**: The system gives incorrect hints (e.g., "Too High" or "Too Low") even when the guess is correct.
- **Root Cause**:
  - The `secret` alternates between an integer and a string depending on the attempt number (`st.session_state.attempts % 2`).
  - The `check_guess` function does not handle type mismatches properly, leading to incorrect comparisons and hints.

---

## Next Steps

- Fix the identified bugs by addressing their root causes.
- Ensure consistent handling of types and state variables.
- Add proper user feedback for revised inputs and reset actions.
- Test thoroughly to verify that all issues are resolved.
