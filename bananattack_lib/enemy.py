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

    def deploy(self, position = None):
        if position == None:
            draw.Draw.__init__(self, config.KIND_ENEMY, config.STARTPOINT, 48, 48, self.image)
        else:
            draw.Draw.__init__(self, config.KIND_ENEMY, position, 48, 48, self.image)

    def trackNextWaypoint(self):
        for waypoint in config.WAYPOINTS:
            if waypoint[0] == self.waypoints_reached+1:
                return waypoint

    def setWaypointsReached(self, number):
        self.waypoints_reached += number

    def move(self):

        speed = config.DEFAULT_SPEED

        # Update enemy's location
        if self.get_position()[0] < self.trackNextWaypoint()[1]:
            if self.trackNextWaypoint()[1] - self.get_position()[0] >= speed:
                self.set_position((self.get_position()[0] + speed, self.get_position()[1]))
            else:
                self.set_position((self.get_position()[0] + (self.trackNextWaypoint()[1] - self.get_position()[0]),
                           self.get_position()[1]))

        if self.get_position()[0] > self.trackNextWaypoint()[1]:
            if self.get_position()[0] - self.trackNextWaypoint()[1] >= speed:
                self.set_position((self.get_position()[0] - speed, self.get_position()[1]))
            else:
                self.set_position((self.get_position()[0] - (self.get_position()[0] - self.trackNextWaypoint()[1]),
                           self.get_position()[1]))

        if self.get_position()[1] < self.trackNextWaypoint()[2]:
            if self.trackNextWaypoint()[2] - self.get_position()[1] >= speed:
                self.set_position((self.get_position()[0], self.get_position()[1] + speed))
            else:
                self.set_position((self.get_position()[0],
                           self.get_position()[1] + (self.trackNextWaypoint()[2] - self.get_position()[1])))

        if self.get_position()[1] > self.trackNextWaypoint()[2]:
            if self.get_position()[1] - self.trackNextWaypoint()[2] >= speed:
                self.set_position((self.get_position()[0], self.get_position()[1] - speed))
            else:
                self.set_position((self.get_position()[0], self.get_position()[1] - (self.get_position()[1] - self.trackNextWaypoint()[2])))

        # If enemy position is on waypoint
        if self.get_position()[0] == self.trackNextWaypoint()[1] and self.get_position()[1] == self.trackNextWaypoint()[2]:
            self.setWaypointsReached(1)


