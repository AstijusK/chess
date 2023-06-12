# Example file showing a circle moving on screen
import pygame
from Board import Board

# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # Board setup
    board = Board()
    dark = (125, 135, 150)
    light = (232, 235, 239)
    colour = 1

    # Sprite loading
    b_pawn = pygame.image.load('res/black/pawn.png')
    b_knight = pygame.image.load('res/black/knight.png')
    b_bishop = pygame.image.load('res/black/bishop.png')
    b_rook = pygame.image.load('res/black/rook.png')
    b_king = pygame.image.load('res/black/king.png')
    b_queen = pygame.image.load('res/black/queen.png')

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
                pygame.draw.rect(screen, dark, (0 + (64 * x), 0 + (64 * y), 64, 64))
                colour = 1
            else:
                pygame.draw.rect(screen, light, (0 + (64 * x), 0 + (64 * y), 64, 64))
                colour = 0

    # Reading board states
    for x in range(0, len(board.squares)):
        for y in range(0, len(board.squares)):

            if Board.States(board.squares[x][y]) == Board.States.B_PAWN:
                screen.blit(b_pawn, (0 + (64*y), 0 + (64*x)))
            if Board.States(board.squares[x][y]) == Board.States.W_PAWN:
                screen.blit(w_pawn, (0 + (64 * y), 0 + (64 * x)))



    # RGB FOR WHITE AND BLACK PIECES FOR LATER
    # WHITE: (242, 242, 242)
    # BLACK: (0, 0, 0)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()