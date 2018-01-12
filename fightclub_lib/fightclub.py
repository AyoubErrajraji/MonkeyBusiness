import pygame
import json
from menu_lib import slidemenu

pygame.init()



width = 1280
height = 720
screenDims = (width, height)
gameDisplay = pygame.display.set_mode(screenDims)
font = pygame.font.SysFont('Comic Sans MS', 30)
done = False

exitButton = pygame.image.load("data/fightclub/exit.png")
hoverExit = pygame.image.load("data/fightclub/exit1.png")
play = pygame.image.load("data/fightclub/play.png")
hoverPlay = pygame.image.load("data/Fightclub/play1.png")

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
        self.backgroundImage = None

    def loadImage(self, name):
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
        self.flagMonkey= self.flagMonkey
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
            self.flagMonkey = pygame.image.load("data/fightclub/images/apprentice_monkey_flag.png").convert_alpha()
        elif self.monkey == ["acid_monkey.png"]:
            self.monkey = pygame.image.load("data/acid_monkey.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/acid_monkey_flag.png").convert_alpha()
        elif self.monkey == ["dragon_monkey.png"]:
            self.monkey = pygame.image.load("data/dragon_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/dragon_monkey_flag.png").convert_alpha()
        elif self.monkey == ["engineer_monkey.png"]:
            self.monkey = pygame.image.load("data/engineer_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/engineer_monkey_flag.png").convert_alpha()
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
        self.speedpos = 6
        self.speedneg = -6

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
            self.flagMonkey = pygame.image.load("data/fightclub/images/apprentice_monkey_flag.png").convert_alpha()
        elif self.monkey == ["acid_monkey.png"]:
            self.monkey = pygame.image.load("data/acid_monkey.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/acid_monkey_flag.png").convert_alpha()
        elif self.monkey == ["dragon_monkey.png"]:
            self.monkey = pygame.image.load("data/dragon_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/dragon_monkey_flag.png").convert_alpha()
        elif self.monkey == ["engineer_monkey.png"]:
            self.monkey = pygame.image.load("data/engineer_monkey_top.png").convert_alpha()
            self.flagMonkey = pygame.image.load("data/fightclub/images/engineer_monkey_flag.png").convert_alpha()
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
        self.speedpos = 6
        self.speedneg = -6

    def blitMonkey(self):
        self.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def score(self):
        self.textsurface = font.render(str(self.points), False, (0, 0, 0))
        self.gameDisplay.blit(self.textsurface, (1240, 5))


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def draw_text(surf, text, size, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


def unpause():
    global pause
    pause = False


def exitGame():
    pygame.quit()
    quit()


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
targetGroup1 = pygame.sprite.Group()
targetGroup2 = pygame.sprite.Group()


def addSprites():
    player1Group.add(player1)
    player2Group.add(player2)
    flagGroup.add(flag)
    targetGroup1.add(target1)
    targetGroup2.add(target2)


def updateFrameImages():
    global background, player1, player2, flag
    background.blitBackground()
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
    targetGroup1.update()
    targetGroup2.update()
    target1.update()
    player2.score()
    player1.score()

def button(msg, x, y, w, h, iimg, aimg, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] + y:
        gameDisplay.blit(aimg, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()

    else:
        gameDisplay.blit(iimg, (x, y, w, h))

def preGameScreen():
    gameDisplay.blit(background.backgroundImage, screenDims)
    draw_text(gameDisplay, "Banana Fight CLub", 64, width / 2, height / 4)
    draw_text(gameDisplay, "W/A/S/D Move left Player. Arrow Keys Move Right player", 32, width / 2, height / 2)
    draw_text(gameDisplay, "Press A Key To Begin", 45, width / 2, height / 3)
    pygame.display.update()
    waiting = True
    while waiting:
        game.frame.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


def gameOver1():

    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.fill((0, 0, 0, 150))

    # Blitting
    background.blitBackground()
    player1.blitMonkey()
    player2.blitMonkey()
    flag.blitFlag()

    gameDisplay.blit(s, (0, 0))

    label = font.render("Player1 Has Won!", 2, (255, 255, 255))
    gameDisplay.blit(label, (130, 280))

    # button("Play Again", 450, 400, 20, 20, play, hoverPlay, restart)
    button("Back To Menu", 600, 280, 100, 50, exitButton, hoverExit, exitGame)

    pygame.display.update()
    waiting = True
    while waiting:
        game.frame.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



def gameOver2():
    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.fill((0, 0, 0, 150))

    # Blitting
    background.blitBackground()
    player1.blitMonkey()
    player2.blitMonkey()
    flag.blitFlag()

    gameDisplay.blit(s, (0, 0))

    label = font.render("Player2 Has Won!", 2, (255, 255, 255))
    gameDisplay.blit(label, (130, 280))

    # button("Play Again", 450, 400, 20, 20, play, hoverPlay, restart)
    button("Back To Menu", 600, 280, 100, 50, exitButton, hoverExit, exitGame)

    pygame.display.update()
    waiting = True
    while waiting:
        game.frame.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def paused():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((width / 2), (height/2))
    gameDisplay.blit(TextSurf, TextRect)

    button("Continue", 400, 450, 20, 20, play, hoverPlay, unpause)
    button("Back To Menu", 600, 450, 100, 50, exitButton, hoverExit, exitGame)

    pygame.display.update()
    while pause:
        game.frame.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


# Calling Classes

game = Game(gameDisplay, screenDims)
player1 = Player1(gameDisplay, screenDims)
player2 = Player2(gameDisplay, screenDims)
flag = Flag(gameDisplay, screenDims)
background = Background(gameDisplay, screenDims)
target1 = TargetP1(gameDisplay, screenDims)
target2 = TargetP2(gameDisplay, screenDims)


# Loading
addSprites()
player1.speed()
player2.speed()
background.loadImage("background1.png")

background.blitBackground()
player1.blitMonkey()
player2.blitMonkey()
flag.blitFlag()


class run():
    def __init__(self):
        self.runm = self.run

    def run(self):
        done = False
        intro = True
        game_over = False
        global pause
        while not done:
            if game_over:
                gameOver1()

            elif intro:
                preGameScreen()
                intro = False




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    quit()


                # Move Player 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player1.x_change = player1.speedneg
                    elif event.key == pygame.K_RIGHT:
                        player1.x_change = player1.speedpos
                    elif event.key == pygame.K_UP:
                        player1.y_change = player1.speedneg
                    elif event.key == pygame.K_DOWN:
                        player1.y_change = player1.speedpos
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player1.x_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player1.y_change = 0

                # Move Player 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player2.x_change = player2.speedneg
                    elif event.key == pygame.K_d:
                        player2.x_change = player2.speedpos
                    elif event.key == pygame.K_w:
                        player2.y_change = player2.speedneg
                    elif event.key == pygame.K_s:
                        player2.y_change = player2.speedpos
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        player2.x_change = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        player2.y_change = 0

            player1.rect.x += player1.x_change
            player1.rect.y += player1.y_change

            player2.rect.x += player2.x_change
            player2.rect.y += player2.y_change

            # Collisions

            if player1.image == player1.monkey and player2.image == player2.monkey:

                if pygame.sprite.spritecollide(player1, flagGroup, False):
                    player1.image = player1.flagMonkey
                    target1.blitTarget()
                    flag.image = flag.noFlag

                if pygame.sprite.spritecollide(player2, flagGroup, False):
                    player2.image = player2.flagMonkey
                    target2.blitTarget()
                    flag.image = flag.noFlag

            if player1.image == player1.flagMonkey:
                if pygame.sprite.spritecollide(player1, targetGroup1, False):
                    player1.image = player1.monkey
                    player1.points += 250
                    flag.image = flag.flag

                if pygame.sprite.spritecollide(player2, player1Group, False):
                    player1.image = player1.monkey
                    player2.image = player2.flagMonkey

            if player2.image == player2.flagMonkey:
                if pygame.sprite.spritecollide(player2, targetGroup2, False):
                    player2.image = player2.monkey
                    player2.points += 250
                    flag.image = flag.flag

                if pygame.sprite.spritecollide(player1, player2Group, False):
                    player2.image = player2.monkey
                    player1.image = player1.flagMonkey

            if player1.points == 250:
                game_over = True

            updateFrameImages()
            game.updateFrame()

        self.runm()