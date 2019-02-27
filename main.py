#keyboard piano
import pygame as game
import sys
from pygame.locals import *

game.init()
screen = game.display.set_mode((1000,700))
bg_color = (0, 190, 255)
game.display.set_caption("Main")
while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            sys.exit()
    screen.fill(bg_color)
    game.display.flip()

