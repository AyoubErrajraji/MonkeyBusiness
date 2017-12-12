import pygame
import sys
import json
import os

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


class Player(object):  # represents the bird, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load('data/finalfight/monkey.png')
        # the bird's position
        self.x = 0
        self.y = 0

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

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

        pygame.init()
        player = Player()  # create an instance
        clock = pygame.time.Clock()

        finished = False

        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    pygame.quit()
                    sys.exit()
                pygame.display.flip()

            player.handle_keys()  # handle the keys

            #screen.fill((255, 255, 255))  # fill the screen with white
            #player.draw(screen)  # draw the bird to the screen
            pygame.display.update()  # update the screen

            clock.tick(40)



