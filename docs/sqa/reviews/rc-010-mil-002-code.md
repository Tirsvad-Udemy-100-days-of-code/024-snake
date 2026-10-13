# RC-010: Code review of MIL-002 (adopted game: snake, food, scoreboard, main flow)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [c784a5c] |

---

## Artifact Under Review

- Instance reviewed: the source and tests that [MIL-002] delivers (adopted game: snake, food, scoreboard, main flow)
- Checklist used: [QC-PY-001]
- Scope: full review of the files changed on the branch of the milestone
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the assistant also wrote the code)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Classes `Snake`, `Food`, `Scoreboard` are `PascalCase`; functions, methods and variables are `snake_case`; constants are `UPPER_SNAKE`. Names such as `create_snake`, `up` and `game_is_on` are the lectures' own. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`eat_food_if_close`, `end_game_if_over`, `hits_tail`); no unexplained abbreviation. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `python -m ruff check src tests` and `python -m ruff format --check src tests` exit 0; no `noqa`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy` strict reports no issue in 13 files; every def has annotations including `-> None`. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | One handler, `except (Terminator, TclError): return` in `main.main`, is specific and deliberate: both mean the player closed the window; it is documented in the docstring. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default argument; no shadowed builtin. |
| 7 | Files, locks and connections are managed with context managers | N-A | No file is opened in this milestone (the high score file is MIL-004). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class, function and method has a Doxygen docstring; `doxygen Doxyfile` ends with 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging; no secret or personal data. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists; this deviation is recorded here and in the pull request: the classes are the base's (`Snake`, `Food`, `Scoreboard`) and trace to the lectures and to the base. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 138 tests in `tests/` run without a display or network, named for behaviour, with the fake `turtle` module of `tests/fakes.py`. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `strict = true`; the only `Protocol` classes (`ScreenLike`, `FoodLike`, `ScoreboardLike`, `Segment`) are narrow and there is no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; the three dev tools are used. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Every value of the lectures is defined once in `constants.py`; modules import them from there. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `snake.py` and `main.py` import no `turtle` or `tkinter` at module level (checked by a test), no import cycle; `food.py` and `scoreboard.py` need `turtle` because they inherit from `Turtle`, as the lectures teach. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | `main.py` depends on narrow protocols, not on concrete turtle classes; `Snake` receives its segment factory as a parameter; each class has one reason to change. |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable. Assessed on 2026-10-13 by the assistant that wrote the code, as stand-in for S01 in autonomous mode. Mode: autonomous, not independent. The pull request is the second look.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this `Go` in the run summary or on the pull request if the stand-in decision is not wanted | S01 | 2026-10-20 |

---

[MIL-002]: ../../milestones/mil-002-adopt-the-game.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[c784a5c]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/c784a5c374e14a26369d217eea8bc6b11d2ac532
