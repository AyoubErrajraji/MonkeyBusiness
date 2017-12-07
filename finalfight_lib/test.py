import pygame
import sys
#import math
pygame.init()

class Game:
    def __init__(self,screen):
        self.fps = 30
        self.frame = pygame.time.Clock()
        self.screen = screen

    def updateFrame(self):
        self.frame.tick(self.fps)
        pygame.display.flip()

class Background(Game):
    def __init__(self,screen):
        Game.__init__(self,screen)
        self.rescale = 2
        self.forrestImage = None

    def loadForrest(self,name):
        self.forrestImage = pygame.image.load(name).convert()
        self.forrestImage = pygame.transform.scale(self.forrestImage, (width, height))

class Player(Game):
    def __init__(self,screen):
        Game.__init__(self,screen)
        self.playerX = 200
        self.playerY = 550
        self.player = None

    def loadPlayer(self,name):
        self.player = pygame.image.load(name).convert_alpha()
        playerWidth = self.player.get_rect().width
        playerHeight = self.player.get_rect().height
        self.player = pygame.transform.scale(self.player, (playerWidth, playerHeight))







width = 900
height = 700
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


finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
            sys.exit()
        pygame.display.flip()

