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

surface = pygame.display.set_mode((1280,720))


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

class run(object):
    def runm(self,resolution=(1280,720)):
        pygame.init()

        duration = 5000
        win = projectWin(500, 500, 'BananAttack')
        Quit = False
        while not Quit:
            # get Mouse
            mouse = pygame.mouse.get_pos()

            # set Background
            surface.blit(pygame.transform.scale(pygame.image.load('data/bananattack/background.jpeg').convert(), (912, 720)),
                         (0, 0))

            # SHOW HIDE Grid
            try:
                grid
            except NameError:
                grid = False
            button("Grid!", 920, 10, 100, 50, GREEN, BRIGHT_GREEN)
            if (grid):
                print(grid)
                win.grid()

            # Display the rest
            win.path()
            win.base()
            for i in win.placeHolders:  # draw and move the placeholder enemy assets
                i.move(59, 0, duration)
                i.move(0, -100, duration)
                i.draw()
            pygame.display.update()
            time.sleep(0.02)

            # Quit handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    Quit = True

        pygame.quit()  # always exit cleanly
        sys.exit()


def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(surface, ac, (x, y, w, h))

        if click[0] == 1:
            global grid
            if (grid):
                grid = False
            else:
                grid = True
    else:
        pygame.draw.rect(surface, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    surface.blit(textSurf, textRect)

class PlaceHolder:
    def __init__(self, win, left, top, width, height, color):
        self.win = win
        self.rect = pygame.Rect(left, top, width, height)
        self.color = color

    def move(self,x,y,duration):
        #self.rect = self.rect.move(self.velocity[0],self.velocity[1])
        xpointlist = [60, 60]
        ypointlist = [236, 136]
        self.rect.left += x
        self.rect.top += y
        self.duration = duration
        counter = 0
        rate = 10
        for counter in range(len(xpointlist)-1):
            dx = x - xpointlist[counter]
            dy = y - ypointlist[counter]
            distance = sqrt(dx*dx + dy*dy)
            return distance
        duration = distance/rate

    def draw(self):
        pygame.draw.ellipse(surface, self.color, self.rect, 0)

class projectWin:
    def __init__(self, width, height, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)
        self.width = width
        self.height = height
        self.placeHolders = []
        self.placeHolders.append(PlaceHolder(surface, 1, 236, 10, 10, GREEN))
        #placeHolder1 = PlaceHolder(surface, 10, 236, 10, 10, GREEN)

    def grid(self):
        for i in range(47, 912, 48): #draw the vertical lines
            pygame.draw.line(surface, WHITE, (i, 0), (i, 720), 1)
        for j in range(47, 720, 48): #draw the horizontal lines
            pygame.draw.line(surface, WHITE, (0, j), (912, j), 1)

    def path(self):
        #the two lines are separated for ease of change
        #line 1
        pygame.draw.line(surface, SAND, (0, 287), (144, 287), 2)
        pygame.draw.line(surface, SAND, (143, 287), (143, 144), 2)
        pygame.draw.line(surface, SAND, (144, 143), (336, 143), 2)
        pygame.draw.line(surface, SAND, (335, 144), (335, 528), 2)
        pygame.draw.line(surface, SAND, (336, 527), (144, 527), 2)
        pygame.draw.line(surface, SAND, (143, 528), (143, 576), 2)
        pygame.draw.line(surface, SAND, (144, 575), (768, 575), 2)
        pygame.draw.line(surface, SAND, (767, 576), (767, 480), 2)
        pygame.draw.line(surface, SAND, (768, 479), (528, 479), 2)
        pygame.draw.line(surface, SAND, (527, 336), (527, 480), 2)
        pygame.draw.line(surface, SAND, (528, 335), (768, 335), 2)
        pygame.draw.line(surface, SAND, (767, 335), (767, 0), 2)

        #line 2
        pygame.draw.line(surface, SAND, (0, 335), (192, 335), 2)
        pygame.draw.line(surface, SAND, (191, 336), (191, 192), 2)
        pygame.draw.line(surface, SAND, (192, 191), (288, 191), 2)
        pygame.draw.line(surface, SAND, (287, 192), (287, 480), 2)
        pygame.draw.line(surface, SAND, (288, 479), (96, 479), 2)
        pygame.draw.line(surface, SAND, (95, 480), (95, 622), 2)
        pygame.draw.line(surface, SAND, (96, 622), (816, 622), 2)
        pygame.draw.line(surface, SAND, (815, 624), (815, 432), 2)
        pygame.draw.line(surface, SAND, (816, 431), (576, 431), 2)
        pygame.draw.line(surface, SAND, (575, 432), (575, 384), 2)
        pygame.draw.line(surface, SAND, (576, 383), (816, 383), 2)
        pygame.draw.line(surface, SAND, (815, 384), (815, 0), 2)

    def base(self): #what the player has to protect
        AHLogo = pygame.image.load('data/bananattack/ah.png').convert_alpha()
        AHLogo = pygame.transform.scale(AHLogo , (48,48))
        surface.blit(AHLogo, (768, 0))


