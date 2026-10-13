# Stakeholder Analysis: Snake Game (Day 24)

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [DICT-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-002 (Go) | pending |

---

## Purpose

This analysis names the people and groups who have a stake in the Snake Game (Day 24) project, a solution to the day-24 assignment of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*, and classifies each one on a power/interest grid so the project knows how closely to involve them. The stakeholder IDs (`S01` to `S03`) are the IDs every other artifact uses for owners, reviewers and RACI (Responsible, Accountable, Consulted, Informed) assignments. The terms follow the Domain Dictionary [DICT-001]. The method is the power/interest grid: the quadrant decides how often and with what deliverable a stakeholder is addressed.

The Product Owner stated S01, S02 and S03, the Power and Interest levels of S01, the quadrant of S01, and the deliverables of S02 and S03. The Power and Interest levels of S02 and S03 were not stated; they are proposed here, as in [021-snake-game], and are open for confirmation by the reviewer.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad (personal learning project) | HIGH | HIGH | Manage Closely | A correct, tested and documented solution of the assignment that is worth keeping and showing |
| S02 | Udemy coursists | Fellow course participants who share code and compare solutions | Udemy course community (external) | LOW | HIGH | Keep Informed | Readable, runnable code that uses the assignment's function names, with README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public (external) | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies to install |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** S01 decides scope, adopts and checks the code, and reviews every artifact, so power and interest are both high. S01 is author and reviewer of the same documents; no independent reviewer exists in this project (see the conflict table).
- **Keep Informed (S02):** S02 cannot change the scope or accept a deliverable, so power is low. They compare solutions with their own, so interest in the code's readability and in the way to run it is high. They need the code and the README, not a say in the plan.
- **Monitor (S03):** S03 arrive by chance, do not take part and cannot influence the project, so power and interest are low. Their first impression is the repository page, which is why description, topics, README and wiki are checked once.

## Primary Concerns and FURPS+ Mapping

FURPS+ stands for Functionality, Usability, Reliability, Performance, Supportability and the added constraints (design, implementation, interface, physical).

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | The game behaves as the day-24 lectures describe: the high score is shown, a collision resets and play continues, and the high score is kept in `data.txt` | Functionality |
| S01 | The day-21 behaviour is kept | Functionality |
| S01 | Behaviour, including the file handling, is proven by tests that run without a display and never touch the real high score | Reliability |
| S01 | Every step is a branch and a pull request, reviewed before the next | Supportability |
| S02 | The code is readable and keeps the assignment's names (`Snake`, `Food`, `Scoreboard`, `reset`, `high_score`, `update_scoreboard`, `increase_score`, `create_snake`, `add_segment`, `extend`, `up`, `down`, `left`, `right`, `segments`, `head`, `game_is_on`) | Usability |
| S02 | The README tells how to create the `.venv`, run the game and run the tests on their operating system | Usability |
| S03 | The repository page says what the project is, with description, topics, README and a wiki in English, Danish and Bahasa Melayu | Usability |
| S03 | Nothing must be installed to run the game apart from Python itself | Implementation (constraint) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Pull request review in the git host | Once per milestone | Pull request with `Closes #N` lines and the review record | Every milestone ([PP-001]) |
| S02 | README in the repository | Once, updated when the game changes | Set-up, run and test instructions per operating system | [MIL-001], completed in [MIL-005] |
| S03 | Repository description, topics and README | Once, updated when the game changes | Description, topics and README overview | [MIL-001], checked in [MIL-005] |
| S03 | Wiki of the repository | Once | Pages `Home`, `Home.da` and `Home.ms` with a short description, the controls and how to run it | [MIL-005] |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants plain code in the style of the lecture; S01 wants constants, tests, Doxygen comments and packaging, which add structure | S01, S02 | Keep the lecture's identifiers and flow; put the extra structure in separate places (`constants.py`, an injectable file path) so the main flow stays readable |
| S03 wants nothing to install; S01 needs pytest and Doxygen | S01, S03 | The project has no runtime dependencies; pytest is an optional `dev` extra and Doxygen is an optional documentation tool |
| S01 is author and reviewer, so a review is not independent | S01 | Use the QC checklists as the objective measure, record every review as an `RC-*` (marked `Mode: autonomous, not independent`), and treat the pull request as the second look; recorded as a plan risk in [PP-001] |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Game behaves as the day-24 lectures describe | [BC-001] objectives 2 to 6 |
| S01 | Day-21 behaviour is kept | [BC-001] objective 1 |
| S01 | Tests run without a display and never touch the real file | [BC-001] objective 9 |
| S01 | Every step is a branch and a pull request | [BC-001] objective 11 |
| S02 | Readable code with the assignment's names | [BC-001] objective 7 |
| S02 | README with run and test instructions | [BC-001] objectives 8 and 10 |
| S03 | Description, topics, README and wiki on the repository page | [BC-001] objective 12 |
| S03 | No runtime dependencies | [BC-001] objective 8 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Go in RC-002 (not independent; S01 can overrule) | 2026-10-13 |

---

[BC-001]: ./business-case.md
[DICT-001]: ./dictionary.md
[PP-001]: ./project-plan.md
[MIL-001]: ./milestones/mil-001-project-foundation.md
[MIL-005]: ./milestones/mil-005-wiki-and-finish.md
[021-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game
