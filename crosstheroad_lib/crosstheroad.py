import pygame, sys, random, json
from menu_lib import slidemenu


def getMemory(key):
    with open("data/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        return data[key]

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersects(self, other):
        oleft = other.x
        oright = other.x + other.w
        otop = other.y
        obottom = other.y + other.h

        left = self.x
        right = self.x + self.w
        top = self.y
        bottom = self.y + self.h

        return (left >= oright or
                right <= oleft or
                top >= obottom or
                bottom <= otop)


class Button(Rectangle):
    def __init__(self, x, y, w, h, img, hvr_img, screen, tooltip='none'):
        Rectangle.__init__(self, x, y, w, h)
        self.img = img
        self.hvr_img = hvr_img
        self.screen = screen
        self.tooltip = tooltip
        self.font = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 30)

    def show(self):
        # Check if the button has a img for on hover
        if self.hvr_img != 'none':
            # Check if cursor is on the button
            if self.x <= pygame.mouse.get_pos()[0] <= self.x + self.w and self.y <= pygame.mouse.get_pos()[1] <= self.y + self.h:
                # If so, set the img to the hover img
                img = pygame.image.load(self.hvr_img).convert_alpha()
                # Check if the button has a tooltip
                if self.tooltip != 'none':
                    tooltip = self.font.render(self.tooltip, 1, (255, 255, 255))
                    self.screen.blit(tooltip, (self.x + self.w/2 - tooltip.get_rect().width/2, self.y - tooltip.get_rect().height - 2))
            # Else set the img to the normal one
            else:
                img = pygame.image.load(self.img).convert_alpha()
        # Else set the img to the normal one
        else:
            img = pygame.image.load(self.img).convert_alpha()
            if self.x <= pygame.mouse.get_pos()[0] <= self.x + self.w and self.y <= pygame.mouse.get_pos()[1] <= self.y + self.h and self.tooltip != 'none':
                tooltip = self.font.render(self.tooltip, 1, (255, 255, 255))
                self.screen.blit(tooltip, (self.x + self.w/2 - tooltip.get_rect().width/2, self.y - tooltip.get_rect().height - 2))

        # Display button img
        self.screen.blit(img, (self.x, self.y))


