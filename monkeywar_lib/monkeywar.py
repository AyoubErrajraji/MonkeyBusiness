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
GREY = (155,155,155)
clock = pygame.time.Clock()
ounter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

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

        secondMonkey = Monkey(1080, "data/monkeywar/tankl.png", "ARROWS")
        firstMonkey = Monkey(100, "data/monkeywar/tankr.png","WASD")




        while not Quit:

            # get Mouse
            mouse = pygame.mouse.get_pos()

            #FPS
            clock.tick(60)

            # set Background
            surface.blit(pygame.transform.scale(pygame.image.load('data/monkeywar/bg.jpg').convert(), (1280, 720)),
                         (0, 0))


            #call classes
            win.ground()

            secondMonkey.move()
            firstMonkey.move()

            # update display
            pygame.display.update()


            # Display the res
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

    def ground(self):
        pygame.draw.rect(surface, GREY, (0, 550, 1280, 170), 0)


class Monkey(object):
    def __init__(self, x, image, movement):
        self.x = x
        self.image = image
        self.movement = movement

    def draw(self, position):
        sprite = pygame.image.load(self.image).convert_alpha()
        surface.blit(pygame.transform.scale(sprite, (110, 80)), position)

    def move(self):
        pygame.event.pump()

        # a key has been pressed
        keyinput = pygame.key.get_pressed()

        # press escape key to quit game
        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit
        # optional exit on window corner x click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # check arrow keys
        # move sprite in direction of arrow by 2 pixels

        if self.movement == "ARROWS":

            if keyinput[pygame.K_LEFT]:
                self.x -= 10
            elif keyinput[pygame.K_RIGHT]:
                self.x += 10

        if self.movement == "WASD":
            if keyinput[pygame.K_a]:
                self.x -= 10
            elif keyinput[pygame.K_d]:
                self.x += 10

        self.draw((self.x,478))













