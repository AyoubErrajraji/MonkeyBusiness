
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







        def things_dodged(self,points):

            font = pygame.font.SysFont(None, 30)
            text = font.render("Current Score: " + str(self.points), False, config.white)







            config.screen.blit(text, (982, 70))

        def back(self):
            mymenu = slidemenu.run()
            mymenu.runm(self.points)

        def banana_count(self,bananapoints):
            font = pygame.font.SysFont(None, 30)
            text = font.render("Banana's picked up: " + str(self.bananapoints), True, config.white)
            config.screen.blit(text, (982, 20))

        def loadImages(self):
            self.monkey = self.getMemory("bought")
            if self.monkey == ["apprentice_monkey.png"]:
                self.monkey = pygame.image.load("data/apprentice_monkey_top.png").convert_alpha()

            elif self.monkey == ["acid_monkey.png"]:
                self.monkey = pygame.image.load("data/acid_monkey.png").convert_alpha()

            elif self.monkey == ["dragon_monkey.png"]:
                self.monkey = pygame.image.load("data/dragon_monkey_top.png").convert_alpha()

            elif self.monkey == ["engineer_monkey.png"]:
                self.monkey = pygame.image.load("data/engineer_monkey_top.png").convert_alpha()

            elif self.monkey == ["farmer_monkey.png"]:
                self.monkey = pygame.image.load("data/farmer_monkey.png").convert_alpha()

            elif self.monkey == ["ninja_monkey.png"]:
                self.monkey = pygame.image.load("data/ninja_monkey_top.png").convert_alpha()

            elif self.monkey == ["robo_monkey.png"]:
                self.monkey = pygame.image.load("data/robo_monkey_top.png").convert_alpha()

            elif self.monkey == ["super_monkey.png"]:
                self.monkey = pygame.image.load("data/super_monkey_top.png").convert_alpha()

            else:
                self.monkey = pygame.image.load("data/default_monkey_top.png").convert_alpha()
                self.flagMonkey = pygame.image.load("data/fightclub/images/charwflag.png").convert_alpha()
            self.monkey = pygame.transform.scale(self.monkey, (50, 50))

        def blitMonkey(self):
            rect_x = 300
            rect_y = 100
            config.screen.blit(self.image, (rect_x, rect_y))

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

        def win(self):
            dodged = 0
            banana = 0
            self.things_dodged(dodged)
            self.banana_count(banana)
            win = True

            s = pygame.Surface((config.screen_width, config.screen_height), pygame.SRCALPHA)
            s.fill((0, 0, 0, 150))

            while win:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        quit()

                    if 3 not in self.getMemory("unlocked"):
                        unlocked = self.getMemory("unlocked")
                        unlocked.append(3)
                        self.setMemory("unlocked", unlocked)





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
                label = myfont.render("You Win!!", 2, (config.white))
                config.screen.blit(label, (260, 280))

                myfont = pygame.font.SysFont("comicsansms", 20)
                label = myfont.render("Your score: 200", 1, (config.black))
                config.screen.blit(label, (300, 280))

                # button("Back to Intro", 590, 350, 100, 50, config.black, config.yellow, "leave")
                # button("Start Game", 590, 550, 100, 50, config.black, config.yellow, "level1")

                self.button("Lets Play", 500, 380, 20, 20, config.replaygame, config.replaygamehover, self.level_1)
                self.button("Back to menu", 660, 380, 100, 50, config.exitgame, config.exitgamehover, self.game_intro)








                pygame.display.update()
                clock.tick(15)

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
                label = myfont.render("YOU'VE BEEN KILLED!!", 2, (config.white))
                config.screen.blit(label, (260, 280))

                # button("Back to Intro", 590, 350, 100, 50, config.black, config.yellow, "leave")
                # button("Start Game", 590, 550, 100, 50, config.black, config.yellow, "level1")

                self.button("Lets Play", 500, 380, 20, 20, config.replaygame, config.replaygamehover, self.level_1)
                self.button("Back to menu", 660, 380, 100, 50, config.exitgame, config.exitgamehover, self.game_intro)


                

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

                label = myfont.render("Top Right X or Key Delete", 1, (config.black))
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

        player_y = 120
        player_x = 280
        player_speed = 0


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
        bananapoints = 0



        def things(self,thingx, thingy, thingw, thingh, color):
            pygame.draw.rect(config.screen, color, [thingx, thingy, thingw, thingh])



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

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.level_1()

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
                config.screen.blit(label, (470, 100))

                # button("Back to Intro", 590, 350, 100, 50, config.black, config.yellow, "leave")
                # button("Start Game", 590, 550, 100, 50, config.black, config.yellow, "level1")

                myfont = pygame.font.SysFont("comicsansms", 20)
                label = myfont.render("What's the goal of this game??", 1, (config.white))
                config.screen.blit(label, (100, 200))

                label = myfont.render(
                    "The goal of this game is to sneak past the guards and collect banana's to get more credits ", 1,
                    (config.white))
                config.screen.blit(label, (100, 250))

                label = myfont.render("so you can buy the powerfull robo monkey!! (or some of the other characters.)",
                                      1, (config.white))
                config.screen.blit(label, (100, 280))

                label = myfont.render("But how do I escape those Guards???", 1, (config.white))
                config.screen.blit(label, (100, 330))

                label = myfont.render("Well...", 1, (config.white))
                config.screen.blit(label, (100, 360))

                label = myfont.render(
                    "Use w/a/s/d to move your character around, once you are out of your cage you have to  ", 1,
                    (config.white))
                config.screen.blit(label, (100, 390))

                label = myfont.render(
                    "run past the guards in order to get to the parking lot, once you are running and avoiding ", 1,
                    (config.white))
                config.screen.blit(label, (100, 420))

                label = myfont.render(
                    "the guards try to pick up banana's to get extra points. Once you passed all the guards ", 1,
                    (config.white))
                config.screen.blit(label, (100, 450))

                label = myfont.render(
                    "and you make it to the parking lot, you will earn your well deserved points, but beware, ", 1,
                    (config.white))
                config.screen.blit(label, (100, 480))

                label = myfont.render("if you get caught halfway, you lose all the points you collected that round.", 1,
                                      (config.white))
                config.screen.blit(label, (100, 510))

                # label = myfont.render("Top Right X", 1, (config.white))
                # config.screen.blit(label, (960, 460))

                # label = myfont.render("The purpose of this game is to get to the ", 1, (config.white))
                # config.screen.blit(label, (780, 520))

                label = myfont.render("Good luck, see you on the parking lot! ;)", 1, (config.white))
                config.screen.blit(label, (100, 560))

                self.button("Lets Play", 500, 580, 20, 20, config.playgame, config.playgamehover, self.level_1)
                self.button("Back to menu", 660, 580, 100, 50, config.exitgame, config.exitgamehover, self.back)

                pygame.display.update()
                config.clock.tick(60)

        def guardblocks(self, blockx, blocky):
            config.screen.blit(config.bullet, (blockx, blocky))



        def level_1(self):

            self.points = 0
            self.bananapoints = 0
            block_startx = 30
            block_starty = random.randrange(0, 720)

            block_speed = 12
            block_width = 150
            block_height = 50

            global pause
            player_speed = 0

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

            player_y = 120
            player_x = 280
            player_speed = 0



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
                        if event.key == pygame.K_a :
                            x_change = -5

                        if event.key == pygame.K_d :
                            x_change = 5
                        if event.key == pygame.K_w:
                            y_change = -5
                        if event.key == pygame.K_s:
                            y_change = 5
                        if event.key == pygame.K_ESCAPE:
                            pause = True
                            self.paused()

                        if event.key == pygame.K_DELETE:
                            pygame.quit()
                            quit()

                        else:
                            print("else is true")
                            player_speed = -1



                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a or event.key == pygame.K_d:
                            x_change = 0
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            y_change = 0



                player_x += x_change
                player_y += y_change

                config.screen.fill(config.light_black)

                pygame.draw.rect(config.screen, config.brown, [0, 250, 500, 30])  # Left middle row!!

                config.screen.blit(config.cage2Img, (30, 0))
                config.screen.blit(config.cage3Img, (30, 490))
                config.screen.blit(config.cage3Img, (400, 490))
                config.screen.blit(config.cagedoorImg, (290, 70))
                config.screen.blit(config.tableImg, (600, 200))

                config.screen.blit(config.guard_rightImg, (100, 300))
                config.screen.blit(config.guard_bottomImg, (850, 100))
                config.screen.blit(config.guard_bottomImg, (850, 500))

                flag = self.setFlag
                player = self.char

                self.player(player_x, player_y)

                pygame.draw.rect(config.screen, config. light_black, [30, 0, 70 ,690])
                pygame.draw.rect(config.screen, config.white, [30,0, 70, 5])
                pygame.draw.rect(config.screen, config.white, [100, 0, 5, 690])
                pygame.draw.rect(config.screen, config.white, [30, 685, 70, 5])


                config.screen.blit(config.roboguard, (-30, 15))
                config.screen.blit(config.roboguard, (-30, 85))
                config.screen.blit(config.roboguard, (-30, 155))
                config.screen.blit(config.roboguard, (-30, 225))
                config.screen.blit(config.roboguard, (-30, 295))
                config.screen.blit(config.roboguard, (-30, 365))
                config.screen.blit(config.roboguard, (-30, 435))
                config.screen.blit(config.roboguard, (-30, 505))
                config.screen.blit(config.roboguard, (-30, 575))

                pygame.draw.rect(config.screen, config.brown, [650, 370, 300, 30])  # Middle row!!

                pygame.draw.rect(config.screen, config.brown, [290, 0, 660, 30])  # Top row!!

                pygame.draw.rect(config.screen, config.brown, [0, 690, 700, 30])  # Bottom row!!






                self.guardblocks(block_startx, block_starty)
                block_startx += block_speed

                if block_startx > config.gs_width:
                    block_startx = 0 - block_height
                    block_starty = random.randrange(0, config.screen_width)


                #if y < block_starty + block_width:

                    #print("there is x crossover!")


               # if x > block_startx and x < block_startx + block_width or x + player_width > block_startx and x + player_width < block_startx + block_width:
                    #print("x crossover")
                    #print("player spotted!")
                    #self.spot()

                #if y > block_starty and y < block_starty +block_height or y + player_height > block_starty and y + player_height < block_starty + block_height:
                    #print("y crossover")
                    #print("player spotted!")
                    #self.spot()

                if player_x < block_startx + block_width:
                    print("crossover")

                #if player_x <

                if y > block_starty and y < block_starty + block_height or y + player_height > block_starty and y + player_height < thing_starty +block_height:
                    self.spot()

                if player_x > 0 and player_x < 500 and player_y > 180 and player_y < 280:
                    x_change *= 0
                    y_change *= 0

                if player_x > 650 and player_x < 950 and player_y > 300 and player_y < 400:
                    x_change *= 0
                    y_change *= 0

                if player_x > 30 and player_x < 290 and player_y > 0 and player_y < 250:
                    x_change *= 0
                    y_change *= 0

                if player_x > 30 and player_x < 280 and player_y > 420 and player_y < 690:
                    x_change *= 0
                    y_change *= 0

                if player_x > 320 and player_x < 650 and player_y > 420 and player_y < 690:
                    x_change *= 0
                    y_change *= 0

                if player_x > 600 and player_x < 830 and player_y > 150 and player_y < 350:
                    x_change *= 0
                    y_change *= 0





                #Boven wall collision
                if player_x > 290 and player_x < 950 and player_y > 0 and player_y < 30:
                    x_change *= 0
                    y_change *= 0

                #Onder wall collision
                if player_x > 0 and player_x < 700 and player_y > 620 and player_y < 720:
                    x_change *= 0
                    y_change *= 0

                #Left wall collision
                if player_x >0 and player_x < 100 and player_y > 0 and player_y < 720:
                    x_change *= 0
                    y_change *= 0

                #right wall collision
                if player_x > 880 and player_x < 980 and player_y > 0 and player_y < 720:
                    x_change *= 0
                    y_change *= 0

                #guard left
                if player_x > 100 and player_x < 200 and player_y > 0 and player_y < 400:
                    x_change *= 0
                    y_change *= 0

                #guard right top
                if player_x > 770 and player_x < 950 and player_y > 60 and player_y < 200:
                    x_change *= 0
                    y_change *= 0

                #guard right bottom
                if player_x > 780 and player_x < 950 and player_y > 450 and player_y < 580:
                    x_change *= 0
                    y_change *= 0

                pygame.draw.rect(config.screen, config.brown, [950, 0, 30, 720])  # Right row!!

                pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])
                config.screen.blit(config.logoImg, (1010, 340))
                config.screen.blit(config.roboflat, (1130, 150))
                pygame.draw.rect(config.screen, config.brown, [0, 0, 30, 720])  # Left row!!



                if player_y > 720 and player_x > 680 and player_x < 950:
                    print("You Won!!!")
                    self.points += 50
                    self.bananapoints += 10
                    self.win()
                    self.points = 0
                    self.bananapoints = 0

                   #print("prachtig")



                #if player_x > 550 and player_x < 950 and player_y > 30 and player_y < 280:
                    #print("You have been spotted!!")
                    #player_speed += -1

                #if player_x > 230 and player_x < 510 and player_y > 320 and player_y < 670:
                    #print("You have been spotted!!")
                    #self.spot()

                if player_x > 600 and player_x < 630 and player_y > 300 and player_y < 330:
                    config.screen.blit(config.noFlagImg, (600,300))




                self.things_dodged(dodged)
                self.banana_count(banana)

                # button("Back to Intro", 1140, 670, 140, 50, config.black, config.yellow, "leave")
                # button("Start Game", 980, 670, 140, 50, config.black, config.yellow, "level1")





                #self.flag(x_flag, y_flag)
                #self.flag2(x2_flag, y2_flag)
                #self.flag3(x3_flag, y3_flag)
                #self.flag4(x4_flag, y4_flag)

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
            quit()


