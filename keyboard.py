import pygame as game
import sys

def Keyboard():
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            sys.exit()

        elif event.type == game.K_1:
            
