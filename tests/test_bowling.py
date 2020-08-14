# test_bowling.py

import pytest
from src.bowling import Game

# @pytest.fixture
# def xxx():
#   return b.xxx('')

@pytest.fixture
def empty_frames():
    return Game()

def test_default_initial_empty_frames(empty_frames):
    assert len(empty_frames.frames) == 0

