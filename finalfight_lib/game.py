import pygame
import sys
import json

def getMemory(self, key):
    with open("memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        return data[key]


def setMemory(self, key, value):
    with open("finalfight_lib/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data[key] = value

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()
    self.score = self.getMemory("score")
    self.setMemory("score", 894)


width = 1280
height = 720
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption("Final Fight")

forrestImage = pygame.image.load("darkForrest.jpg").convert()
forrestImage = pygame.transform.scale(forrestImage,(width,height))
screen.blit(forrestImage,(0,0))

rescale = 2
boss = pygame.image.load("boss2.png").convert_alpha()
bossWidth = boss.get_rect().width
bossHeight = boss.get_rect().height
boss = pygame.transform.scale(boss,(bossWidth,bossHeight))
screen.blit(boss,(350,300))

wolk = pygame.image.load("spreekwolk.png").convert_alpha()
wolkWidth = wolk.get_rect().width
wolkHeight = wolk.get_rect().height
wolk = pygame.transform.scale(wolk,(250,200))
screen.blit(wolk,(430,130))

player = pygame.image.load("monkey.png").convert_alpha()
playerWidth = player.get_rect().width
playerHeight = player.get_rect().height
player = pygame.transform.scale(player,(150,150))
screen.blit(player,(200,550))

screen.blit(getMemory(50,50))


finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
            sys.exit()
        pygame.display.flip()



