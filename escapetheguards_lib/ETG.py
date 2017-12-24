
from menu_lib import slidemenu
from escapetheguards_lib import config
import pygame, sys, random

pygame.init()

class run():
    def runm(self):
        # Set top left text in screen
        pygame.display.set_caption('Escape The Guards')

        # Set up clock for fps count.
        clock = pygame.time.Clock()
        # Different global values defined.
        pause = False

        # Main run class, everything is inside this class.



        def text_objects(text, font):
            config.screen = font.render(text, True, config.white)
            return config.screen, config.screen.get_rect()

        def button(msg, x, y, w, h, ic, ac, action=None):

            click = pygame.mouse.get_pressed()

            mouse = pygame.mouse.get_pos()
            # print(click)

            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(config.screen, ac, (x, y, w, h))

                if click[0] == 1 and action != None:
                    if action == "level1":
                        level_1()
                    # elif action == "level2":
                    # level_2()

                    elif action == "unpaused":
                        unpause()

                    elif action == "leave":
                        game_intro()


                    elif action == "quit":
                        pygame.quit()
                        sys.exit()

                    else:
                        pygame.draw.rect(config.screen, ic, (x, y, w, h))

                        myfont = pygame.font.SysFont("comicsansms", 20)
                        textdisplay, textRect = text_objects(msg, myfont)
                        textRect.center = ((x + (w / 2)), (y + (h / 2)))
                        config.screen.blit(textdisplay, textRect)

        def unpause():
            global pause
            pause = False

        def back():
            mymenu = slidemenu.run()
            mymenu.runm()

        def paused():

            pause = True

            while pause:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                config.screen.fill(config.light_black)
                pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])

                myfont = pygame.font.SysFont("comicsansms", 20)
                label = myfont.render("Levels completed: 0", 2, (config.black))
                config.screen.blit(label, (982, 10))
                label = myfont.render("Banana Points Earned: 10", 1, (config.black))
                config.screen.blit(label, (982, 110))
                label = myfont.render("Current Level: 1", 1, (config.black))
                config.screen.blit(label, (982, 210))
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

                myfont = pygame.font.SysFont("comicsansms", 115)
                label = myfont.render(" GAME PAUSED!", 1, (config.white))
                config.screen.blit(label, (250, 340))

                button("Continue", 980, 670, 100, 50, config.black, config.light_black, "unpaused")
                button("Quit", 1180, 670, 100, 50, config.black, config.light_black, "leave")

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

                config.screen.blit(config.monkeyImg, (-50, 300))
                config.screen.blit(config.monkeyImg, (730, 300))

                button("Let's Play!", 590, 350, 100, 50, config.light_black, config.yellow, "level1")
                button("Quit!", 590, 550, 100, 50, config.yellow, config.light_black, "quit")

                pygame.display.update()
                clock.tick(15)

        def player():
            config.screen.blit(config.player_right, (300, 100))

            x = 300
            y = 100

            x_change = 0
            y_change = 0

            x += x_change
            y += y_change

        def things(thingx, thingy, thingw, thingh, color):
            pygame.draw.rect(config.screen, color, [thingx, thingy, thingw, thingh])

        def crash():
            largeText = pygame.font.SysFont("comicsansms", 115)
            TextSurf, TextRect = text_objects("You Crashed", largeText)
            TextRect.center = ((config.screen_width / 2), (config.screen_height / 2))
            config.screen.blit(TextSurf, TextRect)


        def level_1():

            global pause

            x = (config.screen_width * 0.45)
            y = (config.screen_height * 0.8)

            x_change = 0
            y_change = 0

            thing_startx = random.randrange(0, config.gs_width)
            thing_starty = -600
            thing_speed = 7

            thing_width = 100
            thing_height = 100

            gameExit = False

            while not gameExit:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                x_change = -5
                            elif event.key == pygame.K_RIGHT:
                                x_change = 5
                            elif event.key == pygame.K_UP:
                                y_change = 5
                            elif event.key == pygame.K_DOWN:
                                y_change = -5
                            elif event.key == pygame.K_ESCAPE:
                                pause = True
                                paused()

                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    x_change = 0
                                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                    y_change = 0

                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                x += x_change
                y += y_change
                config.screen.fill(config.light_black)
                pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])

                myfont = pygame.font.SysFont("comicsansms", 20)
                label = myfont.render("Levels completed: 0", 2, (config.black))
                config.screen.blit(label, (982, 10))
                label = myfont.render("Banana Points Earned: 10", 1, (config.black))
                config.screen.blit(label, (982, 110))
                label = myfont.render("Current Level: 1", 1, (config.black))
                config.screen.blit(label, (982, 210))
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

                things(thing_startx, thing_starty, thing_width, thing_height, config.black)
                thing_starty += thing_speed

                if thing_starty > config.gs_height:
                    thing_starty = 0 - thing_height
                    thing_startx = random.randrange(0, config.gs_width)

                if y < thing_starty + thing_height:
                    print('y crossover')

                    if x > thing_startx and x < thing_startx + thing_width or x + config.player_width > thing_startx and x + config.player_width < thing_startx + thing_width:
                        print('x crossover')
                        crash()

                player()

                button("Back to Intro", 1140, 670, 140, 50, config.black, config.light_black, "leave")
                button("Start Game", 1050, 670, 140, 50, config.black, config.light_black, "level1")

                pygame.display.update()
                config.clock.tick(60)

        # LEVEL 2 NOT WORKING YET!! #

        def level_2():

            global pause

            x = (config.screen_width * 0.45)
            y = (config.screen_height * 0.8)

            x_change = 0
            y_change = 0

            gameExit = False

            while not gameExit:

                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x_change = -5
                        elif event.key == pygame.K_RIGHT:
                            x_change = 5
                        elif event.key == pygame.K_UP:
                            y_change = 5
                        elif event.key == pygame.K_DOWN:
                            y_change = -5
                        elif event.key == pygame.K_ESCAPE:
                            pause = True
                            paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                sprite = pygame.image.load('player_right.png')
                spritex = 0
                spritey = 600

                config.screen.blit(sprite, (spritex, spritey))

                for event in pygame.event.get():

                    if event.type == quit:
                        pygame.quit()
                        sys.exit()

                x += x_change
                y += y_change

                config.screen.fill(config.light_black)
                pygame.draw.rect(config.screen, config.dark_green, [980, 0, 300, 720])

                myfont = pygame.font.SysFont("comicsansms", 20)
                label = myfont.render("Levels completed: 1", 2, (config.black))
                config.screen.blit(label, (982, 10))
                label = myfont.render("Banana Points Earned: 10", 1, (config.black))
                config.screen.blit(label, (982, 110))
                label = myfont.render("Current Level: 2", 1, (config.black))
                config.screen.blit(label, (982, 210))
                pygame.draw.rect(config.screen, config.brown, [650, 370, 300, 30])
                pygame.draw.rect(config.screen, config.brown, [950, 0, 30, 720])
                pygame.draw.rect(config.screen, config.brown, [950, 0, 30, 720])
                pygame.draw.rect(config.screen, config.brown, [0, 0, 780, 30])
                pygame.draw.rect(config.screen, config.brown, [0, 0, 30, 520])
                pygame.draw.rect(config.screen, config.brown, [0, 690, 980, 30])

                config.screen.blit(config.containerImg, (30, 30))
                config.screen.blit(config.logoImg, (1010, 350))

                config.screen.blit(config.carImg, (200, 400))
                config.screen.blit(config.excavatorImg, (400, 40))
                config.screen.blit(config.truckImg, (600, 470))
                config.screen.blit(config.carImg, (700, 340))
                config.screen.blit(config.bananaImg, (300, 350))
                config.screen.blit(config.bananaImg, (650, 450))
                config.screen.blit(config.bananaImg, (900, 0))
                config.screen.blit(config.pickupImg, (840, 160))
                config.screen.blit(config.pickupImg, (40, 330))

                config.screen.blit(config.guard_leftImg, (300, 495))
                config.screen.blit(config.guard_topImg, (650, 20))
                button("Pause!", 980, 670, 100, 50, config.black, config.light_black, "unpaused")
                button("Back to Intro", 1140, 670, 140, 50, config.black, config.light_black, "leave")

                pygame.display.update()
                config.clock.tick(60)

        game_intro()
        level_1()
        level_2()

        pygame.quit()
        sys.exit()