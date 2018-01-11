import pygame
from menu_lib import slidemenu
import json
from fightclub_lib import room

pygame.init()

width = 1280
height = 720
screenDims = (width, height)
gameDisplay = pygame.display.set_mode(screenDims)
font = pygame.font.SysFont('Comic Sans MS', 30)
done = False


class Game:
    def __init__(self, gameDisplay, screenDims):
        self.fps = 60
        self.screenDims = screenDims
        self.frame = pygame.time.Clock()
        self.gameDisplay = gameDisplay

    def updateFrame(self):
        self.frame.tick(self.fps)
        pygame.display.update()


class Background(Game):
    def __init__(self, screen, screenDims):
        Game.__init__(self, screen, screenDims)
        self.loadImage()
        self.backgroundImage = self.backgroundImage

    def loadImage(self):
        self.backgroundImage = pygame.image.load("data/fightclub/background1.png")
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, self.screenDims)

    def blitBackground(self):
        self.gameDisplay.blit(self.backgroundImage, (0, 0))


class Flag(Game, pygame.sprite.Sprite):
    def __init__(self, gameDisplay, screenDims):
        Game.__init__(self, gameDisplay, screenDims)
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.flag
        self.noFlag = self.noFlag
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 300

    def loadImages(self):
        self.flag = pygame.image.load("data/fightclub/flag.png")
        self.noFlag = pygame.image.load("data/fightclub/noFlag.png")

    def blitFlag(self):
        self.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))


class TargetP1(Game, pygame.sprite.Sprite):
    def __init__(self, gameDisplay, screenDims):
        Game.__init__(self, gameDisplay, screenDims)
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.target
        self.rect = self.image.get_rect()
        self.rect.x = 1024
        self.rect.y = 576

    def loadImages(self):
        self.target = pygame.image.load("data/fightclub/target.png")

    def blitTarget(self):
        self.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))


class TargetP2(Game, pygame.sprite.Sprite):
    def __init__(self, gameDisplay, screenDims):
        Game.__init__(self, gameDisplay, screenDims)
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.target
        self.rect = self.image.get_rect()
        self.rect.x = 256
        self.rect.y = 144

    def loadImages(self):
        self.target = pygame.image.load("data/fightclub/target.png")

    def blitTarget(self):
        self.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))


class Player1(Game, pygame.sprite.Sprite):
    def __init__(self, gameDisplay, screenDims):
        Game.__init__(self, gameDisplay, screenDims)
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.monkey
        self.flagMonkey = self.flagMonkey
        self.speedpos = None
        self.speedneg = None
        self.points = 0
        self.y_change = 0
        self.x_change = 0
        self.rect = self.image.get_rect()
        self.rect.x = 1024
        self.rect.y = 576

    def loadImages(self):
        self.monkey = getMemory("bought")
        if self.monkey == ["apprentice_monkey.png"]:
            self.monkey = pygame.image.load("data/apprentice_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load(
                "data/fightclub/images/apprentice_monkey_flag.png").convert_alpha()
        elif self.monkey == ["acid_monkey.png"]:
            self.monkey = pygame.image.load("data/acid_monkey.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/acid_monkey_flag.png").convert_alpha()
        elif self.monkey == ["dragon_monkey.png"]:
            self.monkey = pygame.image.load("data/dragon_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/dragon_monkey_flag.png").convert_alpha()
        elif self.monkey == ["engineer_monkey.png"]:
            self.monkey = pygame.image.load("data/engineer_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load(
                "data/fightclub/images/engineer_monkey_flag.png").convert_alpha()
        elif self.monkey == ["farmer_monkey.png"]:
            self.monkey = pygame.image.load("data/farmer_monkey.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/farmer_monkey_flag.png").convert_alpha()
        elif self.monkey == ["ninja_monkey.png"]:
            self.monkey = pygame.image.load("data/ninja_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/ninja_monkey_flag.png").convert_alpha()
        elif self.monkey == ["robo_monkey.png"]:
            self.monkey = pygame.image.load("data/robo_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/robo_monkey_flag.png").convert_alpha()
        elif self.monkey == ["super_monkey.png"]:
            self.monkey = pygame.image.load("data/super_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/super_monkey_flag.png").convert_alpha()
        else:
            self.monkey = pygame.image.load("data/default_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/charwflag.png").convert_alpha()
        self.monkey = pygame.transform.scale(self.monkey, (50, 50))

    def speed(self):
        self.speedpos = 5
        self.speedneg = -5

    def blitMonkey(self):
        self.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def score(self):
        self.textsurface = font.render(str(self.points), False, (0, 0, 0))
        self.gameDisplay.blit(self.textsurface, (5, 5))


