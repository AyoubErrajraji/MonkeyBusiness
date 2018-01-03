import pygame
from menu_lib import slidemenu
import json
from fightclub_lib import room

pygame.init()

class run():
    def runm(self):
        width = 1280
        height = 720

        black = (0, 0, 0)
        white = (255, 255, 255)
        grey = (50, 50, 50)

        font = pygame.font.SysFont('Comic Sans MS', 30)
        WALLS = pygame.sprite.Group()

        gameDisplay = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Banana Fight Club')

        clock = pygame.time.Clock()

        wall = room.Wall(0, 600, 300, 30, black, gameDisplay)
        WALLS.add(wall)

        done = False
        # Loading Images
        # Characters
        acid = pygame.image.load("data/acid_monkey.png").convert_alpha()
        apprentice = pygame.image.load("data/apprentice_monkey_top.png").convert_alpha()
        default = pygame.image.load("data/default_monkey_top.png").convert_alpha()
        dragon = pygame.image.load("data/dragon_monkey_top.png").convert_alpha()
        engineer = pygame.image.load("data/engineer_monkey_top.png").convert_alpha()
        farmer = pygame.image.load("data/farmer_monkey.png").convert_alpha()
        ninja = pygame.image.load("data/ninja_monkey_top.png").convert_alpha()
        robo = pygame.image.load("data/robo_monkey_top.png").convert_alpha()
        superMonkey = pygame.image.load("data/super_monkey_top.png").convert_alpha()

        # Transforming Characters
        acid = pygame.transform.scale(acid, (40, 46))
        apprentice = pygame.transform.scale(apprentice, (40, 46))
        default = pygame.transform.scale(default, (40, 46))
        pygame.transform.scale(dragon, (40, 46))
        engineer = pygame.transform.scale(engineer, (40, 46))
        farmer = pygame.transform.scale(farmer, (40, 46))
        ninja = pygame.transform.scale(ninja, (40, 46))
        robo = pygame.transform.scale(robo, (40, 46))
        superMonkey = pygame.transform.scale(superMonkey, (40, 46))

        mainImg = pygame.image.load('data/fightclub/monkey.png').convert_alpha()
        charwFlagImg = pygame.image.load('data/fightclub/charwflag.png').convert_alpha()

        flagImg = pygame.image.load("data/fightclub/flag.png").convert_alpha()
        noFlagImg = pygame.image.load("data/fightclub/noflag.png").convert_alpha()
        targetImg = pygame.image.load("data/fightclub/target.png").convert_alpha()

        bckImg = pygame.image.load("data/fightclub/background1.png").convert()
        bckImg = pygame.transform.scale(bckImg, (width, height))

        exitButton = pygame.image.load("data/fightclub/exit.png")
        hoverExit = pygame.image.load("data/fightclub/exit1.png")
        play = pygame.image.load("data/fightclub/play.png")
        hoverplay = pygame.image.load("data/fightclub/play1.png")

        def back():
            mymenu = slidemenu.run()
            mymenu.runm()

        def quit():
            pygame.quit()
            quit()

        def background(x, y):
            gameDisplay.blit(bckImg, (x, y))

        def player(x, y):
            if monkey == ["apprentice_monkey.png"]:
                gameDisplay.blit(apprentice, (x, y))
            elif monkey == ["acid_monkey.png"]:
                gameDisplay.blit(acid, (x, y))
            elif monkey == ["dragon_monkey.png"]:
                gameDisplay.blit(dragon, (x, y))
            elif monkey == ["engineer_monkey.png"]:
                gameDisplay.blit(engineer, (x, y))
            elif monkey == ["farmer_monkey.png"]:
                gameDisplay.blit(farmer, (x, y))
            elif monkey == ["ninja_monkey.png"]:
                gameDisplay.blit(ninja, (x, y))
            elif monkey == ["robo_monkey.png"]:
                gameDisplay.blit(robo, (x, y))
            elif monkey == ["super_monkey.png"]:
                gameDisplay.blit(superMonkey, (x, y))
            else:
                gameDisplay.blit(default, (x, y))

        def player2(x, y):
            if monkey == ["apprentice_monkey.png"]:
                gameDisplay.blit(apprentice, (x, y))
            elif monkey == ["acid_monkey.png"]:
                gameDisplay.blit(acid, (x, y))
            elif monkey == ["dragon_monkey.png"]:
                gameDisplay.blit(dragon, (x, y))
            elif monkey == ["engineer_monkey.png"]:
                gameDisplay.blit(engineer, (x, y))
            elif monkey == ["farmer_monkey.png"]:
                gameDisplay.blit(farmer, (x, y))
            elif monkey == ["ninja_monkey.png"]:
                gameDisplay.blit(ninja, (x, y))
            elif monkey == ["robo_monkey.png"]:
                gameDisplay.blit(robo, (x, y))
            elif monkey == ["super_monkey.png"]:
                gameDisplay.blit(superMonkey, (x, y))
            else:
                gameDisplay.blit(default, (x, y))

        def character(x, y):
            gameDisplay.blit(mainImg, (x, y))

        def charwithFlag(x, y):
            gameDisplay.blit(charwFlagImg, (x, y))

        def char(x, y):
            if monkey == ["apprentice_monkey.png"]:
                gameDisplay.blit(apprentice, (x, y))
            elif monkey == ["acid_monkey.png"]:
                gameDisplay.blit(acid, (x, y))
            elif monkey == ["dragon_monkey.png"]:
                gameDisplay.blit(dragon, (x, y))
            elif monkey == ["engineer_monkey.png"]:
                gameDisplay.blit(engineer, (x, y))
            elif monkey == ["farmer_monkey.png"]:
                gameDisplay.blit(farmer, (x, y))
            elif monkey == ["ninja_monkey.png"]:
                gameDisplay.blit(ninja, (x, y))
            elif monkey == ["robo_monkey.png"]:
                gameDisplay.blit(robo, (x, y))
            elif monkey == ["super_monkey.png"]:
                gameDisplay.blit(superMonkey, (x, y))
            else:
                gameDisplay.blit(default, (x, y))

        x = (width * 0.8)
        y = (height * 0.8)
        x_change = 0
        y_change = 0
        speed = 1

        def character2(x, y):
            gameDisplay.blit(mainImg, (x, y))

        def charwithFlag2(x, y):
            gameDisplay.blit(charwFlagImg, (x, y))

        def char2(x, y):
            if monkey == ["apprentice_monkey.png"]:
                gameDisplay.blit(apprentice, (x, y))
            elif monkey == ["acid_monkey.png"]:
                gameDisplay.blit(acid, (x, y))
            elif monkey == ["dragon_monkey.png"]:
                gameDisplay.blit(dragon, (x, y))
            elif monkey == ["engineer_monkey.png"]:
                gameDisplay.blit(engineer, (x, y))
            elif monkey == ["farmer_monkey.png"]:
                gameDisplay.blit(farmer, (x, y))
            elif monkey == ["ninja_monkey.png"]:
                gameDisplay.blit(ninja, (x, y))
            elif monkey == ["robo_monkey.png"]:
                gameDisplay.blit(robo, (x, y))
            elif monkey == ["super_monkey.png"]:
                gameDisplay.blit(superMonkey, (x, y))
            else:
                gameDisplay.blit(default, (x, y))

        x2 = (width * 0.2)
        y2 = (height * 0.2)
        x2_change = 0
        y2_change = 0

        def flag(x, y):
            gameDisplay.blit(flagImg, (x, y))

        def setFlag(x, y):
            gameDisplay.blit(flagImg, (x, y))

        x_flag = 600
        y_flag = 300

        def noFlag(x, y):
            gameDisplay.blit(noFlagImg, (x, y))

        def flag2(x, y):
            gameDisplay.blit(flagImg, (x, y))

        def target(x, y):
            gameDisplay.blit(targetImg, (x, y))

        def target2(x, y):
            gameDisplay.blit(targetImg, (x, y))

        x_target = 1024
        y_target = 576

        x_target2 = width * 0.2
        y_target2 = height * 0.2

        points = 0
        points2 = 0

        def score(x, y):
            textsurface = font.render(str(points), False, (0, 0, 0))
            gameDisplay.blit(textsurface, (x, y))

        def score2(x, y):
            textsurface2 = font.render(str(points2), False, (0, 0, 0))
            gameDisplay.blit(textsurface2, (x, y))

        def text_objects(text, font):
            textSurface = font.render(text, True, white)
            return textSurface, textSurface.get_rect()

        def button(msg, x, y, w, h, iimg, aimg, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                gameDisplay.blit(aimg, (x, y, w, h))

                if click[0] == 1 and action != None:
                    action()
            else:
                gameDisplay.blit(iimg, (x, y, w, h))

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

        def paused():
            largeText = pygame.font.SysFont("comicsansms", 115)
            TextSurf, TextRect = text_objects("Paused", largeText)
            TextRect.center = ((width / 2), (height / 2))
            gameDisplay.blit(TextSurf, TextRect)

            while pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                button("Continue", 400, 450, 20, 20, play, hoverplay, unpause)
                button("Back To Menu", 600, 450, 100, 50, exitButton, hoverExit, back)

                # balance = setMemory("balance", score)

                pygame.display.update()
                clock.tick(30)

        # Game Loop

        global pause
        while done == False :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                # Moving Player 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x_change = -5
                    elif event.key == pygame.K_d:
                        x_change = 5
                    elif event.key == pygame.K_w:
                        y_change = -5
                    elif event.key == pygame.K_s:
                        y_change = 5
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        x_change = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        y_change = 0

                # Moving Player 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x2_change = -5
                    elif event.key == pygame.K_RIGHT:
                        x2_change = 5
                    elif event.key == pygame.K_UP:
                        y2_change = -5
                    elif event.key == pygame.K_DOWN:
                        y2_change = 5
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x2_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y2_change = 0

            x += x_change
            y += y_change

            x2 += x2_change
            y2 += y2_change

            background(0,0)
            player(x, y)
            player2(x2, y2)
            flag(x_flag, y_flag)

            flag = setFlag
            player = char
            player2 = char2

            # Flag Collision Player 1
            if flag == setFlag and player == char:
                if x > 570 and x < 630 and y > 270 and y < 330:
                    player = charwithFlag

                if player == charwithFlag:
                    flag = noFlag
                    target(x_target, y_target)
                    if x > 994 and x < 1054 and y > 546 and y < 606:
                        player = char
                        points += 50

            # Flag Collision Player 2

            score(5, 5)
            score2(1240, 5)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()
        quit()