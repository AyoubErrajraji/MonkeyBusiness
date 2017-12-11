import pygame
import sys
import json

def getMemory(key):
    with open("finalfight_lib/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        return data[key]


def setMemory(key, value):
    with open("finalfight_lib/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data[key] = value

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()

class run():
    def runm(self):
        width = 1280
        height = 720
        screenDim = (width, height)

        screen = pygame.display.set_mode(screenDim)

        pygame.display.set_caption("Final Fight")

        forrestImage = pygame.image.load("data/finalfight/openplek.png").convert()
        forrestImage = pygame.transform.scale(forrestImage,(width,height))
        screen.blit(forrestImage,(0,0))

        rescale = 2
        boss = pygame.image.load("data/finalfight/boss2.png").convert_alpha()
        bossWidth = boss.get_rect().width
        bossHeight = boss.get_rect().height
        boss = pygame.transform.scale(boss,(bossWidth,bossHeight))
        screen.blit(boss,(520,300))

        wolk = pygame.image.load("data/finalfight/spreekwolk.png").convert_alpha()
        wolkWidth = wolk.get_rect().width
        wolkHeight = wolk.get_rect().height
        wolk = pygame.transform.scale(wolk,(350,200))
        screen.blit(wolk,(590,130))

        player = pygame.image.load("data/finalfight/monkey.png").convert_alpha()
        playerWidth = player.get_rect().width
        playerHeight = player.get_rect().height
        player = pygame.transform.scale(player,(150,150))
        screen.blit(player,(300,550))


        pygame.font.init()
        font = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 30)
        score = "score: %d" % getMemory("score")
        temp_surface = font.render(score, 1, (255,255,255))
        screen.blit(temp_surface,(1150,10))

        setMemory("score", 768)

        finished = False

        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    pygame.quit()
                    sys.exit()
                pygame.display.flip()