class Player2(Game, pygame.sprite.Sprite):
    def __init__(self, gameDisplay, screenDims):
        Game.__init__(self, gameDisplay, screenDims)
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.monkey
        self.flagMonkey = self.flagMonkey
        self.speedpos = None
        self.speedneg = None
        self.y_change = 0
        self.x_change = 0
        self.rect = self.image.get_rect()
        self.rect.x = 256
        self.rect.y = 144
        self.points = 0

    def loadImages(self):
        self.monkey = getMemory("bought")
        if self.monkey == ["apprentice_monkey.png"]:
            self.monkey = pygame.image.load("data/apprentice_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load(
                "data/fightclub/images/apprentice_monkey_flag.png").convert_alpha()
        elif self.monkey == ["acid_monkey.png"]:
            self.monkey = pygame.image.load("data/acid_monkey.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/acid_monkey_flag.png").convert_alpha()
        elif self.monkey == ["dragon_monkey.png"]:
            self.monkey = pygame.image.load("data/dragon_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/dragon_monkey_flag.png").convert_alpha()
        elif self.monkey == ["engineer_monkey.png"]:
            self.monkey = pygame.image.load("data/engineer_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load(
                "data/fightclub/images/engineer_monkey_flag.png").convert_alpha()
        elif self.monkey == ["farmer_monkey.png"]:
            self.monkey = pygame.image.load("data/farmer_monkey.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/farmer_monkey_flag.png").convert_alpha()
        elif self.monkey == ["ninja_monkey.png"]:
            self.monkey = pygame.image.load("data/ninja_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/ninja_monkey_flag.png").convert_alpha()
        elif self.monkey == ["robo_monkey.png"]:
            self.monkey = pygame.image.load("data/robo_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/robo_monkey_flag.png").convert_alpha()
        elif self.monkey == ["super_monkey.png"]:
            self.monkey = pygame.image.load("data/super_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/super_monkey_flag.png").convert_alpha()
        else:
            self.monkey = pygame.image.load("data/default_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/charwflag.png").convert_alpha()

        self.monkey = pygame.transform.scale(self.monkey, (50, 50))

    def speed(self):
        self.speedpos = 5
        self.speedneg = -5

    def blitMonkey(self):
        self.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def score(self):
        self.textsurface = font.render(str(self.points), False, (0, 0, 0))
        self.gameDisplay.blit(self.textsurface, (1240, 5))


def unpause():
    global pause
    pause = False


def getMemory(key):
    with open("data/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        return data[key]


def setMemory(key, value):
    with open("data/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data[key] = value

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()


balance = getMemory("balance")
monkey = getMemory("bought")

# Sprite Groups
player1Group = pygame.sprite.Group()
player2Group = pygame.sprite.Group()
flagGroup = pygame.sprite.Group()
targetGroup = pygame.sprite.Group()

targetImg = pygame.image.load("data/fightclub/target.png")
gameDisplay.blit(targetImg, (1024, 728))


def addSprites():
    player1Group.add(player1)
    player2Group.add(player2)
    flagGroup.add(flag)
    targetGroup.add(target1)
    targetGroup.add(target2)


def updateFrameImages():
    global background, player1, player2, flag

    player2.blitMonkey()
    player1.blitMonkey()
    flag.blitFlag()
    if player1.image == player1.flagMonkey:
        target1.blitTarget()
    if player2.image == player2.flagMonkey:
        target2.blitTarget()
    player1Group.update()
    player2Group.update()
    flagGroup.update()
    target1.update()
    player2.score()
    player1.score()


# Calling Classes

game = Game(gameDisplay, screenDims)
player1 = Player1(gameDisplay, screenDims)
player2 = Player2(gameDisplay, screenDims)
flag = Flag(gameDisplay, screenDims)
background = Background(gameDisplay, screenDims)
target1 = TargetP1(gameDisplay, screenDims)
target2 = TargetP2(gameDisplay, screenDims)



# Loading & Blitting
addSprites()

background.blitBackground()

player1.blitMonkey()
player2.blitMonkey()
flag.blitFlag()
player1.speed()
player2.speed()


# Game Loop
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Movement Player1
        if pygame.event == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player1.x_change = player1.speedpos
            if event.key == pygame.K_a:
                player1.x_change = player1.speedneg
            if event.key == pygame.K_w:
                player1.y_change = player1.speedneg
            if event.key == pygame.K_s:
                player1.y_change = player1.speedpos

        if pygame.event == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                player1.x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1.y_change = 0

        player1.rect.x += player1.x_change
        player1.rect.y += player1.y_change

    updateFrameImages()
    game.updateFrame()

pygame.quit()
quit()