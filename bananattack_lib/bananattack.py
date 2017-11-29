'''
Created on Nov 25, 2017
@author: lexdewilligen
'''
import pygame
from bananattack_lib import config
from bananattack_lib import game
from bananattack_lib import button
from bananattack_lib import display

class BananAttack(game.Game):
    def __init__(self, name, screen_width, screen_height, screen = None):
        # setup data members and the screen
        game.Game.__init__(self, name, screen_width, screen_height, screen)

        # set state to playing
        self.state = config.TD_PLAYING

        # set waves completed to 0
        self.waves_comp = 0

        ### Button setup ###
        self.buttons = [button.startWave(),button.pauseGame()]

        ### setup font ###
        self.font = pygame.font.Font(config.FONT, config.FONT_SIZE)
        self.font_color = config.FONT_COLOR

        ### setup location for wave number ###
        self.wave_x = config.WAVE_X
        self.wave_y = config.WAVE_Y

        ### setup location for money ###
        self.money = config.STARTING_MONEY
        self.money_x = config.MONEY_X
        self.money_y = config.MONEY_Y

    # waves can be started while breaktime (TD_CLEAR) and there is a next wave available
    def can_start_wave(self):
        return self.state == config.TD_CLEAR and self.wave+1 <= len(self.waves)-1

    # creates and places all of the enemys
    def begin_wave(self):
        if not self.can_start_wave():
            return
        self.wave += 1

        # create and place the enemys
        ### CODE TO WRITE ###

        self.state = config.TD_PLAYING

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

    # paints all of the objects of the game
    def paint(self, surface):
        # fill the screen with the background color
        surface.fill(config.BG_COLOR)
        surface.blit(pygame.transform.scale(pygame.image.load('data/bananattack/background.jpeg').convert(), (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)), (0, 0))

        # if the game is being played
        # draw the world, enemys, towers,
        # and menus
        if self.state == config.TD_PLAYING:
            ### Draw Right Info Box ###
            self.rightInfoBox()

            ### show wave number ###
            wave = "Waves completed: %d" % (self.waves_comp)
            temp_surface = self.font.render(wave, 1, self.font_color)
            surface.blit(temp_surface, (self.wave_x, self.wave_y))

            ### show balance ###
            money = "Balance: %d" % (self.money)
            temp_surface = self.font.render(money, 1, self.font_color)
            surface.blit(temp_surface, (self.money_x, self.money_y))

            ### Draw path ###
            self.drawPath()

            ### Draw buttons ###
            for button in self.buttons:
                button.paint(surface)







