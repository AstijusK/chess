from Piece import Piece


class Bishop(Piece):

    def __init__(self, piece_type):
        super().__init__(piece_type)
        self.legal_moves = [
            # Diagonal - up right

            # Diagonal - up left

            # Diagonal - down right

            # Diagonal - down left
        ]