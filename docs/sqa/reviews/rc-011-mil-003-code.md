# RC-011: Code review of MIL-003 (continuous play and high score)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the source and tests that [MIL-003] delivers (continuous play and high score)
- Checklist used: [QC-PY-001]
- Scope: full review of the files changed on the branch of the milestone
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the assistant also wrote the code)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `Snake.reset`, `Scoreboard.reset`, `reset_if_collision`, `high_score` and `SEGMENT_PARKING_POSITION` follow PEP 8; `reset` and `high_score` are the lecture's names. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; `HIGH_SCORE_LABEL` and `SEGMENT_PARKING_POSITION` say what they hold. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` exit 0; no `noqa`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy` strict reports no issues in 13 files; every new def is annotated with `-> None` or `-> bool`. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No exception handling was added; the one handler in `main.main` is unchanged. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default argument; no shadowed builtin. |
| 7 | Files, locks and connections are managed with context managers | N-A | No file is opened in this milestone (MIL-004). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | `reset`, `reset_if_collision` and the new constants have Doxygen comments; `doxygen Doxyfile` ends with 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists (deviation recorded in RC-010 and the pull request); the change adds `reset` to the base classes as the lecture does. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 149 tests run without a display; new tests cover higher, equal and lower score on `reset`, the parking of old segments, the new head, the forgotten direction, and `main` going on after the wall and the tail. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `strict = true`; `ScoreboardLike` stays a narrow protocol (`increase_score`, `reset`); no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []` is unchanged. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The label, the parking place and the other values are defined once in `constants.py`; `GAME_OVER_*` is removed, not duplicated. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `snake.py` and `main.py` still import no `turtle` or `tkinter` at module level (tested); no import cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | `Snake.reset` reuses `create_snake`, so the starting positions are one piece of knowledge; `main` depends on the `ScoreboardLike` protocol. |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable. Assessed on 2026-10-13 by the assistant that wrote the code, as stand-in for S01 in autonomous mode. Mode: autonomous, not independent. The pull request is the second look.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this `Go` in the run summary or on the pull request if the stand-in decision is not wanted | S01 | 2026-10-20 |

---

[MIL-003]: ../../milestones/mil-003-continuous-play-and-high-score.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
