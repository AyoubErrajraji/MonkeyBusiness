
import pygame, sys, random, time
from menu_lib import slidemenu
import json
from escapetheguards_lib import config



pygame.init()

# Set top left text in screen
pygame.display.set_caption('Escape The Guards')

# Set up clock for fps count.
clock = pygame.time.Clock()
# Different global values defined.
pause = False

x2 = (200)
y2 = (300)

x2_change = 0
y2_change = 0


player_width = 70
player_height = 70

player_speed  = 7






class run():




        def back(self):
            mymenu = slidemenu.run()
            mymenu.runm()

        def things_dodged(self,count):
            font = pygame.font.SysFont(None, 30)
            text = font.render("Current Score: " + str(count), True, config.white)
            config.screen.blit(text, (982, 70))

        def banana_count(self,count):
            font = pygame.font.SysFont(None, 30)
            text = font.render("Banana's picked up: " + str(count), True, config.white)
            config.screen.blit(text, (982, 20))

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

        def blitMonkey(self):
            self.rect.x = 300
            self.rect.y = 100
            self.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

        def getMemory(self,key):
            with open("data/memory.json", "r+") as jsonFile:
                data = json.load(jsonFile)

                return data[key]

        def setMemory(self,key, value):
            with open("data/memory.json", "r+") as jsonFile:
                data = json.load(jsonFile)

                data[key] = value

                jsonFile.seek(0)  # rewind
                json.dump(data, jsonFile)
                jsonFile.truncate()

        #balance = getMemory("balance")
        #monkey = getMemory("bought")




        player1Group = pygame.sprite.Group()
        player2Group = pygame.sprite.Group()
        flagGroup = pygame.sprite.Group()
        targetGroup1 = pygame.sprite.Group()
        targetGroup2 = pygame.sprite.Group()



        def button(self,msg, x, y, w, h, iimg, aimg, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                config.screen.blit(aimg, (x, y, w, h))

                if click[0] == 1 and action != None:
                    action()
            else:
                config.screen.blit(iimg, (x, y, w, h))

        def spot(self):
            dodged = 0
            banana = 0
            self.things_dodged(dodged)
            self.banana_count(banana)
            spotted = True

            s = pygame.Surface((config.screen_width, config.screen_height), pygame.SRCALPHA)
            s.fill((0, 0, 0, 150))

            while spotted:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        quit()

                config.screen.fill(config.light_black)
                pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])

                pygame.draw.rect(config.screen, config.brown, [650, 370, 300, 30])  # Middle row!!
                pygame.draw.rect(config.screen, config.brown, [950, 0, 30, 720])  # Right row!!
                pygame.draw.rect(config.screen, config.brown, [290, 0, 660, 30])  # Top row!!
                pygame.draw.rect(config.screen, config.brown, [0, 0, 30, 720])  # Left row!!
                pygame.draw.rect(config.screen, config.brown, [0, 690, 750, 30])  # Bottom row!!

                pygame.draw.rect(config.screen, config.brown, [0, 250, 500, 30])  # Left middle row!!

                pygame.draw.rect(config.screen, config.brown, [0, 690, 750, 30])  # Bottom row!!

                config.screen.blit(config.cage2Img, (30, 0))
                config.screen.blit(config.cage3Img, (30, 490))
                config.screen.blit(config.cage3Img, (400, 490))
                config.screen.blit(config.cagedoorImg, (290, 70))
                config.screen.blit(config.tableImg, (600, 200))

                config.screen.blit(config.guard_leftImg, (550, 30))
                config.screen.blit(config.guard_topImg, (230, 320))

                config.screen.blit(config.logoImg, (1010, 350))
                config.screen.blit(config.bananaImg, (300, 350))
                config.screen.blit(config.bananaImg, (600, 620))
                config.screen.blit(config.bananaImg, (900, 300))

                self.things_dodged(dodged)
                self.banana_count(banana)

                config.screen.blit(s, (0, 0))

                myfont = pygame.font.SysFont("comicsansms", 60)
                label = myfont.render("YOU'VE BEEN SPOTTED!!", 2, (config.white))
                config.screen.blit(label, (260, 280))

                # button("Back to Intro", 590, 350, 100, 50, config.black, config.yellow, "leave")
                # button("Start Game", 590, 550, 100, 50, config.black, config.yellow, "level1")

                self.button("Lets Play", 500, 380, 20, 20, config.replaygame, config.replaygamehover, self.level_1)
                self.button("Back to menu", 660, 380, 100, 50, config.exitgame, config.exitgamehover, self.game_intro)

                # button("Play Again!", 590, 350, 100, 50, config.yellow, config.light_black, level_1())

                # button("Back to Intro!", 590, 550, 100, 50, config.yellow, config.light_black, game_intro())

                # counter, text = 10, '10'.rjust(3)
                # pygame.time.set_timer(pygame.USEREVENT, 1000)
                # font = pygame.font.SysFont('comicsansms', 50)

                # while True:
                # for e in pygame.event.get():
                # if e.type == pygame.USEREVENT:
                # counter -= 1
                # text = str(counter).rjust(3) if counter > 0 else face_level1()
                # if e.type == pygame.QUIT: break
                # else:

                # pygame.display.flip()
                # clock.tick(60)
                # continue
                

                pygame.display.update()
                clock.tick(15)

        def unpause(self):
            global pause
            pause = False

        def paused(self):

            pause = True
            dodged = 0
            banana = 0

            s = pygame.Surface((config.screen_width, config.screen_height), pygame.SRCALPHA)
            s.fill((0, 0, 0, 150))

            while pause:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                config.screen.fill(config.light_black)
                pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])

                pygame.draw.rect(config.screen, config.brown, [650, 370, 300, 30])  # Middle row!!
                pygame.draw.rect(config.screen, config.brown, [950, 0, 30, 720])  # Right row!!
                pygame.draw.rect(config.screen, config.brown, [290, 0, 660, 30])  # Top row!!
                pygame.draw.rect(config.screen, config.brown, [0, 0, 30, 720])  # Left row!!
                pygame.draw.rect(config.screen, config.brown, [0, 690, 750, 30])  # Bottom row!!

                pygame.draw.rect(config.screen, config.brown, [0, 250, 500, 30])  # Left middle row!!

                pygame.draw.rect(config.screen, config.brown, [0, 690, 750, 30])  # Bottom row!!

                config.screen.blit(config.cage2Img, (30, 0))
                config.screen.blit(config.cage3Img, (30, 490))
                config.screen.blit(config.cage3Img, (400, 490))
                config.screen.blit(config.cagedoorImg, (290, 70))
                config.screen.blit(config.tableImg, (600, 200))

                config.screen.blit(config.guard_leftImg, (550, 30))
                config.screen.blit(config.guard_topImg, (230, 320))

                config.screen.blit(config.logoImg, (1010, 350))
                config.screen.blit(config.bananaImg, (300, 350))
                config.screen.blit(config.bananaImg, (600, 620))
                config.screen.blit(config.bananaImg, (900, 300))

                self.things_dodged(dodged)
                self.banana_count(banana)

                # button("Back to Intro", 1140, 670, 140, 50, config.black, config.yellow, "leave")
                # button("Start Game", 980, 670, 140, 50, config.black, config.yellow, "level1")

                config.screen.blit(s, (0, 0))

                myfont = pygame.font.SysFont("comicsansms", 60)
                label = myfont.render("Game is Paused", 2, (config.white))
                config.screen.blit(label, (400, 280))

                # button("Back to Intro", 590, 350, 100, 50, config.black, config.yellow, "leave")
                # button("Start Game", 590, 550, 100, 50, config.black, config.yellow, "level1")

                self.button("Back To Menu", 660, 380, 100, 50, config.exitgame, config.exitgamehover, self.game_intro)
                self.button("Continue", 500, 380, 20, 20, config.playgame, config.playgamehover, self.level_1)
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
                        sys.exit()

                config.screen.blit(config.backgroundintro, (0, 0))

                myfont = pygame.font.SysFont("comicsansms", 80)
                label = myfont.render("Escape The Guards!", 1, (config.black))
                config.screen.blit(label, (265, 120))

                # config.screen.blit(config.monkeyImg, (-50, 300))
                # config.screen.blit(config.monkeyImg, (730, 300))

                pygame.draw.rect(config.screen, config.brown, [775, 280, 445, 430])

                myfont = pygame.font.SysFont("comicsansms", 20)
                label = myfont.render("Controls:", 1, (config.black))
                config.screen.blit(label, (780, 280))

                label = myfont.render("Move forwards:", 1, (config.black))
                config.screen.blit(label, (780, 340))

                label = myfont.render("Move backwards:", 1, (config.black))
                config.screen.blit(label, (780, 370))

                label = myfont.render("Move Sideways:", 1, (config.black))
                config.screen.blit(label, (780, 400))

                label = myfont.render("Pause the game:", 1, (config.black))
                config.screen.blit(label, (780, 430))

                label = myfont.render("Key Up", 1, (config.black))
                config.screen.blit(label, (960, 340))

                label = myfont.render("Key Down", 1, (config.black))
                config.screen.blit(label, (960, 370))

                label = myfont.render("Key Left and Key Right", 1, (config.black))
                config.screen.blit(label, (960, 400))

                label = myfont.render("Pause Button or Key Escape", 1, (config.black))
                config.screen.blit(label, (960, 430))

                label = myfont.render("Quit The Game:", 1, (config.black))
                config.screen.blit(label, (780, 460))

                label = myfont.render("Top Right X", 1, (config.black))
                config.screen.blit(label, (960, 460))

                label = myfont.render("The purpose of this game is to get to the ", 1, (config.black))
                config.screen.blit(label, (780, 520))

                label = myfont.render("other side of the zoo before the guards ", 1, (config.black))
                config.screen.blit(label, (780, 550))

                label = myfont.render("spot you, while you try to escape, ", 1, (config.black))
                config.screen.blit(label, (780, 580))

                label = myfont.render("get banana's for extra credits !", 1, (config.black))
                config.screen.blit(label, (780, 610))

                label = myfont.render("Good luck, see you on the other side ! ;)", 1, (config.black))
                config.screen.blit(label, (780, 670))

                config.screen.blit(config.monkeyImg, (0, 190))

                self.button("Lets Play", 580, 300, 20, 20, config.startgame, config.startgamehover, self.face_level1)
                self.button("Back to menu", 580, 450, 100, 50, config.exitgame, config.exitgamehover, self.back)

                pygame.display.update()
                clock.tick(15)

        def player(self,x, y):

            config.screen.blit(config.robo, (x, y))

        def character(self,x, y):
            config.screen.blit(config.mainImg, (x, y))

        def charwithFlag(self,x, y):
            config.screen.blit(config.charwFlagImg, (x, y))

        def char(self,x, y):
            config.screen.blit(config.apprentice, (x, y))

        x = (config.screen_width * 0.8)
        y = (config.screen_height * 0.8)
        x_change = 0
        y_change = 0
        speed = 1

        def flag(self,x, y):
            config.screen.blit(config.flagImg, (x, y))


        def setFlag(self,x, y):
            config.screen.blit(config.flagImg, (x, y))

        x_flag = 600
        y_flag = 300
        flag_width = 70
        flag_height = 70

        def noFlag(self,x, y):
            config.screen.blit(config.noFlagImg, (x, y))

        x_noflag = 600
        y_noflag = 300

        def flag2(self,x, y):
            config.screen.blit(config.flagImg, (x, y))

        x2_flag = 300
        y2_flag = 350

        def flag3(self,x, y):
            config.screen.blit(config.flagImg, (x, y))

        x3_flag = 600
        y3_flag = 620

        def flag4(self,x, y):
            config.screen.blit(config.flagImg, (x, y))


        x4_flag = 900
        y4_flag = 300

        def target(self,x, y):
            config.screen.blit(config.targetImg, (x, y))

        x_target = 1024
        y_target = 576


        def target2(self,x, y):
            config.screen.blit(config.targetImg, (x, y))



        x_target2 = config.screen_width * 0.2
        y_target2 = config.screen_height * 0.2

        points = 0
        points2 = 0

        # def getMemory(key):
        # with open("data/memory.json", "r+") as jsonFile:
        # data = json.load(jsonFile)

        # return data[key]

        # def setMemory(key, value):
        # with open("data/memory.json", "r+") as jsonFile:
        # data = json.load(jsonFile)

        # data[key] = value

        # jsonFile.seek(0)  # rewind
        # json.dump(data, jsonFile)
        # jsonFile.truncate()

        # balance = getMemory("balance")
        # monkey = getMemory("bought")

        def things(self,thingx, thingy, thingw, thingh, color):
            pygame.draw.rect(config.screen, color, [thingx, thingy, thingw, thingh])

        def message_display(self,text):
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = ((config.screen_width / 2), (config.screen_height / 2))
            config.screen.blit(TextSurf, TextRect)

            pygame.display.update()

            time.sleep(2)

        def face_level1(self):
            gameExit = False
            dodged = 0
            banana = 0

            s = pygame.Surface((config.screen_width, config.screen_height), pygame.SRCALPHA)
            s.fill((0, 0, 0, 150))

            while not gameExit:

                for event in pygame.event.get():
                    # print(event)
                    if event.type == pygame.QUIT:
                        gameExit = True
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                config.screen.fill(config.light_black)
                pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])

                pygame.draw.rect(config.screen, config.brown, [650, 370, 300, 30])  # Middle row!!
                pygame.draw.rect(config.screen, config.brown, [950, 0, 30, 720])  # Right row!!
                pygame.draw.rect(config.screen, config.brown, [290, 0, 660, 30])  # Top row!!
                pygame.draw.rect(config.screen, config.brown, [0, 0, 30, 720])  # Left row!!
                pygame.draw.rect(config.screen, config.brown, [0, 690, 750, 30])  # Bottom row!!

                pygame.draw.rect(config.screen, config.brown, [0, 250, 500, 30])  # Left middle row!!

                pygame.draw.rect(config.screen, config.brown, [0, 690, 750, 30])  # Bottom row!!

                config.screen.blit(config.cage2Img, (30, 0))
                config.screen.blit(config.cage3Img, (30, 490))
                config.screen.blit(config.cage3Img, (400, 490))
                config.screen.blit(config.cagedoorImg, (290, 70))
                config.screen.blit(config.tableImg, (600, 200))

                config.screen.blit(config.guard_leftImg, (550, 30))
                config.screen.blit(config.guard_topImg, (230, 320))

                config.screen.blit(config.logoImg, (1010, 350))
                config.screen.blit(config.bananaImg, (300, 350))
                config.screen.blit(config.bananaImg, (600, 620))
                config.screen.blit(config.bananaImg, (900, 300))

                self.things_dodged(dodged)
                self.banana_count(banana)

                # button("Back to Intro", 1140, 670, 140, 50, config.black, config.yellow, "leave")
                # button("Start Game", 980, 670, 140, 50, config.black, config.yellow, "level1")

                config.screen.blit(s, (0, 0))

                myfont = pygame.font.SysFont("comicsansms", 50)
                label = myfont.render("How to play??", 2, (config.white))
                config.screen.blit(label, (470, 150))

                # button("Back to Intro", 590, 350, 100, 50, config.black, config.yellow, "leave")
                # button("Start Game", 590, 550, 100, 50, config.black, config.yellow, "level1")

                myfont = pygame.font.SysFont("comicsansms", 20)
                label = myfont.render("Controls:", 1, (config.white))
                config.screen.blit(label, (780, 280))

                label = myfont.render("Move forwards:", 1, (config.white))
                config.screen.blit(label, (780, 340))

                label = myfont.render("Move backwards:", 1, (config.white))
                config.screen.blit(label, (780, 370))

                label = myfont.render("Move Sideways:", 1, (config.white))
                config.screen.blit(label, (780, 400))

                label = myfont.render("Pause the game:", 1, (config.white))
                config.screen.blit(label, (780, 430))

                label = myfont.render("Key Up", 1, (config.white))
                config.screen.blit(label, (960, 340))

                label = myfont.render("Key Down", 1, (config.white))
                config.screen.blit(label, (960, 370))

                label = myfont.render("Key Left and Key Right", 1, (config.white))
                config.screen.blit(label, (960, 400))

                label = myfont.render("Pause Button or Key Escape", 1, (config.white))
                config.screen.blit(label, (960, 430))

                label = myfont.render("Quit The Game:", 1, (config.white))
                config.screen.blit(label, (780, 460))

                label = myfont.render("Top Right X", 1, (config.white))
                config.screen.blit(label, (960, 460))

                label = myfont.render("The purpose of this game is to get to the ", 1, (config.white))
                config.screen.blit(label, (780, 520))

                label = myfont.render("other side of the zoo before the guards ", 1, (config.white))
                config.screen.blit(label, (780, 550))

                label = myfont.render("spot you, while you try to escape, ", 1, (config.white))
                config.screen.blit(label, (780, 580))

                label = myfont.render("get banana's for extra credits !", 1, (config.white))
                config.screen.blit(label, (780, 610))

                label = myfont.render("Good luck, see you on the other side ! ;)", 1, (config.white))
                config.screen.blit(label, (780, 670))

                self.button("Lets Play", 500, 580, 20, 20, config.playgame, config.playgamehover, self.level_1)
                self.button("Back to menu", 660, 580, 100, 50, config.exitgame, config.exitgamehover, self.back)

                pygame.display.update()
                config.clock.tick(60)

        def level_1(self):

            global pause

            x_flag = 600
            y_flag = 300

            x2_flag = 300
            y2_flag = 350

            x3_flag = 600
            y3_flag = 620

            x4_flag = 900
            y4_flag = 300

            x_target = 1024
            y_target = 576

            x_target2 = config.screen_width * 0.2
            y_target2 = config.screen_height * 0.2



            thing_startx = random.randrange(0, config.gs_width)
            thing_starty = -600
            thing_speed = 7

            thing_width = 100
            thing_height = 100

            dodged = 0
            banana = 0

            y = 0
            x = 0

            x2 = (200)
            y2 = (300)

            x_change = 0
            y_change = 0

            done = False
            global pause
            while done == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True

                    # Moving Player 1
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a and x > config.w - config.w:
                            x_change = -5
                        elif event.key == pygame.K_d:
                            x_change = 5
                        elif event.key == pygame.K_w:
                            y_change = -5
                        elif event.key == pygame.K_s:
                            y_change = 5
                        if event.key == pygame.K_ESCAPE:
                            pause = True
                            paused(self)

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a or event.key == pygame.K_d:
                            x_change = 0
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            y_change = 0

                x += x_change
                y += y_change

                config.screen.fill(config.light_black)
                pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])

                pygame.draw.rect(config.screen, config.brown, [650, 370, 300, 30])  # Middle row!!
                pygame.draw.rect(config.screen, config.brown, [950, 0, 30, 720])  # Right row!!
                pygame.draw.rect(config.screen, config.brown, [290, 0, 660, 30])  # Top row!!
                pygame.draw.rect(config.screen, config.brown, [0, 0, 30, 720])  # Left row!!
                pygame.draw.rect(config.screen, config.brown, [0, 690, 750, 30])  # Bottom row!!

                pygame.draw.rect(config.screen, config.brown, [0, 250, 500, 30])  # Left middle row!!

                pygame.draw.rect(config.screen, config.brown, [0, 690, 750, 30])  # Bottom row!!

                config.screen.blit(config.cage2Img, (30, 0))
                config.screen.blit(config.cage3Img, (30, 490))
                config.screen.blit(config.cage3Img, (400, 490))
                config.screen.blit(config.cagedoorImg, (290, 70))
                config.screen.blit(config.tableImg, (600, 200))

                config.screen.blit(config.guard_leftImg, (550, 30))
                config.screen.blit(config.guard_topImg, (230, 320))

                config.screen.blit(config.logoImg, (1010, 340))

                config.screen.blit(config.roboflat, (1130, 150))

                # things(thing_startx, thing_starty, thing_width, thing_height, config.black)
                thing_starty += thing_speed

                if thing_starty > config.gs_height:
                    thing_starty = 0 - thing_height
                    thing_startx = random.randrange(0, config.gs_width)
                    dodged += 1
                    banana += 2
                if y < thing_starty + thing_height:
                    print('y crossover')

                    if x > thing_startx and x < thing_startx + thing_width or x + config.player_width > thing_startx and x + config.player_width < thing_startx + thing_width:
                        print('x crossover')
                        print('player spotted!!')
                    #self.spot()

                self.things_dodged(dodged)
                self.banana_count(banana)

                # button("Back to Intro", 1140, 670, 140, 50, config.black, config.yellow, "leave")
                # button("Start Game", 980, 670, 140, 50, config.black, config.yellow, "level1")

                flag = self.setFlag
                player = self.char

                self.player(x, y)



                self.flag(x_flag, y_flag)
                self.flag2(x2_flag, y2_flag)
                self.flag3(x3_flag, y3_flag)
                self.flag4(x4_flag, y4_flag)

                # Flag Collision Player 1
                if flag == self.setFlag and player == self.char:
                    if x > 570 and x < 630 and y > 270 and y < 330:
                        player = self.charwithFlag

                    if player == self.charwithFlag:

                        self.target(x_target, y_target)
                        if x > 994 and x < 1054 and y > 546 and y < 606:
                            player = self.char

                player_speed = 0

                x += player_speed

                if x > config.gs_width - player_width or x < 0:
                    player_speed = 0
                if y > config.gs_height - player_height or y < 0:
                    player_speed = 0

                self.button("Back to menu", 993, 600, 100, 50, config.exitwoodgame, config.exitwoodgamehover, self.game_intro)

                self.button("Pause", 1000, 250, 100, 50, config.pausewoodgame, config.pausewoodgamehover, self.paused)

                pygame.display.update()
                # print('screen is updated!')
                config.clock.tick(60)

        def runm(self):
            self.game_intro()
            self.level_1()
            self.spot()
            self.back()
            self.face_level1()
            self.paused()
            pygame.quit()
            sys.quit()


