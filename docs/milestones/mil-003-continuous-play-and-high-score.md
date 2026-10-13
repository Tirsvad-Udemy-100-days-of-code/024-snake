# MIL-003: Continuous play and high score

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-006 (Go) | [e004c34] |

---

## Purpose

This gate decides whether the game follows the day-24 lectures on the high score and on continuous play: the scoreboard has a `high_score`, `reset` replaces `game_over`, a collision resets the snake and the score and the game goes on, and the old snake leaves the screen. The high score lives in memory only; the lecture itself shows that it is lost when the game is started again, and [MIL-004] stores it. The work is delivered on the branch `mil-003-continuous-play-and-high-score` and one pull request.

## Deliverable

Changed `src/snake_game/scoreboard.py`, `snake.py`, `main.py` and `constants.py`, with changed and added tests. `Scoreboard.game_over` and its test are removed; `Scoreboard.reset` and `Snake.reset` are added.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The scoreboard shows both scores | The text is `Score: <score> High Score: <high_score>` and starts as `Score: 0 High Score: 0`; the label texts are constants; the old text is cleared before every write | A different text, a literal label outside `constants.py`, or text that is written over the old one |
| 2 | `Scoreboard.reset` follows the lecture | When `score > high_score`, `high_score` becomes the score; then the score is 0 and the scoreboard is written again; a lower or equal score leaves `high_score` unchanged | Any of the three cases behaves differently |
| 3 | `Snake.reset` clears the old snake | Every old segment is sent to a place off the screen (a constant), `segments` is emptied, the snake is created again at the three starting positions and `head` is the first new segment | An old segment stays on the screen, or `head` still refers to an old segment |
| 4 | A collision no longer ends the game | At the wall and at the tail, `scoreboard.reset()` and `snake.reset()` are called and the loop goes on; `game_over`, `GAME_OVER_TEXT` and the wait for a click are gone | The game stops, or a name of the removed game over remains |
| 5 | The snake is playable after a reset | After a reset the snake moves right from the starting positions, a reversal is still ignored, and the food keeps its place | The snake does not move, or turns back onto itself |
| 6 | The day-24 values are constants | The off-screen place and the label texts used by `reset` and the scoreboard are constants with Doxygen comments | A literal in another module |
| 7 | The day-21 tests still hold | Every test of [MIL-002] passes, or is changed on purpose and the change is named in the pull request | A test is deleted without being named |
| 8 | Tests, lint, format and types are clean | `pytest`, `python -m ruff check src tests`, `python -m ruff format --check src tests` and `python -m mypy` exit 0, as in continuous integration (CI); no test opens a window | Any of them fails |
| 9 | `doxygen Doxyfile` builds | 0 warnings | Any warning |
| 10 | The game can be played | S01 plays in Windows PowerShell: hits the wall and the tail twice, sees the score go back to 0, the high score keep the best, and the old snake disappear | Any of those does not happen |
| 11 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |
| 12 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] accepted and merged | The classes and the main flow that this milestone changes exist there |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2: the high score and the scoreboard text | [BC-001], criterion 2 in Success Criteria |
| Objective 3: continuous play and `reset` | [BC-001], criterion 3 in Success Criteria |
| Objective 4: `Snake.reset` | [BC-001], criterion 3 in Success Criteria |
| Objective 7: the assignment's names | [BC-001], criterion 10 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-19 — third of five gateways.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the high score constants | Add to `constants.py`, with Doxygen comments: the label of the high score text, the place off the screen where an old segment is sent, and any other value the next tasks need. Add the matching test of `test_constants.py`. | No | |
| 2 | Add the high_score attribute and the scoreboard text | `Scoreboard.__init__` sets `self.high_score` to 0 next to `self.score`; `update_scoreboard` clears the old text and writes `Score: <score> High Score: <high_score>`; tests with the fake turtle check the text and the clearing. | No | |
| 3 | Replace game_over with reset in the Scoreboard | Remove `Scoreboard.game_over` and its test. Add `Scoreboard.reset`: when the score is higher than `high_score`, the high score becomes the score; the score becomes 0; `update_scoreboard` is called. Tests: higher, equal and lower score. | No | |
| 4 | Add Snake.reset | Add `Snake.reset`: send every segment of `segments` to the off-screen place, empty the list, call `create_snake` again and set `head` to `segments[0]`. Tests with fake segments check that no old segment remains and that the starting positions are used. | No | |
| 5 | Play on after a collision in the main flow | In `main.py`, a hit of the wall or of the tail calls `scoreboard.reset()` and `snake.reset()` and the loop goes on; the end-of-game check, the game-over text and `exitonclick` are removed; closing the window still ends quietly. Update `tests/test_main.py`. | No | |
| 6 | Update the README for continuous play | Describe in the Run section the two scores on the scoreboard and what a collision does now, and remove the sentences about game over. Serves S02 and S03. | No | |
| 7 | Verify continuous play end to end | Run `pytest`, `ruff check`, `ruff format --check`, `mypy` and `doxygen Doxyfile` in a fresh `.venv`, play with several collisions and close the window, and record the results and the changed tests in the pull request. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-adopt-the-game.md
[MIL-004]: ./mil-004-high-score-file.md
[021-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game
[e004c34]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/e004c34565839b38dc1e06c8a05baaa66ce9eb1d
