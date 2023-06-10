# Example file showing a circle moving on screen
import pygame

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
    black = (0, 0, 0)
    white = (255, 255, 255)
    colour = 1
    for x in range(9):
        for y in range(9):
            if colour == 0:
                pygame.draw.rect(screen, black, (0 + (64 * x), 0 + (64 * y), 64, 64))
                colour = 1
            else:
                pygame.draw.rect(screen, white, (0 + (64 * x), 0 + (64 * y), 64, 64))
                colour = 0




    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()