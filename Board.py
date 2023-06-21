from enum import Enum
from Piece import Piece


class Board:
    # In the future, make separate classes for each piece,
    # and instantiate objects from those classes instead of general class.

    squares = [[Piece(10), Piece(8), Piece(9), Piece(11), Piece(12), Piece(9), Piece(8), Piece(10)],
               [Piece(7), Piece(7), Piece(7), Piece(7), Piece(7), Piece(7), Piece(7), Piece(7)],
               [Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0)],
               [Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0)],
               [Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0)],
               [Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0)],
               [Piece(1), Piece(1), Piece(1), Piece(1), Piece(1), Piece(1), Piece(1), Piece(1)],
               [Piece(4), Piece(2), Piece(3), Piece(6), Piece(5), Piece(3), Piece(2), Piece(4)]]
