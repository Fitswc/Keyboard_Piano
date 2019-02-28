import sys
import pygame as game
from pygame.locals import *
import sound

game.init()
game.mixer.init()

c1 = game.mixer.Sound('C1.mp3')
c1.set_volume(0.6)

c2 = game.mixer.Sound('C2.mp3')
c2.set_volume(0.6)

c3 = game.mixer.Sound('C3.mp3')