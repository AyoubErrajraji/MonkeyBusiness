'''
Created on Nov 25, 2017
@author: lexdewilligen
Project 2 v1.00
'''

import pygame
import sys
import time
from math import *
from pygame.locals import *
from menu_lib import slidemenu
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
SAND = (255,255,100)


surface = pygame.display.set_mode((1280,720))


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, function=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1:
            if function != None:
                function()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

def showGrid():
    for i in range(47, 912, 48): #draw the vertical lines
        pygame.draw.line(screen, WHITE, (i, 0), (i, 720), 1)
    for j in range(47, 720, 48): #draw the horizontal lines
        pygame.draw.line(screen, WHITE, (0, j), (912, j), 1)

def returnMenu():
    mymenu = slidemenu.run()
    mymenu.runm()

def path():
    #the two lines are separated for ease of change
    #line 1
    pygame.draw.line(screen, SAND, (0, 287), (144, 287), 2)
    pygame.draw.line(screen, SAND, (143, 287), (143, 144), 2)
    pygame.draw.line(screen, SAND, (144, 143), (336, 143), 2)
    pygame.draw.line(screen, SAND, (335, 144), (335, 528), 2)
    pygame.draw.line(screen, SAND, (336, 527), (144, 527), 2)
    pygame.draw.line(screen, SAND, (143, 528), (143, 576), 2)
    pygame.draw.line(screen, SAND, (144, 575), (768, 575), 2)
    pygame.draw.line(screen, SAND, (767, 576), (767, 480), 2)
    pygame.draw.line(screen, SAND, (768, 479), (528, 479), 2)
    pygame.draw.line(screen, SAND, (527, 336), (527, 480), 2)
    pygame.draw.line(screen, SAND, (528, 335), (768, 335), 2)
    pygame.draw.line(screen, SAND, (767, 335), (767, 0), 2)

    #line 2
    pygame.draw.line(screen, SAND, (0, 335), (192, 335), 2)
    pygame.draw.line(screen, SAND, (191, 336), (191, 192), 2)
    pygame.draw.line(screen, SAND, (192, 191), (288, 191), 2)
    pygame.draw.line(screen, SAND, (287, 192), (287, 480), 2)
    pygame.draw.line(screen, SAND, (288, 479), (96, 479), 2)
    pygame.draw.line(screen, SAND, (95, 480), (95, 622), 2)
    pygame.draw.line(screen, SAND, (96, 622), (816, 622), 2)
    pygame.draw.line(screen, SAND, (815, 624), (815, 432), 2)
    pygame.draw.line(screen, SAND, (816, 431), (576, 431), 2)
    pygame.draw.line(screen, SAND, (575, 432), (575, 384), 2)
    pygame.draw.line(screen, SAND, (576, 383), (816, 383), 2)
    pygame.draw.line(screen, SAND, (815, 384), (815, 0), 2)

def base(): #what the player has to protect
    AHLogo = pygame.image.load('data/bananattack/ah.png').convert_alpha()
    AHLogo = pygame.transform.scale(AHLogo , (48,48))
    screen.blit(AHLogo, (768, 0))

class run(object):
    def runm(self,resolution=(1280,720)):
        pygame.init()

        duration = 5000
        Quit = False
        while not Quit:
            # get Mouse
            mouse = pygame.mouse.get_pos()

            # set Background
            screen.blit(pygame.transform.scale(pygame.image.load('data/bananattack/background.jpeg').convert(), (912, 720)),(0, 0))

            # Buttons
            button("Grid", 920, 10, 100, 50, GREEN, BRIGHT_GREEN, showGrid)
            button("Menu", 1030, 10, 100, 50, GREEN, BRIGHT_GREEN, returnMenu)

            # Display the rest
            path()
            base()
            pygame.display.update()

            # Sleep
            time.sleep(0.02)

            # Quit handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    Quit = True

        # Always exit cleanly
        pygame.quit()
        sys.exit()




