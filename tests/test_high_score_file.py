"""Tests of reading and writing the high score file, with temporary files."""

from pathlib import Path

from snake_game.high_score_file import read_high_score, write_high_score


def test_read_returns_the_stored_number(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"
    path.write_text("17", encoding="utf-8")

    assert read_high_score(str(path)) == 17


def test_read_accepts_a_trailing_newline(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"
    path.write_text("5\n", encoding="utf-8")

    assert read_high_score(str(path)) == 5


def test_read_creates_a_missing_file_holding_0(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"

    assert read_high_score(str(path)) == 0
    assert path.read_text(encoding="utf-8") == "0"


def test_read_gives_0_for_an_empty_file_and_leaves_it_empty(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"
    path.write_text("", encoding="utf-8")

    assert read_high_score(str(path)) == 0
    assert path.read_text(encoding="utf-8") == ""


def test_read_gives_0_for_text_that_is_not_a_whole_number(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"
    path.write_text("many", encoding="utf-8")

    assert read_high_score(str(path)) == 0
    assert path.read_text(encoding="utf-8") == "many"


def test_read_gives_0_for_a_negative_number(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"
    path.write_text("-4", encoding="utf-8")

    assert read_high_score(str(path)) == 0
    assert path.read_text(encoding="utf-8") == "-4"


def test_read_gives_0_for_bytes_that_are_not_utf_8(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"
    path.write_bytes(b"\xff\xfe\x00\x80")

    assert read_high_score(str(path)) == 0
    assert path.read_bytes() == b"\xff\xfe\x00\x80"


def test_write_replaces_the_old_content(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"
    path.write_text("123456", encoding="utf-8")

    write_high_score(9, str(path))

    assert path.read_text(encoding="utf-8") == "9"


def test_write_creates_the_file(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"

    write_high_score(3, str(path))

    assert path.read_text(encoding="utf-8") == "3"


def test_the_file_is_closed_after_reading_and_writing(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"

    write_high_score(2, str(path))
    read_high_score(str(path))
    path.unlink()  # fails on Windows while a handle is still open

    assert not path.exists()


def test_the_default_path_is_data_txt_in_the_working_directory(
    tmp_path: Path,
) -> None:
    write_high_score(4)

    assert (tmp_path / "data.txt").read_text(encoding="utf-8") == "4"
    assert read_high_score() == 4
