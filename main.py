# Example file showing a circle moving on screen
import pygame

from Piece import Piece
from Board import Board

import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True
dt = 0

# Keeps track of whether piece a piece has been clicked on and 'primed' for movement
selected = 0
piece_to_move = None
square_x_difference = None
square_y_difference = None

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected == 0:
                mouse_pos = pygame.mouse.get_pos()
                square_x = math.trunc(mouse_pos[0] / 64)
                square_y = math.trunc(mouse_pos[1] / 64)

                if Board.squares[square_y][square_x].PieceType is not Piece.Type.EMPTY:
                    piece_to_move = Board.squares[square_y][square_x]
                    selected = 1
            else:
                mouse_pos2 = pygame.mouse.get_pos()
                square_x2 = math.trunc(mouse_pos2[0] / 64)
                square_y2 = math.trunc(mouse_pos2[1] / 64)

                if Board.squares[square_y2][square_x2] is not piece_to_move:
                    # Check if move is legal here.

                    # Find vector difference between piece_to_move and target_square?
                    # If vector difference is not in the list of 'legal_moves' (allowed vector differences),
                    # move is illegal. Otherwise, make the move

                    if square_x2 > square_x:
                        square_x_difference = square_x2 - square_x
                    elif square_x2 < square_x:
                        square_x_difference = square_x - square_x2
                    else:
                        square_x_difference = 0

                    if square_y2 > square_y:
                        square_y_difference = square_y2 - square_y
                    elif square_y2 < square_y:
                        square_y_difference = square_y - square_y2
                    else:
                        square_y_difference = 0

                    if (square_x_difference, square_y_difference) in piece_to_move.legal_moves:
                        Board.squares[square_y2][square_x2] = piece_to_move
                        Board.squares[square_y][square_x] = Piece(0)
                    else:
                        print("illegal move")
                selected = 0

    # flip() the display to put your work on screen
    pygame.display.flip()

    # Board setup
    board = Board()
    dark = (125, 135, 150)
    light = (232, 235, 239)
    colour = 1

    # Sprite loading
    # BLACK PIECES
    b_pawn = pygame.image.load('res/black/pawn.png')
    b_knight = pygame.image.load('res/black/knight.png')
    b_bishop = pygame.image.load('res/black/bishop.png')
    b_rook = pygame.image.load('res/black/rook.png')
    b_king = pygame.image.load('res/black/king.png')
    b_queen = pygame.image.load('res/black/queen.png')

    # WHITE PIECES
    w_pawn = pygame.image.load('res/white/pawn.png')
    w_knight = pygame.image.load('res/white/knight.png')
    w_bishop = pygame.image.load('res/white/bishop.png')
    w_rook = pygame.image.load('res/white/rook.png')
    w_king = pygame.image.load('res/white/king.png')
    w_queen = pygame.image.load('res/white/queen.png')

    # Drawing the board
    for x in range(9):
        for y in range(9):
            if colour == 0:
                pygame.draw.rect(screen, dark, (64 * x, 64 * y, 64, 64))
                colour = 1
            else:
                pygame.draw.rect(screen, light, (64 * x, 64 * y, 64, 64))
                colour = 0

    # Reading board states and drawing pieces
    for x in range(0, len(board.squares)):
        for y in range(0, len(board.squares)):
            match Board.squares[x][y].PieceType:
                # White
                case Piece.Type.W_PAWN:
                    screen.blit(w_pawn, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.W_KNIGHT:
                    screen.blit(w_knight, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.W_BISHOP:
                    screen.blit(w_bishop, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.W_ROOK:
                    screen.blit(w_rook, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.W_KING:
                    screen.blit(w_king, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.W_QUEEN:
                    screen.blit(w_queen, (0 + (64 * y), 0 + (64 * x)))

                # Black
                case Piece.Type.B_PAWN:
                    screen.blit(b_pawn, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.B_KNIGHT:
                    screen.blit(b_knight, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.B_BISHOP:
                    screen.blit(b_bishop, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.B_ROOK:
                    screen.blit(b_rook, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.B_KING:
                    screen.blit(b_king, (0 + (64 * y), 0 + (64 * x)))
                case Piece.Type.B_QUEEN:
                    screen.blit(b_queen, (0 + (64 * y), 0 + (64 * x)))

    # Handling piece movement
        # Method 1: Click once on piece to move, click again on destination square [DONE]
        # Method 2: Mouse hold and drag a piece from starting square to destination square

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
