# MIL-004: High score file

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-007 (Go) | [e004c34] |

---

## Purpose

This gate decides whether the high score survives between games: it is read from `data.txt` with `with open(...)` when the scoreboard is made, converted from text to an integer, and written back to the file when a new high score is reached. It also decides the behaviour where the lecture is silent: a missing, empty or damaged file. The work is delivered on the branch `mil-004-high-score-file` and one pull request.

## Deliverable

Changed `src/snake_game/scoreboard.py` and `constants.py`, functions that read and write the high score, and tests that use a temporary file. The game, started again after a new high score, shows that high score.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The high score is read at the start | `Scoreboard()` reads the file named by the constant `HIGH_SCORE_FILE` (`data.txt`) with a `with` statement, converts the text with `int` and shows the value as `High Score` | The value is not read, the file is opened without `with`, or the text is not converted |
| 2 | A new high score is written | When `reset` finds a score above the high score, the file holds the new value as text; a lower or equal score does not write the file | The file is not written, is written for a lower score, or holds something other than the number |
| 3 | A missing file is created | Starting without `data.txt` shows `High Score: 0` and leaves a `data.txt` that holds `0` | A traceback, or no file |
| 4 | A damaged file reads as 0 | An empty file, a file with text that is not a whole number and a negative number all give a high score of 0 without a traceback | A traceback, or a negative high score |
| 5 | The path is a parameter | The file name is a constant used as the default of a parameter, and every test passes a temporary path | A test uses the real `data.txt` |
| 6 | The high score survives a restart | S01 reaches a new high score, closes the window, starts `python -m snake_game` again and sees the same high score | The value is lost |
| 7 | `data.txt` is not tracked | `git check-ignore data.txt` lists it and no `data.txt` is in the change | The file is tracked |
| 8 | Tests, lint, format and types are clean | `pytest`, `python -m ruff check src tests`, `python -m ruff format --check src tests` and `python -m mypy` exit 0, as in continuous integration (CI); no test opens a window | Any of them fails |
| 9 | `doxygen Doxyfile` builds | 0 warnings | Any warning |
| 10 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |
| 11 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] accepted and merged | `Scoreboard.reset` and the two scores exist there |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5: the file read and written with `with` | [BC-001], criterion 4 in Success Criteria |
| Objective 6: a missing or damaged file | [BC-001], criterion 5 in Success Criteria |
| Objective 9: tests never touch the real file | [BC-001], criterion 6 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-21 — fourth of five gateways.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the high score file constant | Add `HIGH_SCORE_FILE: Final[str] = "data.txt"` to `constants.py` with a Doxygen comment, and a test of it. | No | |
| 2 | Read the high score from the file | Add a function that opens the file with `with open(path) as data`, reads it, converts the text with `int` and returns it; `Scoreboard.__init__` takes the path as a parameter with the constant as default and sets `high_score` from it. Tests with a temporary file. | No | |
| 3 | Write the high score to the file | In `Scoreboard.reset`, when a new high score is reached, open the file with `with open(path, mode="w") as data` and write the number as text. Tests check the file content after a higher, equal and lower score. | No | |
| 4 | Handle a missing or damaged file | A missing file is created holding `0`; an empty file, text that is not a whole number or a negative number read as 0 (objective 6 of the Business Case). Tests for each case. | No | |
| 5 | Keep the tests away from the real data.txt | Every test that makes a `Scoreboard` passes a pytest `tmp_path` file; a guard in `tests/conftest.py` fails a test that would open the default path. | No | |
| 6 | Document the high score file in the README | Describe in the Run section where `data.txt` is, that it is created at the first start, how to reset the high score (delete the file) and that it is not tracked by git. Serves S02. | No | |
| 7 | Verify the high score file end to end | Run `pytest`, `ruff check`, `ruff format --check`, `mypy` and `doxygen Doxyfile` in a fresh `.venv`, reach a high score, restart the game, delete and damage `data.txt` and start again, and record the results in the pull request. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-003]: ./mil-003-continuous-play-and-high-score.md
[MIL-005]: ./mil-005-wiki-and-finish.md
[021-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game
[e004c34]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/e004c34565839b38dc1e06c8a05baaa66ce9eb1d
