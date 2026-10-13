# MIL-006: Screenshot

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-017 (Go) | pending |

---

## Purpose

This gate decides whether the README and the wiki show the finished game in a real screenshot at a score of 5, as S01 asked on 2026-10-13 (objective 13 of [BC-001]). Nothing about the game changes. It is the sixth gate of [PP-001], added after [MIL-005] was merged. The work is delivered on the branch `mil-006-screenshot` and one pull request; the wiki pages are files in the folder `wiki/` of the same pull request and are published by the instance's workflow when it is merged.

## Deliverable

`docs/images/snake-score-5.png`, a capture of the window of the running game while its scoreboard reads `Score: 5 High Score: 12`; the picture in `README.md`; and the picture on the wiki pages `Home.md`, `Home.da.md` and `Home.ms.md`, each with a caption in its own language. The capture is made once with a one-off script outside the repository: it starts the real game classes in a real window, places the food in front of the snake until the score is 5, shows a high score of 12 that comes from a temporary `data.txt` (S01's own file is not used), and takes the window with the operating system's screen capture. The script is not part of the repository.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The file exists and is a PNG of the game window | `docs/images/snake-score-5.png` has the PNG signature and a width and height of at least 600 pixels | The file is missing, is not a PNG or is smaller |
| 2 | The picture shows the running game at a score of 5 | Looking at the file, the window titled "My Snake Game" shows a black screen, the snake with a dark green head, blue food, and the white text `Score: 5 High Score: 12` | The text, the snake or the food is missing, or another window or the desktop is in the picture |
| 3 | The picture shows nothing personal | Only the game window is in the picture: no taskbar, no other window, no file path or user name | Anything outside the game window is visible |
| 4 | The README shows the picture | `README.md` has the image with a link to `docs/images/snake-score-5.png`, an alternative text and a caption under it, once | No picture, a broken link, or the picture shown twice |
| 5 | The wiki shows the picture in three languages | `Home.md`, `Home.da.md` and `Home.ms.md` have the image with the address of the file on `main` and a caption in the language of the page; after the merge the three pages are on the wiki | A language is missing, or the address does not answer HTTP 200 with an image |
| 6 | The game and its checks are unchanged | No Python file is changed; `pytest`, `python -m ruff check src tests`, `python -m ruff format --check src tests`, `python -m mypy` and `doxygen Doxyfile` give the results of [MIL-005] | A Python file is in the change, or a check differs |
| 7 | The player's own file is not used | The repository has no tracked `data.txt`, and the capture script is not in the change | `data.txt` or the script is in the change |
| 8 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |
| 9 | The change is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` (no Python file changed, so every criterion is not applicable) | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-005] accepted and merged | The finished README and the wiki pages exist there |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 13: a real screenshot in the README and on the wiki | [BC-001], criterion 14 in Success Criteria |
| Objective 12: the wiki in three languages is kept | [BC-001], criterion 12 in Success Criteria |
| Objective 9: tests without a display are unchanged | [BC-001], criterion 6 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-25 — sixth of six gateways, in the two buffer days of [PP-001] that ends 2026-10-25.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Take the screenshot of the running game | With a one-off script outside the repository, start the game classes in a real window, place the food in front of the snake until the score is 5, show a high score of 12 from a temporary file, and capture the window with the operating system's screen capture into `docs/images/snake-score-5.png`. Look at the file to check criteria 1 to 3. Serves S03 and objective 13. | No | |
| 2 | Show the screenshot in the README | Add the image, an alternative text and a caption to `README.md`, once, near the top. Serves S02 and S03. | No | |
| 3 | Show the screenshot on the wiki pages | Add the image, which refers to the file on `main`, and a caption in English, Danish and Bahasa Melayu to `wiki/Home.md`, `wiki/Home.da.md` and `wiki/Home.ms.md`. Serves S03. | No | |
| 4 | Verify the screenshot end to end | Run the checks of criterion 6, read the README and the three wiki pages, request the address of the file on `main` and check that it answers HTTP 200 with an image, and record the results in the pull request. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-005]: ./mil-005-wiki-and-finish.md
