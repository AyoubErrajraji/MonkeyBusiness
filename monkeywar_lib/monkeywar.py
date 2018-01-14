#Project 2 v1.00
import pygame, sys, time
from pygame.locals import *
from menu_lib import slidemenu
import json

pygame.font.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
SAND = (255,255,100)
GREY = (155,155,155)
clock = pygame.time.Clock()
surface = pygame.display.set_mode((1280,720))


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

class run(object):
    font = pygame.font.SysFont("helvetica", 64)


    def runm(self):
        pygame.init()
        fase = 2
        win = projectWin(500, 500, 'MonkeyWar')
        Quit = False
        secondMonkey = Monkey(1080, "data/monkeywar/tankl.png", "ARROWS")
        firstMonkey = Monkey(100, "data/monkeywar/tankr.png","WASD")
        font = pygame.font.SysFont("helvetica", 64)

        background = pygame.image.load('data/monkeywar/bg.png').convert()
        pygame.mixer.music.load('data/monkeywar/music.mp3')
        pygame.mixer.music.play(-1)

        while not Quit:


            # FPS
            clock.tick(60)

            # get Mouse
            mouse = pygame.mouse.get_pos()

            #set background
            surface.blit(pygame.transform.scale(background, (1280, 720)), (0, 0))

            #grafity
            grafity = -0.35

            #bullet

            #WASD
            for bullet in firstMonkey.bullets:


                bullet.speedy = bullet.speedy + grafity
                bullet.y -= bullet.speedy

                bullet.x += bullet.speedx



                # Check if bullet is inside screen, else kill

                if bullet.y >= secondMonkey.y and bullet.y <= secondMonkey.y + 80 and bullet.x >= secondMonkey.x and bullet.x <= secondMonkey.x + 100:
                    firstMonkey.bullets.remove(bullet)
                    firstMonkey.amount -=1
                    secondMonkey.health -=1
                if bullet.y < 0:
                    firstMonkey.bullets.remove(bullet)
                    firstMonkey.amount -= 1
                if bullet.x > 1280:
                    bullet.speedx = bullet.speedx*-1
                if bullet.y > 560:
                    firstMonkey.bullets.remove(bullet)
                    firstMonkey.amount -= 1


                #if bullet.y <= 470 and bullet.y >= 469 and bullet.x >= 520 and bullet.x <= 647:
                 #   firstMonkey.bullets.remove(bullet)
                  #  print("hit")

                # Draw Bullet
                bullet.blitBullet(surface)

            #ARROWS
            for bullet in secondMonkey.bullets:

                bullet.speedy = bullet.speedy + grafity
                bullet.y -= bullet.speedy

                bullet.x -= bullet.speedx

                # Check if bullet is inside screen, else kill
                if bullet.y >= firstMonkey.y and bullet.y <= firstMonkey.y + 80 and bullet.x >= firstMonkey.x and bullet.x <= firstMonkey.x + 100:
                    secondMonkey.bullets.remove(bullet)
                    secondMonkey.amount -=1
                    firstMonkey.health -=1

                if bullet.y < 0:
                    secondMonkey.bullets.remove(bullet)
                    secondMonkey.amount -= 1
                if bullet.x < 0:
                    bullet.speedx = bullet.speedx * -1
                if bullet.y > 560:
                    secondMonkey.bullets.remove(bullet)
                    secondMonkey.amount -= 1




                # Draw Bullet
                bullet.blitBullet(surface)



            #call classes
            win.ground()
            if fase == 2:
                secondMonkey.intro()
                firstMonkey.intro()


            if secondMonkey.health<=0:
                fase = 6
                firstMonkey.p1()
                pygame.mixer.music.stop()

            if firstMonkey.health<=0:
                fase = 7
                secondMonkey.p2()
                pygame.mixer.music.stop()

            if fase == 1:
                secondMonkey.move()
                firstMonkey.move()
                secondMonkey.shoot()
                firstMonkey.shoot()
                secondMonkey.lives()
                firstMonkey.lives()


            if fase ==4:
                firstMonkey.pause()
                secondMonkey.pause()


             # pause
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            ## Pause ##
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                fase = 4

            ## Resume ##
            if mouse[0] > 500 and mouse[0] < 580 and mouse[1] > 300 and mouse[1] < 380 and click[0]==True and fase == 2:
               fase = 1

            ## Restart ##
            if mouse[0] > 600 and mouse[0] < 680 and mouse[1] > 300 and mouse[1] < 380 and click[0]==True and fase == 2:
                run.runm(self)

            ## Quit ##
            if mouse[0] > 700 and mouse[0] < 780 and mouse[1] > 300 and mouse[1] < 380 and click[0]== True and fase == 2:
                slidemenu.run().runm()

            ## Resume ##
            if mouse[0] > 500 and mouse[0] < 580 and mouse[1] > 300 and mouse[1] < 380 and click[0] == True and fase == 4:
                fase = 1

            ## Restart ##
            if mouse[0] > 600 and mouse[0] < 680 and mouse[1] > 300 and mouse[1] < 380 and click[0] == True and fase == 4:
                run.runm(self)

            ## Quit ##
            if mouse[0] > 700 and mouse[0] < 780 and mouse[1] > 300 and mouse[1] < 380 and click[0] == True and fase == 4:
                slidemenu.run().runm()

                ## Resume ##
            if mouse[0] > 500 and mouse[0] < 580 and mouse[1] > 300 and mouse[1] < 380 and click[0] == True and fase == 6:
                fase = 1

            ## Restart ##
            if mouse[0] > 600 and mouse[0] < 680 and mouse[1] > 300 and mouse[1] < 380 and click[0] == True and fase == 6:
                mymenu = slidemenu.run()
                mymenu.runm(50)

            ## Quit ##
            if mouse[0] > 700 and mouse[0] < 780 and mouse[1] > 300 and mouse[1] < 380 and click[0] == True and fase == 6:
                mymenu = slidemenu.run()
                mymenu.runm(50)

            ## Resume ##
            if mouse[0] > 500 and mouse[0] < 580 and mouse[1] > 300 and mouse[1] < 380 and click[0] == True and fase == 7:
                fase = 1

            ## Restart ##
            if mouse[0] > 600 and mouse[0] < 680 and mouse[1] > 300 and mouse[1] < 380 and click[0] == True and fase == 7:
                mymenu = slidemenu.run()
                mymenu.runm(50)

            ## Quit ##
            if mouse[0] > 700 and mouse[0] < 780 and mouse[1] > 300 and mouse[1] < 380 and click[0] == True and fase == 7:
                mymenu = slidemenu.run()
                mymenu.runm(50)


            # update display
            pygame.display.update()

            # Display the res

            # Quit handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    Quit = True

            # get FPS
            # print(clock.get_fps())


        pygame.quit()  # always exit cleanly
        sys.exit()



