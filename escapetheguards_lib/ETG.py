
import pygame, sys, random, time
from menu_lib import slidemenu
import json
from escapetheguards_lib import config


pygame.init()

class run():
    def runm(self):
        pygame.display.set_caption('Escape The Guards')

        # Set up clock for fps count.
        clock = pygame.time.Clock()
        # Different global values defined.
        pause = False
        x_player = (200)
        y_player = (300)

        def back():
            mymenu = slidemenu.run()
            mymenu.runm()

        def things_dodged(count):
            font = pygame.font.SysFont(None, 30)
            text = font.render("Current Score: " + str(count), True, config.white)
            config.screen.blit(text, (982, 70))

        def banana_count(count):
            font = pygame.font.SysFont(None, 30)
            text = font.render("Banana's picked up: " + str(count), True, config.white)
            config.screen.blit(text, (982, 20))

        def text_objects(text, font):
            config.screen = font.render(text, False, config.white)
            return config.screen, config.screen.get_rect()

        def button(msg, x, y, w, h, iimg, aimg, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                config.screen.blit(aimg, (x, y, w, h))

                if click[0] == 1 and action != None:
                    action()
            else:
                config.screen.blit(iimg, (x, y, w, h))

        def spot():
            dodged = 0
            banana = 0
            things_dodged(dodged)
            banana_count(banana)
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

                player()
                things_dodged(dodged)
                banana_count(banana)

                config.screen.blit(s, (0, 0))

                myfont = pygame.font.SysFont("comicsansms", 60)
                label = myfont.render("YOU'VE BEEN SPOTTED!!", 2, (config.white))
                config.screen.blit(label, (260, 280))

                # button("Back to Intro", 590, 350, 100, 50, config.black, config.yellow, "leave")
                # button("Start Game", 590, 550, 100, 50, config.black, config.yellow, "level1")

                button("Lets Play", 450, 400, 20, 20, config.playgame, config.playgamehover, level_1)
                button("Back to menu", 600, 380, 100, 50, config.exitgame, config.exitgamehover, game_intro)

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
                # break

                pygame.display.update()
                clock.tick(15)

        def unpause():
            global pause
            pause = False

        def paused():

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

                monkey = ("apprentice_monkey.png")

                player()
                things_dodged(dodged)
                banana_count(banana)

                # button("Back to Intro", 1140, 670, 140, 50, config.black, config.yellow, "leave")
                # button("Start Game", 980, 670, 140, 50, config.black, config.yellow, "level1")

                config.screen.blit(s, (0, 0))

                myfont = pygame.font.SysFont("comicsansms", 60)
                label = myfont.render("Game is Paused", 2, (config.white))
                config.screen.blit(label, (430, 280))

                # button("Back to Intro", 590, 350, 100, 50, config.black, config.yellow, "leave")
                # button("Start Game", 590, 550, 100, 50, config.black, config.yellow, "level1")

                button("Back To Menu", 680, 380, 100, 50, config.exitgame, config.exitgamehover, game_intro)
                button("Continue", 450, 400, 20, 20, config.playgame, config.playgamehover, level_1)
                pygame.display.update()
                clock.tick(15)

        def game_intro():
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
                label = myfont.render("Escape Those Guards!", 1, (config.black))
                config.screen.blit(label, (230, 120))

                # config.screen.blit(config.monkeyImg, (-50, 300))
                # config.screen.blit(config.monkeyImg, (730, 300))

                pygame.draw.rect(config.screen, config.brown, [775, 280, 420, 220])

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

                label = myfont.render("Key P", 1, (config.black))
                config.screen.blit(label, (960, 430))

                label = myfont.render("Quit The Game:", 1, (config.black))
                config.screen.blit(label, (780, 460))

                label = myfont.render("Key Escape or top left X", 1, (config.black))
                config.screen.blit(label, (960, 460))

                config.screen.blit(config.monkeyImg, (0, 190))

                button("Lets Play", 580, 300, 20, 20, config.playgame, config.playgamehover, face_level1)
                button("Back to menu", 500, 450, 100, 50, config.exitgame, config.exitgamehover, back)

                pygame.display.update()
                clock.tick(15)

        def player():
            x_player = (200)
            y_player = (300)

            config.screen.blit(config.apprentice, (x_player, y_player))

        def things(thingx, thingy, thingw, thingh, color):
            pygame.draw.rect(config.screen, color, [thingx, thingy, thingw, thingh])

        def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = ((config.screen_width / 2), (config.screen_height / 2))
            config.screen.blit(TextSurf, TextRect)

            pygame.display.update()

            time.sleep(2)

        def face_level1():
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

                player()
                things_dodged(dodged)
                banana_count(banana)

                # button("Back to Intro", 1140, 670, 140, 50, config.black, config.yellow, "leave")
                # button("Start Game", 980, 670, 140, 50, config.black, config.yellow, "level1")

                config.screen.blit(s, (0, 0))

                myfont = pygame.font.SysFont("comicsansms", 50)
                label = myfont.render("NOW GO AND ESCAPE THOSE GUARDS!!", 2, (config.white))
                config.screen.blit(label, (130, 280))

                # button("Back to Intro", 590, 350, 100, 50, config.black, config.yellow, "leave")
                # button("Start Game", 590, 550, 100, 50, config.black, config.yellow, "level1")

                button("Lets Play", 450, 400, 20, 20, config.playgame, config.playgamehover, level_1)
                button("Back to menu", 600, 380, 100, 50, config.exitgame, config.exitgamehover, back)

                pygame.display.update()
                config.clock.tick(60)

        def level_1():

            global pause

            x_player = (200)
            y_player = (300)

            x = 500
            y = 500

            x_change = 0
            y_change = 0

            thing_startx = random.randrange(0, config.gs_width)
            thing_starty = -600
            thing_speed = 7

            thing_width = 100
            thing_height = 100

            dodged = 0
            banana = 0

            gameExit = False
            done = False
            global pause
            while done == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        quit()

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

                        if event.key == pygame.K_SPACE:
                            pause = False
                            unpause()

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a or event.key == pygame.K_d:
                            x_change = 0
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            y_change = 0

                x_player += x_change
                y_player += y_change

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
                config.screen.blit(config.bananaImg, (300, 350))
                config.screen.blit(config.bananaImg, (600, 620))
                config.screen.blit(config.bananaImg, (900, 300))

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
                        spot()

                player()
                things_dodged(dodged)
                banana_count(banana)

                # button("Back to Intro", 1140, 670, 140, 50, config.black, config.yellow, "leave")
                # button("Start Game", 980, 670, 140, 50, config.black, config.yellow, "level1")

                button("Back to menu", 993, 580, 100, 50, config.exitgame, config.exitgamehover, game_intro)

                pygame.display.update()
                config.clock.tick(60)