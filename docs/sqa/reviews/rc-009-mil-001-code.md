# RC-009: Code review of MIL-001 (project foundation: constants, package, tests)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [61d6df7] |

---

## Artifact Under Review

- Instance reviewed: the source and tests that [MIL-001] delivers (project foundation: constants, package, tests)
- Checklist used: [QC-PY-001]
- Scope: full review of the files changed on the branch of the milestone
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the assistant also wrote the code)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `SCREEN_WIDTH`, `BODY_COLOR` and the other constants are `UPPER_SNAKE`; test functions are `snake_case`; the package is `snake_game`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`STARTING_POSITIONS`, `FOOD_COLLISION_DISTANCE`); the only short names are `x` and `y` in tiny comprehensions. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `python -m ruff check src tests` and `python -m ruff format --check src tests` exit 0 with the selection E, F, W, I, N, UP, B, SIM; no `noqa`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every test function is annotated `-> None`; `constants.py` holds `Final[...]` annotated values. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | The changed files contain no exception handling. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No function has a default argument and no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | The changed files open no file. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | `constants.py` has a Doxygen `##` comment for every constant; the module and the package have docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | The changed files neither log nor print. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No class exists in these files; the classes of later milestones have no Design Class Diagram, a deviation recorded here: the project is a learning project of this size, and the classes trace to the lectures and to the base. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_constants.py` has 27 tests named for the value they fix; none depends on order or the network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `python -m mypy` runs with `strict = true` and reports no issues; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; the `dev` extra declares pytest, ruff and mypy with lower bounds, and all three are used. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Every value of the lectures is defined once, in `constants.py`; the tests read it from there. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `constants.py` imports only `typing.Final`; no import cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | A module of constants has one reason to change; there is no class to extend. |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable. Assessed on 2026-10-13 by the assistant that wrote the code, as stand-in for S01 in autonomous mode. Mode: autonomous, not independent. The pull request is the second look.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this `Go` in the run summary or on the pull request if the stand-in decision is not wanted | S01 | 2026-10-20 |

---

[MIL-001]: ../../milestones/mil-001-project-foundation.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[61d6df7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/61d6df778418312a964b8dba879177c201d28eaf
