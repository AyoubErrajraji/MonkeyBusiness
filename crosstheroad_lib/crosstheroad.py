import pygame, sys
from random import randint


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersects(self, x, y, w, h):
        oleft = x
        oright = x + w
        otop = y
        obottom = y + h

        left = self.x
        right = self.x + self.w
        top = self.y
        bottom = self.y + self.h

        return (left > oright or
                right < oleft or
                top > obottom or
                bottom < otop)


class Monkey(Rectangle):
    def __init__(self, x, y, w, h, screen, config):
        Rectangle.__init__(self, x, y, w, h)
        self.screen = screen
        self.config = config

    def show(self):
        mr = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.config.blue, mr)

    def move(self, xdir, ydir):
            self.y += ydir * self.config.grid
            self.x += xdir * self.config.grid


class Car(Rectangle):
    def __init__(self, x, y, w, h, screen, config):
        Rectangle.__init__(self, x, y, w, h)
        self.screen = screen
        self.config = config
        self.speed = 4

    def update(self):
        self.x = self.x + self.speed

        if self.x > self.config.screenDim[0]:
            self.x = - self.w

    def show(self):
        cr = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.config.green, cr)


class Crosstheroad:
    def __init__(self, screen, config):
        self.clock = pygame.time.Clock()
        self.config = config
        self.screen = screen

        # Set quit to False, so loop will continue
        self.quit = False
        self.monkey = Monkey(self.config.screenDim[0]/2 - self.config.grid/2, self.config.screenDim[1]-self.config.grid, self.config.grid, self.config.grid, self.screen, self.config)
        self.car = []
        self.i = 0

    def addCars(self):
        if self.config.cars > self.i:
            print(randint(0, 3))
            self.car.append(Car(0 - (self.i * (self.config.grid*2)) - (self.i * (self.config.grid * randint(1, 4))), self.config.screenDim[1]-self.config.grid*2, self.config.grid*2, self.config.grid, self.screen, self.config))
            self.i = self.i + 1
            print("Added car to carlist")

    def background(self, color):
        self.screen.fill(color)

    def blit(self):
        self.background(self.config.yellow)
        self.monkey.show()
        self.addCars()
        for index in range(len(self.car)):
            self.car[index].show()
            self.car[index].update()

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            print("Key Left pressed")
            self.monkey.move(-1, 0)
        elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            print("Key Right pressed")
            self.monkey.move(1, 0)
        elif pygame.key.get_pressed()[pygame.K_UP] != 0:
            print("Key Up pressed")
            self.monkey.move(0, -1)
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            print("Key Down pressed")
            self.monkey.move(0, 1)


    def run(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Set quit to True, so pygame will close
                    self.quit = True
                    pygame.quit()
                    sys.exit()
                self.update()

            self.blit()
            pygame.display.update()
