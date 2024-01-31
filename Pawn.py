from Piece import Piece


class Pawn(Piece):
    def __init__(self, piece_type):
        super().__init__(piece_type)

        self.legal_moves.append((0, 1))
        self.legal_moves.append((0, 2))

        if self.times_moved > 0:
            self.legal_moves.remove((0, 2))

