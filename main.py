# Example file showing a circle moving on screen
import pygame

from Piece import Piece
from Board import Board

import math

# Debug state - shout out to my lecturer Brian Tompset - this is where I got the debug idea from. Makes code cleaner.
debug = True

# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True
dt = 0

# Keeps track of whether piece a piece has been clicked on and 'primed' for movement
selected = 0
piece_to_move = None


def get_mouse_pos():
    mp = pygame.mouse.get_pos()
    sx = math.trunc(mp[0] / 64)
    sy = math.trunc(mp[1] / 64)
    return [sx, sy]


def calculate_sx_diff(sx, sx2):
    sx_diff = 0
    if sx2 > sx:
        sx_diff = sx2 - sx
    elif sx2 < sx:
        sx_diff = sx - sx2
    else:
        sx_diff = 0
    return sx_diff


def calculate_sy_diff(sy, sy2):
    sy_diff = 0
    if sy2 > sy:
        sy_diff = sy2 - sy
    elif sy2 < sy:
        sy_diff = sy - sy2
    else:
        sy_diff = 0
    return sy_diff


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected == 0:
                square_x = get_mouse_pos()[0]
                square_y = get_mouse_pos()[1]

                if debug:
                    # Identifying the square clicked and piece clicked on (works)
                    print("x: " + str(square_x+1) + " y: " + str(square_y+1))
                    print(Board.squares[square_y][square_x].PieceType)
                if Board.squares[square_y][square_x].PieceType is not Piece.Type.EMPTY:
                    # Call piece.set_pos() here after method is implemented
                    piece_to_move = Board.squares[square_y][square_x]
                    selected = 1

                    if debug:
                        print(piece_to_move.legal_moves)
                        print(selected)
            else:
                square_x2 = get_mouse_pos()[0]
                square_y2 = get_mouse_pos()[1]

                if debug:
                    print("x: " + str(square_x2 + 1) + " y: " + str(square_y2 + 1))
                    print(Board.squares[square_y2][square_x2].PieceType)

                # If the destination square is not the same as the starting square
                if Board.squares[square_y2][square_x2] is not piece_to_move:
                    # Check if move is legal here.

                    # Find vector difference between piece_to_move and target_square?
                    # If vector difference is not in the list of 'legal_moves' (allowed vector differences),
                    # move is illegal. Otherwise, make the move
                    square_x_difference = calculate_sx_diff(square_x, square_x2)
                    square_y_difference = calculate_sy_diff(square_y, square_y2)

                    if (square_x_difference, square_y_difference) in piece_to_move.legal_moves:
                        # Call piece.set_pos() here after method is implemented
                        Board.squares[square_y2][square_x2] = piece_to_move
                        Board.squares[square_y][square_x] = Piece(0)
                    else:
                        if debug:
                            print("illegal move")
                            print(piece_to_move.legal_moves)
                else:
                    if debug:
                        print("destination square is same as starting square")
                        print(selected)
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
