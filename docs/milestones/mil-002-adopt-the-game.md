# MIL-002: Adopt the game

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-005 (Go) | [e004c34] |

---

## Purpose

This gate decides whether the finished game of the base ([021-snake-game], `main`) runs in this repository: the snake, the food, the scoreboard, the main flow and all their tests are here, they pass, and the game can be played. It changes no behaviour; the day-24 changes start in [MIL-003]. The work is delivered on the branch `mil-002-adopt-the-game` and one pull request.

## Deliverable

`src/snake_game/snake.py`, `food.py`, `scoreboard.py`, `main.py` and `__main__.py`, and the tests `tests/fakes.py`, `test_snake.py`, `test_food.py`, `test_scoreboard.py` and `test_main.py`. Running `python -m snake_game` plays the game of day 21. The files are copied from the base and changed only where the identity of this repository requires it; the pull request lists every difference from the base.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The adopted files match the base | The pull request lists every difference between each adopted file and the base, or says that there is none | A difference that the list does not name |
| 2 | All tests pass without a display | `pytest` exits 0; no test opens a window; every test of the base is present | A failing test, or a test of the base is missing |
| 3 | Tests, lint, format and types are clean | `pytest`, `python -m ruff check src tests`, `python -m ruff format --check src tests` and `python -m mypy` exit 0, as in continuous integration (CI); no test opens a window | Any of them fails |
| 4 | `doxygen Doxyfile` builds | 0 warnings | Any warning |
| 5 | The game can be played | S01 runs `python -m snake_game` in Windows PowerShell: the window opens, the snake moves and turns, food is shown, the snake eats and grows, the score rises, and the game ends at the wall and at the tail | The game does not start, or one of those things does not happen |
| 6 | Closing the window ends quietly | Closing the window during play, and after game over, ends the program with exit code 0 and no traceback | A traceback |
| 7 | Importing the main flow needs no display | Importing `snake_game.main` loads neither `turtle` nor `tkinter` | Either module is loaded by the import |
| 8 | Constants are in one place | No module other than `constants.py` defines a value of the lectures | A value is a literal in another module |
| 9 | The README matches the adopted game | The Run section and the Project layout of `README.md` describe the files and the command of this milestone | A sentence that is out of date, or a file or command that the README does not name |
| 10 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |
| 11 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] accepted and merged | The package, `constants.py`, the test set-up, the Doxyfile and the CI workflow exist there |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1: the day-21 behaviour is kept | [BC-001], criterion 1 in Success Criteria |
| Objective 7: the assignment's names | [BC-001], criterion 10 in Success Criteria |
| Objective 9: tests without a display | [BC-001], criterion 6 in Success Criteria |
| Objective 11: the base is adopted without hidden change | [BC-001], criteria 11 and 13 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-17 — second of five gateways.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the test fakes | Copy `tests/fakes.py` from the base: the fake segment, the fake screen and the fake `Turtle` base class that record their calls, so that every test runs without a display. The fake `turtle` module is installed before `food` and `scoreboard` are imported. | No | |
| 2 | Adopt the Snake class and its tests | Copy `src/snake_game/snake.py` and `tests/test_snake.py` from the base: `create_snake`, `add_segment`, `extend`, `move`, `hits_wall`, `hits_tail`, `up`, `down`, `left`, `right`, the `segments` list and the `head`. | No | |
| 3 | Adopt the Food class and its tests | Copy `src/snake_game/food.py` and `tests/test_food.py` from the base: `class Food(Turtle)` with `refresh`, whose random place comes from one function that the tests replace. | No | |
| 4 | Adopt the Scoreboard class and its tests | Copy `src/snake_game/scoreboard.py` and `tests/test_scoreboard.py` from the base: `class Scoreboard(Turtle)` with `update_scoreboard`, `increase_score` and `game_over`. `game_over` is replaced in MIL-003. | No | |
| 5 | Adopt the main flow and the entry point | Copy `src/snake_game/main.py`, `src/snake_game/__main__.py` and `tests/test_main.py` from the base: the screen set-up, the key bindings, the animation loop with `game_is_on`, the eating check, the game-over check, the wait for a click and the quiet exit when the window is closed. | No | |
| 6 | Describe the adopted game in the README | Update the Run section and the Project layout of `README.md` so that they match the files and the command of this milestone (`python -m snake_game`, the modules of `src/snake_game/`, the tests). Serves S02 and S03. | No | |
| 7 | Verify the adopted game end to end | Run `pytest`, `ruff check`, `ruff format --check`, `mypy` and `doxygen Doxyfile` in a fresh `.venv`, run `python -m snake_game` until the game is over, close the window during play, and record the results and the list of differences from the base in the pull request. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ./mil-001-project-foundation.md
[MIL-003]: ./mil-003-continuous-play-and-high-score.md
[021-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game
[e004c34]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/e004c34565839b38dc1e06c8a05baaa66ce9eb1d
