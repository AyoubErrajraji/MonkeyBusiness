import pygame
import json
from menu_lib import slidemenu
from fightclub_lib import fightclub

pygame.init()



width = 1280
height = 720
screenDims = (width, height)
gameDisplay = pygame.display.set_mode(screenDims)
font1 = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 60)
font2 = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 45)
font3 = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 30)
done = False
pause = False

exitButton = pygame.image.load("data/fightclub/exit.png")
hoverExit = pygame.image.load("data/fightclub/exit1.png")
play = pygame.image.load("data/fightclub/play.png")
hoverPlay = pygame.image.load("data/Fightclub/play1.png")
stopMusicButton = pygame.image.load("data/fightclub/music.png").convert_alpha()
stopMusicButtonHover = pygame.image.load("data/fightclub/musicHover.png").convert_alpha()
stopMusicButton = pygame.transform.scale(stopMusicButton, (50, 50))
stopMusicButtonHover = pygame.transform.scale(stopMusicButtonHover, (50, 50))

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
        self.backgroundImage = pygame.image.load("data/fightclub/background.png")
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, self.screenDims)

    def blitBackground(self):
        self.gameDisplay.blit(self.backgroundImage, (0, 0))


class Wall(Game, pygame.sprite.Sprite):
    def __init__(self, x, y):
        Game.__init__(self, gameDisplay, screenDims)
        pygame.sprite.Sprite.__init__(self)
        self.loadImage()
        self.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def loadImage(self):
        self.image = pygame.image.load("data/fightclub/bush.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
    def draw(self):
        self.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))


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
        self.mask = pygame.mask.from_surface(self.image)

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
        self.mask = pygame.mask.from_surface(self.image)

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
        self.textsurface = font2.render(str(self.points), False, (0, 0, 0))
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
        self.mask = pygame.mask.from_surface(self.image)

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
        self.textsurface = font2.render(str(self.points), False, (0, 0, 0))
        self.gameDisplay.blit(self.textsurface, (1220, 5))


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def draw_text1(surf, text, size, x, y):
    text_surface = font1.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

def draw_text2(surf, text, size, x, y):
    text_surface = font2.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

def draw_text3(surf, text, size, x, y):
    text_surface = font3.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


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
wallGroup = pygame.sprite.Group()


def addSprites():
    player1Group.add(player1)
    player2Group.add(player2)
    flagGroup.add(flag)
    targetGroup1.add(target1)
    targetGroup2.add(target2)
    wallGroup.add(wall1)
    wallGroup.add(wall1_1)
    wallGroup.add(wall1_2)
    wallGroup.add(wall1_3)
    wallGroup.add(wall1_4)
    wallGroup.add(wall1_5)
    wallGroup.add(wall1_6)
    wallGroup.add(wall2)
    wallGroup.add(wall2_1)
    wallGroup.add(wall2_2)
    wallGroup.add(wall2_3)
    wallGroup.add(wall2_4)
    wallGroup.add(wall2_5)
    wallGroup.add(wall2_6)
    wallGroup.add(wall3)
    wallGroup.add(wall4)


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
    wall1.draw()
    wall1_1.draw()
    wall1_2.draw()
    wall1_3.draw()
    wall1_4.draw()
    wall1_5.draw()
    wall1_6.draw()
    wall2.draw()
    wall2_1.draw()
    wall2_2.draw()
    wall2_3.draw()
    wall2_4.draw()
    wall2_5.draw()
    wall2_6.draw()
    wall3.draw()
    wall4.draw()

