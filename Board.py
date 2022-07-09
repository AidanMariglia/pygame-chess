## @file Board.py
#  @author Ben Dubois
#  @brief A class for storing the board

import chess

## @brief Board is used to save the current state of the game board

class Board():
    
    ## @brief Board class constuctor. Creates an n*n board.
    def __init__(self, n=8):

        ## @brief The array storing each space on the board
        self._board = [["e" for x in range(n)] for y in range(n)]
    
    ## @brief resets the state of the board
    def reset(self):
        self._board = [["e" for x in range(len(self._board))] for y in range(len(self._board))] 
    
    ## @brief getter for the board state at a specific square
    #  @param i, the rank of the square
    #  @param j, the file of the square
    #  @return, returns a string with the piece located at a specific square
    def get(self, i, j):
        if 0 < i < len(self._board) and 0 < j < len(self._board):
            return self._board[i][j]
    
    ## @brief setter for the board state at a specific square
    #  @param i, the rank of the square
    #  @param j, the file of the square
    #  @param element, the value to be set at the square
    def put(self, i, j, element):
        if 0 < i < len(self._board) and 0 < j < len(self._board):
            self._board[i][j] = element
