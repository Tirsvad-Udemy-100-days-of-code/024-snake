## @file constants.py
#  @brief Constants of the snake game.
#
#  Every value that the day-20, day-21 and day-24 lectures fix lives here, so
#  that no other module contains a magic number. The turtle coordinate system
#  has its centre at (0, 0); the 600 by 600 screen therefore reaches from -300
#  to 300 on both axes. A direction is a turtle heading in degrees: 0 points
#  right and the angle grows counter-clockwise.

"""Constants of the snake game, as fixed by the day-20, day-21 and day-24 lectures."""

from typing import Final

## @brief Width of the screen in pixels.
SCREEN_WIDTH: Final[int] = 600

## @brief Height of the screen in pixels.
SCREEN_HEIGHT: Final[int] = 600

## @brief Background colour of the screen.
SCREEN_BACKGROUND_COLOR: Final[str] = "black"

## @brief Title of the game window.
SCREEN_TITLE: Final[str] = "My Snake Game"

## @brief Shape of every body segment of the snake; the head has `HEAD_SHAPE`.
SEGMENT_SHAPE: Final[str] = "square"

## @brief Colour of every body segment, that is every segment behind the head.
BODY_COLOR: Final[str] = "light green"

## @brief Colour of the head of the snake.
HEAD_COLOR: Final[str] = "dark green"

## @brief Name under which the shape of the head is registered with the screen.
HEAD_SHAPE: Final[str] = "snake_head"

## @brief Outline of the head: a 20 by 20 pixel square, as the corners (x, y).
#
#  These are turtle shape coordinates: the front of the shape is the positive y
#  direction, which a turtle with heading 0 draws pointing right.
HEAD_OUTLINE: Final[tuple[tuple[int, int], ...]] = (
    (-10, -10),
    (-10, 10),
    (10, 10),
    (10, -10),
)

## @brief Outline of the mouth: a wedge cut into the middle of the front edge.
#
#  It is 12 pixels wide at the edge and 8 pixels deep, in the same shape
#  coordinates as `HEAD_OUTLINE`.
MOUTH_OUTLINE: Final[tuple[tuple[int, int], ...]] = ((-6, 10), (0, 2), (6, 10))

## @brief Colour of the mouth: the background colour, so that it looks cut out.
MOUTH_COLOR: Final[str] = "black"

## @brief Where the segments are drawn when the game starts, from head to tail.
#
#  The positions lie on one row, 20 pixels apart, which is the width of a
#  default turtle square, so the segments touch without overlapping.
STARTING_POSITIONS: Final[tuple[tuple[int, int], ...]] = ((0, 0), (-20, 0), (-40, 0))

## @brief Distance in pixels that the head moves in one move.
MOVE_DISTANCE: Final[int] = 20

## @brief Direction up, as a turtle heading in degrees.
UP: Final[int] = 90

## @brief Direction down, as a turtle heading in degrees.
DOWN: Final[int] = 270

## @brief Direction left, as a turtle heading in degrees.
LEFT: Final[int] = 180

## @brief Direction right, as a turtle heading in degrees.
RIGHT: Final[int] = 0

## @brief Wait in seconds between two moves.
REFRESH_DELAY_SECONDS: Final[float] = 0.1

## @brief Shape of the food.
FOOD_SHAPE: Final[str] = "circle"

## @brief Stretch factor of the food in both directions; 0.5 is half a default turtle.
FOOD_SIZE: Final[float] = 0.5

## @brief Colour of the food.
FOOD_COLOR: Final[str] = "blue"

## @brief Speed of the food; `fastest` switches its animation off.
FOOD_SPEED: Final[str] = "fastest"

## @brief How far from the centre the wall is, on every side, in pixels.
#
#  The head must stay inside it, and the food is shown inside it.
WALL_LIMIT: Final[int] = 280

## @brief The snake eats the food when the head is closer to it than this, in pixels.
FOOD_COLLISION_DISTANCE: Final[int] = 15

## @brief Text in front of the score on the scoreboard.
SCORE_LABEL: Final[str] = "Score: "

## @brief Colour of the scoreboard text.
SCOREBOARD_COLOR: Final[str] = "white"

## @brief Where the scoreboard text is written: the top centre of the screen.
SCOREBOARD_POSITION: Final[tuple[int, int]] = (0, 270)

## @brief Alignment of the scoreboard text around its position.
SCOREBOARD_ALIGNMENT: Final[str] = "center"

## @brief Font of the scoreboard text: family, size and style.
SCOREBOARD_FONT: Final[tuple[str, int, str]] = ("Arial", 24, "normal")

## @brief The head touches the tail when it is closer to a segment than this, in pixels.
TAIL_COLLISION_DISTANCE: Final[int] = 10

## @brief Text in front of the high score on the scoreboard.
#
#  The scoreboard writes `Score: <score> High Score: <high_score>`: the score
#  label, the score, a space, this label and the high score.
HIGH_SCORE_LABEL: Final[str] = "High Score: "

## @brief Where a segment of the old snake is sent when the snake is reset.
#
#  The place is far outside the 600 by 600 screen, so the old segments are out
#  of sight, as the day-24 lecture does it.
SEGMENT_PARKING_POSITION: Final[tuple[int, int]] = (1000, 1000)

## @brief Name of the text file that keeps the high score between games.
#
#  A relative path: the file lies in the working directory the game is started
#  from. The file is not tracked by git.
HIGH_SCORE_FILE: Final[str] = "data.txt"

## @brief Text encoding used to read and write the high score file.
HIGH_SCORE_FILE_ENCODING: Final[str] = "utf-8"

## @brief The high score of a new game, and of a file that cannot be read.
DEFAULT_HIGH_SCORE: Final[int] = 0
