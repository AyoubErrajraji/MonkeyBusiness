import pygame, sys
from escapetheguards_lib import config

pygame.init()

pygame.display.set_caption('Escape The Guards')

clock = pygame.time.Clock()
pause = False

backgroundintro = pygame.image.load('data/escapetheguards/bgintro.png').convert()
backgroundintro = pygame.transform.scale(backgroundintro, (config.screen_width, config.screen_height))
logoImg = pygame.image.load('data/escapetheguards/logo.png')
playerImg = pygame.image.load('data/escapetheguards/player.png')
playerImg = pygame.transform.scale(playerImg, (70, 70))
containerImg = pygame.image.load('data/escapetheguards/container1.png').convert_alpha()

barrelsideImg = pygame.image.load('data/escapetheguards/barrelside.png')
barrelsideImg = pygame.transform.scale(barrelsideImg, (200, 250))
carImg = pygame.image.load('data/escapetheguards/car.png').convert_alpha()
car1Img = pygame.image.load('data/escapetheguards/car1.png').convert_alpha()
car1Img = pygame.transform.scale(car1Img, (300, 200))
excavatorImg = pygame.image.load('data/escapetheguards/excavator.png').convert_alpha()
truckImg = pygame.image.load('data/escapetheguards/truck.png').convert_alpha()
monkeyImg = pygame.image.load('data/escapetheguards/monkey.png').convert_alpha()
config.screen.blit(backgroundintro, (0, 0))
config.screen.blit(logoImg, (300, 300))
config.screen.blit(logoImg, (730, 300))

