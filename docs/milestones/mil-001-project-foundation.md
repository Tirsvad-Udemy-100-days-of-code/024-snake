# MIL-001: Project foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-004 (Go) | [e004c34] |

---

## Purpose

This gate decides whether the repository has the files that carry no game logic yet: configuration, ignore rules, constants, README, source documentation settings, the continuous integration workflow, and the repository description and topics. The work is delivered on the branch `mil-001-project-foundation` and one pull request.

## Deliverable

`pyproject.toml`, the Python `.gitignore`, the package `src/snake_game/` with `__init__.py` and `constants.py`, `tests/test_constants.py`, `README.md` following the Product Owner's template, `Doxyfile`, and `.gitea/workflows/ci.yml`. The repository description and topics on the git host are set. Each adopted file is copied from [021-snake-game] and changed only where the identity of this repository requires it; the pull request lists every difference from the base.

Proposed repository description and topics, for S01 to confirm by accepting the plan:

- Description: "Snake game in Python with turtle graphics, day 24 of Udemy's 100 Days of Code bootcamp: continuous play and a high score kept in a file between games. pytest tests, Doxygen docs, no runtime dependencies."
- Topics: `100-days-of-code`, `doxygen`, `education`, `file-handling`, `game`, `high-score`, `oop`, `pytest`, `python`, `python-bootcamp`, `snake-game`, `turtle-graphics`, `udemy`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | In a fresh clone, `python -m venv .venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` succeed in Windows PowerShell | All three commands exit 0 | Any command fails |
| 2 | `pytest` runs | Exit code 0, at least one test of `constants.py`, no window opened | Failing test, or no test of `constants.py` |
| 3 | `pyproject.toml` states the Python version and the dependencies | `requires-python = ">=3.13"`, `dependencies = []`, a `dev` extra with pytest, and a repository URL that names this repository | Any of the four is missing or different |
| 4 | The `.gitignore` protects local files | `git check-ignore .venv .env __pycache__ data.txt` lists all four | One of them is not ignored |
| 5 | `constants.py` holds the values of the base, with Doxygen comments | Every value of the `constants.py` of [021-snake-game] is a constant with a Doxygen comment | A value is missing or has no Doxygen comment |
| 6 | `doxygen Doxyfile` builds the source documentation | Ends with 0 warnings and writes HTML for `src/` | Any warning, or no output |
| 7 | The README follows the Product Owner's template | Every section title of the template in the given order (Requirements, Set up with Windows powershell, Linux debian and MacOS, Run, Run the tests, Continuous integration, Build the source documentation, Project layout, License), with commands for the three systems | A heading is missing or out of order, or a section has no commands |
| 8 | The CI workflow exists | `.gitea/workflows/ci.yml` installs `.[dev]` and runs `pytest`, `ruff` and `mypy` on Python 3.13, and nothing under `.github/workflows` exists | No workflow, or it does not run the tests, or a file exists under `.github/workflows` |
| 9 | The repository page is complete | Description is non-empty and there are at least 5 topics on the git host | Description empty or fewer than 5 topics |
| 10 | The adopted files are traceable to the base | The pull request lists every difference between each adopted file and the base, or says that there is none | A difference that the list does not name |
| 11 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |
| 12 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [PP-001] accepted | The plan schedules this gateway; the plan-first gate needs it before any code |
| This milestone accepted with a `Go` review | The plan-first gate allows no file under `src/` or `tests/` before that |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 8: reproducible environment, no runtime dependencies | [BC-001], criteria 7 and 9 in Success Criteria |
| Objective 9: tests without a display | [BC-001], criterion 6 in Success Criteria |
| Objective 10: Doxygen and README | [BC-001], criteria 7 and 8 in Success Criteria |
| Objective 12: repository page | [BC-001], criterion 12 in Success Criteria |
| Objective 11: traceable steps; the base is adopted without hidden change | [BC-001], criteria 11 and 13 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-15 — first of five gateways, inside the plan of [PP-001] that ends 2026-10-25.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml for the Day 24 repository | Adopt `pyproject.toml` from the base for the `snake-game` project: `requires-python = ">=3.13"`, an empty `dependencies` list, a `dev` extra with pytest, ruff and mypy, the `src` layout for the package `snake_game`, the pytest settings, and a description and repository URL that name this repository and day 24. Serves objective 8: a reproducible environment without runtime dependencies. | No | |
| 2 | Add the Python .gitignore for the Day 24 repository | Adopt the Python `.gitignore` from the base: bytecode, `.venv/`, build and packaging output, pytest, ruff, mypy and Doxygen caches. It also ignores `.env`, so the personal tokens can never be committed, and `data.txt`, the player's own high score file. | No | |
| 3 | Adopt constants.py and its test | Copy `src/snake_game/__init__.py`, `src/snake_game/constants.py` and `tests/test_constants.py` from the base. Every value is an `UPPER_SNAKE` constant with a Doxygen comment. The day-24 constants are added in MIL-003 and MIL-004. | No | |
| 4 | Add the README for the Day 24 repository | Adopt `README.md` from the base and rewrite its identity for this repository (name, day 24, clone address). Keep the Product Owner's template. Document creating a local `.venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"`; name `python3-tk` and Debian 13 for Linux. The Run section is finished in MIL-005. Serves S02 and S03. | No | |
| 5 | Add the Doxyfile for the Day 24 repository | Adopt the `Doxyfile` from the base: it reads `src/`, writes to `build/doxygen`, extracts documentation for Python and treats warnings as failures; the project brief names day 24. | No | |
| 6 | Add the continuous integration workflow | Adopt `.gitea/workflows/ci.yml` from the base: check out, set up Python 3.13, upgrade `pip`, install `.[dev]`, run `pytest`, `ruff` and `mypy`. The file stays in `.gitea/workflows`, not `.github/workflows`, so the push mirror to GitHub is not blocked. | No | |
| 7 | Set the repository description and topics | Set the description and at least 5 topics of this repository on the git host with the Gitea application programming interface (API), using `GITEA_TOKEN` from the personal `.env` file; the file is only read by the command, never imported, tested or tracked. Use the proposed text of the Deliverable section. Serves S03 and objective 12. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[021-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game
[e004c34]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/e004c34565839b38dc1e06c8a05baaa66ce9eb1d
