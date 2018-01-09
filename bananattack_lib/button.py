'''
Created on Nov 25, 2017
@author: lexdewilligen
'''
from bananattack_lib import config
from bananattack_lib import draw
from bananattack_lib import main
from menu_lib import slidemenu
import json
import pygame

class Button(draw.Draw):
    def __init__(self, position, width, height, image, image_hover):
        # image shown when the mouse is on the button
        self.image_hover = pygame.image.load(image_hover)
        self.image_hover = pygame.transform.scale(self.image_hover, (width, height))

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

        # set default state
        self.state = 0

        # pressed
        self.pressed = 0

    # Overwrite the Draw.paint function because we need to implement hovering
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

    def get_state(self):
        return self.state

    def getMemory(self, key):
        with open("data/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            return data[key]

# Available Buttons
class startWave(Button):
    def __init__(self, state, canStartWave):
        Button.__init__(self, (config.BUTTON_STARTWAVE_X,config.BUTTON_STARTWAVE_Y), config.BUTTON_STARTWAVE_WIDTH, config.BUTTON_STARTWAVE_HEIGHT, config.BUTTON_STARTWAVE_IMG, config.BUTTON_STARTWAVE_HOVER_IMG)
        self.item = None
        self.state = state
        self.canStartWave = canStartWave

    def task(self):
        if self.canStartWave:
            self.state = config.BA_PLAYING

class playGame(Button):
    def __init__(self, state, running):
        Button.__init__(self, (config.BUTTON_PLAYGAME_X,config.BUTTON_PLAYGAME_Y), config.BUTTON_PLAYGAME_WIDTH, config.BUTTON_PLAYGAME_HEIGHT, config.BUTTON_PLAYGAME_IMG, config.BUTTON_PLAYGAME_HOVER_IMG)
        self.item = None
        self.state = state
        self.running = running

    def task(self):
        if self.running:
            self.state = config.BA_PLAYING
        else:
            self.state = config.BA_CLEAR

class exitGame(Button):
    def __init__(self, state, balance=0, unlocked=None):
        Button.__init__(self, (config.BUTTON_EXITGAME_X,config.BUTTON_EXITGAME_Y), config.BUTTON_EXITGAME_WIDTH, config.BUTTON_EXITGAME_HEIGHT, config.BUTTON_EXITGAME_IMG, config.BUTTON_EXITGAME_HOVER_IMG)
        self.item = None
        self.state = state
        self.balance = balance
        self.unlocked = unlocked

    def task(self):
        mymenu = slidemenu.run()
        mymenu.runm(self.balance, self.unlocked)

class restartGame(Button):
    def __init__(self):
        Button.__init__(self, (config.BUTTON_RESTARTGAME_X,config.BUTTON_RESTARTGAME_Y), config.BUTTON_RESTARTGAME_WIDTH, config.BUTTON_RESTARTGAME_HEIGHT, config.BUTTON_RESTARTGAME_IMG, config.BUTTON_RESTARTGAME_HOVER_IMG)
        self.item = None

    def task(self):
        main.main()

class monkeyButton(Button):
    def __init__(self, state):
        Button.__init__(self, (config.BUTTON_MONKEYBUTTON_X,config.BUTTON_MONKEYBUTTON_Y), config.BUTTON_MONKEYBUTTON_WIDTH, config.BUTTON_MONKEYBUTTON_HEIGHT, "data/" + self.getMemory("monkey"), "data/" + self.getMemory("monkey"))
        self.item = None
        self.state = state

    def task(self):
        self.pressed = 1

class skipTutorial(Button):
    def __init__(self, state):
        Button.__init__(self, (config.BUTTON_SKIPTUTORIAL_X,config.BUTTON_SKIPTUTORIAL_Y), config.BUTTON_SKIPTUTORIAL_WIDTH, config.BUTTON_SKIPTUTORIAL_HEIGHT, config.BUTTON_SKIPTUTORIAL_IMG, config.BUTTON_SKIPTUTORIAL_HOVER_IMG)
        self.item = None
        self.state = state

    def task(self):
        self.state = config.BA_CLEAR

    #operator overloading



