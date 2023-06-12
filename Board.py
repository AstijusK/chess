from enum import Enum


class Board:
    class States(Enum):
        EMPTY = 0
        W_PAWN = 1
        W_KNIGHT = 2
        W_BISHOP = 3
        W_ROOK = 4
        W_KING = 5
        W_QUEEN = 6
        B_PAWN = 7
        B_KNIGHT = 8
        B_BISHOP = 9
        B_ROOK = 10
        B_KING = 11
        B_QUEEN = 12

    def __init__(self):
        self.squares = [[10, 8, 9, 11, 12, 9, 8, 10],
                        [7, 7, 7, 7, 7, 7, 7, 7],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 1, 1],
                        [4, 2, 3, 6, 5, 3, 2, 4]]
