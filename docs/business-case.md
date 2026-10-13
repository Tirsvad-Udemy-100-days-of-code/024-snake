# Business Case: Snake Game (Day 24)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [DICT-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-001 (Go) | [e004c34] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 13 (a screenshot of the running game in the README and on the wiki), scope, success criterion 14, two risks, an assumption and the cost; reviewed in RC-014 (Go) | [988ebba] |

---

## Executive Summary

Snake Game (Day 24) is the day-24 assignment of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*: the snake game of days 20 and 21 gets a high score that survives between games. Day 24 teaches the local file system and reading and writing files with `open` and the `with` keyword. Applied to the game, the lectures change four things: the scoreboard keeps a `high_score` next to the score, the game no longer ends on a collision but resets the snake and the score and goes on, the high score is read from and written to the file `data.txt`, and so it is still there when the game is started again.

This repository starts from the finished game of the day-21 repository [021-snake-game] (the same way that repository started from [020-snake-game]), changes it as the day-24 lectures describe, and gives it the identity of this repository: name, README, description, topics and a wiki in English, Danish and Bahasa Melayu. The work is planned in five milestones, each delivered by one branch and one pull request. The game has no runtime dependencies.

## Methodological and Standards Foundation

- **Process:** the Software Quality Assurance (SQA) and Quality Criteria (QC) framework mounted at `framework/`: Business Case, Stakeholder Analysis, Project Plan, milestones, tasks synced as issues, then code, each step reviewed before the next. Analysis follows Larman, *Applying UML and Patterns*.
- **Quality model:** ISO/IEC 25010:2023; every QC criterion is tagged with a characteristic of it.
- **Code:** Python Enhancement Proposals (PEP) 8, 257 and 484, reviewed against `QC-PY-001`; comments in Doxygen style; tests with pytest.
- **Domain terms:** the lectures' own terms and names, recorded in the Domain Dictionary [DICT-001]: screen, snake, segment, head, food, score, scoreboard, high score, reset, game over, file, mode (`r`, `w`, `a`), `with`, and the names `Snake`, `Food`, `Scoreboard`, `reset`, `high_score`, `update_scoreboard`, `increase_score`.

## Problem Statement

- The high score of the lectures lives in a variable, so it is zero again each time the game is started; the lecture itself calls this out as a flaw.
- A game that stops at the first collision cannot be played again without starting the program again, so a high score has nothing to compete against.
- Reading and writing a file is easy to get subtly wrong: a file left open, a text that is not a number, a file that does not exist yet. The lecture shows the happy path only.
- A turtle program opens a window, so it is normally not tested, and the file handling needs tests that touch no real window and do not overwrite the player's real high score.
- A repository without a description, topics, README or wiki is hard to find and to judge for the people who browse for ideas.

## Business Opportunity

A finished, reproducible repository shows the path from the day-24 lectures to documented, tested code. Starting from the finished day-21 game saves the rebuild, so the effort goes into what is new: continuous play, the high score and its persistence, and the testing of the file handling. It can be compared with the solutions of other participants and shared.

## Objectives

