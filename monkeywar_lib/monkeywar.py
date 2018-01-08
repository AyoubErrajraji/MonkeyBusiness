#Project 2 v1.00
import pygame, sys, time
from pygame.locals import *

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
        fase = 1
        win = projectWin(500, 500, 'MonkeyWar')
        Quit = False
        secondMonkey = Monkey(1080, "data/monkeywar/tankl.png", "ARROWS")
        firstMonkey = Monkey(100, "data/monkeywar/tankr.png","WASD")



        while not Quit:
            # get Mouse
            mouse = pygame.mouse.get_pos()

            #FPS
            clock.tick(60)

            #set Background
            surface.blit(pygame.transform.scale(pygame.image.load('data/monkeywar/bg.png').convert(), (1280, 720)), (0, 0))

            #bullet
            for bullet in firstMonkey.bullets:
                # Move bullet
                bullet.y -= 30

                # Check if bullet is inside screen, else kill
                if bullet.y < 0:
                    firstMonkey.bullets.remove(bullet)
                if bullet.y <= 470 and bullet.y >= 469 and bullet.x >= 520 and bullet.x <= 647:
                    firstMonkey.bullets.remove(bullet)
                    print("hit")

                # Draw Bullet
                bullet.blitBullet(surface)

            for bullet in secondMonkey.bullets:
                # Move bullet
                bullet.y -= 30

                # Check if bullet is inside screen, else kill
                if bullet.y < 0:
                    secondMonkey.bullets.remove(bullet)
                if bullet.y <= 470 and bullet.y >= 469 and bullet.x >= 520 and bullet.x <= 647:
                    secondMonkey.bullets.remove(bullet)
                    print("hit")

                # Draw Bullet
                bullet.blitBullet(surface)


            #call classes
            win.ground()

            if fase == 1:
                secondMonkey.move()
                firstMonkey.move()
                secondMonkey.shoot()
                firstMonkey.shoot()


            if fase ==4:
                firstMonkey.pause()
                secondMonkey.pause()


             # pause
            if pygame.key.get_pressed()[pygame.K_p]:
                fase = 4

            if pygame.key.get_pressed()[pygame.K_SPACE] and fase == 4:
                fase = 1

            # update display
            pygame.display.update()

            # Display the res
            time.sleep(0.02)

            # Quit handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    Quit = True


        pygame.quit()  # always exit cleanly
        sys.exit()



class Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 10

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


class Monkey():
    def __init__(self, x, image, movement):
        self.x = x
        self.y = 478
        self.image = image
        self.movement = movement
        self.bullets = []
        self.bullet_timer = 0



    def draw(self, position):
        sprite = pygame.image.load(self.image).convert_alpha()
        surface.blit(pygame.transform.scale(sprite, (110, 80)), position)

    def pause(self):
        keyinput = pygame.key.get_pressed()

        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        pygame.draw.rect(surface, BLACK, (550, 478, 200, 100), 0)
        self.draw((self.x, 478))



    def shoot(self):

        """ Handles Space """

        clock = pygame.time.Clock()
        dt = clock.tick(60) / 1000
        key = pygame.key.get_pressed()
        self.bullet_timer -= dt  # Subtract the time since the last tick.
        if self.bullet_timer <= 0:
            self.bullet_timer = 0  # Bullet ready.
            if self.movement == "ARROWS":
                if key[pygame.K_UP]:
                    print("shoot")
                    self.bullets.append(Bullet(self.x + 55, self.y))
                    self.bullet_timer = .1  # Reset the timer.
            if self.movement == "WASD":
                if key[pygame.K_w]:
                    print("shoot 2")
                    self.bullets.append(Bullet(self.x + 55, self.y))
                    self.bullet_timer = .1  # Reset the timer.

        #  print("Hit")

    def move(self):
        pygame.event.pump()

        # a key has been pressed
        keyinput = pygame.key.get_pressed()

        # press escape key to quit game
        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit
        # optional exit on window corner x click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit



        # check arrow keys
        # move sprite in direction of arrow by 2 pixels

        if self.movement == "ARROWS":

            if keyinput[pygame.K_LEFT]:
                self.x -= 10
            elif keyinput[pygame.K_RIGHT]:
                self.x += 10

        if self.movement == "WASD":
            if keyinput[pygame.K_a]:
                self.x -= 10
            elif keyinput[pygame.K_d]:
                self.x += 10

        self.crossx = self.x + 55

        self.draw((self.x,478))















