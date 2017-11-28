#Project 2 v1.00
import pygame, sys, time
from math import *
from pygame.locals import *
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
SAND = (255,255,100)
GREY = (182, 179, 179)

surface = pygame.display.set_mode((1280,720))


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

class run(object):
    def runm(self,resolution=(1280,720)):
        pygame.init()

        duration = 5000
        win = projectWin(500, 500, 'MonkeyWar')
        Quit = False
        while not Quit:
            # get Mouse
            mouse = pygame.mouse.get_pos()
            # set Background
            surface.blit(pygame.transform.scale(pygame.image.load('data/monkeywar/bg.jpg').convert(), (1280, 720)),
                         (0, 0))

            #call classes
            win.ground()

            # Display the res
            pygame.display.update()
            time.sleep(0.02)

            # Quit handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    Quit = True

        pygame.quit()  # always exit cleanly
        sys.exit()


class PlaceHolder:
    def __init__(self, win, left, top, width, height, color):
        self.win = win
        self.rect = pygame.Rect(left, top, width, height)
        self.color = color


class projectWin:
    def __init__(self, width, height, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)
        self.width = width
        self.height = height
        self.placeHolders = []
        self.placeHolders.append(PlaceHolder(surface, 1, 236, 10, 10, GREEN))
        #placeHolder1 = PlaceHolder(surface, 10, 236, 10, 10, GREEN)

    def ground(self):
        pygame.draw.rect(surface, GREY, (0, 565, 1270, 165), 0)





