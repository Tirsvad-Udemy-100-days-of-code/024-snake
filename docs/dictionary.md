# Domain Dictionary: Snake Game (Day 24)

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-003 (Go) | [e004c34] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the term screenshot; reviewed in RC-016 (Go) | [988ebba] |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional information technology (IT) term. PO language: `en` (domain `it`), from the registry's `Languages` section. The PO terms are the words of the lectures of days 20, 21 and 24 as the planning documents use them; the IT terms are the names in the code. The dictionary covers the vocabulary of the game; it exists so that the planning documents use one word for one thing and so that S02 can find the lectures' names in the code. It is adopted from the dictionary of [021-snake-game] and gains the terms high score, reset, continuous play, data file, read, write, mode and `with`, which the day-24 lectures introduce.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| window | en | Tk window | The desktop window that holds the screen and is opened when the game starts. | BC, SA, PP, MIL | PY |
| screen | en | `Screen` | The drawing area that the game sets up (size, colour, title) and on which the snake is shown. | BC, SA, PP, MIL | PY |
| snake | en | `Snake` | The creature the player steers, made of segments. | BC, SA, PP, MIL | PY |
| segment | en | `Turtle` | One square of the snake: light green in the body, dark green with a mouth in the head. | BC, SA, PP, MIL | PY |
| head | en | `head` | The first segment, which leads the snake and is turned by the arrow keys. | BC, SA, PP, MIL | PY |
| tail | en | `segments[1:]` | Every segment behind the head; the snake is reset when the head touches one of them. | BC, SA, PP, MIL | PY |
| body | en | `segments` | All segments of the snake, the head included, in order, the head first. | BC, SA, PP, MIL | PY |
| starting position | en | `STARTING_POSITIONS` | One of the three places at which a segment is drawn when the game starts and after a reset. | BC, MIL | PY |
| move | en | `move` | One pass in which each segment takes the place of the one before it and the head goes forward by the move distance. | BC, SA, PP, MIL | PY |
| direction | en | `heading` | The way the head points: up, down, left or right. | BC, SA, PP, MIL | PY |
| reversal | en | opposite heading | A turn by 180 degrees, so that the head would run into the segment behind it. | BC, SA, PP, MIL | PY |
| arrow key | en | key name `"Up"`, `"Down"`, `"Left"`, `"Right"` | One of the four keys with which the player turns the head. | BC, SA, PP, MIL | PY |
| animation loop | en | `while game_is_on` loop | The loop that refreshes the screen, waits and makes one move, again and again. | BC, PP, MIL | PY |
| food | en | `Food` | The small blue circle that the snake eats; it is shown at a random place. | BC, SA, PP, MIL | PY |
| refresh | en | `refresh` | The food moves to a new random place; it happens when the game starts and every time the food is eaten. | BC, SA, MIL | PY |
| eat | en | `FOOD_COLLISION_DISTANCE` | The head comes closer to the food than this distance, which makes the snake grow and the score rise. | BC, MIL | PY |
| grow | en | `extend` | The snake gets one more segment, at the place where its last segment is. | BC, SA, MIL | PY |
| score | en | `score` | The number of foods the snake has eaten since the last reset. | BC, SA, PP, MIL | PY |
| high score | en | `high_score` | The largest score reached in any game so far; it is kept in the data file between games. | BC, SA, PP, MIL | PY |
| scoreboard | en | `Scoreboard` | The text at the top of the screen that shows the score and the high score. | BC, SA, MIL | PY |
| wall | en | `WALL_LIMIT` | The line on every side of the playing field, 280 pixels from the centre; the head must stay inside it. | BC, SA, PP, MIL | PY |
| touch | en | `TAIL_COLLISION_DISTANCE` | The head comes closer to a segment of the tail than this distance. | BC, MIL | PY |
| reset | en | `reset` | The snake and the score go back to their start, and the high score is kept or raised; it happens when the head passes the wall or touches the tail. | BC, SA, PP, MIL | PY |
| continuous play | en | main flow without `game_over` | The game goes on after a reset and does not stop until the window is closed. | BC, SA, PP, MIL | PY |
| data file | en | `HIGH_SCORE_FILE` (`data.txt`) | The text file that holds the high score between games. | BC, SA, PP, MIL | PY |
| read | en | `open` in mode `r`, then `read` | The game gets the high score from the data file as text and converts it to a whole number. | BC, PP, MIL | PY |
| write | en | `open` in mode `w`, then `write` | The game replaces the content of the data file with the new high score as text. | BC, PP, MIL | PY |
| inheritance | en | subclass of `Turtle` | A class takes over the attributes and methods of another class; `Food` and `Scoreboard` take over those of `Turtle`. | BC, SA, MIL | PY |
| screenshot | en | `docs/images/snake-score-5.png` | The picture of the running game window that the README and the wiki show. | BC, SA, PP, MIL | none |

## Rules

- The Business Case, Stakeholder Analysis, Project Plan and milestones use the PO term; the source code and its tests use the IT term. The other design artifacts (Domain Model, Operation Contract, Sequence Diagram, Design Class Diagram, ERD) do not exist in this project.
- One IT term per PO term and one PO term per IT term; no synonyms.
- The planning documents use British spelling (colour, centre); identifiers such as `color` follow the `turtle` module and the lectures.
- A code identifier written in backticks in a planning document is an IT term and is allowed there.
- "Game over" is a PO term of day 21 only; from day 24 the game does not end, and the planning documents use "reset" for what happens at the wall and at the tail.
- "Step" is not a PO term of the game. In the planning documents it means a step of the project (a task, a milestone), never a move of the snake.
- "Base" is not a PO term of the game. In the planning documents it means the finished `main` of [021-snake-game] that this project adopts, never a part of the game.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[021-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game
[e004c34]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/e004c34565839b38dc1e06c8a05baaa66ce9eb1d
[988ebba]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/024-snake/commit/988ebba060c1ec69728a7fa36b24bc70737096d8
