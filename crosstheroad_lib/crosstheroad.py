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
            if not self.x == self.config.screenDim[0] - self.config.grid - self.config.sideMenu[0]:
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
        self.state = "alive"

    def update(self):
        self.x = self.x + self.speed

        if self.x > self.config.screenDim[0] - self.config.sideMenu[0] and self.speed > 0:
            self.x = - self.w

        if self.x + self.w < 0 and self.speed < 0:
            self.x = self.config.screenDim[0] + self.w - self.config.sideMenu[0]

    def show(self):
        cr = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.config.green, cr)


class Crosstheroad:
    def __init__(self, screen, config):
        self.clock = pygame.time.Clock()
        self.config = config
        self.screen = screen
        self.state = "alive"

        # Set quit to False, so loop will continue
        self.quit = False
        self.monkey = Monkey((self.config.screenDim[0] - self.config.sideMenu[0])/2 - self.config.grid/2, self.config.screenDim[1]-self.config.grid, self.config.grid, self.config.grid, self.screen, self.config)
        self.cars = []
        self.i = 0

    def sideMenu(self):
        sm = pygame.Rect(self.config.screenDim[0] - self.config.sideMenu[0], 0, self.config.sideMenu[0], self.config.sideMenu[1])
        pygame.draw.rect(self.screen, self.config.yellow, sm)
        font = pygame.font.SysFont("helvetica", 15)
        state = font.render(self.state, 1, self.config.black)
        self.screen.blit(state, (self.config.screenDim[0] - self.config.sideMenu[0]/2 - state.get_rect().width, self.config.sideMenu[1] - 100))

    def addCars(self):
        # Add first row of cars
        if len(self.cars) < 3:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 2, self.config.grid * 2, self.config.grid, self.screen, self.config, 4))
            self.cars.append(Car(0 + (self.config.grid * 7), self.config.screenDim[1] - self.config.grid * 2, self.config.grid * 2, self.config.grid, self.screen, self.config, 4))
            self.cars.append(Car(0 + (self.config.grid * 16), self.config.screenDim[1] - self.config.grid * 2, self.config.grid * 2, self.config.grid, self.screen, self.config, 4))
        # Add second row of cars
        if len(self.cars) < 7:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.25))
            self.cars.append(Car(0 + (self.config.grid * 3), self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.25))
            self.cars.append(Car(0 + (self.config.grid * 9), self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.25))
            self.cars.append(Car(0 + (self.config.grid * 15), self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.25))
        # Add third row of cars (busses)
        if len(self.cars) < 9:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 4, self.config.grid * 3, self.config.grid, self.screen, self.config, 2.2))
            self.cars.append(Car(0 + (self.config.grid * 8), self.config.screenDim[1] - self.config.grid * 4, self.config.grid * 3, self.config.grid, self.screen, self.config, 2.2))
        # Add forth row of cars
        if len(self.cars) < 13:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.75))
            self.cars.append(Car(0 + (self.config.grid * 3), self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.75))
            self.cars.append(Car(0 + (self.config.grid * 9), self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.75))
            self.cars.append(Car(0 + (self.config.grid * 14), self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -3.75))

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
        self.sideMenu()

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
            if not self.monkey.intersects(self.cars[index].x, self.cars[index].y, self.cars[index].w, self.cars[index].h):
                self.state = "died"

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
