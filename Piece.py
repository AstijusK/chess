from enum import Enum


class Piece:
    class Type(Enum):
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

    def __init__(self, piece_type):
        self.PieceType = Piece.Type(piece_type)
        self.times_moved = 0
        self.legal_moves = []