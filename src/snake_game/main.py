"""! @file
@brief The main flow of the game: set up the screen, draw the snake and run it.

The flow follows the lectures "Screen Setup and Creating a Snake Body",
"Animating the Snake Segments on Screen" and "Controlling the Snake with
Keypresses", the day-21 steps in which the snake eats food and the score rises,
and the day-24 steps in which a collision resets the game and it goes on.
"""

import time
from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol

from snake_game.constants import (
    FOOD_COLLISION_DISTANCE,
    HEAD_COLOR,
    HEAD_OUTLINE,
    HEAD_SHAPE,
    MOUTH_COLOR,
    MOUTH_OUTLINE,
    REFRESH_DELAY_SECONDS,
    SCREEN_BACKGROUND_COLOR,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
)
from snake_game.snake import Snake

if TYPE_CHECKING:  # for the annotation only: nothing is imported when running
    from turtle import Shape


class ScreenLike(Protocol):
    """! @brief What the helper functions need from the screen.

    A `turtle.Screen` fits this description, and so does a fake in a test.
    """

    def setup(self, width: float, height: float) -> None:
        """! @brief Set the size of the window.

        @param width Width in pixels.
        @param height Height in pixels.
        """
        ...

    def bgcolor(self, color: str, /) -> None:
        """! @brief Set the background colour.

        @param color Name of the colour, for example `black`.
        """
        ...

    def title(self, titlestring: str, /) -> None:
        """! @brief Set the title of the window.

        @param titlestring The title.
        """
        ...

    def register_shape(self, name: str, shape: "Shape", /) -> None:
        """! @brief Make a shape known under a name, so that a turtle can use it.

        @param name The name of the shape.
        @param shape The shape to register.
        """
        ...

    def update(self) -> None:
        """! @brief Draw everything that has changed since the last update."""
        ...

    def listen(self) -> None:
        """! @brief Make the screen receive the key presses."""
        ...

    def onkey(self, fun: Callable[[], object], key: str) -> None:
        """! @brief Call a function when a key is pressed.

        @param fun The function to call.
        @param key Name of the key, for example `Up`.
        """
        ...


class FoodLike(Protocol):
    """! @brief What `eat_food_if_close` needs from the food.

    A `Food` fits this description, and so does a fake in a test.
    """

    def refresh(self) -> None:
        """! @brief Move the food to a new random place."""
        ...

    def position(self) -> tuple[float, float]:
        """! @brief Tell where the food is.

        @return The x and y coordinates.
        """
        ...


class ScoreboardLike(Protocol):
    """! @brief What the eating and reset checks need from the scoreboard.

    A `Scoreboard` fits this description, and so does a fake in a test.
    """

    def increase_score(self) -> None:
        """! @brief Add 1 to the score and write it."""
        ...

    def reset(self) -> None:
        """! @brief Keep the best score and start the score again at 0."""
        ...


def configure_screen(screen: ScreenLike) -> None:
    """! @brief Give the screen the size, background colour and title of the game.

    @param screen The screen to set up.
    """
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BACKGROUND_COLOR)
    screen.title(SCREEN_TITLE)


def register_head_shape(screen: ScreenLike) -> None:
    """! @brief Build the shape of the head and register it as `HEAD_SHAPE`.

    The shape is compound: the head outline in `HEAD_COLOR` and, on top of it, the
    mouth in `MOUTH_COLOR`. Turtle shape coordinates have their front in the
    positive y direction, which is what the constants use, so the mouth turns with
    the head and no conversion is needed.

    `turtle.Shape` is imported here and not at the top of the module, so that
    importing this module needs neither a display nor `tkinter`.

    @param screen The screen that learns the shape.
    """
    from turtle import Shape

    shape = Shape("compound")
    shape.addcomponent(HEAD_OUTLINE, HEAD_COLOR)
    shape.addcomponent(MOUTH_OUTLINE, MOUTH_COLOR)
    screen.register_shape(HEAD_SHAPE, shape)


def bind_keys(screen: ScreenLike, snake: Snake) -> None:
    """! @brief Turn the snake with the arrow keys.

    @param screen The screen that receives the key presses.
    @param snake The snake to steer.
    """
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def play_frame(screen: ScreenLike, snake: Snake) -> None:
    """! @brief Show the snake, wait for `REFRESH_DELAY_SECONDS`, then move it.

    This is one pass of the animation loop. The screen is updated by hand because
    automatic drawing is off, so the whole snake appears at once.

    @param screen The screen to update.
    @param snake The snake to move.
    """
    screen.update()
    time.sleep(REFRESH_DELAY_SECONDS)
    snake.move()


def eat_food_if_close(snake: Snake, food: FoodLike, scoreboard: ScoreboardLike) -> None:
    """! @brief Let the snake eat the food when the head is close enough to it.

    Eating moves the food to a new place, makes the snake one segment longer and
    adds 1 to the score. The head must be closer than `FOOD_COLLISION_DISTANCE`.

    @param snake The snake.
    @param food The food.
    @param scoreboard The scoreboard that shows the score.
    """
    if snake.head.distance(food.position()) < FOOD_COLLISION_DISTANCE:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


def reset_if_collision(snake: Snake, scoreboard: ScoreboardLike) -> bool:
    """! @brief Start again when the head passes the wall or touches the tail.

    The game does not end: the scoreboard keeps the best score and starts the
    score again, and the snake is made again at the starting positions.

    @param snake The snake.
    @param scoreboard The scoreboard that keeps the high score.
    @return True when the snake and the score were reset.
    """
    if snake.hits_wall() or snake.hits_tail():
        scoreboard.reset()
        snake.reset()
        return True
    return False


def main() -> None:
    """! @brief Open the game window and run the snake until the window is closed.

    Closing the window during the animation loop makes `screen.update()` raise
    `tkinter.TclError` ("invalid command name"), and `turtle` raises
    `turtle.Terminator` in some other calls once its window is gone. Both mean
    "the player closed the window", so the game ends quietly with exit code 0.
    When the snake passes the wall or touches its tail the score and the snake are
    reset and the game goes on, so the loop runs until the window is closed.

    `turtle` and `tkinter` are imported here and not at the top of the module, and
    so are `food` and `scoreboard`, whose classes inherit from `Turtle`: importing
    this module needs neither a display nor `tkinter`.
    """
    from tkinter import TclError
    from turtle import Screen, Terminator

    from snake_game.food import Food
    from snake_game.scoreboard import Scoreboard

    screen = Screen()
    configure_screen(screen)
    screen.tracer(0)
    register_head_shape(screen)
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    bind_keys(screen, snake)

    game_is_on = True
    try:
        while game_is_on:
            play_frame(screen, snake)
            eat_food_if_close(snake, food, scoreboard)
            reset_if_collision(snake, scoreboard)
    except (Terminator, TclError):
        return  # the window was closed: there is nothing left to do
