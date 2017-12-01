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
        self.waypoints_reached = 0

        draw.Draw.__init__(self, config.KIND_ENEMY, config.STARTPOINT, 48, 48, self.image)
        print("Enemy Created")

    def trackNextWaypoint(self):
        for waypoint in config.WAYPOINTS:
            if waypoint[0] == self.waypoints_reached+1:
                return waypoint
                break

    def setWaypointsReached(self, number):
        self.waypoints_reached += number

    def move(self, position):
        # set new position
        self.set_position(position)
        print("NewPos: ", position)

