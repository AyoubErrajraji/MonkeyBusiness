import pygame, sys, time, json
from math import *
from pygame.locals import *

pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 255, 0)
red = (255, 0, 0)
green = (0, 200, 0)
yellow = (255, 255, 0)

data = json.load(open('../data/data.json'))
screenDim = (data["data"]["resolution"]["width"], data["data"]["resolution"]["height"])
print(screenDim)

screen = pygame.display.set_mode(screenDim)
