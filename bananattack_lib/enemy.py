'''
Created on Nov 25, 2017
@author: lexdewilligen
'''
import pygame
from bananattack_lib import config
from bananattack_lib import draw

class Enemy(draw.Draw):
    def __init__(self):
        self.image = config.DEFAULT_IMAGE
        self.position = config.STARTPOINT

        draw.Draw.__init__(self, config.KIND_ENEMY, self.position, 48, 48, self.image)

    def trackNextWaypoint(self):
        code = "ToBeWritten"

    def move(self,position):
        # set new position
        self.set_position(position)
        print(position)
