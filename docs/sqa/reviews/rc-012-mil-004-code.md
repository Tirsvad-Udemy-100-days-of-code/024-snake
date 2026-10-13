# RC-012: Code review of MIL-004 (high score file)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the source and tests that [MIL-004] delivers (high score file)
- Checklist used: [QC-PY-001]
- Scope: full review of the files changed on the branch of the milestone
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the assistant also wrote the code)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `read_high_score`, `write_high_score`, `high_score_file` and the constants `HIGH_SCORE_FILE`, `DEFAULT_HIGH_SCORE` follow PEP 8. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; `path`, `data` and `text` are the lecture's own and are used in short scopes. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` exit 0; no `noqa`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy` strict reports no issues in 16 files; every new def is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Only `FileNotFoundError`, `UnicodeDecodeError` and `ValueError` are caught, each with a defined result (create the file with 0 and return 0; read as 0); other `OSError`s propagate; none is swallowed without a defined result. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default argument; no shadowed builtin (`open` is called, not rebound). |
| 7 | Files, locks and connections are managed with context managers | Pass | Both functions use `with open(...) as data`, as the lecture teaches; a test checks that the file can be replaced afterwards. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Both functions, the module and the new constants have Doxygen docstrings; `doxygen Doxyfile` ends with 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists (deviation recorded in RC-010); `high_score_file.py` is a function module and `Scoreboard` gains a `path` and the two calls, as the lecture does with `data.txt`. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 169 tests; `test_high_score_file.py` covers stored, newline, missing, empty, non-numeric, negative, undecodable, replace and create; `conftest.py` runs every test in a temporary folder so no test touches a real `data.txt`; no test depends on order or the network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `strict = true`; no `Any` was added. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []` is unchanged. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The file name, encoding and the fallback value are defined once in `constants.py`; reading and writing the file live only in `high_score_file.py`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `high_score_file.py` imports only `constants`; `scoreboard.py` imports it; no cycle; the module needs no `turtle`. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Reading and writing are separate functions with one reason each; `Scoreboard` receives the path as a parameter, so tests pass a temporary file. |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable. Assessed on 2026-10-13 by the assistant that wrote the code, as stand-in for S01 in autonomous mode. Mode: autonomous, not independent. The pull request is the second look.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this `Go` in the run summary or on the pull request if the stand-in decision is not wanted | S01 | 2026-10-20 |

---

[MIL-004]: ../../milestones/mil-004-high-score-file.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
