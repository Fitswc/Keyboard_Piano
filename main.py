import sys
import pygame as game
from pygame.locals import *
import Sound


def main():
    
    game.init()
    game.mixer.init()

    c1 = game.mixer.Sound('C1.wav')
    c1.set_volume(0.4)

    c2 = game.mixer.Sound('C2.wav')
    c2.set_volume(0.6)

    c3 = game.mixer.Sound('C3.wav')
    c3.set_volume(0.6)

    c4 = game.mixer.Sound('C4.wav')
    c4.set_volume(0.6)

    c5 = game.mixer.Sound('C5.wav')
    c5.set_volume(0.6)

    c6 = game.mixer.Sound('C6.wav')
    c6.set_volume(0.6)

    c7 = game.mixer.Sound('C7.wav')
    c7.set_volume(0.6)

    c8 = game.mixer.Sound('C8.wav')
    c8.set_volume(0.6)

    screen = game.display.set_mode((650,400))
    screen.fill((255,255,255))
    game.display.set_caption("Keyboard Piano")
    #bg = (0,0,0)
    bg = game.image.load('bg.jpg')
    screen.blit(bg,[0,0])
    game.display.update()
    while True:
        
        for event in game.event.get(): 

            if event.type == QUIT:
                game.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    Sound.c1.play()

                if event.key == K_2:
                    Sound.c2.play()

                if event.key == K_3:
                    Sound.c3.play()

                if event.key == K_4:
                    Sound.c4.play()

                if event.key == K_5:
                    Sound.c5.play()
            
                if event.key == K_6:
                    Sound.c6.play()

                if event.key == K_7:
                    Sound.c7.play()
            
                if event.key == K_8:
                    Sound.c8.play()