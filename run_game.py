# Example file showing a basic pygame "game loop"
import pygame as pg
from sys import exit

# pygame setup
pg.init()
window_height, window_width = 800, 600
screen = pg.display.set_mode((window_height, window_width))
clock = pg.time.Clock()
pg.display.set_caption('Pacman Pygame')

pacman_level_0_surface = pg.image.load('Assets/level_0_empty.png')
level_scaled = pg.transform.scale(pacman_level_0_surface, (window_height, window_width))

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(level_scaled,(0,0))

    # RENDER YOUR GAME HERE

    pg.display.update()
    clock.tick(60)  # limits FPS to 60