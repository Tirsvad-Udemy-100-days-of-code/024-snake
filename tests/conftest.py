"""Shared pytest configuration for the snake game tests."""

from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def isolated_working_directory(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Run every test in an empty temporary working directory.

    The high score file has a relative default path (`data.txt`). Without this
    fixture, a test that uses the default would read and write the real file of
    the repository or of the directory pytest was started from.
    """
    monkeypatch.chdir(tmp_path)
