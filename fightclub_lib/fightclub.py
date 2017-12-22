import pygame
pygame.init()


class run():
    def runm(self):
        width = 1280
        height = 720

        color = (0, 255, 0)

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

        #Game Loop
        while done == False :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5
                    elif event.key == pygame.K_UP:
                        y_change = -5
                    elif event.key == pygame.K_DOWN:
                        y_change = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
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

            pygame.display.update()
            clock.tick(60)

        pygame.quit()
        quit()