import pygame
import sys
import json
import os
import math
import itertools
import random
import time
from menu_lib import slidemenu
from menu_lib import *
from finalfight_lib import game as finalfight
from pygame.locals import *



pygame.init()
pygame.font.init()


class Game:
    def __init__(self,screen):
        self.fps = 30
        self.frame = pygame.time.Clock()
        self.screen = screen
        self.bullet_timer = 0

    def updateFrame(self):
        self.frame.tick(self.fps)
        pygame.display.flip()

class Background(Game):
    def __init__(self,screen):
        Game.__init__(self,screen)
        self.rescale = 2
        self.forrestImage = None

    def loadForrest(self,name):
        self.forrestImage = pygame.image.load(name).convert()
        self.forrestImage = pygame.transform.scale(self.forrestImage, (1280, 720))

    def blitForrest(self):
        self.screen.blit(self.forrestImage, (0, 0))
def getMemory(key):
    with open("data/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        return data[key]

class Player(Game):  # represents the bird, not the game
    def __init__(self,screen):
        Game.__init__(self, screen)
        """ The constructor of the class """
        self.width = 100
        self.height = 100
        self.image = pygame.image.load("data/" + getMemory("monkey").replace(".png", ".png"))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # the bird's position
        self.x = 300
        self.y = 550
        self.bullets = []
        monkey = getMemory("monkey")
        if monkey == "default_monkey.png":
            self.health = 50
        elif monkey == "ninja_monkey.png":
            self.health = 55
        elif monkey == "engineer_monkey.png":
            self.health = 60
        elif monkey == "apprentice_monkey.png":
            self.health = 65
        elif monkey == "dragon_monkey.png":
            self.health = 70
        elif monkey == "super_monkey.png":
            self.health = 80
        elif monkey == "robo_monkey.png":
            self.health = 90
        else:
            self.health = 50

    def movePlayer(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        #dist = 3  # distance moved in 1 frame, try changing it to 5
        monkey = getMemory("monkey")
        if monkey == "default_monkey.png":
            dist = 1
        elif monkey == "ninja_monkey.png":
            dist = 2
        elif monkey == "engineer_monkey.png":
            dist = 3
        elif monkey == "apprentice_monkey.png":
            dist = 4
        elif monkey == "dragon_monkey.png":
            dist = 5
        elif monkey == "super_monkey.png":
            dist = 6
        elif monkey == "robo_monkey.png":
            dist = 7
        else:
            dist = 7
        if key[pygame.K_RIGHT] and self.x < 1166:  # right key
            self.x += dist  # move right
        elif key[pygame.K_LEFT] and self.x > -43:  # left key
            self.x -= dist  # move left

    def shoot(self):
        """ Handles Space """
        clock = pygame.time.Clock()
        dt = clock.tick(60) / 1000
        key = pygame.key.get_pressed()
        self.bullet_timer -= dt  # Subtract the time since the last tick.
        if self.bullet_timer <= 0:
            self.bullet_timer = 0  # Bullet ready.
            if key[pygame.K_SPACE]:
                self.bullets.append(Bullet(self.x + 64, self.y))
                self.bullet_timer = .2  # Reset the timer.
          #  print("Hit")


    def draw(self, screen):
        """ Draw on surface """
         #blit yourself at your current position
        screen.blit(self.image, (self.x, self.y))

class Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        monkey = getMemory("monkey")
        if monkey == "default_monkey.png":
            self.damage = 10
        elif monkey == "ninja_monkey.png":
            self.damage = 15
        elif monkey == "engineer_monkey.png":
            self.damage = 20
        elif monkey == "apprentice_monkey.png":
            self.damage = 25
        elif monkey == "dragon_monkey.png":
            self.damage = 30
        elif monkey == "super_monkey.png":
            self.damage = 40
        elif monkey == "robo_monkey.png":
            self.damage = 50
        else:
            self.damage = 50

        self.loadBullet("data/finalfight/bullet.png")


    def loadBullet(self,name):
        self.bulletpicture = pygame.image.load(name)
        self.bulletpicture = pygame.transform.scale(self.bulletpicture, (10, 20))

    def blitBullet(self,screen):
        screen.blit(self.bulletpicture, (self.x, self.y))

class Boss(Game):
    def __init__(self,screen):
        Game.__init__(self, screen)
        self.bossX = 520
        self.bossY = 300
        self.boss = None
        self.health = 100
        self.damage = 10

    def loadBoss(self,name):
        self.boss = pygame.image.load(name).convert_alpha()
        bossWidth = self.boss.get_rect().width
        bossHeight = self.boss.get_rect().height
        self.boss = pygame.transform.scale(self.boss, (bossWidth, bossHeight))

    def blitBoss(self,screen):
        #screen.blit(self.health, (700,300))
        screen.blit(self.boss, (520, 300))

class Wolk(Game):
    def __init__(self, screen):
        Game.__init__(self, screen)
        self.wolkX = 430
        self.wolkY = 130
        self.wolk = None

    def loadWolk(self, name):
        self.wolk = pygame.image.load(name).convert_alpha()

        self.wolk = pygame.transform.scale(self.wolk, (350,200))

    def blitwolk(self,screen):
        screen.blit(self.wolk, (590, 130))

class Score(Game):
    def __init__(self,screen):
        Game.__init__(self,screen)
        self.score = 0

    def updateScore(self,new):
        self.score = self.score + new


    def getMemory(self, key):
        with open("data/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            return data[key]

    def setMemory(self, key, value):

        with open("data/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            data[key] = value

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def blitScore(self,screen):
        font = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 30)
        score = "score: %d" % self.score
        self.temp_surface = font.render(score, 1, (255, 255, 255))
        screen.blit(self.temp_surface, (1135, 10))

class Pause(Game):
    def __init__(self, screen):
        Game.__init__(self, screen)
        RUNNING, PAUSE = 0, 1

        self.state = RUNNING

    def magnitude(v):
        return math.sqrt(sum(v[i] * v[i] for i in range(len(v))))

    def sub(u, v):
        return [u[i] - v[i] for i in range(len(u))]

    def normalize(v):
        return [v[i] / magnitude(v) for i in range(len(v))]

    def loadPause(self):
        self.pause_text = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 60).render('Paused', True,
                                                                                 pygame.color.Color('White'))
        s = pygame.Surface((1280, 720), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))

    def loadPauseButton(self,name):
        self.pauseButton = pygame.image.load(name).convert_alpha()

        self.pauseButton = pygame.transform.scale(self.pauseButton, (50, 50))

    def blitPauseButton(self, screen):
        screen.blit(self.pauseButton, (1190, 60))

    def loadHoverPauseButton(self,name):
        self.hoverPauseButton = pygame.image.load(name).convert_alpha()

        self.hoverPauseButton = pygame.transform.scale(self.hoverPauseButton, (50, 50))

    def blitHoverPauseButton(self, screen):
        screen.blit(self.hoverPauseButton, (1190, 60))

    def loadPlayButton(self,name):
        self.playButton = pygame.image.load(name).convert_alpha()

        self.playButton = pygame.transform.scale(self.playButton, (50, 50))

    def blitPlayButton(self, screen):
        screen.blit(self.playButton, (600, 320))

    def loadPlayButton2(self,name):
        self.playButton = pygame.image.load(name).convert_alpha()

        self.playButton = pygame.transform.scale(self.playButton, (50, 50))

    def blitPlayButton2(self, screen):
        screen.blit(self.playButton, (1200, 10))

    def loadHoverPlayButton(self,name):
        self.hoverPlayButton = pygame.image.load(name).convert_alpha()

        self.hoverPlayButton = pygame.transform.scale(self.hoverPlayButton, (50, 50))

    def blitHoverPlayButton(self, screen):
        screen.blit(self.hoverPlayButton, (600, 320))

    def loadHoverPlayButton2(self,name):
        self.hoverPlayButton = pygame.image.load(name).convert_alpha()

        self.hoverPlayButton = pygame.transform.scale(self.hoverPlayButton, (50, 50))

    def blitHoverPlayButton2(self, screen):
        screen.blit(self.hoverPlayButton, (1200, 10))

    def loadExitButton(self, name):
        self.exitButton = pygame.image.load(name).convert_alpha()

        self.exitButton = pygame.transform.scale(self.exitButton, (50, 50))

    def blitExitButton(self, screen):
        screen.blit(self.exitButton, (650, 320))

    def loadHoverExitButton(self, name):
        self.hoverExitButton = pygame.image.load(name).convert_alpha()

        self.hoverExitButton = pygame.transform.scale(self.hoverExitButton, (50, 50))

    def blitHoverExitButton(self, screen):
        screen.blit(self.hoverExitButton, (650, 320))

    def loadReplayButton(self, name):
        self.replayButton = pygame.image.load(name).convert_alpha()

        self.replayButton = pygame.transform.scale(self.replayButton, (50, 50))

    def blitReplayButton(self, screen):
        screen.blit(self.replayButton, (700, 320))

    def loadHoverReplayButton(self, name):
        self.hoverReplayButton = pygame.image.load(name).convert_alpha()

        self.hoverReplayButton = pygame.transform.scale(self.hoverReplayButton, (50, 50))

    def blitHoverReplayButton(self, screen):
        screen.blit(self.hoverReplayButton, (700, 320))

    def loadNextButton(self,name):
        self.nextButton = pygame.image.load(name).convert_alpha()

        self.nextButton = pygame.transform.scale(self.nextButton, (50, 50))

    def blitNextButton(self, screen):
        screen.blit(self.nextButton, (1200, 80))

    def loadHoverNextButton(self,name):
        self.hoverNextButton = pygame.image.load(name).convert_alpha()

        self.hoverNextButton = pygame.transform.scale(self.hoverNextButton, (50, 50))

    def blitHoverNextButton(self, screen):
        screen.blit(self.hoverNextButton, (1200, 80))

    def task(self):
        slidemenu.run().runm(1000)

    def task2(self):
        slidemenu.run().runm()
    def task3(self):
        slidemenu.run().runm(100)
    def task4(self):
        slidemenu.run().runm(300)

    def restartGame(self):
        mymenu = finalfight.run()
        mymenu.runm()

class run():
    def runm(self):
        width = 1280
        height = 720
        screenDim = (width, height)

        screen = pygame.display.set_mode(screenDim)
        black = (0,0,0)

        def things(thingx, thingy, thingw, thingh, color):
            pygame.draw.rect(screen,color,[thingx, thingy, thingw, thingh])



        gameDisplay = pygame.display.set_mode((width, height))

        pygame.display.set_caption("Final Fight")

        pygame.init()
        player = Player(screen)
        newBoss = Boss(screen)
        newWolk = Wolk(screen)
        background = Background(screen)
        newScore = Score(screen)
        newPause = Pause(screen)
        #newBullet = Bullet()
        game = Game(screen)

        background.loadForrest("data/finalfight/openplek.png")

        newPause.loadExitButton("data/finalfight/exitknop.png")

        newPause.loadHoverExitButton("data/finalfight/hoverexitknop.png")

        newPause.loadPauseButton("data/finalfight/pause_button.png")

        newPause.loadHoverPauseButton("data/finalfight/hoverpause_button.png")

        newPause.loadPlayButton("data/finalfight/play.png")

        newPause.loadHoverPlayButton("data/finalfight/knop.png")

        newPause.loadPlayButton2("data/finalfight/play.png")

        newPause.loadHoverPlayButton2("data/finalfight/knop.png")

        newPause.loadReplayButton("data/finalfight/replay_button.png")

        newPause.loadHoverReplayButton("data/finalfight/hoverreplay_button.png")

        newPause.loadNextButton("data/finalfight/next_button.png")

        newPause.loadHoverNextButton("data/finalfight/hoverNext_button.png")

        newBoss.loadBoss("data/finalfight/boss2.png")

        newWolk.loadWolk("data/finalfight/spreekwolk.png")

        #newScore.loadScore(screen)

        newPause.loadPause()

        background.blitForrest()

        newWolk.blitwolk(screen)

        newBoss.blitBoss(screen)

        newPause.blitHoverPauseButton(screen)

        newPause.blitPauseButton(screen)

        newPause.blitPlayButton(screen)

        newPause.blitHoverPlayButton(screen)

        newPause.blitPlayButton2(screen)

        newPause.blitHoverPlayButton2(screen)

        newPause.blitNextButton(screen)

        newPause.blitHoverNextButton(screen)

        newPause.blitExitButton(screen)

        newPause.blitHoverExitButton(screen)

        newPause.blitReplayButton(screen)

        newPause.blitHoverReplayButton(screen)

        #newScore.blitScore(screen)

        #Score.setMemory("score", 0)

        #newScore.score("score", 0)

        INTRO, RUNNING, RUNNING2, RUNNING3, PAUSE, PAUSE2, PAUSE3, YOUWON, GAMEOVER, GAMEOVER2, GAMEOVER3 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        old_state = PAUSE
        state = INTRO


        pause_text = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 60).render('Paused', True, pygame.color.Color('White'))
        won_text = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 60).render('You Won!!!', True, pygame.color.Color('White'))
        lose_text = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 60).render('Game Over!', True, pygame.color.Color('White'))
        lose_text2 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 60).render('Completed level 1!', True, pygame.color.Color('White'))
        lose_text3 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 60).render('Completed level 2!', True, pygame.color.Color('White'))
        intro_text = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 60).render('The FinalFight!!!', True, pygame.color.Color('White'))
        intro_text2 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 40).render('Welcome to the FIGHT!', True, pygame.color.Color('White'))
        intro_text3 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 40).render('EVERYTHING depends on THIS moment!', True, pygame.color.Color('White'))
        intro_text4 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 50).render('The Goal?', True, pygame.color.Color('White'))
        intro_text5 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 40).render('It is simple, destroy the boss before he destroys you! ', True, pygame.color.Color('White'))
        intro_text6 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 40).render('But watch out...', True, pygame.color.Color('White'))
        intro_text7 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 40).render('He has allies trowing stones from the trees!!!', True, pygame.color.Color('White'))
        intro_text8 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 50).render('CONTROLS', True, pygame.color.Color('White'))
        intro_text9 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 40).render('Use the arrows(left/right) avoid the stones', True, pygame.color.Color('White'))
        intro_text10 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 40).render('Use the spacebar to attack the boss', True, pygame.color.Color('White'))
        intro_text11 = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 40).render('May the bananas be with you!!!', True, pygame.color.Color('White'))


        s = pygame.Surface((width, height), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))

        clock = pygame.time.Clock()

        counter, text = 3, '3'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 60)

        x_change = 10
        thing_startx = random.randrange(400,800)
        thing_starty = 0
        thing_speed = 5
        thing_speed1 = 25
        thing_speed2 = 25
        thing_width = 25
        thing_height = 25

        while True:

            for e in pygame.event.get():

                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'GO!'
                click = pygame.mouse.get_pressed()
                mouse = pygame.mouse.get_pos()
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if newScore.score >= 100 and state != PAUSE:
                    old_state = state
                    state = RUNNING2
                if newScore.score >= 400 and state != PAUSE:
                    old_state = state
                    state = RUNNING3
                if newScore.score >= 1000:
                    old_state = state
                    state = YOUWON
                    if 5 not in newScore.getMemory("unlocked") and 6 not in newScore.getMemory("unlocked"):
                        unlocked = newScore.getMemory("unlocked")
                        unlocked.append(5)
                        unlocked.append(6)
                        newScore.setMemory("unlocked", unlocked)
                if player.health <= 0 and newScore.score < 100:
                    state = GAMEOVER
                if player.health <= 0 and newScore.score > 100 and newScore.score < 400:
                    state = GAMEOVER2
                if player.health <= 0 and newScore.score > 400 and newScore.score < 1000:
                    state = GAMEOVER3


            else:
                screen.fill((0, 0, 0))

                if state == INTRO:
                    background.blitForrest()
                    screen.blit(s, (0, 0))
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 1200 + 50 > mouse[0] > 1200 and 10 + 50 > mouse[1] > 10:
                        state = RUNNING
                    if 1200 + 50 > mouse[0] > 1200 and 10 + 50 > mouse[1] > 10:
                        newPause.blitHoverPlayButton2(screen)
                    else:
                        newPause.blitPlayButton2(screen)
                    screen.blit(intro_text, (500, 20))
                    screen.blit(intro_text2, (510, 80))
                    screen.blit(intro_text3, (400, 120))
                    screen.blit(intro_text4, (10, 160))
                    screen.blit(intro_text5, (10, 220))
                    screen.blit(intro_text6, (10, 260))
                    screen.blit(intro_text7, (10, 300))
                    screen.blit(intro_text8, (10, 350))
                    screen.blit(intro_text9, (10, 400))
                    screen.blit(intro_text10, (10, 440))
                    screen.blit(intro_text11, (10, 480))

                    #newScore.blitScore(screen)
                elif state == RUNNING:
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 1190 + 50 > mouse[0] > 1190 and 60 + 50 > mouse[1] > 60:
                        old_state = state
                        state = PAUSE

                    player.movePlayer()
                    player.shoot()

                    background.blitForrest()
                    things(thing_startx, thing_starty, thing_width, thing_height, (0, 0, 0))
                    thing_starty += thing_speed

                    if thing_starty > height:
                        thing_starty = 0 - thing_height
                        thing_startx = random.randrange(300,700)
                    if player.y < thing_starty + thing_height:
                        #print('y crossover')

                        if player.x < thing_startx and player.x + player.width > thing_startx and player.y == thing_starty:
                            print('x crossover')
                            player.health -= 10

                    for bullet in player.bullets:
                        # Move bullet
                        bullet.y -= 10

                        # Check if bullet is inside screen, else kill
                        if bullet.y < 0:
                            player.bullets.remove(bullet)
                        if bullet.y <= 470 and bullet.y >= 469 and bullet.x>= 520 and bullet.x <= 647:
                            player.bullets.remove(bullet)

                        if bullet.y <= 520 and bullet.y >= 519 and bullet.x>= 520 and bullet.x <= 647:
                            #bullet.damage = 10
                            newBoss.health -= bullet.damage
                            newScore.score += bullet.damage
                            #bullet.update()


                            print("hit")

                        # Draw Bullet
                        bullet.blitBullet(screen)

                    if 1190 + 50 > mouse[0] > 1190 and 60 + 50 > mouse[1] > 60:
                        newPause.blitHoverPauseButton(screen)
                    else:
                        newPause.blitPauseButton(screen)

                    #newWolk.blitwolk(screen)
                    newBoss.blitBoss(screen)
                    player.draw(screen)
                    newScore.blitScore(screen)
                    screen.blit(font.render(text, True, (0, 0, 0)), (620, 100))


                if state == RUNNING2:
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 1190 + 50 > mouse[0] > 1190 and 60 + 50 > mouse[1] > 60:
                        old_state = state
                        state = PAUSE
                    player.movePlayer()
                    player.shoot()

                    background.blitForrest()
                    things(thing_startx, thing_starty, thing_width, thing_height, (0, 0, 0))
                    thing_starty += thing_speed1

                    if thing_starty > height:
                        thing_starty = 0 - thing_height
                        thing_startx = random.randrange(300,700)
                    if player.y < thing_starty + thing_height:
                        #print('y crossover')

                        if player.x < thing_startx and player.x + player.width > thing_startx and player.y == thing_starty:

                                    print('x crossover')
                                    player.health -= 10

                    for bullet in player.bullets:
                        # Move bullet
                        bullet.y -= 10

                        # Check if bullet is inside screen, else kill
                        if bullet.y < 0:
                            player.bullets.remove(bullet)
                        if bullet.y <= 470 and bullet.y >= 469 and bullet.x>= 520 and bullet.x <= 647:
                            player.bullets.remove(bullet)

                        if bullet.y <= 520 and bullet.y >= 519 and bullet.x>= 520 and bullet.x <= 647:
                            #bullet.damage = 10
                            newBoss.health -= bullet.damage
                            newScore.score += bullet.damage
                            #bullet.update()


                            print("hit")

                        # Draw Bullet
                        bullet.blitBullet(screen)

                    if 1190 + 50 > mouse[0] > 1190 and 60 + 50 > mouse[1] > 60:
                        newPause.blitHoverPauseButton(screen)
                    else:
                        newPause.blitPauseButton(screen)

                    #newWolk.blitwolk(screen)
                    newBoss.blitBoss(screen)
                    player.draw(screen)
                    newScore.blitScore(screen)
                    screen.blit(font.render(text, True, (0, 0, 0)), (620, 100))

                if state == RUNNING3:
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 1190 + 50 > mouse[0] > 1190 and 60 + 50 > mouse[1] > 60:
                        old_state = state
                        state = PAUSE
                    player.movePlayer()
                    player.shoot()

                    background.blitForrest()
                    things(thing_startx, thing_starty, thing_width, thing_height, (0, 0, 0))
                    thing_starty += thing_speed2

                    if thing_starty > height:
                        thing_starty = 0 - thing_height
                        thing_startx = random.randrange(300,700)
                    if player.y < thing_starty + thing_height:
                        #print('y crossover')

                        if player.x < thing_startx and player.x + player.width > thing_startx and player.y == thing_starty:
                            print('x crossover')
                            player.health -= 10

                    for bullet in player.bullets:
                        # Move bullet
                        bullet.y -= 10

                        # Check if bullet is inside screen, else kill
                        if bullet.y < 0:
                            player.bullets.remove(bullet)
                        if bullet.y <= 470 and bullet.y >= 469 and bullet.x>= 520 and bullet.x <= 647:
                            player.bullets.remove(bullet)

                        if bullet.y <= 520 and bullet.y >= 519 and bullet.x>= 520 and bullet.x <= 647:
                            #bullet.damage = 10
                            newBoss.health -= bullet.damage
                            newScore.score += bullet.damage
                            #bullet.update()


                            print("hit")

                        # Draw Bullet
                        bullet.blitBullet(screen)

                    if 1190 + 50 > mouse[0] > 1190 and 60 + 50 > mouse[1] > 60:
                        newPause.blitHoverPauseButton(screen)
                    else:
                        newPause.blitPauseButton(screen)

                    #newWolk.blitwolk(screen)
                    newBoss.blitBoss(screen)
                    player.draw(screen)
                    newScore.blitScore(screen)
                    screen.blit(font.render(text, True, (0, 0, 0)), (620, 100))

                elif state == PAUSE:
                    background.blitForrest()
                    screen.blit(s, (0, 0))
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 600 + 50 > mouse[0] > 600 and 320 + 50 > mouse[1] > 320:
                        state = old_state
                        old_state = PAUSE
                    if pygame.mouse.get_pressed()[0] and 700 + 50 > mouse[0] > 700 and 320 + 50 > mouse[1] > 320:
                        newPause.restartGame()
                    if pygame.mouse.get_pressed()[0] and 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[1] > 320:
                        newPause.task2()

                    if 600 + 50 > mouse[0] > 600 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverPlayButton(screen)
                    else:
                        newPause.blitPlayButton(screen)

                    if 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverExitButton(screen)
                    else:
                        newPause.blitExitButton(screen)

                    if 700 + 50 > mouse[0] > 700 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverReplayButton(screen)
                    else:
                        newPause.blitReplayButton(screen)
                    newScore.blitScore(screen)
                    screen.blit(pause_text, (600, 260))

                elif state == YOUWON:
                    background.blitForrest()
                    screen.blit(s, (0, 0))
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[
                        1] > 320 and state == YOUWON:
                        newPause.task()
                    if pygame.mouse.get_pressed()[0] and 700 + 50 > mouse[0] > 700 and 320 + 50 > mouse[1] > 320:
                        newPause.restartGame()
                    screen.blit(won_text, (550, 260))

                    if 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverExitButton(screen)
                    else:
                        newPause.blitExitButton(screen)

                    newScore.blitScore(screen)


                elif state == GAMEOVER:
                    background.blitForrest()
                    screen.blit(s, (0, 0))
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 700 + 50 > mouse[0] > 700 and 320 + 50 > mouse[1] > 320:
                        newPause.restartGame()
                    if pygame.mouse.get_pressed()[0] and 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[1] > 320:
                        newPause.task2()

                    #if 600 + 50 > mouse[0] > 600 and 320 + 50 > mouse[1] > 320:
                     #   newPause.blitHoverPlayButton(screen)
                    #else:
                     #   newPause.blitPlayButton(screen)

                    if 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverExitButton(screen)
                    else:
                        newPause.blitExitButton(screen)

                    if 700 + 50 > mouse[0] > 700 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverReplayButton(screen)
                    else:
                        newPause.blitReplayButton(screen)
                    newScore.blitScore(screen)
                    screen.blit(lose_text, (550, 260))

                elif state == GAMEOVER2:
                    background.blitForrest()
                    screen.blit(s, (0, 0))
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 700 + 50 > mouse[0] > 700 and 320 + 50 > mouse[1] > 320:
                        newPause.restartGame()
                    if pygame.mouse.get_pressed()[0] and 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[1] > 320:
                        newPause.task3()

                    #if 600 + 50 > mouse[0] > 600 and 320 + 50 > mouse[1] > 320:
                     #   newPause.blitHoverPlayButton(screen)
                    #else:
                     #   newPause.blitPlayButton(screen)

                    if 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverExitButton(screen)
                    else:
                        newPause.blitExitButton(screen)

                    if 700 + 50 > mouse[0] > 700 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverReplayButton(screen)
                    else:
                        newPause.blitReplayButton(screen)
                    newScore.blitScore(screen)
                    screen.blit(lose_text2, (500, 260))

                elif state == GAMEOVER3:
                    background.blitForrest()
                    screen.blit(s, (0, 0))
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 700 + 50 > mouse[0] > 700 and 320 + 50 > mouse[1] > 320:
                        newPause.restartGame()
                    if pygame.mouse.get_pressed()[0] and 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[1] > 320:
                        newPause.task4()

                    #if 600 + 50 > mouse[0] > 600 and 320 + 50 > mouse[1] > 320:
                     #   newPause.blitHoverPlayButton(screen)
                    #else:
                     #   newPause.blitPlayButton(screen)

                    if 650 + 50 > mouse[0] > 650 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverExitButton(screen)
                    else:
                        newPause.blitExitButton(screen)

                    if 700 + 50 > mouse[0] > 700 and 320 + 50 > mouse[1] > 320:
                        newPause.blitHoverReplayButton(screen)
                    else:
                        newPause.blitReplayButton(screen)
                    newScore.blitScore(screen)
                    screen.blit(lose_text3, (500, 260))



            pygame.display.flip()

            clock.tick(60)