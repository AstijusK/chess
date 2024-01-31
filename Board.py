from Piece import Piece

from Pawn import Pawn
from Bishop import Bishop
from Rook import Rook
from Knight import Knight
from King import King
from Queen import Queen


class Board:
    # In the future, make separate classes for each piece,
    # and instantiate objects from those classes instead of general class.

    squares = [[Rook(10), Knight(8), Bishop(9), Piece(11), Piece(12), Bishop(9), Knight(8), Rook(10)],
               [Pawn(7), Pawn(7), Pawn(7), Pawn(7), Pawn(7), Pawn(7), Pawn(7), Pawn(7)],
               [Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0)],
               [Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0)],
               [Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0)],
               [Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0), Piece(0)],
               [Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
               [Rook(4), Knight(2), Bishop(3), Queen(6), King(5), Bishop(3), Knight(2), Rook(4)]]
