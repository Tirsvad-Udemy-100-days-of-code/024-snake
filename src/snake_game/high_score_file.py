"""! @file
@brief Reading and writing the high score file: the day-24 file lectures.

The high score is kept as text in a file, so that it is still there the next time
the game is started. Both functions open the file with a `with` statement, which
closes it again even when something goes wrong, as the lecture teaches. The module
does not import `turtle`, so it needs no display and the tests use a temporary
file.
"""

from snake_game.constants import (
    DEFAULT_HIGH_SCORE,
    HIGH_SCORE_FILE,
    HIGH_SCORE_FILE_ENCODING,
)


def write_high_score(high_score: int, path: str = HIGH_SCORE_FILE) -> None:
    """! @brief Replace the content of the file with the high score, as text.

    The file is opened in write mode `w`, so the old content is overwritten and a
    file that does not exist yet is created.

    @param high_score The high score to store.
    @param path The file to write; defaults to `HIGH_SCORE_FILE`.
    """
    with open(path, mode="w", encoding=HIGH_SCORE_FILE_ENCODING) as data:
        data.write(str(high_score))


def read_high_score(path: str = HIGH_SCORE_FILE) -> int:
    """! @brief Read the high score from the file and turn the text into a number.

    A file that does not exist yet is created holding `DEFAULT_HIGH_SCORE`. A file
    that does not hold a whole number, or holds a negative one, is read as
    `DEFAULT_HIGH_SCORE` and is left as it is; the next new high score replaces it.

    @param path The file to read; defaults to `HIGH_SCORE_FILE`.
    @return The stored high score, 0 or more.
    """
    try:
        with open(path, encoding=HIGH_SCORE_FILE_ENCODING) as data:
            text = data.read()
    except FileNotFoundError:
        write_high_score(DEFAULT_HIGH_SCORE, path)
        return DEFAULT_HIGH_SCORE
    except UnicodeDecodeError:
        return DEFAULT_HIGH_SCORE
    try:
        high_score = int(text)
    except ValueError:
        return DEFAULT_HIGH_SCORE
    return max(high_score, DEFAULT_HIGH_SCORE)
