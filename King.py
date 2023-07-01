from Piece import Piece


class King(Piece):

    def __init__(self, piece_type):
        super().__init__(piece_type)
        self.legal_moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]