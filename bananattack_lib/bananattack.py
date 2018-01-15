'''
Created on Nov 25, 2017
@author: lexdewilligen
'''
import pygame
import json
from bananattack_lib import config
from bananattack_lib import game
from bananattack_lib import button
from bananattack_lib import enemy
from bananattack_lib import monkey
from bananattack_lib import draw

class BananAttack(game.Game):
    def __init__(self, name, screen_width, screen_height, screen = None):
        ### setup data members and the screen ###
        game.Game.__init__(self, name, screen_width, screen_height, screen)

        ### Set state to playing ###
        self.state = config.BA_STARTING
        self.last_state = config.BA_STARTING

        ### Start Music ###
        pygame.mixer.music.load('data/bananattack/SBM.mp3')
        pygame.mixer.music.play()

        ### Enemy setup ###
        self.enemies = [
            [],
            [enemy.Enemy()],
            [enemy.Enemy()],
            [enemy.Enemy()],
            [enemy.Enemy(), enemy.Enemy()],
            [enemy.Enemy(), enemy.Enemy()],
            [enemy.Enemy(), enemy.Enemy()],
            [enemy.Enemy(), enemy.Enemy(), enemy.Enemy()],
            [enemy.Enemy(), enemy.Enemy(), enemy.Enemy()],
            [enemy.Enemy(), enemy.Enemy(), enemy.Enemy(), enemy.Enemy(), enemy.Enemy(), enemy.Enemy()]
        ]

        ### Set waves ###
        self.waves_comp = 0             # number of waves that have ended (are completed)
        self.wave = 0                   # the next wave to start or which is currently running
        self.waves = len(self.enemies)  # number of waves that exist

        ### Button setup ###
        self.buttons = []

        ### setup font ###
        self.font = pygame.font.Font(config.FONT, config.FONT_SIZE)
        self.font_color = config.FONT_COLOR
        self.big_font = pygame.font.Font(config.FONT, config.FONT_BIG_SIZE)

        ### setup location for wave number ###
        self.wave_x = config.WAVE_X
        self.wave_y = config.WAVE_Y

        ### setup location for money ###
        self.money = config.STARTING_MONEY
        self.money_x = config.MONEY_X
        self.money_y = config.MONEY_Y

        ### setup location for state ###
        self.state_x = config.STATE_X
        self.state_y = config.STATE_Y

        ### setup location for state ###
        self.lives_x = config.LIVES_X
        self.lives_y = config.LIVES_Y
        self.lives = config.LIVES

        ### setup monkeys ###
        self.rects = []

        self.selected = None

    # waves can be started while breaktime (TD_CLEAR) and there is a next wave available
    def can_start_wave(self):
        if self.waves_comp < self.waves-1 and self.state == config.BA_CLEAR:
            return True
        else:
            return False

    # creates and places all of the enemies
    def begin_wave(self, resume=False):

        if not resume:
            # Mark next wave as started
            self.wave += 1

            # Deploy enemies #
            for index, object in enumerate(self.enemies[self.wave]):
                object.deploy((config.STARTPOINT[0] - (config.DEFAULT_DELAY * index), config.STARTPOINT[1]))

        completed = 0
        length = len(self.enemies[self.wave])

        time = pygame.time.Clock()
        ticks = 0

        # Draw Enemy #
        def step(completed, length, ticks):

            if completed < length:
                for enemy in self.enemies[self.wave]:
                    if enemy.waypoints_reached < len(config.WAYPOINTS):

                        # Move enemy
                        enemy.move(ticks, len(self.enemies[self.wave]))

                        # Paint game + new enemy location
                        self.paint(self.screen)

                        # Check for Monkey Shots
                        for monkey in self.rects:

                            # Run monkey logic
                            monkey.game_logic()

                            if monkey.getDistance(enemy.position) <= monkey.radius:

                                # Create Bullet
                                if monkey.can_attack():
                                    monkey.attack(enemy)

                                # Check if enemy is dead
                                if enemy.is_dead():
                                    if len(self.enemies[self.wave]) > 0:
                                        self.enemies[self.wave].pop(0)
                                        self.money += config.DEFAULT_KILLVALUE
                                        completed += 1
                                        pygame.mixer.Channel(2).play(pygame.mixer.Sound('data/bananattack/sounds/Explosion.wav'))

                        # Update Screen
                        pygame.display.update()

                        ticks = time.tick(60)

                    else:
                        # Kill enemies -> hasReached base
                        self.enemies[self.wave].pop(0)
                        self.lives -= enemy.health
                        completed += 1

                # did the user just press the escape key?
                pygame.event.get()
                if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
                    self.last_state = self.state
                    self.state = config.BA_PAUSE
                    self.buttons = [button.playGame(self.state, self.wave_started()), button.exitGame(self.state, self.lives)]
                    self.paint(self.screen)

                    pygame.mixer.pause()
                    pygame.mixer.music.load('data/bananattack/SBM.mp3')
                    pygame.mixer.music.play()

                else:
                    # Recursion
                    step(completed, length, ticks)
            else:
                # no Trucks Alive
                pygame.mixer.Channel(0).stop()

                pygame.mixer.music.load('data/bananattack/SBM.mp3')
                pygame.mixer.music.play()

        step(completed, length, ticks)

        if self.state == config.BA_PLAYING:
            # Wave Done
            self.waves_comp += 1
            self.last_state = self.state
            self.state = config.BA_CLEAR
            if self.waves_comp == self.waves - 1:
                self.last_state = self.state
                self.state = config.BA_SUCCESS

                # Check if next game is unlocked
                if 2 not in self.getMemory("unlocked"):

                    # Fetch de huidige unlocked
                    unlocked = self.getMemory("unlocked")

                    # Voeg daar de volgende game aan toe
                    unlocked.append(2)

                    # Update de memory
                    self.setMemory("unlocked",unlocked)

        if self.lives <= 0:
            self.last_state = self.state
            self.state = config.BA_FAILURE

    # check whether the next wave is running
    def wave_started(self):
        if self.waves_comp < self.wave:
            return True
        else:
            return False

    # paints all of the objects of the game
    def paint(self, surface):
        # fill the screen with the background color
        surface.blit(pygame.transform.scale(pygame.image.load('data/bananattack/background.jpeg').convert(), (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)), (0, 0))

        # if the game is being played
        # draw the world, enemys, towers,
        # and menus
        if self.state == config.BA_STARTING or self.state == config.BA_PLAYING or self.state == config.BA_PAUSE or self.state == config.BA_CLEAR or self.state == config.BA_SUCCESS or self.state == config.BA_FAILURE:
            ### Draw Right Info Box ###
            self.rightInfoBox()

            ### show wave number ###
            wave = "Wave: %d " % (self.wave)
            temp_surface = self.font.render(wave, 1, self.font_color)
            surface.blit(temp_surface, (self.wave_x, self.wave_y))

            ### show balance ###
            money = "Balance: %d" % (self.money)
            temp_surface = self.font.render(money, 1, self.font_color)
            surface.blit(temp_surface, (self.money_x, self.money_y))

            ### show state ###
            state = "State: %d" % (self.state)
            temp_surface = self.font.render(state, 1, self.font_color)
            surface.blit(temp_surface, (self.state_x, self.state_y))

            ### show lives ###
            lives = "Lives: %d" % (self.lives)
            temp_surface = self.font.render(lives, 1, self.font_color)
            surface.blit(temp_surface, (self.lives_x, self.lives_y))

            ### Draw path ###
            self.drawPath()

            ### Draw arrow ###
            self.drawArrow()

            ### Draw enemies ###
            for index, enemy in enumerate(self.enemies[self.wave]):
                enemy.paint(surface, enemy.health)

            ### Show waypoints ###
            #self.showWaypoints()

            ### Draw monkeys ###
            for index, tower in enumerate(self.rects):
                if index == self.selected:
                    if self.rects[self.selected].canPlace(pygame.mouse.get_pos()):
                        tower.paint(surface)
                    else:
                        tower.paint(surface, (255, 0, 0, 255))
                else:
                    for truck in self.enemies[self.wave]:
                        if tower.getDistance(truck.position) < config.MONKEY_RADIUS:
                            tower.closest = tower.getDistance(truck.position)
                            tower.closest_pos = truck.position
                            break
                    tower.paint(surface, range=False)
                    tower.paint_bullets(surface)

            ### Start Overlay ###
            if self.state == config.BA_STARTING:
                self.startOverlay()

            ### Pause Overlay ###
            if self.state == config.BA_PAUSE:
                self.pauseOverlay()

            ### Fail Game ###
            if self.state == config.BA_FAILURE:
                self.failGame()

            ### End Game ###
            if self.state == config.BA_SUCCESS:
                self.endGame()

            ### Draw buttons ###
            for button in self.buttons:
                button.paint(surface)
                if button.get_state() != self.state and button.get_state() != 0:
                    self.last_state = self.state
                    self.state = button.get_state()

                    # if button has changed state, stop performing other buttons
                    break
                if button.pressed == 1:
                    if self.money >= config.DEFAULT_PRICE:
                        self.rects.append(monkey.Monkey())
                        self.selected = len(self.rects)-1
                        self.selected_offset_x = pygame.mouse.get_pos()[0]-(config.MONKEY_SIZE // 2)
                        self.selected_offset_y = pygame.mouse.get_pos()[1]-(config.MONKEY_SIZE // 2)
                        self.money -= 50

    def game_logic(self, keys):
        ### Push correct buttons ###
        # State 0
        if self.state == config.BA_STARTING:
            self.buttons = [button.skipTutorial(self.state)]

        # State 10
        if self.state == config.BA_PAUSE:
            self.buttons = [button.playGame(self.state, self.wave_started()), button.restartGame(),button.exitGame(self.state, 0, 1)]

        # State 20
        if self.state == config.BA_PLAYING:
            self.buttons = []

            # Start wave if it isn't started yet
            if not self.wave_started():
                # Add enemies to self.enemies
                self.begin_wave()
            else:
                self.begin_wave(True)

        # State 30
        if self.state == config.BA_CLEAR:
            self.buttons = [button.startWave(self.state, self.can_start_wave()), button.monkeyButton(self.state)]

        # State 40
        if self.state == config.BA_FAILURE:
            self.buttons = [button.exitGame(self.state)]

        # State 50
        if self.state == config.BA_SUCCESS:
            self.buttons = [button.exitGame(self.state, self.money)]

    def getMemory(self, key):
        with open("data/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            return data[key]

    def setMemory(self, key, value):
        with open("data/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            data[key] = value

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def drawPath(self):
        # line 1
        pygame.draw.line(self.screen, config.SAND, (0, 287), (144, 287), 2)
        pygame.draw.line(self.screen, config.SAND, (143, 287), (143, 144), 2)
        pygame.draw.line(self.screen, config.SAND, (144, 143), (336, 143), 2)
        pygame.draw.line(self.screen, config.SAND, (335, 144), (335, 528), 2)
        pygame.draw.line(self.screen, config.SAND, (336, 527), (144, 527), 2)
        pygame.draw.line(self.screen, config.SAND, (143, 528), (143, 576), 2)
        pygame.draw.line(self.screen, config.SAND, (144, 575), (768, 575), 2)
        pygame.draw.line(self.screen, config.SAND, (767, 576), (767, 480), 2)
        pygame.draw.line(self.screen, config.SAND, (768, 479), (528, 479), 2)
        pygame.draw.line(self.screen, config.SAND, (527, 336), (527, 480), 2)
        pygame.draw.line(self.screen, config.SAND, (528, 335), (768, 335), 2)
        pygame.draw.line(self.screen, config.SAND, (767, 335), (767, 0), 2)

        # line 2
        pygame.draw.line(self.screen, config.SAND, (0, 335), (192, 335), 2)
        pygame.draw.line(self.screen, config.SAND, (191, 336), (191, 192), 2)
        pygame.draw.line(self.screen, config.SAND, (192, 191), (288, 191), 2)
        pygame.draw.line(self.screen, config.SAND, (287, 192), (287, 480), 2)
        pygame.draw.line(self.screen, config.SAND, (288, 479), (96, 479), 2)
        pygame.draw.line(self.screen, config.SAND, (95, 480), (95, 622), 2)
        pygame.draw.line(self.screen, config.SAND, (96, 622), (816, 622), 2)
        pygame.draw.line(self.screen, config.SAND, (815, 624), (815, 432), 2)
        pygame.draw.line(self.screen, config.SAND, (816, 431), (576, 431), 2)
        pygame.draw.line(self.screen, config.SAND, (575, 432), (575, 384), 2)
        pygame.draw.line(self.screen, config.SAND, (576, 383), (816, 383), 2)
        pygame.draw.line(self.screen, config.SAND, (815, 384), (815, 0), 2)

    def drawArrow(self):
        arrow = pygame.image.load("data/bananattack/arrow.png")
        arrow.convert_alpha()
        arrow = pygame.transform.scale(arrow, (48, 48))
        self.screen.blit(arrow, (0,287))

    def rightInfoBox(self):
        pygame.draw.rect(self.screen, config.INFO_BOX_BG_COLOR, (940,10,320,500), 1)

    def startOverlay(self):
        # overlay
        s = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))  # notice the alpha value in the color
        self.screen.blit(s, (0, 0))

        # start text #
        text = "How to play?!"
        temp_surface = self.big_font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (450, 80))

        text = "What is the goal of this game?"
        temp_surface = self.font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (50, 220))

        text = "Prevent the Trucks from reaching their destination"
        temp_surface = self.font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (110, 260))

        text = "How do I do that?"
        temp_surface = self.font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (50, 320))

        text = "1. Use your mouse to buy a monkey from the green right block"
        temp_surface = self.font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (110, 360))

        text = "2. Drag the monkey to the postion where you would like to place it"
        temp_surface = self.font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (110, 400))

        text = "3. Press start wave to make the enemied trucks drive to their destination"
        temp_surface = self.font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (110, 440))

        text = "4. Your monkeys will automatically attack the trucks once they are in range"
        temp_surface = self.font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (110, 480))

    def pauseOverlay(self):
        # overlay
        s = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))  # notice the alpha value in the color
        self.screen.blit(s, (0, 0))

        # pause text #
        text = "Game Paused!"
        temp_surface = self.big_font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (450, 280))

    def failGame(self):
        # overlay
        s = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))  # notice the alpha value in the color
        self.screen.blit(s, (0, 0))

        # fail text #
        text = "You loser...!"
        temp_surface = self.big_font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (450, 280))

    def endGame(self):
        # overlay
        s = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))  # notice the alpha value in the color
        self.screen.blit(s, (0, 0))

        # completed text #
        text = "Game Completed!"
        temp_surface = self.big_font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (450, 280))

    def showWaypoints(self):
        for waypoint in config.WAYPOINTS:
            pygame.draw.circle(self.screen, config.SAND, (waypoint[1], waypoint[2]), 2)