class run():
    def text_objects(text, font):
        textSurface = font.render(text, True, config.white)
        return textSurface, textSurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, action=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(config.screen, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                if action == "start":
                    self.game_loop()
                elif action == "quit":
                    pygame.quit()
                    quit()
                elif action == "leave":
                    self.game_intro()
                elif action == "settings":
                    self.settings_game()
                elif action == "unpaused":
                    self.unpause()



                else:
                    pygame.draw.rect(config.screen, ic, (x, y, w, h))

                    smallText = pygame.font.SysFont("comicsansms", 20)
                    textSurf, textRect = self.text_objects(msg, smallText)
                    textRect.center = ((x + (w / 2)), (y + (h / 2)))
                    config.screen.blit(textSurf, textRect)

    def unpause(self):
        global pause
        pause = False

    def paused(self):

        pause = True
        while pause:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                config.screen.fill(config.light_black)
                pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])

                myfont = pygame.font.SysFont("comicsansms", 20)
                label = myfont.render("Levels completed: 2", 1, (config.black))
                config.screen.blit(label, (982, 10))
                label = myfont.render("Banana Points Earned: 10", 1, (config.black))
                config.screen.blit(label, (982, 110))
                label = myfont.render("Current Level: 3", 1, (config.black))
                config.screen.blit(label, (982, 210))
                pygame.draw.rect(config.screen, config.brown, [650, 370, 300, 30])
                pygame.draw.rect(config.screen, config.brown, [950, 0, 30, 720])
                pygame.draw.rect(config.screen, config.brown, [0, 0, 780, 30])
                pygame.draw.rect(config.screen, config.brown, [0, 0, 30, 520])
                pygame.draw.rect(config.screen, config.brown, [0, 690, 980, 30])
                config.screen.blit(playerImg, (0, 600))
                config.screen.blit(containerImg, (30, 30))
                config.screen.blit(logoImg, (1010, 350))

                config.screen.blit(carImg, (200, 400))
                config.screen.blit(excavatorImg, (500, 100))
                config.screen.blit(truckImg, (650, 500))

                myfont = pygame.font.SysFont("comicsansms", 115)
                label = myfont.render(" GAME PAUSED!!", 1, (config.black))
                config.screen.blit(label, (300, 340))

                self.button("Continue!", 980, 670, 100, 50, config.black, config.light_black, "unpaused")
                self.button("Settings!", 1080, 670, 100, 50, config.black, config.light_black, "settings")
                self.button("Quit!", 1180, 670, 100, 50, config.black, config.light_black, "quit")

                pygame.display.update()
                clock.tick(15)

    def game_intro(self):
        global pause
        intro = True

        x = (config.screen_width * 0.785)
        y = (config.screen_height * 0.58)

        while intro:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

            config.screen.blit(backgroundintro, (0, 0))

            myfont = pygame.font.SysFont("comicsansms", 80)
            label = myfont.render("Escape Those Guards!", 1, (config.black))
            config.screen.blit(label, (230, 120))

            self.button("Let's Play!", 590, 350, 100, 50, config.black, config.light_black, "start")
            self.button("Settings!", 590, 450, 100, 50, config.black, config.light_black, "settings")
            self.button("Quit!", 590, 550, 100, 50, config.black, config.light_black, "quit")

            config.screen.blit(monkeyImg, (-50, 300))
            config.screen.blit(monkeyImg, (730, 300))

            pygame.display.update()
            clock.tick(15)

    def settings_game(self):
        global pause

        x = (config.screen_width * 0.785)
        y = (config.screen_height * 0.58)

        while settings_game:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            config.screen.blit(backgroundintro, (0, 0))

            myfont = pygame.font.SysFont("comicsansms", 80)
            label = myfont.render("Settings:", 1, (config.black))
            config.screen.blit(label, (470, 80))

            myfont = pygame.font.SysFont("comicsansms", 20)
            label = myfont.render("Resolution:", 1, (config.black))
            config.screen.blit(label, (470, 220))

            label = myfont.render("1280 x  720", 1, (config.black))
            config.screen.blit(label, (600, 220))

            label = myfont.render("1920 x 1080", 1, (config.black))
            config.screen.blit(label, (600, 250))

            label = myfont.render("Fullscreen", 1, (config.black))
            config.screen.blit(label, (600, 280))

            label = myfont.render("Controls:", 1, (config.black))
            config.screen.blit(label, (470, 310))

            label = myfont.render("Move forwards:", 1, (config.black))
            config.screen.blit(label, (600, 340))

            label = myfont.render("Move backwards:", 1, (config.black))
            config.screen.blit(label, (600, 370))

            label = myfont.render("Move Sideways:", 1, (config.black))
            config.screen.blit(label, (600, 400))

            label = myfont.render("Pause the game:", 1, (config.black))
            config.screen.blit(label, (600, 430))

            label = myfont.render("Key W", 1, (config.black))
            config.screen.blit(label, (780, 340))

            label = myfont.render("Key S", 1, (config.black))
            config.screen.blit(label, (780, 370))

            label = myfont.render("Key A (Left) and Key D (Right)", 1, (config.black))
            config.screen.blit(label, (780, 400))

            label = myfont.render("Key P", 1, (config.black))
            config.screen.blit(label, (780, 430))

            label = myfont.render("Quit The Game:", 1, (config.black))
            config.screen.blit(label, (600, 460))

            label = myfont.render("Key Escape or top left X", 1, (config.black))
            config.screen.blit(label, (780, 460))

            button("Back to Intro", 450, 670, 140, 50, config.black, config.light_black, "leave")
            button("Back to Game", 740, 670, 140, 50, config.black, config.light_black, "start")

            pygame.display.update()
            clock.tick(15)

    def game_loop(self):

        global pause

        x = (config.screen_width * 0.45)
        y = (config.screen_height * 0.8)

        x_change = 0

        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                x_change = -5
                            if event.key == pygame.K_RIGHT:
                                x_change = 5
                            if event.key == pygame.K_p:
                                pause = True
                                paused()

                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                x_change = 0

            x += x_change

            config.screen.fill(config.light_black)
            pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])

            myfont = pygame.font.SysFont("comicsansms", 20)
            label = myfont.render("Levels completed: 2", 1, (config.black))
            config.screen.blit(label, (982, 10))
            label = myfont.render("Banana Points Earned: 10", 1, (config.black))
            config.screen.blit(label, (982, 110))
            label = myfont.render("Current Level: 3", 1, (config.black))
            config.screen.blit(label, (982, 210))
            pygame.draw.rect(config.screen, config.brown, [650, 370, 300, 30])
            pygame.draw.rect(config.screen, config.brown, [950, 0, 30, 720])
            pygame.draw.rect(config.screen, config.brown, [0, 0, 780, 30])
            pygame.draw.rect(config.screen, config.brown, [0, 0, 30, 520])
            pygame.draw.rect(config.screen, config.brown, [0, 690, 980, 30])
            config.screen.blit(playerImg, (0, 600))
            config.screen.blit(containerImg, (30, 30))
            config.screen.blit(logoImg, (1010, 350))

            config.screen.blit(carImg, (200, 400))
            config.screen.blit(excavatorImg, (500, 100))
            config.screen.blit(truckImg, (650, 500))

            self.button("Settings!", 980, 670, 100, 50, config.black, config.light_black, "settings")
            self.button("Back to Intro", 1140, 670, 140, 50, config.black, config.light_black, "leave")

            pygame.display.update()
            clock.tick(60)

    def runm(self):
        self.game_intro()
        self.settings_game()
        self.game_loop()
        pygame.quit()
        sys.exit()