class button():
    def __init__(self, msg, x, y, w, h, iimg, aimg, action=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.msg = msg

        self.iimg = iimg
        self.aimg = aimg

        self.action = action

        self.paint()

    def paint(self):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.w >= mouse[0] >= self.x and self.y + self.h >= mouse[1] >= self.y:
            gameDisplay.blit(self.aimg, (self.x, self.y, self.w, self.h))

            if click[0] == 1 and self.action != None:
                self.action()

        else:
            gameDisplay.blit(self.iimg, (self.x, self.y, self.w, self.h))
        pygame.display.update()

    def game_logic(self):
        self.paint()

def preGameScreen():
    gameDisplay.fill((0, 0, 0))
    draw_text1(gameDisplay, "Banana Fight CLub", 64, width / 2, height / 4)
    draw_text2(gameDisplay, "W/A/S/D Move left Player. Arrow Keys Move Right player", 32, width / 2, height / 2)
    draw_text3(gameDisplay, "Press A Key To Begin", 45, width / 2, height / 3)
    pygame.display.update()
    waiting = True
    while waiting:
        game.frame.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


def unpause():
    global pause
    pause = False


def exitGame():
    pygame.mixer.stop()
    mymenu = slidemenu.run()
    mymenu.runm(100)

def restart():
    mymenu = fightclub.run()
    mymenu.runm()


def gameOver1():
    points = getMemory("balance")
    points += 250

    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.fill((0, 0, 0, 150))

    # Blitting
    background.blitBackground()
    player1.blitMonkey()
    player2.blitMonkey()
    flag.blitFlag()

    gameDisplay.blit(s, (0, 0))

    draw_text1(gameDisplay, "Player 1 has won!", 60, width / 2, height / 4)
    global intro
    intro = False
    player2.points = 0
    player1.points = 0
    player1.x_change = 0
    player2.x_change = 0

    pygame.display.update()
    waiting = True
    while waiting:
        game.frame.tick(60)
        button("Play Again", 580, height / 2, 20, 20, play, hoverPlay, restart)
        button("Back To Menu", 700, height / 2, 100, 50, exitButton, hoverExit, exitGame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



def gameOver2():
    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.fill((0, 0, 0, 150))

    # Blitting
    background.blitBackground()
    player1.blitMonkey()
    player2.blitMonkey()
    flag.blitFlag()

    gameDisplay.blit(s, (0, 0))

    draw_text1(gameDisplay, "Player 2 has won!", 60, width / 2, height / 4)
    global intro
    intro = False
    player2.points = 0
    player1.points = 0
    player1.x_change = 0
    player2.x_change = 0

    pygame.display.update()
    waiting = True
    while waiting:
        game.frame.tick(60)
        button("Play Again", 580, height / 2, 20, 20, play, hoverPlay, restart)
        button("Back To Menu", 700, height / 2, 100, 50, exitButton, hoverExit, exitGame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def paused():
    global pause
    draw_text1(gameDisplay, "Paused", 80, width / 2, height / 4)

    pygame.display.update()

    while pause:
        game.frame.tick(60)
        button("Continue", 400, 450, 20, 20, play, hoverPlay, unpause)
        button("Back To Menu", 600, 450, 100, 50, exitButton, hoverExit, exitGame)
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
wall1 = Wall(400, 0)
wall1_1 = Wall(400, 50)
wall1_2 = Wall(400, 100)
wall1_3 = Wall(400, 150)
wall1_4 = Wall(400, 200)
wall1_5 = Wall(400, 250)
wall1_6 = Wall(400, 300)
wall2 = Wall(820, 320)
wall2_1 = Wall(820, 370)
wall2_2 = Wall(820, 420)
wall2_3 = Wall(820, 470)
wall2_4 = Wall(820, 520)
wall2_5 = Wall(820, 570)
wall2_6 = Wall(820, 620)
wall3 = Wall(1100, 180)
wall4 = Wall(250, 500)



# Loading
addSprites()
player1.speed()
player2.speed()
background.loadImage("background1.png")

background.blitBackground()
player1.blitMonkey()
player2.blitMonkey()
flag.blitFlag()
wall1.draw()
wall1_1.draw()
wall1_2.draw()
wall1_3.draw()
wall1_4.draw()
wall1_5.draw()
wall1_6.draw()
wall2.draw()
wall2_1.draw()
wall2_2.draw()
wall2_3.draw()
wall2_4.draw()
wall2_5.draw()
wall2_6.draw()
wall3.draw()
wall4.draw()


class run():
    def __init__(self):
        self.runm = self.run

    def run(self):
        done = False
        intro = True
        game_over1 = False
        game_over2 = False
        pygame.mixer.music.load("data/fightclub/CantinaBand.mp3")
        pygame.mixer.music.play(-1)
        horn = pygame.mixer.Sound("data/fightclub/horn.wav")
        global points
        global pause
        while not done:
            if game_over1:
                gameOver1()
                setMemory("balance", points)

            if game_over2:
                gameOver2()

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

                        while pause:
                            paused()
                            pause = False

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
                    # if event.key == pygame.K_ESCAPE:
                        # pause = True
                        # paused()

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
            # Flag
            if player1.image == player1.monkey and player2.image == player2.monkey:

                if pygame.sprite.spritecollide(player1, flagGroup, False, pygame.sprite.collide_mask):
                    player1.image = player1.flagMonkey
                    target1.blitTarget()
                    flag.image = flag.noFlag

                if pygame.sprite.spritecollide(player2, flagGroup, False, pygame.sprite.collide_mask):
                    player2.image = player2.flagMonkey
                    target2.blitTarget()
                    flag.image = flag.noFlag

            # Player 1

            if player1.image == player1.flagMonkey:
                if pygame.sprite.spritecollide(player1, targetGroup1, False):
                    player1.image = player1.monkey
                    player1.points += 40
                    flag.image = flag.flag
                    horn.play()

                elif pygame.sprite.spritecollide(player2, player1Group, False, pygame.sprite.collide_mask):
                    player1.image = player1.monkey
                    player2.image = player2.flagMonkey

            # Player 2

            if player2.image == player2.flagMonkey:
                if pygame.sprite.spritecollide(player2, targetGroup2, False):
                    player2.image = player2.monkey
                    player2.points += 40
                    flag.image = flag.flag
                    horn.play()

                elif pygame.sprite.spritecollide(player1, player2Group, False, pygame.sprite.collide_mask):
                    player2.image = player2.monkey
                    player1.image = player1.flagMonkey

            # Wall Collisions

            if pygame.sprite.spritecollide(player1, wallGroup, False, pygame.sprite.collide_mask):
                player1.x_change *= 0
                player1.y_change *= 0

            if pygame.sprite.spritecollide(player2, wallGroup, False, pygame.sprite.collide_mask):
                player2.x_change *= 0
                player2.y_change *= 0

            if player1.points == 200:
                game_over1 = True

            if player2.points == 200:
                game_over2 = True

            # Out Of Boundary Player 2

            angle = 90
            rotplayer2 = pygame.transform.rotate(player2.image, angle)
            position = rotplayer2.get_rect(center=(player2.rect.x, player2.rect.y))

            wrap_around = False

            if position[0] < 0:
                # off screen left
                position.move_ip(width, 0)
                wrap_around = True

            if position[0] + rotplayer2.get_width() > width:
                # off screen right
                position.move_ip(-width, 0)
                wrap_around = True

            if position[1] < 0:
                # off screen top
                position.move_ip(0, height)
                wrap_around = True

            if position[1] + rotplayer2.get_height() > height:
                # off screen bottom
                position.move_ip(0, -height)
                wrap_around = True

            if wrap_around:
                gameDisplay.blit(rotplayer2, position)

            position[0] %= width
            position[1] %= height
            player2.rect.x %= width
            player2.rect.y %= height

            # Out Of Boundary Player 1
            angle = 90
            rotplayer1 = pygame.transform.rotate(player1.image, angle)
            position = rotplayer1.get_rect(center=(player1.rect.x, player1.rect.y))

            wrap_around = False

            if position[0] < 0:
                # off screen left
                position.move_ip(width, 0)
                wrap_around = True

            if position[0] + rotplayer1.get_width() > width:
                # off screen right
                position.move_ip(-width, 0)
                wrap_around = True

            if position[1] < 0:
                # off screen top
                position.move_ip(0, height)
                wrap_around = True

            if position[1] + rotplayer1.get_height() > height:
                # off screen bottom
                position.move_ip(0, -height)
                wrap_around = True

            if wrap_around:
                gameDisplay.blit(rotplayer1, position)

            position[0] %= width
            position[1] %= height
            player1.rect.x %= width
            player1.rect.y %= height

            updateFrameImages()
            game.updateFrame()

        self.runm()