| # | Objective |
| --- | --- |
| 1 | Keep the behaviour of the day-21 base: a 600 by 600 black window titled "My Snake Game"; a snake of three segments that moves by itself and turns with the arrow keys without reversing; food that is eaten, makes the snake longer and raises the score |
| 2 | Deliver the high score of the lectures: `Scoreboard` has a `high_score` attribute that starts at the stored value, and the scoreboard shows `Score: <score> High Score: <high_score>` |
| 3 | Deliver continuous play: `Scoreboard.game_over` is replaced by `Scoreboard.reset`, which sets `high_score` to the score when the score is higher, sets the score to 0 and writes the scoreboard again; touching the wall or the tail calls `reset` of the scoreboard and of the snake and the game goes on |
| 4 | Deliver `Snake.reset`: every segment is moved off the screen, the segment list is emptied, the snake is created again at the starting positions and `head` is the first new segment |
| 5 | Deliver the persistence of the lectures: the high score is read from `data.txt` with `with open(...)` when the scoreboard is made and written to it, as text, when a new high score is reached; the value is still there after the game is closed and started again |
| 6 | Handle the file robustly where the lecture does not: a missing file is created with 0, and a file that does not hold a whole number is treated as 0 |
| 7 | Keep the assignment's structure and names (`Snake`, `Food`, `Scoreboard`, `create_snake`, `add_segment`, `extend`, `move`, `reset`, `up`, `down`, `left`, `right`, `segments`, `head`, `high_score`, `update_scoreboard`, `increase_score`, `game_is_on`), constants in `constants.py` |
| 8 | Provide a reproducible environment: Python 3.13 or newer, a local `.venv`, a `pyproject.toml`, and zero runtime dependencies |
| 9 | Prove the behaviour with pytest tests that need no display and never touch the player's real `data.txt` |
| 10 | Document the project: Doxygen comments in the source with a `Doxyfile`, and a README with set-up instructions for Windows PowerShell, Linux Debian and macOS |
| 11 | Keep every step traceable: one branch and one pull request per milestone, each pull request closing the issues it completes |
| 12 | Publish the repository with a description and topics, and a wiki in English, Danish and Bahasa Melayu |
| 13 | Show the game in a screenshot: a real capture of the running game window at a score of 5 with a high score on the scoreboard, kept in the repository and shown in the README and on the wiki of the repository |

## Scope

### In Scope

- Adopting the finished game of [021-snake-game] (source, tests, configuration, continuous integration workflow) as the base of this repository, and recording every difference from it.
- The day-24 lectures about the snake game: the high score attribute, `reset` instead of `game_over`, continuous play, `Snake.reset`, and reading and writing `data.txt`.
- Constants in `constants.py`; source in `src/`, tests in `tests/`, documents in `docs/`.
- `pyproject.toml`, Python `.gitignore`, `Doxyfile`, `README.md` following the Product Owner's template, a continuous integration (CI) workflow.
- Repository description and topics on the git host.
- A wiki in English, Danish and Bahasa Melayu, in the form of the wiki of `TirSystem/github-action`.
- A screenshot of the running game at a score of 5, kept in `docs/images/`, shown in the README and on the three wiki pages.

### Out of Scope

- The day-24 project that follows the snake game, the personalised letters (mail merge); it is a separate program and gets its own repository if S01 wants it (see the open issues of [PP-001]).
- File paths and directories beyond the single file `data.txt`; the lecture announces them as the next topic.
- Anything the lectures do not cover: sound, a menu, a list of players, levels, configurable speed or window size.
- Keeping this repository and [021-snake-game] in step after today.
- Packaging for or publishing to the Python Package Index (PyPI), and runtime dependencies of any kind.
- A tool in the repository that takes the screenshot: the screenshot is taken once with a one-off script outside the repository, and a later change of the look needs a new screenshot by hand.
- Using or testing the tokens in `.env`; the file is for personal use only and is never imported by the project.

## Expected Benefits

### Tangible Benefits

- A finished game (day 24) with a high score that survives between games, running with one command after the README steps.
- A test suite that runs in continuous integration without a display and without touching a real high score file.
- Generated source documentation.
- A repository page with description, topics, README and a three-language wiki.
- A screenshot of the running game in the README and on the wiki, so that a visitor sees what it looks like before cloning it.

### Intangible Benefits

- Practice with file handling, the `with` statement and the string-to-integer conversion, which is the aim of the lectures.
- A pattern for the following days of the course.
- Confidence from a step-by-step, reviewed delivery.

## Strategic Alignment

