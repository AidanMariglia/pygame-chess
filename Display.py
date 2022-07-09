## @file Display.py
#  @author Aidan Mariglia
#  @brief A class for handling rendering instructions for pygame

import pygame, sys
from pygame.locals import *
from squareMap import *

## @brief Display is used to make pygame api calls

class Display:

    ## @brief constant defining cell size
    __CELL__SIZE = 100
    ## @brief constants defining square color rgb values
    __DARK, __LIGHT = (118, 150, 86), (238, 238, 210)
    ## @brief constant defining board size
    __SIZE = ____WIDTH, __HEIGHT = __CELL__SIZE*8, __CELL__SIZE*8

    __HIGHLIGHT = (0,250,0)

    ## @brief Display class constuctor
    def __init__(self):
        self.__board = pygame.Surface((Display.__CELL__SIZE*8, Display.__CELL__SIZE*8))
        self.__board.fill(Display.__DARK)
        self.__screen = pygame.display.set_mode(Display.__SIZE)
        self.__pieces = self.__import_pngs()
        self.__pieceRects = self.__get_rects(self.__pieces)
        self.__gameState = 0

        self.__create_board()

    ## @brief setup method for creating the pygame board
    def __create_board(self):
        for x in range (0, 8, 2):
            for y in range(0, 8, 2):
                pygame.draw.rect(self.__board, Display.__LIGHT,
                                 (x * Display.__CELL__SIZE, y * Display.__CELL__SIZE,
                                  Display.__CELL__SIZE, Display.__CELL__SIZE))

        for x in range (1, 8, 2):
            for y in range(1, 8, 2):
                pygame.draw.rect(self.__board, Display.__LIGHT,
                                 (x * Display.__CELL__SIZE, y * Display.__CELL__SIZE,
                                  Display.__CELL__SIZE, Display.__CELL__SIZE))

    ## @brief setup method to import piece PNG's and place them in a dict
    #  @return returns a dict of piece PNG's
    def __import_pngs(self):
        return {
            'P': pygame.image.load("assets/white_pawn.png"),
            'N': pygame.image.load("assets/white_horse.png"),
            'B': pygame.image.load("assets/white_bishop.png"),
            'R': pygame.image.load("assets/white_rook.png"),
            'Q': pygame.image.load("assets/white_queen.png"),
            'K': pygame.image.load("assets/white_king.png"),
            'p': pygame.image.load("assets/black_pawn.png"),
            'n': pygame.image.load("assets/black_horse.png"),
            'b': pygame.image.load("assets/black_bishop.png"),
            'r': pygame.image.load("assets/black_rook.png"),
            'q': pygame.image.load("assets/black_queen.png"),
            'k': pygame.image.load("assets/black_king.png"),
        }

    ## @brief method to create rect object for piece PNG's
    #  @param pngs, takes a dict object of piece PNG's
    #  @return returns a dict of piece rects
    def __get_rects(self, pngs):
        return {
            'P': pngs['P'].get_rect(),
            'N': pngs['N'].get_rect(),
            'B': pngs['B'].get_rect(),
            'R': pngs['R'].get_rect(),
            'Q': pngs['Q'].get_rect(),
            'K': pngs['K'].get_rect(),
            'p': pngs['p'].get_rect(),
            'n': pngs['n'].get_rect(),
            'b': pngs['b'].get_rect(),
            'r': pngs['r'].get_rect(),
            'q': pngs['q'].get_rect(),
            'k': pngs['k'].get_rect(),
        }

    ## @brief method to draw pieces on game board
    #  @param piece_dict, takes a dictionary of active pieces and their
    #  current position
    def __draw_pieces(self, piece_dict):
        for square, piece in piece_dict.items():
            self.__pieceRects[piece.symbol()].x = \
                squareMap[chess.square_name(square)][0]
            self.__pieceRects[piece.symbol()].y = \
                squareMap[chess.square_name(square)][1]
            self.__screen.blit(
                self.__pieces[piece.symbol()], self.__pieceRects[piece.symbol()])

    ## @brief method to update game screen
    #  @param piece_dict, takes a dictionary of piece positions
    def update(self, piece_dict):
        if(self.__gameState == 0):
            self.__screen.blit(self.__board, self.__board.get_rect())
            self.__draw_pieces(piece_dict)
            pygame.display.flip()


    ## @brief method to highlight a square on the game screen
    #  @param square, string takes the rank and file of the square
    #  @param color, string takes the color the square will be highlighted
    def highlight_square(self, square):
        pygame.draw.rect(self.__board, Display.__HIGHLIGHT,
                         (square[0], square[1],
                         Display.__CELL__SIZE, Display.__CELL__SIZE), 0)
        for i in range(4):
            pygame.draw.rect(self.__board, (0, 0, 0),
                            (square[0] - i, square[1] - i,
                            Display.__CELL__SIZE, Display.__CELL__SIZE), 1)


   ## @brief method to restore a square that was previously highlighted
   #  @param square, string takes the rank and file of the square
    def restore_square(self, square):
        color = Display.__DARK

        # if the sum of the x and y is an even number then they were both odd
        # or both even, meaning the color is light
        if ((square[0] + square[1])/100)%2 == 0:
            color = Display.__LIGHT

        pygame.draw.rect(self.__board, color, (square[0], square[1],
                         Display.__CELL__SIZE, Display.__CELL__SIZE), 0)
        for i in range(4):
            pygame.draw.rect(self.__board, color,
                            (square[0] - i, square[1] - i,
                            Display.__CELL__SIZE, Display.__CELL__SIZE), 1)

    ## @brief method to display an endgame message when white wins by checkmate
    def white_by_checkmate_message(self):
        self.__screen.blit(pygame.image.load("assets/White_Checkmate.png"), (25, 300))
        self.__gameState = 1
        pygame.display.flip()

    ## @brief method to display an endgame message when black wins by checkmate
    def black_by_checkmate_message(self):
        self.__screen.blit(pygame.image.load("assets/Black_Checkmate.png"), (25, 300))
        self.__gameState = 1
        pygame.display.flip()


    def get_gameState(self):
        return self.__gameState

    ## @brief method to display a draw message
    def draw_message(self):
        self.__screen.blit(pygame.image.load("assets/Draw.png"), (25, 300))
        self.__gameState = 1
        pygame.display.flip()

#ifndef SKIP
if __name__=="__main__":
    d = Display()
    d.__create_board()
    b = chess.BaseBoard()

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
#endif SKIP
        d.update(b.piece_map())
