"""! @file
@brief The scoreboard: the text at the top of the screen that shows the score.

The class follows the day-21 lecture on inheritance: `Scoreboard` is a `Turtle`
that writes text. Like `food`, this module needs `turtle` when it is imported;
the game imports it only when it starts, and the tests install a fake `turtle`
module first.
"""

from turtle import Turtle

from snake_game.constants import (
    HIGH_SCORE_FILE,
    HIGH_SCORE_LABEL,
    SCORE_LABEL,
    SCOREBOARD_ALIGNMENT,
    SCOREBOARD_COLOR,
    SCOREBOARD_FONT,
    SCOREBOARD_POSITION,
)
from snake_game.high_score_file import read_high_score, write_high_score


class Scoreboard(Turtle):
    """! @brief Shows the score as text at the top centre of the screen."""

    def __init__(self, path: str = HIGH_SCORE_FILE) -> None:
        """! @brief Set the scoreboard up and write the score 0 and the stored best.

        @param path The file that keeps the high score; defaults to
            `HIGH_SCORE_FILE`.
        """
        super().__init__()
        ## @brief The file that keeps the high score between games.
        self.path = path
        ## @brief The number of foods the snake has eaten since the last reset.
        self.score = 0
        ## @brief The largest score reached so far, as stored in the file.
        self.high_score = read_high_score(path)
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """! @brief Wipe the old text and write the score and the high score."""
        self.clear()
        self.write(
            f"{SCORE_LABEL}{self.score} {HIGH_SCORE_LABEL}{self.high_score}",
            align=SCOREBOARD_ALIGNMENT,
            font=SCOREBOARD_FONT,
        )

    def increase_score(self) -> None:
        """! @brief Add 1 to the score and write it."""
        self.score += 1
        self.update_scoreboard()

    def reset(self) -> None:
        """! @brief Keep the best score, start a new game and write the scoreboard.

        When the score is higher than the high score, it becomes the new high
        score and is written to the file; a lower or equal score does not write
        the file. The score then goes back to 0.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            write_high_score(self.high_score, self.path)
        self.score = 0
        self.update_scoreboard()
