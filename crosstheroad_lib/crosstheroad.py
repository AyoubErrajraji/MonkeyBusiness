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

        return (left >= oright or
                right <= oleft or
                top >= obottom or
                bottom <= otop)


class Monkey(Rectangle):
    def __init__(self, x, y, w, h, screen, config):
        Rectangle.__init__(self, x, y, w, h)
        self.screen = screen
        self.config = config

    def show(self):
        mr = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.config.blue, mr)

    def move(self, xdir, ydir):
        if xdir == -1:
            if not self.x == 0:
                self.x += xdir * self.config.grid
        elif xdir == 1:
            if not self.x == self.config.screenDim[0] - self.config.grid:
                self.x += xdir * self.config.grid
        elif ydir == -1:
            if not self.y == 0:
                self.y += ydir * self.config.grid
        elif ydir == 1:
            if not self.y == self.config.screenDim[1] - self.config.grid:
                self.y += ydir * self.config.grid


class Car(Rectangle):
    def __init__(self, x, y, w, h, screen, config, speed):
        Rectangle.__init__(self, x, y, w, h)
        self.screen = screen
        self.config = config
        self.speed = speed

    def update(self):
        self.x = self.x + self.speed

        if self.x > self.config.screenDim[0] and self.speed > 0:
            self.x = - self.w

        if self.x + self.w < 0 and self.speed < 0:
            self.x = self.config.screenDim[0] + self.w

    def show(self):
        cr = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.config.green, cr)

    def xcoord(self):
        return self.x

    def ycoord(self):
        return self.y

    def width(self):
        return self.w

    def heigth(self):
        return self.h


class Crosstheroad:
    def __init__(self, screen, config):
        self.clock = pygame.time.Clock()
        self.config = config
        self.screen = screen

        # Set quit to False, so loop will continue
        self.quit = False
        self.monkey = Monkey(self.config.screenDim[0]/2 - self.config.grid/2, self.config.screenDim[1]-self.config.grid, self.config.grid, self.config.grid, self.screen, self.config)
        self.cars = []
        self.i = 0

    def addCars(self):
        # Add first row of cars
        if len(self.cars) < 3:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 2, self.config.grid * 2, self.config.grid, self.screen, self.config, 3.25))
            self.cars.append(Car(0 + (self.config.grid * 7), self.config.screenDim[1] - self.config.grid * 2, self.config.grid * 2, self.config.grid, self.screen, self.config, 3.25))
            self.cars.append(Car(0 + (self.config.grid * 16), self.config.screenDim[1] - self.config.grid * 2, self.config.grid * 2, self.config.grid, self.screen, self.config, 3.25))
        # Add second row of cars
        if len(self.cars) < 7:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -2.75))
            self.cars.append(Car(0 + (self.config.grid * 3), self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -2.75))
            self.cars.append(Car(0 + (self.config.grid * 9), self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -2.75))
            self.cars.append(Car(0 + (self.config.grid * 15), self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -2.75))
        # Add third row of cars (busses)
        if len(self.cars) < 9:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 4, self.config.grid * 3, self.config.grid, self.screen, self.config, 1.8))
            self.cars.append(Car(0 + (self.config.grid * 8), self.config.screenDim[1] - self.config.grid * 4, self.config.grid * 3, self.config.grid, self.screen, self.config, 1.8))
        # Add forth row of cars
        if len(self.cars) < 13:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.25))
            self.cars.append(Car(0 + (self.config.grid * 3), self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.25))
            self.cars.append(Car(0 + (self.config.grid * 9), self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.25))
            self.cars.append(Car(0 + (self.config.grid * 14), self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.25))

    def background(self, color):
        self.screen.fill(color)

    def blit(self):
        self.background(self.config.black)
        self.monkey.show()
        self.addCars()
        # Debugging console info
        # print(len(self.cars))
        for index in range(len(self.cars)):
            self.cars[index].show()
            self.cars[index].update()

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            # print("Key Left pressed")
            self.monkey.move(-1, 0)
        elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            # print("Key Right pressed")
            self.monkey.move(1, 0)
        elif pygame.key.get_pressed()[pygame.K_UP] != 0:
            # print("Key Up pressed")
            self.monkey.move(0, -1)
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            # print("Key Down pressed")
            self.monkey.move(0, 1)

    def collisionDet(self):
        for index in range(len(self.cars)):
            if not self.monkey.intersects(self.cars[index].xcoord(), self.cars[index].ycoord(), self.cars[index].width(), self.cars[index].heigth()):
                print("You died")

    def run(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Set quit to True, so pygame will close
                    self.quit = True
                    pygame.quit()
                    sys.exit()
                self.update()
            self.collisionDet()
            self.clock.tick(30)

            self.blit()
            pygame.display.update()
