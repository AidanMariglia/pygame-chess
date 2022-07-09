import Game
import Display
import pygame
import sys
import chess
from squareMap import *

## @brief Main game controller
class Main:

    ## @brief Main module constructor
    def __init__(self):
        self.__g = Game.Game()
        ##  stores turn state, true: white false: black
        self.turn = True
        self.highlighted = []
        self.d = None

    def __normalize_mouse_pos(self, p):
        return (p[0] - p[0]%100, p[1] - p[1]%100)

    ## @brief start method for main game loop
    def start(self):
        self.d = Display.Display()
        sq1 = None
        prev_np = None

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    p = event.pos
                    np = self.__normalize_mouse_pos(p)
                    print(p)
                    print(np)
                    print(squareMapRev[np])

                    if sq1 != None:
                        self.d.restore_square(prev_np)
                        sq2 = chess.parse_square(squareMapRev[np])
                        self.__g.move(sq1, sq2)
                        self.restore_highlighted_squares()
                        sq1 = None
                        sq2 = None
                        if self.__g.check_endgames() == 1:
                            self.d.update(self.__g.get_piece_map())
                            if self.__g.get_board().outcome().winner == True:
                                self.d.white_by_checkmate_message()
                            else:
                                self.d.black_by_checkmate_message()
                        elif self.__g.check_endgames() == 2:
                            self.d.update(self.__g.get_piece_map())
                            self.d.draw_message()
                        else:
                            self.d.update(self.__g.get_piece_map())

                    else:
                        sq1 = chess.parse_square(squareMapRev[np])
                        self.d.highlight_square(np)
                        self.highlight_possible_moves(sq1)
                        prev_np = np
                        if self.__g.check_endgames() != 0:
                            self.__g.reset()
                            self.d = Display.Display()
                        else:
                            self.d.update(self.__g.get_piece_map())

                elif self.d.get_gameState() == 0:
                    self.d.update(self.__g.get_piece_map())

    ## @brief highlights the squares of possible moves originating form sq1
    #  @param sq1, the originating square
    def highlight_possible_moves(self, sq1):
        self.highlighted = self.__g.list_highlighted_moves(sq1)

        for sq in self.highlighted:
            self.d.highlight_square(sq)


    ## @brief restores the color of any highlighted squares
    def restore_highlighted_squares(self):
        for sq in self.highlighted:
            self.d.restore_square(sq)


if __name__=="__main__":
    m = Main()
    m.start()
