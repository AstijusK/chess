from Piece import Piece


class Knight(Piece):

    def __init__(self, piece_type):
        super().__init__(piece_type)
        self.legal_moves = [
            (),
            (),
            (),
            ()
        ]

