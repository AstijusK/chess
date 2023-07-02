from Piece import Piece


class Bishop(Piece):

    def __init__(self, piece_type):
        super().__init__(piece_type)
        self.legal_moves = [
            # Diagonal - up right
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),

            # Diagonal - up left
            (-1, 1),
            (-2, 2),
            (-3, 3),
            (-4, 4),
            (-5, 5),
            (-6, 6),
            (-7, 7),
            (-8, 8),

            # Diagonal - down right
            (1, -1),
            (2, -2),
            (3, -3),
            (4, -4),
            (5, -5),
            (6, -6),
            (7, -7),
            (8, -8),

            # Diagonal - down left
            (-1, -1),
            (-2, -2),
            (-3, -3),
            (-4, -4),
            (-5, -5),
            (-6, -6),
            (-7, -7),
            (-8, -8),
        ]