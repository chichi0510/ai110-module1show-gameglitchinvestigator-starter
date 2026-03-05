def get_range_for_difficulty(difficulty: str):
    """
    Return the range of numbers for a given difficulty level.

    Args:
        difficulty (str): The difficulty level (e.g., "Easy", "Normal", "Hard").

    Returns:
        tuple: A tuple containing the lower and upper bounds of the range.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an integer guess.

    Args:
        raw (str): The raw input string from the user.

    Returns:
        tuple: A tuple containing a boolean indicating success, the parsed integer (or None),
               and an error message (or None).
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            return (
                False,
                None,
                "Decimal numbers are not allowed. Please enter an integer.",
            )
        else:
            value = int(raw)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare the user's guess to the secret number.

    Args:
        guess (int or str): The user's guess.
        secret (int or str): The secret number to compare against.

    Returns:
        tuple: A tuple containing the outcome ("Win", "Too High", "Too Low", or "Error")
               and a corresponding message.
    """
    try:
        guess = int(guess)
        secret = int(secret)

        if guess == secret:
            return "Win", "🎉 Correct!"
        elif guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except ValueError:
        return "Error", "Invalid input. Please enter a number."


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update the player's score based on the game outcome and attempt number.

    Args:
        current_score (int): The player's current score.
        outcome (str): The outcome of the guess ("Win", "Too High", "Too Low").
        attempt_number (int): The current attempt number.

    Returns:
        int: The updated score.
    """
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
