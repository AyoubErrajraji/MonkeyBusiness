import pygame
import sys
#import math
#import itertools
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

    def blitPlayer(self):
        self.screen.blit(self.player, (200, 550))

    def movePlayer(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1  # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]:  # down key
            self.y += dist  # move down
        elif key[pygame.K_UP]:  # up key
            self.y -= dist  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.x += dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.x -= dist  # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

class Boss(Game):
    def __init__(self,screen):
        Game.__init__(self, screen)
        self.bossX = 350
        self.bossY = 300
        self.boss = None

    def loadBoss(self,name):
        self.boss = pygame.image.load(name).convert_alpha()
        bossWidth = self.boss.get_rect().width
        bossHeight = self.boss.get_rect().height
        self.boss = pygame.transform.scale(self.boss, (bossWidth, bossHeight))

    def blitBoss(self):
        screen.blit(boss, (350, 300))


class Wolk(Game):
    def __init__(self, screen):
        Game.__init__(self, screen)
        self.wolkX = 430
        self.wolkY = 130
        self.wolk = None

    def loadWolk(self, name):
        self.wolk = pygame.image.load(name).convert_alpha()
        wolkWidth = self.wolk.get_rect().width
        wolkHeight = self.wolk.get_rect().height
        self.wolk = pygame.transform.scale(self.wolk, (wolkWidth,wolkHeight))

    def blitwolk(self):
        screen.blit(self.wolk, (250, 200))

width = 900
height = 700
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption("Final Fight")

newPlayer = Player(screen)
newBoss = Boss(screen)
newWolk = Wolk(screen)
background = Background(screen)

background.loadForrest("darkForrest.jpg")


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

