'''
Created on Nov 25, 2017
@author: lexdewilligen
'''
import pygame
import time
from bananattack_lib import config
from bananattack_lib import game
from bananattack_lib import button
from bananattack_lib import enemy

class BananAttack(game.Game):
    def __init__(self, name, screen_width, screen_height, screen = None):
        # setup data members and the screen
        game.Game.__init__(self, name, screen_width, screen_height, screen)

        # set state to playing
        self.state = config.BA_CLEAR

        # set waves
        self.waves_comp = 0             # number of waves that have ended (are completed)
        self.wave = 0                   # the next wave to start or which is currently running
        self.waves = config.MAX_WAVES   # number of waves that exist

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

        ### Enemy setup ###
        self.enemies = [enemy.Enemy()]

    # waves can be started while breaktime (TD_CLEAR) and there is a next wave available
    def can_start_wave(self):
        if self.waves_comp < self.waves and self.state ==  config.BA_CLEAR:
            return True
        else:
            return False

    # creates and places all of the enemys
    def begin_wave(self):
        # mark next waves as started
        self.wave += 1
        print("Wave number: ", self.wave)

        ### Draw Enemy ###
        for enemy in self.enemies:
            while enemy.waypoints_reached < len(config.WAYPOINTS):
                speed = config.DEFAULT_SPEED

                # Update enemy's location
                if enemy.get_position()[0] < enemy.trackNextWaypoint()[1]:
                    if enemy.trackNextWaypoint()[1] - enemy.get_position()[0] >= 10:
                        enemy.move((enemy.get_position()[0] + speed, enemy.get_position()[1]))
                    else:
                        enemy.move((enemy.get_position()[0] + enemy.trackNextWaypoint()[1] - enemy.get_position()[0], enemy.get_position()[1]))
                if enemy.get_position()[0] > enemy.trackNextWaypoint()[1]:
                    enemy.move((enemy.get_position()[0] - speed, enemy.get_position()[1]))
                if enemy.get_position()[1] < enemy.trackNextWaypoint()[2]:
                    enemy.move((enemy.get_position()[0], enemy.get_position()[1] + speed))
                if enemy.get_position()[1] > enemy.trackNextWaypoint()[2]:
                    enemy.move((enemy.get_position()[0], enemy.get_position()[1] - speed))

                # If enemy position is on waypoint
                if enemy.get_position()[0] == enemy.trackNextWaypoint()[1]:
                    print("Done")
                    enemy.setWaypointsReached(12)

                # Paint game + new enemy location
                self.paint(self.screen)
                enemy.paint(self.screen)

                # Update Screen
                pygame.display.update()
                time.sleep(.1)

        # if done -> set state to BA_CLEAR
        print("Wave Completed!")
        self.waves_comp += 1
        self.state = config.BA_CLEAR
        print("State updated to: %d by %s from %s" % (config.BA_CLEAR, button, " the bottom of the begin_wave function"))

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
        if self.state == config.BA_PLAYING or self.state == config.BA_PAUSE or self.state == config.BA_CLEAR:
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

            ### Draw path ###
            self.drawPath()

            ### Pause Overlay ###
            if self.state == config.BA_PAUSE:
                self.pauseOverlay()

            ### Draw buttons ###
            for button in self.buttons:
                button.paint(surface)
                if button.get_state() != self.state and button.get_state() != 0:
                    self.state = button.get_state()

                    print("State updated to: %d by %s from %s" % (button.get_state(),button," the bottom of the paint function"))

                    # if button has changed state, stop performing other buttons
                    break

            ### Draw enemies ###
            for enemy in self.enemies:
                enemy.paint(surface)

            ### Show waypoints ###
            self.showWaypoints()

    def game_logic(self, keys):

        ### Push correct buttons ###
        # State 10
        if self.state == config.BA_PAUSE:
            self.buttons = [button.playGame(self.state, self.wave_started())]

        # State 20
        if self.state == config.BA_PLAYING:
            self.buttons = [button.pauseGame(self.state)]

            # Start wave if it isn't started yet
            if not self.wave_started():
                # Add enemies to self.enemies
                self.begin_wave()

        # State 30
        if self.state == config.BA_CLEAR:
            self.buttons = [button.pauseGame(self.state), button.startWave(self.state, self.can_start_wave())]


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

    def rightInfoBox(self):
        pygame.draw.rect(self.screen, config.INFO_BOX_BG_COLOR, (940,10,320,500), 1)

    def pauseOverlay(self):
        # overlay
        s = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))  # notice the alpha value in the color
        self.screen.blit(s, (0, 0))

        # pause text #
        text = "Game Paused!"
        temp_surface = self.big_font.render(text, 1, self.font_color)
        self.screen.blit(temp_surface, (450, 280))

    def showWaypoints(self):
        for waypoint in config.WAYPOINTS:
            pygame.draw.circle(self.screen, config.SAND, (waypoint[1], waypoint[2]), 2)















