# MIL-005: Wiki and finish

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-008 (Go) | [e004c34] |

---

## Purpose

This gate decides whether the repository is finished: the wiki exists in English, Danish and Bahasa Melayu, the README matches the finished game, the repository page is complete, and the whole game has been checked end to end. The work is delivered on the branch `mil-005-wiki-and-finish` and one pull request.

## Deliverable

The folder `wiki/` with `Home.md`, `Home.da.md`, `Home.ms.md`, `_Sidebar.md` and the marker `.publish`, in the form of the wiki of `TirSystem/github-action` and of [021-snake-game]; the finished `README.md`; a checked description and topics.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The wiki is in three languages | The wiki has the pages `Home` (English), `Home.da` (Danish, Dansk) and `Home.ms` (Bahasa Melayu), each with a short description of the game, its controls, the high score file and how to run it, a language switch at the top, and a `_Sidebar` that lists the three languages | A language is missing, or a page does not link to the other two |
| 2 | The wiki is published | `wiki/.publish` exists and, after the merge, the three pages are on the wiki of the repository | The pages are not on the wiki; a missing secret is reported to S01 |
| 3 | The README is finished | Every section of the template is filled, the commands match the game, and no sentence is out of date | A heading is missing or a sentence is out of date |
| 4 | The repository page is complete | Description non-empty and at least 5 topics on the git host | Description empty or fewer than 5 topics |
| 5 | The whole game works | `pytest`, `ruff`, `mypy` and `doxygen Doxyfile` are clean in a fresh clone, and S01 plays: collision, reset, high score kept after a restart | Any check fails |
| 6 | No runtime dependencies | `[project].dependencies` is empty | An entry is present |
| 7 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |
| 8 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] accepted and merged | The high score file exists there, and the wiki describes it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 10: README | [BC-001], criteria 7 and 8 in Success Criteria |
| Objective 12: repository page and wiki | [BC-001], criterion 12 in Success Criteria |
| Objective 11: traceable steps | [BC-001], criterion 11 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-23 — last of five gateways; two buffer days follow.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the wiki pages in three languages | In the folder `wiki/`, as the wiki of `TirSystem/github-action` does, write `Home.md` (English), `Home.da.md` (Danish) and `Home.ms.md` (Bahasa Melayu), each with a short description of the game, its controls, the high score file and how to run it, and a language switch (English, Dansk, Bahasa Melayu) at the top; add `_Sidebar.md` that lists the three languages. Serves S03. | No | |
| 2 | Add the wiki publish marker | Add the empty marker `wiki/.publish`, which makes the instance's workflow copy the pages to the wiki of the repository when a pull request is merged to `main`. It needs the secret `TOKEN_FOR_GITEA_WIKI` of the organization; a token is never printed or typed, and a missing secret is reported to S01. | No | |
| 3 | Finish the README | Check every section of `README.md` against the finished game: set-up on the three systems, run, the controls, the two scores, `data.txt`, the tests, CI, Doxygen, layout and license; correct what is out of date. Serves S02 and S03. | No | |
| 4 | Check the repository description and topics again | Read the description and topics from the git host and compare them with the finished game; correct them with the Gitea API when they differ. | No | |
| 5 | Verify the finished game end to end | In a fresh clone follow the README alone: create the `.venv`, upgrade `pip`, install, run `pytest`, `ruff`, `mypy` and `doxygen Doxyfile`, play, restart, and record the results in the pull request. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-004]: ./mil-004-high-score-file.md
[021-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game
[e004c34]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/e004c34565839b38dc1e06c8a05baaa66ce9eb1d
