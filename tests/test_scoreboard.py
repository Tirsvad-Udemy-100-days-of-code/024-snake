"""Tests of the scoreboard, with a fake `Turtle` as its base class."""

import importlib
import sys
from pathlib import Path

import pytest

from fakes import install_fake_turtle, make_scoreboard
from snake_game import constants

START_TEXT = (
    "write",
    ("Score: 0 High Score: 0", "center", ("Arial", 24, "normal")),
)


def test_scoreboard_is_white_hidden_and_at_the_top_centre(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    assert ("color", ("white",)) in scoreboard.calls
    assert "penup" in scoreboard.call_names()
    assert "hideturtle" in scoreboard.call_names()
    assert ("goto", constants.SCOREBOARD_POSITION) in scoreboard.calls


def test_scoreboard_inherits_from_turtle(monkeypatch: pytest.MonkeyPatch) -> None:
    install_fake_turtle(monkeypatch)
    module = importlib.import_module("snake_game.scoreboard")

    assert issubclass(module.Scoreboard, sys.modules["turtle"].Turtle)


def test_scoreboard_starts_by_writing_both_scores_0_centred_in_arial_24(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    assert scoreboard.calls[-1] == START_TEXT


def test_increase_score_wipes_the_old_text_and_writes_the_new_score(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    scoreboard.increase_score()

    assert scoreboard.call_names()[-2:] == ["clear", "write"]
    assert scoreboard.calls[-1] == (
        "write",
        ("Score: 1 High Score: 0", "center", ("Arial", 24, "normal")),
    )


def test_every_food_adds_one_to_the_score(monkeypatch: pytest.MonkeyPatch) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    for _ in range(3):
        scoreboard.increase_score()

    assert scoreboard.calls[-1][1][0] == "Score: 3 High Score: 0"


def test_high_score_starts_at_0(monkeypatch: pytest.MonkeyPatch) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    assert scoreboard.high_score == 0
    assert scoreboard.score == 0


def test_reset_keeps_a_higher_score_as_the_high_score_and_starts_again(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)
    for _ in range(3):
        scoreboard.increase_score()

    scoreboard.reset()

    assert scoreboard.high_score == 3
    assert scoreboard.score == 0
    assert scoreboard.call_names()[-2:] == ["clear", "write"]
    assert scoreboard.calls[-1] == (
        "write",
        ("Score: 0 High Score: 3", "center", ("Arial", 24, "normal")),
    )


def test_reset_keeps_the_high_score_when_the_score_is_lower(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)
    for _ in range(3):
        scoreboard.increase_score()
    scoreboard.reset()
    scoreboard.increase_score()

    scoreboard.reset()

    assert scoreboard.high_score == 3
    assert scoreboard.calls[-1][1][0] == "Score: 0 High Score: 3"


def test_reset_keeps_the_high_score_when_the_score_is_equal(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)
    scoreboard.increase_score()
    scoreboard.reset()
    scoreboard.increase_score()

    scoreboard.reset()

    assert scoreboard.high_score == 1
    assert scoreboard.score == 0


def test_the_score_text_shows_both_scores_while_playing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)
    scoreboard.increase_score()
    scoreboard.increase_score()
    scoreboard.reset()
    scoreboard.increase_score()

    assert scoreboard.calls[-1][1][0] == "Score: 1 High Score: 2"


def test_scoreboard_shows_the_stored_high_score_at_start(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    path = tmp_path / "scores.txt"
    path.write_text("12", encoding="utf-8")

    scoreboard = make_scoreboard(monkeypatch, path)

    assert scoreboard.high_score == 12
    assert scoreboard.calls[-1][1][0] == "Score: 0 High Score: 12"


def test_a_new_high_score_is_written_to_the_file_on_reset(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    path = tmp_path / "scores.txt"
    path.write_text("1", encoding="utf-8")
    scoreboard = make_scoreboard(monkeypatch, path)
    for _ in range(2):
        scoreboard.increase_score()

    scoreboard.reset()

    assert path.read_text(encoding="utf-8") == "2"


def test_a_lower_score_does_not_write_the_file(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    path = tmp_path / "scores.txt"
    path.write_text("5", encoding="utf-8")
    scoreboard = make_scoreboard(monkeypatch, path)
    scoreboard.increase_score()
    path.write_text("sentinel", encoding="utf-8")

    scoreboard.reset()

    assert path.read_text(encoding="utf-8") == "sentinel"
    assert scoreboard.high_score == 5


def test_an_equal_score_does_not_write_the_file(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    path = tmp_path / "scores.txt"
    path.write_text("2", encoding="utf-8")
    scoreboard = make_scoreboard(monkeypatch, path)
    scoreboard.increase_score()
    scoreboard.increase_score()
    path.write_text("sentinel", encoding="utf-8")

    scoreboard.reset()

    assert path.read_text(encoding="utf-8") == "sentinel"


def test_a_missing_file_shows_high_score_0_and_is_created(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    path = tmp_path / "scores.txt"

    scoreboard = make_scoreboard(monkeypatch, path)

    assert scoreboard.calls[-1] == START_TEXT
    assert path.read_text(encoding="utf-8") == "0"


def test_a_damaged_file_shows_high_score_0(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    path = tmp_path / "scores.txt"
    path.write_text("not a number", encoding="utf-8")

    scoreboard = make_scoreboard(monkeypatch, path)

    assert scoreboard.high_score == 0
    assert scoreboard.calls[-1] == START_TEXT


def test_scoreboard_has_no_game_over_any_more(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    assert not hasattr(scoreboard, "game_over")
