import pygame
import sys
import json
import os
import math
import itertools


def getMemory(key):
    with open("memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        return data[key]


def setMemory(key, value):
    with open("memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data[key] = value

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()


#class Player(object):  # represents the bird, not the game
 #   def __init__(self):
  #      """ The constructor of the class """
   #     self.player = pygame.image.load("data/finalfight/monkey.png").convert_alpha()
    #    # playerWidth = player.get_rect().width
     #   # playerHeight = player.get_rect().height
      #  self.player = pygame.transform.scale(player, (150, 150))
       # self.x = 0
        #self.y = 0

#def handle_keys(self):
 #   """ Handles Keys """
  #  key = pygame.key.get_pressed()
   # dist = 1 # distance moved in 1 frame, try changing it to 5
    #if key[pygame.K_DOWN]: # down key
     #   self.y += dist # move down
    #elif key[pygame.K_UP]: # up key
     #   self.y -= dist # move up
    #if key[pygame.K_RIGHT]: # right key
     #   self.x += dist # move right
    #elif key[pygame.K_LEFT]: # left key
     #   self.x -= dist # move left

def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

def sub(u, v):
    return [u[i]-v[i] for i in range(len(u))]

def normalize(v):
    return [v[i]/magnitude(v)  for i in range(len(v))]

width = 1280
height = 720
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption("Final Fight")

forrestImage = pygame.image.load("openplek.png").convert()
forrestImage = pygame.transform.scale(forrestImage,(width,height))
screen.blit(forrestImage,(0,0))

#rescale = 2
boss = pygame.image.load("boss2.png").convert_alpha()
bossWidth = boss.get_rect().width
bossHeight = boss.get_rect().height
boss = pygame.transform.scale(boss,(bossWidth,bossHeight))
screen.blit(boss,(520,300))

wolk = pygame.image.load("spreekwolk.png").convert_alpha()
#wolkWidth = wolk.get_rect().width
#wolkHeight = wolk.get_rect().height
wolk = pygame.transform.scale(wolk,(350,200))
screen.blit(wolk,(590,130))

player = pygame.image.load("monkey.png").convert_alpha()
#playerWidth = player.get_rect().width
#playerHeight = player.get_rect().height
player = pygame.transform.scale(player,(150,150))
screen.blit(player,(300,550))


pygame.font.init()
font = pygame.font.Font("FEASFBRG.ttf", 30)
score = "score: %d" % getMemory("score")
temp_surface = font.render(score, 1, (255,255,255))
screen.blit(temp_surface,(1150,10))

setMemory("score", 768)

pygame.init()

screen = pygame.display.set_mode((width, height))
#clock = pygame.time.Clock()


pause_text = pygame.font.Font("FEASFBRG.ttf", 60).render('Paused', True, pygame.color.Color('White'))
s = pygame.Surface((width, height), pygame.SRCALPHA)  # per-pixel alpha
s.fill((0, 0, 0, 150))

RUNNING, PAUSE = 0, 1
state = RUNNING


#player = Player()  # create an instance
clock = pygame.time.Clock()

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT: break
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_p: state = PAUSE
            if e.key == pygame.K_s: state = RUNNING
    else:
        screen.fill((0, 0, 0))

        if state == RUNNING:
            screen.blit(forrestImage, (0, 0))
            screen.blit(boss, (520, 300))
            screen.blit(wolk, (590, 130))
            screen.blit(player, (300, 550))
            screen.blit(temp_surface, (1150, 10))



        elif state == PAUSE:

            screen.blit(forrestImage, (0, 0))
            screen.blit(boss, (520, 300))

            screen.blit(player, (300, 550))
            screen.blit(temp_surface, (1150, 10))
            screen.blit(s, (0, 0))
            screen.blit(pause_text, (600, 360))



        pygame.display.flip()
        clock.tick(60)
        continue
    #player.handle_keys()  # handle the keys

    break

