"""Tests of the main flow, with fakes instead of a real screen."""

import pytest

from fakes import (
    FakeFood,
    FakeScoreboard,
    FakeScreen,
    FakeShape,
    FakeTclError,
    FakeTerminatorError,
    imports_turtle_or_tkinter,
    install_fake_turtle,
    make_snake,
    script_randint,
)
from snake_game import constants
from snake_game import snake as snake_module
from snake_game.main import (
    bind_keys,
    configure_screen,
    eat_food_if_close,
    main,
    play_frame,
    register_head_shape,
    reset_if_collision,
)
from snake_game.snake import Snake

ARROW_KEYS = ("Up", "Down", "Left", "Right")


@pytest.fixture(autouse=True)
def food_far_away(monkeypatch: pytest.MonkeyPatch) -> None:
    """Make the food appear at the top right corner of the wall, far from the snake."""
    script_randint(monkeypatch, [])


@pytest.fixture
def sleeps(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Replace `time.sleep` for one test and collect the waits requested."""
    waited: list[float] = []
    monkeypatch.setattr("time.sleep", waited.append)
    return waited


def test_configure_screen_sets_size_background_and_title_and_nothing_else() -> None:
    screen = FakeScreen()

    configure_screen(screen)

    assert screen.calls == [
        ("setup", (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)),
        ("bgcolor", (constants.SCREEN_BACKGROUND_COLOR,)),
        ("title", (constants.SCREEN_TITLE,)),
    ]


def test_bind_keys_listens_and_binds_the_four_arrow_keys_to_the_snake() -> None:
    screen = FakeScreen()
    snake, _ = make_snake()

    bind_keys(screen, snake)

    assert screen.call_names() == ["listen", "onkey", "onkey", "onkey", "onkey"]
    assert screen.bindings == {
        "Up": snake.up,
        "Down": snake.down,
        "Left": snake.left,
        "Right": snake.right,
    }


@pytest.mark.parametrize(
    ("key", "degrees"),
    [("Up", constants.UP), ("Down", constants.DOWN), ("Right", constants.RIGHT)],
)
def test_pressing_a_bound_key_turns_the_head(key: str, degrees: int) -> None:
    screen = FakeScreen()
    snake, _ = make_snake()
    bind_keys(screen, snake)

    screen.bindings[key]()

    assert snake.head.heading() == degrees


def test_play_frame_updates_the_screen_then_waits_then_moves(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    screen = FakeScreen(frames_before_close=1)
    snake, created = make_snake()
    seen: list[tuple[float, list[str], list[str]]] = []

    def record_sleep(seconds: float) -> None:
        seen.append((seconds, screen.call_names(), created[0].call_names()))

    monkeypatch.setattr("time.sleep", record_sleep)

    play_frame(screen, snake)

    assert len(seen) == 1
    seconds, screen_calls_at_sleep, head_calls_at_sleep = seen[0]
    assert seconds == constants.REFRESH_DELAY_SECONDS
    assert screen_calls_at_sleep == ["update"]
    assert "forward" not in head_calls_at_sleep
    assert "forward" in created[0].call_names()


def test_main_sets_up_the_screen_turns_off_drawing_and_binds_the_keys(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    _, screens = install_fake_turtle(monkeypatch)

    main()

    assert len(screens) == 1
    assert screens[0].call_names()[:10] == [
        "setup",
        "bgcolor",
        "title",
        "tracer",
        "register_shape",
        "listen",
        "onkey",
        "onkey",
        "onkey",
        "onkey",
    ]
    assert ("tracer", (0,)) in screens[0].calls
    assert sorted(screens[0].bindings) == sorted(ARROW_KEYS)


def test_register_head_shape_builds_two_components_from_the_constants(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    install_fake_turtle(monkeypatch)
    screen = FakeScreen()

    register_head_shape(screen)  # the fake `Shape` is installed above

    ((_, (shape_name, shape)),) = [
        call for call in screen.calls if call[0] == "register_shape"
    ]
    assert isinstance(shape, FakeShape)
    assert shape_name == constants.HEAD_SHAPE
    assert shape.type == "compound"
    assert shape.components == [
        (constants.HEAD_OUTLINE, constants.HEAD_COLOR, None),
        (constants.MOUTH_OUTLINE, constants.MOUTH_COLOR, None),
    ]


def test_main_registers_the_head_shape_once_before_the_snake_is_made(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    turtles, screens = install_fake_turtle(monkeypatch)
    registered_when_snake_made: list[bool] = []
    real_snake = snake_module.Snake

    def spying_snake() -> Snake:
        registered_when_snake_made.append("register_shape" in screens[0].call_names())
        return real_snake()

    monkeypatch.setattr("snake_game.main.Snake", spying_snake)

    main()

    registrations = [c for c in screens[0].calls if c[0] == "register_shape"]
    assert len(registrations) == 1
    assert registrations[0][1][0] == constants.HEAD_SHAPE
    assert registered_when_snake_made == [True]
    assert ("shape", (constants.HEAD_SHAPE,)) in turtles[0].calls


def test_main_draws_the_snake_before_the_first_frame(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    turtles, _ = install_fake_turtle(monkeypatch)

    main()

    snake_segments = turtles[: len(constants.STARTING_POSITIONS)]
    assert len(turtles) == len(constants.STARTING_POSITIONS) + 2  # food, scoreboard
    assert all(
        ("goto", position) in turtle.calls
        for turtle, position in zip(
            snake_segments, constants.STARTING_POSITIONS, strict=True
        )
    )


@pytest.mark.parametrize("closing_error", [FakeTerminatorError, FakeTclError])
def test_main_ends_quietly_when_the_window_is_closed(
    monkeypatch: pytest.MonkeyPatch,
    sleeps: list[float],
    closing_error: type[Exception],
) -> None:
    turtles, screens = install_fake_turtle(
        monkeypatch, frames_before_close=3, closing_error=closing_error
    )

    main()

    assert screens[0].call_names().count("update") == 3 + 1
    assert turtles[0].call_names().count("forward") == 3
    assert sleeps == [constants.REFRESH_DELAY_SECONDS] * 3
    assert "exitonclick" not in screens[0].call_names()


def test_main_lets_other_errors_through(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    install_fake_turtle(monkeypatch, closing_error=KeyError)

    with pytest.raises(KeyError):
        main()


def test_the_snake_eats_food_closer_than_the_eating_distance() -> None:
    snake, created = make_snake()
    food = FakeFood(constants.FOOD_COLLISION_DISTANCE - 1, 0)
    scoreboard = FakeScoreboard()

    eat_food_if_close(snake, food, scoreboard)

    assert food.refreshes == 1
    assert scoreboard.increases == 1
    assert len(snake.segments) == len(created) == len(constants.STARTING_POSITIONS) + 1


@pytest.mark.parametrize(
    "place",
    [
        (constants.FOOD_COLLISION_DISTANCE, 0),
        (0, -constants.FOOD_COLLISION_DISTANCE),
        (2 * constants.FOOD_COLLISION_DISTANCE, 0),
        (200, 200),
    ],
)
def test_the_snake_does_not_eat_food_at_or_beyond_the_eating_distance(
    place: tuple[int, int],
) -> None:
    snake, _ = make_snake()
    food = FakeFood(*place)
    scoreboard = FakeScoreboard()

    eat_food_if_close(snake, food, scoreboard)

    assert food.refreshes == 0
    assert scoreboard.increases == 0
    assert len(snake.segments) == len(constants.STARTING_POSITIONS)


def test_the_snake_eats_food_that_is_close_diagonally() -> None:
    snake, _ = make_snake()
    food = FakeFood(10, 10)  # a distance of about 14.1
    scoreboard = FakeScoreboard()

    eat_food_if_close(snake, food, scoreboard)

    assert scoreboard.increases == 1


def test_main_lets_the_snake_eat_the_food_that_lies_on_its_way(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    script_randint(monkeypatch, [20, 0])  # the first food lies one move ahead
    turtles, _ = install_fake_turtle(monkeypatch, frames_before_close=1)

    main()

    snake_head, _, _, food, scoreboard, new_segment = turtles
    assert snake_head.position() == (20, 0)
    assert [call for call in food.calls if call[0] == "goto"] == [
        ("goto", (20, 0)),
        ("goto", (constants.WALL_LIMIT, constants.WALL_LIMIT)),
    ]
    assert scoreboard.calls[-1][1][0] == "Score: 1 High Score: 0"
    assert new_segment.position() == (-20, 0)  # where the last segment was


def test_main_does_not_raise_the_score_when_the_food_is_far_away(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    turtles, _ = install_fake_turtle(monkeypatch, frames_before_close=3)

    main()

    scoreboard = turtles[4]
    assert scoreboard.calls[-1][1][0] == "Score: 0 High Score: 0"
    assert len(turtles) == len(constants.STARTING_POSITIONS) + 2


def test_nothing_is_reset_while_the_snake_is_inside_and_clear_of_its_tail() -> None:
    snake, created = make_snake()
    scoreboard = FakeScoreboard()

    assert not reset_if_collision(snake, scoreboard)
    assert scoreboard.resets == 0
    assert len(created) == len(constants.STARTING_POSITIONS)


def test_the_game_is_reset_when_the_head_passes_the_wall() -> None:
    snake, created = make_snake()
    snake.head.goto(constants.WALL_LIMIT + 1, 0)
    scoreboard = FakeScoreboard()

    assert reset_if_collision(snake, scoreboard)
    assert scoreboard.resets == 1
    assert len(created) == 2 * len(constants.STARTING_POSITIONS)


def test_the_game_is_reset_when_the_head_touches_the_tail() -> None:
    snake, created = make_snake()
    created[1].goto(3, 4)
    scoreboard = FakeScoreboard()

    assert reset_if_collision(snake, scoreboard)
    assert scoreboard.resets == 1
    assert snake.head is not created[0]


def test_main_goes_on_after_the_wall_with_a_new_snake_and_no_game_over(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    moves_to_pass_the_wall = constants.WALL_LIMIT // constants.MOVE_DISTANCE + 1
    turtles, screens = install_fake_turtle(
        monkeypatch, frames_before_close=moves_to_pass_the_wall + 2
    )

    main()

    old_head, scoreboard = turtles[0], turtles[4]
    new_head = turtles[5]
    written = [call[1][0] for call in scoreboard.calls if call[0] == "write"]
    assert old_head.position() == constants.SEGMENT_PARKING_POSITION
    assert new_head.call_names().count("forward") == 2
    assert new_head.position() == (2 * constants.MOVE_DISTANCE, 0)
    assert scoreboard.calls[-1] == (
        "write",
        ("Score: 0 High Score: 0", "center", ("Arial", 24, "normal")),
    )
    assert "GAME OVER" not in written
    assert "exitonclick" not in screens[0].call_names()


def test_main_shows_the_best_score_after_a_reset(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    script_randint(monkeypatch, [20, 0])  # the first food lies one move ahead
    moves_to_pass_the_wall = constants.WALL_LIMIT // constants.MOVE_DISTANCE + 1
    turtles, _ = install_fake_turtle(
        monkeypatch, frames_before_close=moves_to_pass_the_wall
    )

    main()

    scoreboard = turtles[4]
    assert scoreboard.calls[-1][1][0] == "Score: 0 High Score: 1"


def test_main_resets_when_the_snake_touches_its_tail(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    monkeypatch.setattr("snake_game.snake.Snake.hits_tail", lambda self: True)
    turtles, screens = install_fake_turtle(monkeypatch, frames_before_close=2)

    main()

    assert turtles[0].call_names().count("forward") == 1
    assert turtles[0].position() == constants.SEGMENT_PARKING_POSITION
    assert "exitonclick" not in screens[0].call_names()


@pytest.mark.parametrize("closing_error", [FakeTerminatorError, FakeTclError])
def test_main_ends_quietly_when_the_window_is_closed_after_a_reset(
    monkeypatch: pytest.MonkeyPatch,
    sleeps: list[float],
    closing_error: type[Exception],
) -> None:
    moves_to_pass_the_wall = constants.WALL_LIMIT // constants.MOVE_DISTANCE + 1
    turtles, screens = install_fake_turtle(
        monkeypatch,
        frames_before_close=moves_to_pass_the_wall,
        closing_error=closing_error,
    )

    main()

    assert turtles[4].calls[-1][1][0] == "Score: 0 High Score: 0"
    assert "exitonclick" not in screens[0].call_names()


def test_importing_the_main_module_does_not_import_turtle_or_tkinter() -> None:
    assert not imports_turtle_or_tkinter("snake_game.main")