The project supports the participant's goal of finishing the bootcamp with repositories that other people can read, run and learn from, and it exercises the framework's rule that planning, review and code stay in step.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The day-21 behaviour is kept | Window, snake, steering, food, eating and score behave as in [021-snake-game] | Manual run by S01 against the Go/No-Go list of [MIL-002], plus the matching tests |
| 2 | The scoreboard shows both scores | The text reads `Score: 0 High Score: 0` at the start and updates when the score or the high score changes | Manual run by S01 against the Go/No-Go list of [MIL-003], plus the matching tests |
| 3 | A collision resets and play continues | At the wall or the tail the score becomes 0, the snake is back at the three starting positions, the old segments are off the screen, and the game goes on; the high score is the largest score reached | Manual run by S01 against the Go/No-Go list of [MIL-003], plus the matching tests |
| 4 | The high score persists | After a new high score the file `data.txt` holds it as text; after closing and starting the game it is shown again | Manual run by S01 against the Go/No-Go list of [MIL-004], plus the matching tests |
| 5 | The file handling is robust | A missing file is created holding 0; an empty or non-numeric file reads as 0; the file is always closed (`with`) | Matching tests, review of `src/` |
| 6 | Tests are green and need no display | 100% of tests pass; 0 tests open a window; 0 tests read or write the real `data.txt` | `pytest` exit code 0 locally and in CI |
| 7 | The set-up steps work | A fresh clone reaches a green `pytest` by following the README alone, on Windows PowerShell (by S01) and on Linux (by CI) | One run per operating system, recorded in the pull request |
| 8 | Source documentation builds | `doxygen Doxyfile` ends with 0 warnings | Doxygen output |
| 9 | No runtime dependencies | 0 entries in `[project].dependencies` | `pyproject.toml` |
| 10 | Names follow the assignment | 100% of the names listed in objective 7 exist with that spelling | Review of `src/` against objective 7 |
| 11 | Steps are traceable | 5 of 5 milestones merged by pull request, each description with one `Closes #N` line per completed issue | Pull request list and issue states |
| 12 | The repository page is complete | Non-empty description, at least 5 topics, and the wiki pages `Home`, `Home.da` and `Home.ms` | Git host |
| 13 | The base is adopted without hidden change | Every difference between the adopted files and [021-snake-game] is listed in the pull request that introduces it | Pull request descriptions |
| 14 | The game is shown in a real screenshot | `docs/images/snake-score-5.png` is a capture of the window of the running game while its scoreboard reads `Score: 5` followed by a high score; the README and the wiki pages `Home`, `Home.da` and `Home.ms` show it, and its address on `main` answers HTTP 200 with an image | The file, the README and the wiki, checked against the Go/No-Go list of [MIL-006] |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| `tkinter` is missing from the Python installation (typical on Debian) | The game cannot start | README lists `python3-tk` for Debian; the tests install a fake `turtle` module and need no `tkinter` |
| Debian 12 ships Python 3.11, below the required 3.13 | Linux set-up fails | README states Debian 13 or newer, or a separately installed Python 3.13 |
| A turtle window cannot be opened in continuous integration | The tests cannot cover the game | Only `main` opens a window; the classes are tested with fakes, as in the base |
| A test overwrites the player's real `data.txt` | The player loses a high score | The path of the file is a parameter with the constant as default; tests pass a temporary path (pytest `tmp_path`) |
| `data.txt` is resolved against the current working directory, so the game started from another folder finds another file | The high score seems to be lost | Decided in [MIL-004] and recorded in an open issue of [PP-001]; the lecture's plain file name is the default |
| The file is missing, empty or damaged | The game crashes at start | Objective 6: read as 0 and create the file; covered by tests |
| Author and reviewer are the same person (S01) | A defect can pass review unnoticed | Review against the QC checklists, record each review as an `RC-*`, and let the pull request be the second look |
| The lectures are available only as the summaries in the request | The game differs from the video | S01 compares the finished game with the video at the [MIL-003] and [MIL-004] Go/No-Go |
| The adopted files drift away from [021-snake-game] | A fix made in one repository is missing in the other | Out of scope by decision; each pull request lists the differences from the base |
| Tokens in `.env` leak into the repository | Credentials exposed | `.env` is in `.gitignore`, is never imported, and is not part of any task |
| The wiki is published with a secret of the organization that may be missing | The wiki stays empty | The pages are files in `wiki/` of the pull request; the marker `wiki/.publish` makes the instance's workflow publish them; a missing secret is reported, not worked around |
| The screenshot is a capture of a real window, which needs a display and the operating system's window capture | It cannot be repeated in CI or on another machine | It is taken once on S01's machine and committed as a file; the pull request says how it was taken and that the food was placed to reach the score quickly; a capture tool is out of scope |
| The screenshot goes out of date when the look changes | The README and the wiki show a look that the game no longer has | The wiki refers to the file on `main`, so a new screenshot replaces it in all places; a change of the look has its own milestone that retakes it |