class Monkey(Rectangle):
    def __init__(self, x, y, w, h, screen, config, amount, monkeyList):
        Rectangle.__init__(self, x, y, w, h)
        self.screen = screen
        self.config = config
        self.amount = amount
        self.monkeys = monkeyList

    def show(self):
        image = pygame.image.load("data/" + getMemory("monkey").replace(".png", "_top.png"))
        image = pygame.transform.scale(image, (self.config.grid, self.config.grid))
        self.screen.blit(image, (self.x, self.y))

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
        self.state = 'Intro'
        self.dt = 0
        self.timer = 90

        # Set quit to False, so loop will continue
        self.quit = False
        self.cars = []
        self.monkeys = []

        # Define fonts
        self.font1 = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 60)
        self.font2 = pygame.font.SysFont("Helvetica", 15)
        self.font3 = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 30)
        self.font4 = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 80)
        self.font5 = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 100)

    def sideMenu(self):
        # Make sidemenu overlay
        sm = pygame.Rect(self.config.screenDim[0] - self.config.sideMenu[0], 0, self.config.sideMenu[0], self.config.sideMenu[1])
        pygame.draw.rect(self.screen, self.config.sevopblack, sm)

        # Add score to sidemenu
        text = self.font1.render("Score:", 1, self.config.white)
        score = self.font1.render(str(self.score), 1, self.config.white)

        if self.timer < 15:
            if self.timer == 0.0:
                color = self.config.white
            elif self.timer < 7.5:
                color = self.config.red
            else:
                color = self.config.orange
        else:
            color = self.config.white

        time = self.font1.render(str(self.timer), 1, color)

        self.screen.blit(score, (self.config.screenDim[0] - self.config.sideMenu[0]/2 - score.get_rect().width/2,
                                 self.config.sideMenu[1] / 2 - score.get_rect().height/2))
        self.screen.blit(text, (self.config.screenDim[0] - self.config.sideMenu[0]/2 - text.get_rect().width/2,
                                self.config.sideMenu[1] / 2 - text.get_rect().height - score.get_rect().height))
        self.screen.blit(time, (self.config.screenDim[0] - self.config.sideMenu[0]/2 - time.get_rect().width/2,
                                100))

        # Add next monkey text to sidemenu
        next = self.font3.render("Next:", 1, self.config.white)
        self.screen.blit(next, (self.config.screenDim[0] - self.config.sideMenu[0] + self.config.grid * 0.6,
                                self.config.screenDim[1] - next.get_rect().height - self.config.grid/2))

        # Add FPS to side menu IF FPS is true in settings
        if self.settings['FPS']:
            fps = self.font2.render("fps: " + str(round(self.clock.get_fps(), 3)), 1, self.config.yellow)
            self.screen.blit(fps, (self.config.screenDim[0] - fps.get_rect().width - 20,
                                   self.config.sideMenu[1] - fps.get_rect().height))

        if self.state == 'Game' :
            pauseButton = Button((self.config.screenDim[0] - self.config.sideMenu[0]) + self.config.sideMenu[0]/2 - 25,
                                450,
                                50,
                                50,
                                'crosstheroad_lib/src/pauseButton.png',
                                'crosstheroad_lib/src/pauseButton_hvr.png',
                                self.screen,
                                'Pause game')
            pauseButton.show()

            if pygame.mouse.get_pressed()[0] and pauseButton.x <= pygame.mouse.get_pos()[0] <= pauseButton.x + pauseButton.w and pauseButton.y <= pygame.mouse.get_pos()[1] <= pauseButton.y + pauseButton.h:
                self.loadPause()

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
            self.cars.append(Car(0 + (self.config.grid * 8), self.config.screenDim[1] - self.config.grid * 11, self.config.grid * 10, self.config.grid, self.screen, self.config, 30, 'crosstheroad_lib/src/train.png'))

    def blit(self):
        background = pygame.image.load("crosstheroad_lib/src/background.jpg").convert()
        self.screen.blit(background, (0, 0))

        if len(self.cars) < 27: self.addCars()
        # Debugging console info
        # print(len(self.cars))
        for index in range(len(self.cars)):
            self.cars[index].show()

        self.sideMenu()

        for index in range(len(self.monkeys)):
            self.monkeys[index].show()

    def update(self):
        # Update cars
        for index in range(len(self.cars)):
            self.cars[index].update()
        # Add the second monkey if there is only one
        if len(self.monkeys) < 2:
            monkey = getMemory("monkey")
            if monkey == "default_monkey.png":
                randomPoints = random.randrange(1, 10)
            elif monkey == "ninja_monkey.png":
                randomPoints = random.randrange(3, 12)
            elif monkey == "engineer_monkey.png":
                randomPoints = random.randrange(5, 16)
            elif monkey == "apprentice_monkey.png":
                randomPoints = random.randrange(7, 20)
            elif monkey == "dragon_monkey.png":
                randomPoints = random.randrange(10, 25)
            elif monkey == "super_monkey.png":
                randomPoints = random.randrange(15, 35)
            elif monkey == "robo_monkey.png":
                randomPoints = random.randrange(20, 50)
            else:
                randomPoints = random.randrange(1, 25)

            self.monkeys.append(Monkey((self.config.screenDim[0] - self.config.sideMenu[0])/2 - self.config.grid/2,
                                       self.config.screenDim[1]-self.config.grid,
                                       self.config.grid,
                                       self.config.grid,
                                       self.screen,
                                       self.config,
                                       randomPoints,
                                       self.monkeys))
            self.monkeys[0].place((self.config.screenDim[0] - self.config.sideMenu[0])/2 - self.config.grid/2,
                                  self.config.screenDim[1]-self.config.grid,)

        # Set the seconds monkey (next) position to the sidemenu
        if len(self.monkeys) == 2:
            self.monkeys[1].place(self.config.screenDim[0] - self.config.sideMenu[0] + self.config.grid * 2,
                                  self.config.screenDim[1] - self.config.grid)

        self.dt = self.clock.tick(self.clock.get_fps()) / 1000
        self.timer -= self.dt

        self.timer = round(self.timer, 1)
        if self.timer <= 0:
            self.state = 'TimeOver'

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

        # Reset the monkey when it reaches the finish
        if self.monkeys[0].y < 150:
            self.score += self.monkeys[0].amount
            self.monkeys[0].reset()

    def collisionDet(self):
        # Go trough all cars
        for index in range(len(self.cars)):
            # Check if the monkey is collision is not true (.intersect returns true if not colliding)
            if not self.monkeys[0].intersects(self.cars[index]):
                # Check if score is high enough to be adjusted
                if self.score > self.monkeys[0].amount:
                    self.score -= self.monkeys[0].amount
                else:
                    self.score = 0

                # Reset monkey that collided
                self.monkeys[0].reset()

    def loadPause(self):
        self.state = 'Paused'

    def loadGame(self):
        self.state = 'Game'

    def restartGame(self):
        self.score = 0
        self.timer = 90
        self.dt = 0
        self.monkeys.pop(0)
        self.monkeys.pop(0)
        self.loadGame()

    def exitGame(self):
        slidemenu.run().runm(self.score)
        self.quit = True

    def pauseOverlay(self):
        Pscreen = pygame.Surface((self.config.screenDim[0], self.config.screenDim[1]), pygame.SRCALPHA)
        Pscreen.fill((0, 0, 0, 150))

        text1 = self.font1.render("Paused", 1, self.config.white)
        Pscreen.blit(text1, ((self.config.screenDim[0] / 2) - (text1.get_rect().width / 2), 200))

        continueButton = Button(self.config.screenDim[0]/2 - 150,
                                self.config.screenDim[1] / 2 + 50,
                                50,
                                50,
                                'crosstheroad_lib/src/continueButton.png',
                                'none',
                                Pscreen,
                                'Continue game')
        continueButton.show()

        replayButton = Button(self.config.screenDim[0]/2 - 25,
                              self.config.screenDim[1]/2 + 50,
                              50,
                              50,
                              'crosstheroad_lib/src/replayButton.png',
                              'none',
                              Pscreen,
                              'Restart game')
        replayButton.show()

        exitToMenuButton = Button(self.config.screenDim[0]/2 + 100,
                                  self.config.screenDim[1] / 2 + 50,
                                  50,
                                  50,
                                  'crosstheroad_lib/src/exitToMenuButton.png',
                                  'none',
                                  Pscreen,
                                  'Exit to menu')
        exitToMenuButton.show()

        # Button functionallities
        # Continue
        if pygame.mouse.get_pressed()[0] and continueButton.x <= pygame.mouse.get_pos()[0] <= continueButton.x + continueButton.w and continueButton.y <= pygame.mouse.get_pos()[1] <= continueButton.y + continueButton.h:
            self.loadGame()
        # Replay
        if pygame.mouse.get_pressed()[0] and replayButton.x <= pygame.mouse.get_pos()[0] <= replayButton.x + replayButton.w and replayButton.y <= pygame.mouse.get_pos()[1] <= replayButton.y + replayButton.h:
            self.restartGame()
        # Exit to menu
        if pygame.mouse.get_pressed()[0] and exitToMenuButton.x <= pygame.mouse.get_pos()[0] <= exitToMenuButton.x + exitToMenuButton.w and exitToMenuButton.y <= pygame.mouse.get_pos()[1] <= exitToMenuButton.y + exitToMenuButton.h:
            self.exitGame()

        self.screen.blit(Pscreen, (0, 0))

    def introOverlay(self):
        Iscreen = pygame.Surface((self.config.screenDim[0], self.config.screenDim[1]), pygame.SRCALPHA)
        Iscreen.fill((0, 0, 0, 150))

        text1 = self.font1.render("Cross the Road", 1, self.config.white)
        Iscreen.blit(text1, (self.config.screenDim[0] / 2 - text1.get_rect().width / 2, 200))

        skipButton = Button(self.config.screenDim[0] - self.config.grid * 3,
                            self.config.screenDim[1] - self.config.grid * 2,
                            50,
                            50,
                            'crosstheroad_lib/src/skipButton.png',
                            'none',
                            Iscreen,
                            'Skip tutorial')
        skipButton.show()

        # Skip tutorial button functionality
        if pygame.mouse.get_pressed()[0] and skipButton.x <= pygame.mouse.get_pos()[0] <= skipButton.x + skipButton.w and skipButton.y <= pygame.mouse.get_pos()[1] <= skipButton.y + skipButton.h:
            self.loadGame()

        self.screen.blit(Iscreen, (0, 0))

    def timeOverlay(self):
        Pscreen = pygame.Surface((self.config.screenDim[0], self.config.screenDim[1]), pygame.SRCALPHA)
        Pscreen.fill((0, 0, 0, 150))

        text1 = self.font1.render("Time over", 1, self.config.white)
        Pscreen.blit(text1, ((self.config.screenDim[0] / 2) - (text1.get_rect().width / 2), 200))

        text2 = self.font3.render("You scored:", 1, self.config.black)

        if self.score > 85:
            font = self.font5
        else:
            font = self.font4

        text3 = font.render(str(self.score), 2, self.config.black)

        pygame.draw.circle(Pscreen,
                           self.config.yellow,
                           (self.config.screenDim[0] - 200, 300),
                           120)
        Pscreen.blit(text2, (self.config.screenDim[0] - 200 - text2.get_rect().width/2, 210))
        Pscreen.blit(text3, (self.config.screenDim[0] - 200 - text3.get_rect().width/2, 300 - text3.get_rect().height/2))

        replayButton = Button(self.config.screenDim[0]/2 - 75,
                              self.config.screenDim[1]/2 + 50,
                              50,
                              50,
                              'crosstheroad_lib/src/replayButton.png',
                              'none',
                              Pscreen,
                              'Restart game')
        replayButton.show()

        exitToMenuButton = Button(self.config.screenDim[0]/2 + 25,
                                  self.config.screenDim[1] / 2 + 50,
                                  50,
                                  50,
                                  'crosstheroad_lib/src/exitToMenuButton.png',
                                  'none',
                                  Pscreen,
                                  'Exit to menu')
        exitToMenuButton.show()

        # Button functionallities
        # Replay
        if pygame.mouse.get_pressed()[0] and replayButton.x <= pygame.mouse.get_pos()[0] <= replayButton.x + replayButton.w and replayButton.y <= pygame.mouse.get_pos()[1] <= replayButton.y + replayButton.h:
            self.restartGame()
        # Exit to menu
        if pygame.mouse.get_pressed()[0] and exitToMenuButton.x <= pygame.mouse.get_pos()[0] <= exitToMenuButton.x + exitToMenuButton.w and exitToMenuButton.y <= pygame.mouse.get_pos()[1] <= exitToMenuButton.y + exitToMenuButton.h:
            self.exitGame()

        self.screen.blit(Pscreen, (0, 0))

    def run(self):
        while not self.quit:
            if self.state == 'Game':
                self.blit()
                self.update()
                self.collisionDet()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # Set quit to True, so pygame will close
                        self.quit = True
                        pygame.quit()
                        sys.exit()
                    self.move(event)

            elif self.state == 'Paused':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # Set quit to True, so pygame will close
                        self.quit = True
                        pygame.quit()
                        sys.exit()
                self.blit()
                self.pauseOverlay()

            elif self.state == 'Intro':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # Set quit to True, so pygame will close
                        self.quit = True
                        pygame.quit()
                        sys.exit()
                self.blit()
                self.introOverlay()

            elif self.state == 'TimeOver':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # Set quit to True, so pygame will close
                        self.quit = True
                        pygame.quit()
                        sys.exit()
                self.blit()
                self.timeOverlay()

            self.clock.tick(30)
            pygame.display.update()

