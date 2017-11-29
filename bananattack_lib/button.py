'''
Created on Nov 25, 2017
@author: lexdewilligen
'''
from bananattack_lib import config
from bananattack_lib import draw
import pygame

class Button(draw.Draw):
    def __init__(self, position, width, height, image, image_hover):
        # image shown when the mouse is on the button
        self.image_hover = pygame.image.load(image_hover)

        draw.Draw.__init__(self, config.KIND_BUTTON, position, width, height, image)

        # mouse-over data
        self.message = None
        self.hover = False

        # size data
        self.width = width
        self.height = height

        # message shown on mouse-over
        self.description = ""

        # object to be sent on click
        self.item = None

    def paint(self, surface):
        # get mouse positions
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # check whether we hover or not
        if mouse_x >= self.position[0] and mouse_x < (self.position[0] + self.width) and mouse_y > self.position[1] and mouse_y < (self.position[1] + self.height):
            self.hover = True

            # do action on click
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.task()
        else:
            self.hover = False

        # display the hover image on mouse-overs
        if self.hover:
            surface.blit(self.image_hover, self.position)
        # otherwise use the normal image
        else:
            surface.blit(self.image, self.position)

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

# Available Buttons
class startWave(Button):
    def __init__(self):
        Button.__init__(self, (config.BUTTON_STARTWAVE_X,config.BUTTON_STARTWAVE_Y), config.BUTTON_STARTWAVE_WIDTH, config.BUTTON_STARTWAVE_HEIGHT, config.BUTTON_STARTWAVE_IMG, config.BUTTON_STARTWAVE_HOVER_IMG)
        self.item = None

    def task(self):
        print("Wave Started")

class pauseGame(Button):
    def __init__(self):
        Button.__init__(self, (config.BUTTON_PAUSEGAME_X,config.BUTTON_PAUSEGAME_Y), config.BUTTON_PAUSEGAME_WIDTH, config.BUTTON_PAUSEGAME_HEIGHT, config.BUTTON_PAUSEGAME_IMG, config.BUTTON_PAUSEGAME_HOVER_IMG)
        self.item = None

    def task(self):
        print("Game Paused")


