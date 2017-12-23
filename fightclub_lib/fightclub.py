import pygame

pygame.init()

class run():
    def runm(self):
        width = 1280
        height = 720

        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 0)
        bright_green = (0, 200, 0)
        red = (255, 0, 0)
        bright_red = (200, 0, 0)

        font = pygame.font.SysFont('Comic Sans MS', 30)

        gameDisplay = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Banana Fight Club')

        clock = pygame.time.Clock()
        done = False
        #Loading Images
        mainImg = pygame.image.load('data/fightclub/monkey.png').convert_alpha()
        charwFlagImg = pygame.image.load('data/fightclub/charwflag.png').convert_alpha()

        flagImg = pygame.image.load("data/fightclub/flag.png").convert_alpha()
        noFlagImg = pygame.image.load("data/fightclub/noflag.png").convert_alpha()
        targetImg = pygame.image.load("data/fightclub/target.png").convert_alpha()

        bckImg = pygame.image.load("data/fightclub/background1.png").convert()
        bckImg = pygame.transform.scale(bckImg, (width, height))


        def quitgame():
            pygame.quit()
            quit()

        def background(x, y):
            gameDisplay.blit(bckImg, (x, y))

        def character(x, y):
            gameDisplay.blit(mainImg, (x, y))

        def charwithFlag(x, y):
            gameDisplay.blit(charwFlagImg, (x, y))

        def char(x, y):
            gameDisplay.blit(mainImg, (x, y))

        x = (width * 0.8)
        y = (height * 0.8)
        x_change = 0
        y_change = 0
        character_speed = 0

        def flag(x, y):
            gameDisplay.blit(flagImg, (x, y))

        x_flag = 600
        y_flag = 300

        def noFlag(x, y):
            gameDisplay.blit(noFlagImg, (x, y))

        def flag2(x, y):
            gameDisplay.blit(flagImg, (x, y))

        def target(x, y):
            gameDisplay.blit(targetImg, (x, y))

        x_target = 1024
        y_target = 576

        points = 0

        def score(x, y):
            textsurface = font.render(str(points), False, (0, 0, 0))
            gameDisplay.blit(textsurface, (x, y))

        def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()

        def button(msg, x, y, w, h, ic, ac, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            print(click)
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

                if click[0] == 1 and action != None:
                    action()
            else:
                pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

            smallText = pygame.font.SysFont("comicsansms", 20)
            textSurf, textRect = text_objects(msg, smallText)
            textRect.center = ((x + (w / 2)), (y + (h / 2)))
            gameDisplay.blit(textSurf, textRect)

        def unpause():
            global pause
            pause = False

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

                button("Continue", 150, 450, 100, 50, green,bright_green, unpause)
                button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

                pygame.display.update()
                clock.tick(30)

        #Game Loop

        global pause
        while done == False :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x_change = -5
                    elif event.key == pygame.K_d:
                        x_change = 5
                    elif event.key == pygame.K_w:
                        y_change = -5
                    elif event.key == pygame.K_s:
                        y_change = 5
                    if event.key == pygame.K_p:
                        pause = True
                        paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        x_change = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        y_change = 0

            x += x_change
            y += y_change

            background(0,0)
            character(x, y)
            flag(x_flag, y_flag)

            #Flag Collision
            if y > 270 and y < 330 and x > 570 and x < 630:
                character = charwithFlag
                flag = noFlag

            if character == charwithFlag:
                target(x_target, y_target)
                if x > 994 and x < 1054 and y > 546 and y < 606:
                    character = char
                    flag = flag2
                    points += 50

            score(5, 5)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()
        quit()