## Assumptions

- Python 3.13 or newer with `tkinter` is available on the machines that run the game.
- S01 is the only person who reviews and accepts artifacts.
- The git host is the Tirsvad Gitea instance, and its issues and milestones are used for tracking.
- The day-24 lecture summaries in the request are the specification of day 24; the video is the tie-breaker when a detail is missing.
- The finished `main` of [021-snake-game] is correct as far as its own tests and review records show, and is the base for every file that the milestones adopt; S01 pointed to it in chat on 2026-10-13.
- The look of the snake (light green body, dark green head with a mouth) of [021-snake-game] is kept.
- The wiki of the repository is enabled and has no page yet.
- The screenshot is of the finished game as it runs on S01's Windows machine; S01 accepts the plan that adds it by chat, which also confirms the score of 5 and a high score on the scoreboard as its content.

## Constraints

- Python 3.13 or newer, in a virtual environment (`venv`).
- pytest for tests; `constants.py` for constants; `pyproject.toml` for project configuration; a Python `.gitignore`; Doxygen comments in the source and a `Doxyfile`.
- Folder structure `src/`, `tests/`, `docs/`.
- No runtime dependencies unless needed.
- Plan window from 2026-10-14 to 2026-10-25 (proposed, see [PP-001]).
- S01 switched on autonomous mode in chat on 2026-10-13: S01's acceptance of the plan is the request to commit, push, open and merge the pull requests; the assistant's reviews are then not independent (see `AGENTS.md`, Modes).
- The plan gate holds: no file under `src/` or `tests/` before an accepted, reviewed milestone that lists the task.

## Cost–Benefit Assessment

The assessment is qualitative on purpose: this is an unpaid learning project with one participant, so money does not measure either side.

| Costs | Benefits |
| --- | --- |
| About ten days of S01's spare time, most of it review of the planning documents, and two more days for the screenshot | A finished and shareable repository (objectives 1 to 13) |
| Two repositories that hold similar code and can drift apart | No rebuild of a game that already exists and is tested |
| Doxygen and pytest as development tools (not runtime) | Source documentation and automatic checks |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Wants a correct, tested and documented solution of the assignment: objectives 1 to 13 |
| S02 | Needs readable, runnable code with the assignment's names and README instructions (objectives 2 to 4, 7, 8 and 10) |
| S03 | Needs a clear repository page and nothing to install (objectives 8, 10, 12 and 13) |

## Recommendation

Proceed — the work is small (adopt a finished and tested base, add the high score, continuous play and the file, document and publish), the cost is about ten days of the Product Owner's spare time, and the result is a reusable, documented repository.

---

[SA-001]: ./stakeholder-analysis.md
[DICT-001]: ./dictionary.md
[PP-001]: ./project-plan.md
[MIL-002]: ./milestones/mil-002-adopt-the-game.md
[MIL-003]: ./milestones/mil-003-continuous-play-and-high-score.md
[MIL-004]: ./milestones/mil-004-high-score-file.md
[MIL-006]: ./milestones/mil-006-screenshot.md
[020-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game
[021-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game
[e004c34]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/e004c34565839b38dc1e06c8a05baaa66ce9eb1d
[988ebba]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/988ebba060c1ec69728a7fa36b24bc70737096d8
