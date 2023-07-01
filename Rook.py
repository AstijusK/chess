from Piece import Piece


class Rook(Piece):

    def __init__(self, piece_type):
        super().__init__(piece_type)
        self.legal_moves = [
            # Straight right

            # Straight left

            # Straight up

            # Straight down
        ]