import pygame, sys, random


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


class Button(Rectangle):
    def __int__(self, x, y, w, h, img, hvr_img, screen):
        Rectangle.__init__(self, x, y, w, h)
        self.img = img
        self.hvr_img = hvr_img
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen

    def show(self):
        img = pygame.image.load(self.img).convert_alpha()
        self.screen.blit(img, (self.x, self.y))


class Monkey(Rectangle):
    def __init__(self, x, y, w, h, screen, config, amount, monkeyList):
        Rectangle.__init__(self, x, y, w, h)
        self.screen = screen
        self.config = config
        self.amount = amount
        self.monkeys = monkeyList

    def show(self):
        mr = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.config.blue, mr)
        pygame.draw.circle(self.screen, self.config.yellow, (int(self.x + self.w), int(self.y)), self.config.circle_radius)
        font = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 20)
        amount = font.render(str(self.amount), False, self.config.black)
        self.screen.blit(amount, (int(self.x + self.w - amount.get_rect().width/2), int(self.y - amount.get_rect().height/2)))

    def place(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.monkeys.pop(0)

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
    def __init__(self, x, y, w, h, screen, config, speed, img):
        Rectangle.__init__(self, x, y, w, h)
        self.screen = screen
        self.config = config
        self.speed = speed
        self.img = img

    def update(self):
        self.x = self.x + self.speed

        if self.x > self.config.screenDim[0] - self.config.sideMenu[0] and self.speed > 0:
            self.x = - self.w

        if self.x + self.w < 0 and self.speed < 0:
            self.x = self.config.screenDim[0] + self.w - self.config.sideMenu[0]

    def show(self):
        if self.img == 'none':
            cr = pygame.Rect(self.x, self.y, self.w, self.h)
            pygame.draw.rect(self.screen, self.config.green, cr)
        else:
            img = pygame.image.load(self.img).convert_alpha()
            self.screen.blit(img, (self.x, self.y))


class Crosstheroad:
    def __init__(self, screen, config, settings):
        self.clock = pygame.time.Clock()
        self.config = config
        self.screen = screen
        self.score = 0
        self.settings = settings

        # Set quit to False, so loop will continue
        self.quit = False
        self.cars = []
        self.monkeys = []

    def sideMenu(self):
        sm = pygame.Rect(self.config.screenDim[0] - self.config.sideMenu[0], 0, self.config.sideMenu[0], self.config.sideMenu[1])
        pygame.draw.rect(self.screen, self.config.sevopblack, sm)
        font1 = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 60)
        font2 = pygame.font.SysFont("Helvetica", 15)
        score = font1.render(str(self.score), 1, self.config.white)
        self.screen.blit(score, (self.config.screenDim[0] - self.config.sideMenu[0]/2 - score.get_rect().width/2, self.config.sideMenu[1] / 2 - score.get_rect().height/2))
        if self.settings['FPS']:
            fps = font2.render("fps: " + str(round(self.clock.get_fps(), 3)), 1, self.config.yellow)
            self.screen.blit(fps, (self.config.screenDim[0] - fps.get_rect().width - 20, self.config.sideMenu[1] - fps.get_rect().height))

    def addCars(self):
        # Add first row of cars
        if len(self.cars) < 3:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 2, self.config.grid * 2, self.config.grid, self.screen, self.config, 6, 'crosstheroad_lib/src/car1_r.png'))
            self.cars.append(Car(0 + (self.config.grid * 7), self.config.screenDim[1] - self.config.grid * 2, self.config.grid * 2, self.config.grid, self.screen, self.config, 6, 'crosstheroad_lib/src/car3_r.png'))
            self.cars.append(Car(0 + (self.config.grid * 16), self.config.screenDim[1] - self.config.grid * 2, self.config.grid * 2, self.config.grid, self.screen, self.config, 6, 'crosstheroad_lib/src/car4_r.png'))
        # Add second row of cars
        if len(self.cars) < 7:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -4, 'crosstheroad_lib/src/car5.png'))
            self.cars.append(Car(0 + (self.config.grid * 3), self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -4, 'crosstheroad_lib/src/car4.png'))
            self.cars.append(Car(0 + (self.config.grid * 9), self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -4, 'crosstheroad_lib/src/car1.png'))
            self.cars.append(Car(0 + (self.config.grid * 15), self.config.screenDim[1] - self.config.grid * 3, self.config.grid * 2, self.config.grid, self.screen, self.config, -4, 'crosstheroad_lib/src/car3.png'))
        # Add third row of cars (busses)
        if len(self.cars) < 9:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 4, self.config.grid * 3, self.config.grid, self.screen, self.config, 3, 'crosstheroad_lib/src/bus1_r.png'))
            self.cars.append(Car(0 + (self.config.grid * 8), self.config.screenDim[1] - self.config.grid * 4, self.config.grid * 3, self.config.grid, self.screen, self.config, 3, 'crosstheroad_lib/src/bus2_r.png'))
        # Add forth row of cars
        if len(self.cars) < 13:
            self.cars.append(Car(0, self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -4.75, 'crosstheroad_lib/src/car6.png'))
            self.cars.append(Car(0 + (self.config.grid * 3), self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -4.75, 'crosstheroad_lib/src/car7.png'))
            self.cars.append(Car(0 + (self.config.grid * 9), self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -4.75, 'crosstheroad_lib/src/car3.png'))
            self.cars.append(Car(0 + (self.config.grid * 14), self.config.screenDim[1] - self.config.grid * 5, self.config.grid * 2, self.config.grid, self.screen, self.config, -4.75, 'crosstheroad_lib/src/car5.png'))
        # Add sixth row of cars (busses), 5th is safe
        if len(self.cars) < 17:
            self.cars.append(Car(0 + self.config.grid, self.config.screenDim[1] - self.config.grid * 7, self.config.grid * 2, self.config.grid, self.screen, self.config, 4.5, 'crosstheroad_lib/src/car4_r.png'))
            self.cars.append(Car(0 + (self.config.grid * 6), self.config.screenDim[1] - self.config.grid * 7, self.config.grid * 2, self.config.grid, self.screen, self.config, 4.5, 'crosstheroad_lib/src/car6_r.png'))
            self.cars.append(Car(0 + (self.config.grid * 10), self.config.screenDim[1] - self.config.grid * 7, self.config.grid * 2, self.config.grid, self.screen, self.config, 4.5, 'crosstheroad_lib/src/car3_r.png'))
            self.cars.append(Car(0 + (self.config.grid * 16), self.config.screenDim[1] - self.config.grid * 7, self.config.grid * 2, self.config.grid, self.screen, self.config, 4.5, 'crosstheroad_lib/src/car2_r.png'))
        # Add 7th row of cars (busses)
        if len(self.cars) < 19:
            self.cars.append(Car(0 + (self.config.grid * 3), self.config.screenDim[1] - self.config.grid * 8, self.config.grid * 3, self.config.grid, self.screen, self.config, -2.75, 'crosstheroad_lib/src/bus1.png'))
            self.cars.append(Car(0 + (self.config.grid * 12), self.config.screenDim[1] - self.config.grid * 8, self.config.grid * 3, self.config.grid, self.screen, self.config, -2.75, 'crosstheroad_lib/src/bus1.png'))
        # Add 8th row of cars
        if len(self.cars) < 22:
            self.cars.append(Car(0 + (self.config.grid * 2), self.config.screenDim[1] - self.config.grid * 9, self.config.grid * 2, self.config.grid, self.screen, self.config, 6, 'crosstheroad_lib/src/car1_r.png'))
            self.cars.append(Car(0 + (self.config.grid * 9), self.config.screenDim[1] - self.config.grid * 9, self.config.grid * 2, self.config.grid, self.screen, self.config, 6, 'crosstheroad_lib/src/car2_r.png'))
            self.cars.append(Car(0 + (self.config.grid * 16), self.config.screenDim[1] - self.config.grid * 9, self.config.grid * 2, self.config.grid, self.screen, self.config, 6, 'crosstheroad_lib/src/car3_r.png'))
        # Add 9th row of cars
        if len(self.cars) < 26:
            self.cars.append(Car(0 + self.config.grid, self.config.screenDim[1] - self.config.grid * 10, self.config.grid * 2, self.config.grid, self.screen, self.config, -5, 'crosstheroad_lib/src/car4.png'))
            self.cars.append(Car(0 + (self.config.grid * 6), self.config.screenDim[1] - self.config.grid * 10, self.config.grid * 2, self.config.grid, self.screen, self.config, -5, 'crosstheroad_lib/src/car5.png'))
            self.cars.append(Car(0 + (self.config.grid * 10), self.config.screenDim[1] - self.config.grid * 10, self.config.grid * 2, self.config.grid, self.screen, self.config, -5, 'crosstheroad_lib/src/car4.png'))
            self.cars.append(Car(0 + (self.config.grid * 16), self.config.screenDim[1] - self.config.grid * 10, self.config.grid * 2, self.config.grid, self.screen, self.config, -5, 'crosstheroad_lib/src/car7.png'))
        # Add 10th row (last) of cars
        if len(self.cars) < 27:
            self.cars.append(Car(0 + (self.config.grid * 8), self.config.screenDim[1] - self.config.grid * 11, self.config.grid * 10, self.config.grid, self.screen, self.config, 25, 'crosstheroad_lib/src/train.png'))

    def background(self, color):
        self.screen.fill(color)

    def blit(self):
        background = pygame.image.load("crosstheroad_lib/src/background.jpg").convert()
        self.screen.blit(background, (0,0))
        self.addCars()
        # Debugging console info
        # print(len(self.cars))
        for index in range(len(self.cars)):
            self.cars[index].show()
            self.cars[index].update()
        self.sideMenu()
        for index in range(len(self.monkeys)):
            self.monkeys[index].show()

    def update(self):
        if len(self.monkeys) < 2:
            self.monkeys.append(Monkey((self.config.screenDim[0] - self.config.sideMenu[0])/2 - self.config.grid/2,
                                       self.config.screenDim[1]-self.config.grid,
                                       self.config.grid,
                                       self.config.grid,
                                       self.screen,
                                       self.config,
                                       random.randrange(1, 20),
                                       self.monkeys))
        # self.monkeys[1].place((self.config.screenDim[0] - self.config.sideMenu[0])/2 - self.config.grid/2 + self.config.grid,self.config.screenDim[1] - self.config.grid)

    def move(self, e):
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            # print("Key Left pressed")
            self.monkeys[0].move(-1, 0)
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            # print("Key Right pressed")
            self.monkeys[0].move(1, 0)
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            # print("Key Up pressed")
            self.monkeys[0].move(0, -1)
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            # print("Key Down pressed")
            self.monkeys[0].move(0, 1)
        if self.monkeys[0].y < 150:
            self.score += self.monkeys[0].amount
            self.monkeys[0].reset()

    def collisionDet(self):
        for index in range(len(self.cars)):
            if not self.monkeys[0].intersects(self.cars[index].x, self.cars[index].y, self.cars[index].w, self.cars[index].h):
                if self.score > self.monkeys[0].amount:
                    self.score -= self.monkeys[0].amount
                else:
                    self.score = 0
                self.monkeys[0].reset()

    def run(self):
        while not self.quit:
            self.collisionDet()
            self.clock.tick(30)

            self.blit()
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Set quit to True, so pygame will close
                    self.quit = True
                    pygame.quit()
                    sys.exit()
                self.move(event)
            pygame.display.update()