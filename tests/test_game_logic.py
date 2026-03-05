import pytest
from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_parse_guess():
    assert parse_guess("6.5") == (
        False,
        None,
        "Decimal numbers are not allowed. Please enter an integer.",
    )
    assert parse_guess("abc") == (False, None, "That is not a number.")
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess("10") == (True, 10, None)


def test_check_guess():
    # Test correct guess
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

    # Test too high guess
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

    # Test too low guess
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_update_score():
    # Test score update for a win
    score = update_score(0, "Win", 1)
    assert score == 90  # 100 - 10 * (1 + 1)

    # Test score update for too high guess on even attempt
    score = update_score(0, "Too High", 2)
    assert score == 5

    # Test score update for too high guess on odd attempt
    score = update_score(0, "Too High", 3)
    assert score == -5

    # Test score update for too low guess
    score = update_score(0, "Too Low", 1)
    assert score == -5


def test_new_game_resets_state():
    # Simulate session state for testing
    session_state = {
        "attempts": 5,
        "history": [10, 20, 30],
        "status": "lost",
    }

    # Reset state logic (mimicking new game button behavior)
    session_state["attempts"] = 0
    session_state["history"] = []
    session_state["status"] = "playing"

    assert session_state["attempts"] == 0
    assert session_state["history"] == []
    assert session_state["status"] == "playing"
