import pytest
from .. import Game
import chess
from .fixtures import *

# Test setup
game = Game.Game()
@pytest.fixture(autouse=True)
def before_each():
    game.reset()
    yield

# Tests for check_legal_moves 
def test_check_legal_moves(a2_legal_moves, a2_legal_moves_control):
    for move in a2_legal_moves_control:
        if game.check_legal_moves(move.from_square, move.to_square) != a2_legal_moves:
            assert False

    assert True

def test_check_legal_moves(a2_legal_moves, a2_illegal_moves_control):
    for move in a2_illegal_moves_control:
        if game.check_legal_moves(move.from_square, move.to_square) == a2_legal_moves:
            assert False

    assert True


# Tests for reset
def test_reset():
    new_game = Game.Game()
    game.move(chess.B2, chess.B4)
    assert game.get_piece_map() != new_game.get_piece_map()

    game.reset()
    game.move(chess.B2, chess.B4)
    
    assert game.get_piece_map() != new_game.get_piece_map()

# Tests for get_piece_map
def test_get_piece_map(default_piece_map):
    assert game.get_piece_map() == default_piece_map

def test_get_piece_map_moved(moved_piece_map):
    game.move(chess.B2, chess.B4)
    assert game.get_piece_map() == moved_piece_map

# Tests for move 
def test_move_bishop(moved_bishop_piece_map):
    game.move(chess.D2, chess.D3)
    game.move(chess.C1, chess.H6)

    assert game.get_piece_map() == moved_bishop_piece_map

def test_move_multiple(multiple_moves_map):
    game.move(chess.E2, chess.E4)
    game.move(chess.E7, chess.E5)
    game.move(chess.G1, chess.G3)
    game.move(chess.F8, chess.A3)
    game.move(chess.E1, chess.E2)
    game.move(chess.E2, chess.D3)
    game.move(chess.F3, chess.G5)

    assert game.get_piece_map() == multiple_moves_map

def test_bad_move(default_piece_map):
    game.move(chess.H1, chess.C6)

    assert game.get_piece_map() == default_piece_map


def test_move_capture(captured_piece_map):
    game.move(chess.B2, chess.B4)
    game.move(chess.C7, chess.C5)
    game.move(chess.B4, chess.C5)

    assert game.get_piece_map() == captured_piece_map

def test_first_move(moved_piece_map):
    #Move the black pawn out of turn(should do nothing)
    game.move(chess.E8, chess.E5)

    #Move white pawn
    game.move(chess.B2, chess.B4)

    assert game.get_piece_map() == moved_piece_map

def test_promote_pawn():
    #TODO
    assert True

# Tests for check_endgames
def test_check_endgames_checkmate():
    game.set_board("3b1q1q/1N2PRQ1/rR3KBr/B4PP1/2Pk1r1b/1P2P1N1/2P2P2/8 b - -")
    
    assert game.check_endgames() == 1

def test_check_endgames_stalemate():
    game.set_board("8/8/5k2/8/8/1q6/8/K7 w - - 0 1")
    print(game.get_piece_map())
    assert game.check_endgames() == 2 

def test_check_endgames_insufficient_material():
    game.set_board('7k/5K2/8/8/8/8/8/8 w - - 0 1')
    assert game.check_endgames() == 2

def test_check_endgames_none():
    assert game.check_endgames() == 0
