#Project 2 v1.00
import pygame, sys, time
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
count = 5
count2 = 15



def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

class run(object):
    font = pygame.font.SysFont("helvetica", 64)


    def runm(self,resolution=(1280,720)):
        pygame.init()
        fase = 0
        duration = 5000
        win = projectWin(500, 500, 'MonkeyWar')
        Quit = False
        seconds = 15
        seconds2 = 15
        timestart = 0
        secondMonkey = Monkey(1080, "data/monkeywar/tankl.png", "ARROWS")
        firstMonkey = Monkey(100, "data/monkeywar/tankr.png","WASD")
        space = pygame.key.get_pressed()[pygame.K_SPACE]
        self.running = 0



        while not Quit:
            # get Mouse
            mouse = pygame.mouse.get_pos()

            #FPS
            clock.tick(60)

            # set Background
            surface.blit(pygame.transform.scale(pygame.image.load('data/monkeywar/bg.png').convert(), (1280, 720)),
                         (0, 0))



            #call classes
            win.ground()
            if timestart == 1:
                if fase == 1:
                    secondMonkey.move()
                    firstMonkey.move()

            if timestart ==2:
                if fase == 2:
                    secondMonkey.aim()
                    firstMonkey.aim()
                    secondMonkey.crosshair()
                    firstMonkey.crosshair()

            if fase ==3:
                secondMonkey.shoot()
                firstMonkey.shoot()

            if fase ==4:
                firstMonkey.pause()
                secondMonkey.pause()

            #Display time fase 1
            if fase <= 1:
                temp_surface = self.font.render(str(seconds), 1, BLACK)
                surface.blit(temp_surface, (620, 100))  # print how many seconds
                if pygame.key.get_pressed()[pygame.K_SPACE] and fase < 1:
                    timestart = 1
                    self.running = 1
                    start_ticks = pygame.time.get_ticks()  # starter tick
                    fase = 1

                if self.running == 1:
                    # Timer 
                    start = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
                    seconds = round(count - start)
                    #print(self.running)
                    pygame.display.update()
                    if seconds <= 0:  # if less than 0 seconds run next phase
                        fase = 2





                # Display time fase 2
            if fase == 2:
                temp_surface = self.font.render(str(seconds2), 1, BLACK)
                surface.blit(temp_surface, (620, 100))  # print how many seconds
                if fase == 2:
                    timestart = 2
                    self.running = 2

                if self.running == 2:
                    # Timer2
                    current_tick= pygame.time.get_ticks()
                    start2 = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
                    seconds2 = round(count2+count - start2)
                    pygame.display.update()
                    if seconds2 <= 0:  # if less than 0 seconds run next phase
                        fase = 3

                # pause
                if pygame.key.get_pressed()[pygame.K_p]:
                    fase = 4
                    temp_surface = self.font.render(str(seconds), 1, BLACK)
                    surface.blit(temp_surface, (620, 100))  # print how many seconds

                if pygame.key.get_pressed()[pygame.K_SPACE] and fase == 4:
                    fase = 1

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
        self.y = 478
        self.image = image
        self.movement = movement

        self.crossx = self.x + 55
        self.crossy = 528

        self.range = 150


    def halfcircle(self, position):
        pygame.draw.circle(surface, BLACK, (position), self.range, 3)


    def schuin(self, x, y):
        return round((x**2 + y**2)**(1/2))

    def correctX(self, x, crossx):
        if x >= crossx:
            return (x + 55) - crossx
        else:
            return crossx - (x + 55)

    def correctY(self, y, crossy):
        if y < crossy:
            return crossy - y + 40
        else:
            return y - crossy + 40

    def crosshair(self):
        keyinput = pygame.key.get_pressed()

        if self.movement == "ARROWS":
            if keyinput[pygame.K_LEFT]:
                print(self.schuin(self.correctX(self.x, self.crossx) - 10, self.correctY(self.y, self.crossy)))
                if self.schuin(self.correctX(self.x, self.crossx) - 10, self.correctY(self.y, self.crossy)) < self.range:
                    self.crossx -= 10
            if keyinput[pygame.K_RIGHT]:
                if self.schuin(self.correctX(self.x, self.crossx) + 10, self.correctY(self.y, self.crossy)) < self.range:
                    self.crossx += 10
            if keyinput[pygame.K_UP]:
                if self.schuin(self.correctX(self.x, self.crossx), self.correctY(self.y, self.crossy) - 10) < self.range:
                    self.crossy -= 10
            if keyinput[pygame.K_DOWN]:
                if self.schuin(self.correctX(self.x, self.crossx), self.correctY(self.y, self.crossy) + 10) < self.range:
                    self.crossy += 10


        if self.movement == "WASD":
            if keyinput[pygame.K_a]:
                if self.schuin(self.crossx - 10, self.crossy) < self.range:
                    self.crossx -= 10
            if keyinput[pygame.K_d]:
                if self.schuin(self.crossx + 10, self.crossy) < self.range:
                    self.crossx += 10
            if keyinput[pygame.K_w]:
                if self.schuin(self.crossx, self.crossy - 10) < self.range:
                    self.crossy -= 10
            if keyinput[pygame.K_s]:
                if self.schuin(self.crossx, self.crossy + 10) < self.range:
                    self.crossy += 10

        pygame.draw.circle(surface, BLACK, (self.crossx, self.crossy), 5, 0)


    def draw(self, position):
        sprite = pygame.image.load(self.image).convert_alpha()
        surface.blit(pygame.transform.scale(sprite, (110, 80)), position)

    def pause(self):
        keyinput = pygame.key.get_pressed()

        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        pygame.draw.rect(surface, BLACK, (550, 478, 200, 100), 0)
        self.draw((self.x, 478))


    def aim(self):


        keyinput = pygame.key.get_pressed()

        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit


        self.draw((self.x, 478))
        self.halfcircle((self.x+55, 558))

    def shoot(self):
        keyinput = pygame.key.get_pressed()

        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        self.draw((self.x, 478))

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

        self.crossx = self.x + 55

        self.draw((self.x,478))















