import sys, random
from menu_lib import slidemenu
from pygame import *

from crosstheroad_lib.button import *
from crosstheroad_lib.monkey import *
from crosstheroad_lib.car import *

def appUnlocked(key):
    unlocked = getMemory('unlocked')
    unlocked.append(key)

    with open("data/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        data['unlocked'] = unlocked
        jsonFile.seek(0)
        json.dump(data, jsonFile)
        jsonFile.truncate()

def getSettings(key):
    with open("crosstheroad_lib/settings.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        return data[key]

def setSettings(key, value):
    with open("crosstheroad_lib/settings.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data[key] = value

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()

def setMemory(key, value):
    with open("data/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data[key] = value

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()


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

    def RoundedRect(self, surface, rect, color, radius=0.4):
        """
        RoundedRect(surface,rect,color,radius=0.4)

        surface : destination
        rect    : rectangle
        color   : rgb or rgba
        radius  : 0 <= radius <= 1
        """

        rect = Rect(rect)
        color = Color(*color)
        alpha = color.a
        color.a = 0
        pos = rect.topleft
        rect.topleft = 0, 0
        rectangle = Surface(rect.size, SRCALPHA)

        circle = Surface([min(rect.size) * 3] * 2, SRCALPHA)
        draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
        circle = transform.smoothscale(circle, [int(min(rect.size) * radius)] * 2)

        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)

        rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
        rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

        rectangle.fill(color, special_flags=BLEND_RGBA_MAX)
        rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)

        return surface.blit(rectangle, pos)

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
        if getSettings('FPS'):
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

        # Set the second's monkey (next) position to the sidemenu
        if len(self.monkeys) == 2:
            self.monkeys[1].place(self.config.screenDim[0] - self.config.sideMenu[0] + self.config.grid * 2,
                                  self.config.screenDim[1] - self.config.grid)

        self.dt = self.clock.tick(self.clock.get_fps()) / 1000
        self.timer -= self.dt

        self.timer = round(self.timer, 1)
        if self.timer <= 0:
            if 4 not in getMemory('unlocked'):
                appUnlocked(4)

            points = getMemory('balance')
            setMemory('balance', points + self.score)
            
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

            pygame.mixer.music.load("crosstheroad_lib/src/sounds/succes.mp3")
            pygame.mixer.music.play()

            pygame.time.wait(100)
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
                    self.state = 'GameOver'

                # Reset monkey that collided
                self.monkeys[0].reset()

                pygame.mixer.music.load("crosstheroad_lib/src/sounds/killed.mp3")
                pygame.mixer.music.play()

    def loadPause(self):
        self.state = 'Paused'

    def loadGame(self):
        self.state = 'Game'

    def restartGame(self):
        self.score = 0
        self.timer = 90
        self.dt = 0
        if len(self.monkeys) > 0:
            self.monkeys.pop(0)
        if len(self.monkeys) > 0:
            self.monkeys.pop(0)
        self.loadGame()

    def exitGame(self):
        slidemenu.run().runm()
        self.quit = True

    def toggleFPS(self):
        if getSettings('FPS'):
            setSettings('FPS', False)
        else:
            setSettings('FPS', True)

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

        text2 = self.font1.render("FPS:", 1, self.config.white)

        Pscreen.blit(text2,
                     ((self.config.screenDim[0] / 2 - text2.get_rect().width/2 - 10) - (text1.get_rect().width / 2),
                      600))

        if getSettings('FPS'):
            fpsButton = Button(self.config.screenDim[0]/2 + 10,
                               600,
                               50,
                               50,
                               'crosstheroad_lib/src/toggle.png',
                               'none',
                               Pscreen,
                               '')
        else:
            fpsButton = Button(self.config.screenDim[0] / 2 + 10,
                               600,
                               50,
                               50,
                               'crosstheroad_lib/src/toggle_active.png',
                               'none',
                               Pscreen,
                               '')
        fpsButton.show()

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
        # Toggle FPS
        if pygame.mouse.get_pressed()[0] and fpsButton.x <= pygame.mouse.get_pos()[0] <= fpsButton.x + fpsButton.w and fpsButton.y <= pygame.mouse.get_pos()[1] <= fpsButton.y + fpsButton.h:
            self.toggleFPS()

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
                            'Start game')
        skipButton.show()

        rr_w = 800
        rr_h = 350
        rr_c = (100, 100, 100)

        self.RoundedRect(self.screen, (self.config.screenDim[0] / 2 - rr_w / 2,
                                       280, rr_w, rr_h), rr_c, 0.05)

        discriptionIcon = Button(self.config.screenDim[0] / 2 - rr_w / 2 + 20, 300,
                                 50, 50,
                                 'crosstheroad_lib/src/discription.png', 'none',
                                 Iscreen, 'none')
        discriptionIcon.show()

        pygame.draw.line(Iscreen, self.config.white,
                         (self.config.screenDim[0]/2 - rr_w/2 + 20, 355),
                         (self.config.screenDim[0]/2 + rr_w/2 - 20, 355), 2)

        text2 = self.font3.render("Discription", 1, self.config.white)
        Iscreen.blit(text2, (self.config.screenDim[0] / 2 - rr_w / 2 + 70, 310))

        disc1 = self.font3.render("The goal is to get to the other side of the road. To get there,", 1, self.config.white)
        disc2 = self.font3.render("use the arrow keys on the keyboard. The better monkey you", 1, self.config.white)
        disc3 = self.font3.render("have, the more points you can get", 1, self.config.white)

        disc4 = self.font3.render("You have 90 seconds to play the game. If the 90 seconds", 1, self.config.white)
        disc5 = self.font3.render("run out, you get the option to go back to the menu and", 1, self.config.white)
        disc6 = self.font3.render("play th next game or relay the game. The score is", 1, self.config.white)
        disc7 = self.font3.render("saved in both cases.", 1, self.config.white)
        disc8 = self.font3.render("You can enable/disable the FPS counter in the pause menu.", 1, self.config.white)

        Iscreen.blit(disc1, (self.config.screenDim[0] / 2 - rr_w / 2 + 20, 365))
        Iscreen.blit(disc2, (self.config.screenDim[0] / 2 - rr_w / 2 + 20, 392))
        Iscreen.blit(disc3, (self.config.screenDim[0] / 2 - rr_w / 2 + 20, 419))

        Iscreen.blit(disc4, (self.config.screenDim[0] / 2 - rr_w / 2 + 20, 471))
        Iscreen.blit(disc5, (self.config.screenDim[0] / 2 - rr_w / 2 + 20, 498))
        Iscreen.blit(disc6, (self.config.screenDim[0] / 2 - rr_w / 2 + 20, 525))
        Iscreen.blit(disc7, (self.config.screenDim[0] / 2 - rr_w / 2 + 20, 552))
        Iscreen.blit(disc8, (self.config.screenDim[0] / 2 - rr_w / 2 + 20, 579))


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

    def gameOverlay(self):
        Pscreen = pygame.Surface((self.config.screenDim[0], self.config.screenDim[1]), pygame.SRCALPHA)
        Pscreen.fill((0, 0, 0, 150))

        text1 = self.font1.render("Game over", 1, self.config.white)
        Pscreen.blit(text1, ((self.config.screenDim[0] / 2) - (text1.get_rect().width / 2), 200))

        replayButton = Button(self.config.screenDim[0] / 2 - 75,
                              self.config.screenDim[1] / 2 + 50,
                              50,
                              50,
                              'crosstheroad_lib/src/replayButton.png',
                              'none',
                              Pscreen,
                              'Restart game')
        replayButton.show()

        exitToMenuButton = Button(self.config.screenDim[0] / 2 + 25,
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
        if pygame.mouse.get_pressed()[0] and replayButton.x <= pygame.mouse.get_pos()[
            0] <= replayButton.x + replayButton.w and replayButton.y <= pygame.mouse.get_pos()[
            1] <= replayButton.y + replayButton.h:
            self.restartGame()
        # Exit to menu
        if pygame.mouse.get_pressed()[0] and exitToMenuButton.x <= pygame.mouse.get_pos()[
            0] <= exitToMenuButton.x + exitToMenuButton.w and exitToMenuButton.y <= pygame.mouse.get_pos()[
            1] <= exitToMenuButton.y + exitToMenuButton.h:
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
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.loadPause()

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
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.loadGame()
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

            elif self.state == 'GameOver':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # Set quit to True, so pygame will close
                        self.quit = True
                        pygame.quit()
                        sys.exit()
                self.blit()
                self.gameOverlay()

            self.clock.tick(60)
            pygame.display.update()

