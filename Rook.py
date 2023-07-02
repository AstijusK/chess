from Piece import Piece


class Rook(Piece):

    def __init__(self, piece_type):
        super().__init__(piece_type)
        self.legal_moves = [
            # Straight right
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (8, 0),

            # Straight left
            (-1, 0),
            (-2, 0),
            (-3, 0),
            (-4, 0),
            (-5, 0),
            (-6, 0),
            (-7, 0),
            (-8, 0),

            # Straight up
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (0, 6),
            (0, 7),
            (0, 8),

            # Straight down
            (0, -1),
            (0, -2),
            (0, -3),
            (0, -4),
            (0, -5),
            (0, -6),
            (0, -7),
            (0, -8)
        ]