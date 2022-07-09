import pytest 
from .. import Board
from .fixtures import default_board

# Test setup
board = Board.Board()
@pytest.fixture(autouse=True)
def before_each():
    board.reset()
    yield

# Test for reset
def test_reset(default_board):
    board.put(1, 1, "P")
    board.reset()

    assert board._board == default_board

# Test for get
def test_get_empty():
    assert board.get(1, 1) == "e"

def test_get_nonempty():
    board._board[2][2] = "P"

    assert board.get(1, 1) == "e"
    assert board.get(2, 2) == "P"

def test_get_outofbounds():
    board.get(100, 100)

    # No error thrown
    assert True 

def test_put():
    board.put(5, 6, "Q")

    assert board._board[5][6] == "Q"

def test_put_outofbounds():
    board.put(100, 100, "ABC")

    # No error thrown
    assert True 