class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 10
        self.speedy = 14
        self.speedx = 15.2

        self.loadBullet("data/monkeywar/bullet.png")

    def loadBullet(self,name):
        self.bulletpicture = pygame.image.load(name)
        self.bulletpicture = pygame.transform.scale(self.bulletpicture, (15, 15))

    def blitBullet(self,surface):
        surface.blit(self.bulletpicture, (self.x, self.y))



class PlaceHolder:
    def __init__(self, win, left, top, width, height, color):
        self.win = win
        self.rect = pygame.Rect(left, top, width, height)
        self.color = color


class projectWin:
    def __init__(self, width, height, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)
        self.width = width
        self.height = height
        self.placeHolders = []
        self.placeHolders.append(PlaceHolder(surface, 1, 236, 10, 10, GREEN))

    def ground(self):
        pygame.draw.rect(surface, GREY, (0, 550, 1280, 170), 0)
        pygame.draw.rect(surface, GREY, (630, 520, 20, 50), 0)


class Monkey():
    def __init__(self, x, image, movement):
        self.x = x
        self.y = 478
        self.image = image
        self.movement = movement
        self.bullets = []
        self.bullet_timer = 0
        self.sprite = pygame.image.load(self.image).convert_alpha()
        self.amount = 0
        self.play = pygame.image.load("data/monkeywar/play.png")
        self.restart = pygame.image.load("data/monkeywar/replay_button.png")
        self.quit = pygame.image.load("data/monkeywar/exitknop.png")
        self.hplay = pygame.image.load("data/monkeywar/knop.png")
        self.hrestart = pygame.image.load("data/monkeywar/hoverreplay_button.png")
        self.hquit = pygame.image.load("data/monkeywar/hoverexitknop.png")
        self.pause_text = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 90).render('Paused', True,
                                                                                 pygame.color.Color('White'))
        self.intro_textp1 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 30).render('P2: move with "A" and "D", shoot with "W"', True,
                                                                                 pygame.color.Color('White'))
        self.intro_textp2 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 30).render('P1: move with "Left" and "Right" arrows, shoot with "Up" arrow', True,
                                                                                 pygame.color.Color('White'))
        self.intro_textp3 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 30).render('Win by shooting the your opponent until your opponent is out of lives', True,
                                                                                 pygame.color.Color('White'))
        self.win1 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 90).render('Player 2 Wins!', True,
                                                                                 pygame.color.Color('White'))
        self.win2 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 90).render('Player 1 Wins!', True,
                                                                                 pygame.color.Color('White'))
        self.health = 9
        self.fheart = pygame.image.load("data/monkeywar/Full_Heart.png")
        self.eheart = pygame.image.load("data/monkeywar/Empty_Heart.png")
        self.aheart = pygame.image.load("data/monkeywar/2_3_Heart.png")
        self.bheart = pygame.image.load("data/monkeywar/1_3_Heart.png")
        self.cannon = pygame.mixer.Sound("data/monkeywar/cannon.wav")
        self.win = pygame.mixer.Sound("data/monkeywar/win.wav")



    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        s = pygame.Surface((1280, 720), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))
        self.draw((self.x, 478))

        ## Dark background ##
        surface.blit(s, (0, 0))

        ## Buttons ##
        mouse = pygame.mouse.get_pos()

        if mouse[0] > 500 and mouse[0] < 580 and mouse[1] > 300 and mouse[1] < 380:
            surface.blit(pygame.transform.scale(self.hplay, (80, 80)), (500, 300))
        else:
            surface.blit(pygame.transform.scale(self.play, (80, 80)), (500, 300))


        if mouse[0] > 700 and mouse[0] < 780 and mouse[1] > 300 and mouse[1] < 380:
            surface.blit(pygame.transform.scale(self.hquit, (80, 80)), (700, 300))
        else:
            surface.blit(pygame.transform.scale(self.quit, (80, 80)), (700, 300))

        surface.blit(self.intro_textp1, (100, 200))
        surface.blit(self.intro_textp2, (100, 150))
        surface.blit(self.intro_textp3, (100, 100))

    def p1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        s = pygame.Surface((1280, 720), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))
        self.draw((self.x, 478))
        self.win.play()

        ## Dark background ##
        surface.blit(s, (0, 0))

        ## Buttons ##
        mouse = pygame.mouse.get_pos()

        if mouse[0] > 600 and mouse[0] < 680 and mouse[1] > 300 and mouse[1] < 380:
            surface.blit(pygame.transform.scale(self.hrestart, (80, 80)), (600, 300))
        else:
            surface.blit(pygame.transform.scale(self.restart, (80, 80)), (600, 300))

        if mouse[0] > 700 and mouse[0] < 780 and mouse[1] > 300 and mouse[1] < 380:
            surface.blit(pygame.transform.scale(self.hquit, (80, 80)), (700, 300))
        else:
            surface.blit(pygame.transform.scale(self.quit, (80, 80)), (700, 300))

        surface.blit(self.win1, (525, 200))

    def p2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        s = pygame.Surface((1280, 720), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))
        self.draw((self.x, 478))
        self.win.play()

        ## Dark background ##
        surface.blit(s, (0, 0))

        ## Buttons ##
        mouse = pygame.mouse.get_pos()

        if mouse[0] > 600 and mouse[0] < 680 and mouse[1] > 300 and mouse[1] < 380:
            surface.blit(pygame.transform.scale(self.hrestart, (80, 80)), (600, 300))
        else:
            surface.blit(pygame.transform.scale(self.restart, (80, 80)), (600, 300))

        if mouse[0] > 700 and mouse[0] < 780 and mouse[1] > 300 and mouse[1] < 380:
            surface.blit(pygame.transform.scale(self.hquit, (80, 80)), (700, 300))
        else:
            surface.blit(pygame.transform.scale(self.quit, (80, 80)), (700, 300))

        surface.blit(self.win2, (525, 200))

    def draw(self, position):
        surface.blit(pygame.transform.scale(self.sprite, (110, 80)), position)

    def lives(self):
        #Full HP
        if self.health == 9:
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 10, self.y - 20))
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 35, self.y - 20))
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 60, self.y - 20))

        if self.health == 8:
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 10, self.y - 20))
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 35, self.y - 20))
            surface.blit(pygame.transform.scale(self.aheart, (20, 20)), (self.x + 60, self.y - 20))

        if self.health == 7 :
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 10, self.y - 20))
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 35, self.y - 20))
            surface.blit(pygame.transform.scale(self.bheart, (20, 20)), (self.x + 60, self.y - 20))

        # 2 hearts
        if self.health == 6 :
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 10, self.y - 20))
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 35, self.y - 20))
            surface.blit(pygame.transform.scale(self.eheart, (20, 20)), (self.x + 60, self.y - 20))

        if self.health == 5:
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 10, self.y - 20))
            surface.blit(pygame.transform.scale(self.aheart, (20, 20)), (self.x + 35, self.y - 20))
            surface.blit(pygame.transform.scale(self.eheart, (20, 20)), (self.x + 60, self.y - 20))

        if self.health == 4:
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 10, self.y - 20))
            surface.blit(pygame.transform.scale(self.bheart, (20, 20)), (self.x + 35, self.y - 20))
            surface.blit(pygame.transform.scale(self.eheart, (20, 20)), (self.x + 60, self.y - 20))

        # 1 Heart
        if self.health == 3:
            surface.blit(pygame.transform.scale(self.fheart, (20, 20)), (self.x + 10, self.y - 20))
            surface.blit(pygame.transform.scale(self.eheart, (20, 20)), (self.x + 35, self.y - 20))
            surface.blit(pygame.transform.scale(self.eheart, (20, 20)), (self.x + 60, self.y - 20))

        if self.health == 2:
            surface.blit(pygame.transform.scale(self.aheart, (20, 20)), (self.x + 10, self.y - 20))
            surface.blit(pygame.transform.scale(self.eheart, (20, 20)), (self.x + 35, self.y - 20))
            surface.blit(pygame.transform.scale(self.eheart, (20, 20)), (self.x + 60, self.y - 20))

        if self.health == 1:
            surface.blit(pygame.transform.scale(self.bheart, (20, 20)), (self.x + 10, self.y - 20))
            surface.blit(pygame.transform.scale(self.eheart, (20, 20)), (self.x + 35, self.y - 20))
            surface.blit(pygame.transform.scale(self.eheart, (20, 20)), (self.x + 60, self.y - 20))

    def pause(self):
        keyinput = pygame.key.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        s = pygame.Surface((1280, 720), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))
        self.draw((self.x, 478))

        ## Dark background ##
        surface.blit(s, (0, 0))

        ## Buttons ##
        mouse = pygame.mouse.get_pos()

        if mouse[0] > 500 and mouse[0] < 580 and mouse[1] > 300 and mouse[1] < 380:
            surface.blit(pygame.transform.scale(self.hplay, (80, 80)), (500, 300))
        else:
            surface.blit(pygame.transform.scale(self.play, (80, 80)), (500, 300))

        if mouse[0] > 600 and mouse[0] < 680 and mouse[1] > 300 and mouse[1] < 380:
            surface.blit(pygame.transform.scale(self.hrestart, (80, 80)), (600, 300))
        else:
            surface.blit(pygame.transform.scale(self.restart, (80, 80)), (600, 300))

        if mouse[0] > 700 and mouse[0] < 780 and mouse[1] > 300 and mouse[1] < 380:
            surface.blit(pygame.transform.scale(self.hquit, (80, 80)), (700, 300))
        else:
            surface.blit(pygame.transform.scale(self.quit, (80, 80)), (700, 300))

        surface.blit(self.pause_text, (525, 200))


    def shoot(self):

        """ Handles Space """


        dt = 1 / 60
        key = pygame.key.get_pressed()
        self.bullet_timer -= dt  # Subtract the time since the last tick.
        if self.bullet_timer <= 0:
            self.bullet_timer = 0  # Bullet ready.:
            if self.movement == "ARROWS":
                if self.amount < 3:
                        if key[pygame.K_UP]:
                            self.cannon.play()
                            self.bullets.append(Bullet(self.x + 55, self.y))
                            self.bullet_timer = .3 # Reset the timer.
                            self.amount += 1


            if self.movement == "WASD":
                if self.amount < 3:
                    if key[pygame.K_w]:
                        self.cannon.play()
                        self.bullets.append(Bullet(self.x + 55, self.y))
                        self.bullet_timer = .3  # Reset the timer.
                        self.amount += 1


        #  print("Hit")

    def move(self):
        pygame.event.pump()

        # a key has been pressed
        keyinput = pygame.key.get_pressed()


        # optional exit on window corner x click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit



        # check arrow keys
        # move sprite in direction of arrow by 2 pixels

        if self.movement == "ARROWS":

            if self.x < 1280-100:
                if keyinput[pygame.K_RIGHT]:
                    self.x += 6
            if self.x > 650 - 8:
                if keyinput[pygame.K_LEFT]:
                    self.x -= 6

        if self.movement == "WASD":
            if self.x > 0-10:
                if keyinput[pygame.K_a]:
                    self.x -= 6
            if self.x < 630 - 8 - 100:
                if keyinput[pygame.K_d]:
                    self.x += 6


        self.draw((self.x,478))

        def exitGame():
            mymenu = slidemenu.run()
            mymenu.runm(50)

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

















