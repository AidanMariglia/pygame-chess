import chess
from squareMap import *

## Represents the core game functionality
class Game():

    ## @brief Game class constructor
    def __init__(self):
        #TODO
        self.__board = chess.Board()

    ## @brief resets the state of the game
    def reset(self):
        self.__board = chess.Board()
    

    ## @brief returns the gameboard
    #  @return returns the gameboard
    def get_board(self):
        return self.__board

    ## @brief returns a dictionary mapping pieces to squares
    #  @return returns a dictionary mapping pieces to squares
    def get_piece_map(self):
        return self.__board.piece_map()

    ## @brief checks legal moves for a specified piece
    #  @param square, string rank and file of the piece in question
    #  @return returns a list of legal moves
    def check_legal_moves(self, sq1, sq2):
        return chess.Move(sq1, sq2) in self.__board.legal_moves

    def __check_promotion(self, sq1, sq2):
        return chess.Move(sq1, sq2, promotion=chess.QUEEN) \
            in self.__board.legal_moves


    ## @brief returns a list of possible moves for a selected piece
    #  @param sq1, square that the possible moves originate from
    #  @return returns a list of highlighted move 
    def list_highlighted_moves(self, sq1):
        return [squareMap[chess.square_name(move.to_square)] for move \
                in self.__board.legal_moves if move.from_square == sq1]


    ## @brief moves a piece from one square to another
    #  @param start, string the rank and file of the piece being moved
    #  @param destination, string the rank and file of the square the
    # piece is being moved to
    def move(self, start, destination):
        m = chess.Move(start, destination)
        m_promote = chess.Move(start, destination, promotion = chess.QUEEN)

        if self.__check_promotion(start, destination):
            self.__board.push(m_promote)

        elif self.check_legal_moves(start, destination):
            self.__board.push(m)

    ## @brief checks the current board state for endgames, and ends the game
    # if they exist
    def check_endgames(self):
        if self.__board.is_checkmate():
            return 1
        elif self.__board.is_stalemate():
            return 2
        elif self.__board.is_fivefold_repetition():
            return 2
        elif self.__board.is_insufficient_material():
            return 2
        else:
            return 0

    ## @brief A utility method currently used only for directly manipulating the game board in tests. May be used for 
    # forcing a custom board layout. 
    def set_board(self, fen=chess.STARTING_BOARD_FEN):
        new_board = chess.Board(fen)
        if new_board.is_valid():
            self.__board = new_board


if __name__=="__main__":
    g = Game()
    for move in g.check_legal_moves(chess.A2):
        print(move.uci())

