import pytest
import chess
from chess import Piece, Move
from .. import Game

@pytest.fixture
def a2_legal_moves():
    g = Game.Game()
    return g.check_legal_moves(chess.A2, chess.A3)

@pytest.fixture
def a2_legal_moves_control():
    return [Move(chess.A2, chess.A3), chess.Move(chess.A2, chess.A4)]

@pytest.fixture
def a2_illegal_moves_control():
    return [chess.Move(chess.A2, chess.A6), chess.Move(chess.A2, chess.A2)]

@pytest.fixture
def default_piece_map():
    return {63: Piece.from_symbol('r'), 62: Piece.from_symbol('n'), 61: Piece.from_symbol('b'), 60: Piece.from_symbol('k'), 59: Piece.from_symbol('q'), 58: Piece.from_symbol('b'), 57: Piece.from_symbol('n'), 56: Piece.from_symbol('r'), 55: Piece.from_symbol('p'), 54: Piece.from_symbol('p'), 53: Piece.from_symbol('p'), 52: Piece.from_symbol('p'), 51: Piece.from_symbol('p'), 50: Piece.from_symbol('p'), 49: Piece.from_symbol('p'), 48: Piece.from_symbol('p'), 15: Piece.from_symbol('P'), 14: Piece.from_symbol('P'), 13: Piece.from_symbol('P'), 12: Piece.from_symbol('P'), 11: Piece.from_symbol('P'), 10: Piece.from_symbol('P'), 9: Piece.from_symbol('P'), 8: Piece.from_symbol('P'), 7: Piece.from_symbol('R'), 6: Piece.from_symbol('N'), 5: Piece.from_symbol('B'), 4: Piece.from_symbol('K'), 3: Piece.from_symbol('Q'), 2: Piece.from_symbol('B'), 1: Piece.from_symbol('N'), 0: Piece.from_symbol('R')}

@pytest.fixture
def moved_piece_map():
    return {63: Piece.from_symbol('r'), 62: Piece.from_symbol('n'), 61: Piece.from_symbol('b'), 60: Piece.from_symbol('k'), 59: Piece.from_symbol('q'), 58: Piece.from_symbol('b'), 57: Piece.from_symbol('n'), 56: Piece.from_symbol('r'), 55: Piece.from_symbol('p'), 54: Piece.from_symbol('p'), 53: Piece.from_symbol('p'), 52: Piece.from_symbol('p'), 51: Piece.from_symbol('p'), 50: Piece.from_symbol('p'), 49: Piece.from_symbol('p'), 48: Piece.from_symbol('p'), 25: Piece.from_symbol('P'), 15: Piece.from_symbol('P'), 14: Piece.from_symbol('P'), 13: Piece.from_symbol('P'), 12: Piece.from_symbol('P'), 11: Piece.from_symbol('P'), 10: Piece.from_symbol('P'), 8: Piece.from_symbol('P'), 7: Piece.from_symbol('R'), 6: Piece.from_symbol('N'), 5: Piece.from_symbol('B'), 4: Piece.from_symbol('K'), 3: Piece.from_symbol('Q'), 2: Piece.from_symbol('B'), 1: Piece.from_symbol('N'), 0: Piece.from_symbol('R')}

@pytest.fixture 
def moved_bishop_piece_map():
    return {63: Piece.from_symbol('r'), 62: Piece.from_symbol('n'), 61: Piece.from_symbol('b'), 60: Piece.from_symbol('k'), 59: Piece.from_symbol('q'), 58: Piece.from_symbol('b'), 57: Piece.from_symbol('n'), 56: Piece.from_symbol('r'), 55: Piece.from_symbol('p'), 54: Piece.from_symbol('p'), 53: Piece.from_symbol('p'), 52: Piece.from_symbol('p'), 51: Piece.from_symbol('p'), 50: Piece.from_symbol('p'), 49: Piece.from_symbol('p'), 48: Piece.from_symbol('p'), 19: Piece.from_symbol('P'), 15: Piece.from_symbol('P'), 14: Piece.from_symbol('P'), 13: Piece.from_symbol('P'), 12: Piece.from_symbol('P'), 10: Piece.from_symbol('P'), 9: Piece.from_symbol('P'), 8: Piece.from_symbol('P'), 7: Piece.from_symbol('R'), 6: Piece.from_symbol('N'), 5: Piece.from_symbol('B'), 4: Piece.from_symbol('K'), 3: Piece.from_symbol('Q'), 2: Piece.from_symbol('B'), 1: Piece.from_symbol('N'), 0: Piece.from_symbol('R')}

@pytest.fixture
def captured_piece_map():
    return {63: Piece.from_symbol('r'), 62: Piece.from_symbol('n'), 61: Piece.from_symbol('b'), 60: Piece.from_symbol('k'), 59: Piece.from_symbol('q'), 58: Piece.from_symbol('b'), 57: Piece.from_symbol('n'), 56: Piece.from_symbol('r'), 55: Piece.from_symbol('p'), 54: Piece.from_symbol('p'), 53: Piece.from_symbol('p'), 52: Piece.from_symbol('p'), 51: Piece.from_symbol('p'), 49: Piece.from_symbol('p'), 48: Piece.from_symbol('p'), 34: Piece.from_symbol('P'), 15: Piece.from_symbol('P'), 14: Piece.from_symbol('P'), 13: Piece.from_symbol('P'), 12: Piece.from_symbol('P'), 11: Piece.from_symbol('P'), 10: Piece.from_symbol('P'), 8: Piece.from_symbol('P'), 7: Piece.from_symbol('R'), 6: Piece.from_symbol('N'), 5: Piece.from_symbol('B'), 4: Piece.from_symbol('K'), 3: Piece.from_symbol('Q'), 2: Piece.from_symbol('B'), 1: Piece.from_symbol('N'), 0: Piece.from_symbol('R')}

@pytest.fixture
def multiple_moves_map():
    return {63: Piece.from_symbol('r'), 62: Piece.from_symbol('n'), 61: Piece.from_symbol('b'), 60: Piece.from_symbol('k'), 59: Piece.from_symbol('q'), 58: Piece.from_symbol('b'), 57: Piece.from_symbol('n'), 56: Piece.from_symbol('r'), 55: Piece.from_symbol('p'), 54: Piece.from_symbol('p'), 53: Piece.from_symbol('p'), 51: Piece.from_symbol('p'), 50: Piece.from_symbol('p'), 49: Piece.from_symbol('p'), 48: Piece.from_symbol('p'), 36: Piece.from_symbol('p'), 28: Piece.from_symbol('P'), 15: Piece.from_symbol('P'), 14: Piece.from_symbol('P'), 13: Piece.from_symbol('P'), 12: Piece.from_symbol('K'), 11: Piece.from_symbol('P'), 10: Piece.from_symbol('P'), 9: Piece.from_symbol('P'), 8: Piece.from_symbol('P'), 7: Piece.from_symbol('R'), 6: Piece.from_symbol('N'), 5: Piece.from_symbol('B'), 3: Piece.from_symbol('Q'), 2: Piece.from_symbol('B'), 1: Piece.from_symbol('N'), 0: Piece.from_symbol('R')}

@pytest.fixture
def default_board():
    return [['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']]