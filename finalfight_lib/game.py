import pygame
import sys
import json
import os
import math
import itertools

pygame.init()
pygame.font.init()


class Game:
    def __init__(self,screen):
        self.fps = 30
        self.frame = pygame.time.Clock()
        self.screen = screen

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

class Player(Game):  # represents the bird, not the game
    def __init__(self,screen):
        Game.__init__(self, screen)
        """ The constructor of the class """
        self.image = pygame.image.load("data/finalfight/monkey.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        # the bird's position
        self.x = 300
        self.y = 550

    #def loadPlayer(self,name):
        #self.player = pygame.image.load(name).convert_alpha()
       # playerWidth = self.player.get_rect().width
      #  playerHeight = self.player.get_rect().height
     #   self.player = pygame.transform.scale(self.player, (150, 150))

    #def blitPlayer(self):
    #    self.screen.blit(self.player, (300, 550))

    def movePlayer(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1  # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]:  # down key
            self.y += dist  # move down
        elif key[pygame.K_UP]:  # up key
            self.y -= dist  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.x += dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.x -= dist  # move left

    def draw(self, screen):
        """ Draw on surface """
         #blit yourself at your current position
        screen.blit(self.image, (self.x, self.y))

class Boss(Game):
    def __init__(self,screen):
        Game.__init__(self, screen)
        self.bossX = 350
        self.bossY = 300
        self.boss = None

    def loadBoss(self,name):
        self.boss = pygame.image.load(name).convert_alpha()
        bossWidth = self.boss.get_rect().width
        bossHeight = self.boss.get_rect().height
        self.boss = pygame.transform.scale(self.boss, (bossWidth, bossHeight))

    def blitBoss(self,screen):
        screen.blit(self.boss, (520, 300))


class Wolk(Game):
    def __init__(self, screen):
        Game.__init__(self, screen)
        self.wolkX = 430
        self.wolkY = 130
        self.wolk = None

    def loadWolk(self, name):
        self.wolk = pygame.image.load(name).convert_alpha()
        wolkWidth = self.wolk.get_rect().width
        wolkHeight = self.wolk.get_rect().height
        self.wolk = pygame.transform.scale(self.wolk, (350,200))

    def blitwolk(self,screen):
        screen.blit(self.wolk, (590, 130))

class Score(Game):
    def __init__(self,screen):
        Game.__init__(self,screen)


    def getMemory(key):
        with open("finalfight_lib/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            return data[key]

    def setMemory(key, value):
        with open("finalfight_lib/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            data[key] = value

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def loadScore(self,screen):
        font = pygame.font.Font("data/finalfight/FEASFBRG.ttf", 30)
        score = "score: %d" % Score.getMemory("score")
        self.temp_surface = font.render(score, 1, (255, 255, 255))

    def blitScore(self,screen):
        screen.blit(self.temp_surface, (1150, 10))

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
        self.pause_text = pygame.font.Font("finalfight_lib/FEASFBRG.ttf", 60).render('Paused', True,
                                                                                 pygame.color.Color('White'))
        s = pygame.Surface((1280, 720), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))

    def loadExitButton(self, name):
        self.exitButton = pygame.image.load(name).convert_alpha()

        self.exitButton = pygame.transform.scale(self.exitButton, (150, 50))

    def blitExitButton(self, screen):
        screen.blit(self.exitButton, (605, 420))

    #def loadMenuButton(self, name):
    #   self.menuButton = pygame.image.load(name).convert_alpha()

    #    self.menuButton = pygame.transform.scale(self.menuButton, (150, 50))

    #def blitMenuButton(self, screen):
    #    screen.blit(self.menuButton, (605, 420))



class run():
    def runm(self):
        width = 1280
        height = 720
        screenDim = (width, height)

        screen = pygame.display.set_mode(screenDim)

        pygame.display.set_caption("Final Fight")

        pygame.init()
        #newPlayer = Player(screen)
        player = Player(screen)
        newBoss = Boss(screen)
        newWolk = Wolk(screen)
        background = Background(screen)
        newScore = Score(screen)
        newPause = Pause(screen)

        background.loadForrest("data/finalfight/openplek.png")

        #newPlayer.loadPlayer("data/finalfight/monkey.png")

        #newPlayer.movePlayer()

        #newPlayer.draw(screen)

        newPause.loadExitButton("data/finalfight/exitButton.png")

        #newPause.loadMenuButton("data/finalfight/menuButton.png")

        newBoss.loadBoss("data/finalfight/boss2.png")

        newWolk.loadWolk("data/finalfight/spreekwolk.png")

        newScore.loadScore(screen)

        newPause.loadPause()

        background.blitForrest()

        newWolk.blitwolk(screen)

        newBoss.blitBoss(screen)

        #newPlayer.blitPlayer()

        #newPlayer.movePlayer()  # handle the keys

        newPause.blitExitButton(screen)

        #newPause.blitMenuButton(screen)

        newScore.blitScore(screen)

        Score.setMemory("score", 876)

        RUNNING, notRUNNING, PAUSE = 0, 1, 2
        state = RUNNING

        pause_text = pygame.font.Font("finalfight_lib/FEASFBRG.ttf", 60).render('Paused', True, pygame.color.Color('White'))

        s = pygame.Surface((width, height), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((0, 0, 0, 150))

        clock = pygame.time.Clock()

        counter, text = 3, '3'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.Font("finalfight_lib/FEASFBRG.ttf", 60)

        while True:

            for e in pygame.event.get():
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'GO!'

                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                   # RUNNING = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_p : state = PAUSE
                    if e.key == pygame.K_s : state = RUNNING


            else:
                screen.fill((0, 0, 0))
                #screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
                #pygame.display.flip()
                #clock.tick(60)
                #if text == 'GO!':
                 #   state = RUNNING
                #elif counter > 0:
                 #   state = notRUNNING


                if state == RUNNING:
                    player.movePlayer()

                    background.blitForrest()
                    newWolk.blitwolk(screen)
                    newBoss.blitBoss(screen)
                    #newPlayer.blitPlayer()
                    player.draw(screen)
                    newScore.blitScore(screen)
                    screen.blit(font.render(text, True, (0, 0, 0)), (620, 100))

                #if state == notRUNNING:
                    #player.movePlayer()

                 #   background.blitForrest()
                    #newWolk.blitwolk(screen)
                  #  newBoss.blitBoss(screen)
                    #newPlayer.blitPlayer()
                   # player.draw(screen)
                    #newScore.blitScore(screen)
                    #screen.blit(font.render(text, True, (0, 0, 0)), (620, 100))



                elif state == PAUSE:
                    background.blitForrest()
                    #newWolk.blitwolk()
                    #newBoss.blitBoss(screen)
                    #newPlayer.blitPlayer()
                    #player.draw(screen)
                    newScore.blitScore(screen)
                    screen.blit(s, (0, 0))
                    screen.blit(pause_text, (600, 360))
                    #newPause.blitMenuButton(screen)
                    newPause.blitExitButton(screen)

 #               if state == RUNNING:
#                    player.movePlayer()

                #elif state == PAUSE:
                    #player.draw(screen)



            #player.movePlayer()  # handle the keys
            #player.draw(screen)
            pygame.display.flip()

            clock.tick(60)




        #key = pygame.key.get_pressed()
         #   dist = 1  # distance moved in 1 frame, try changing it to 5
          #  if key[pygame.K_DOWN]:  # down key
           #     newPlayer.movePlayer() # move down
            #elif key[pygame.K_UP]:  # up key
             #   newPlayer.movePlayer()  # move up
            #if key[pygame.K_RIGHT]:  # right key
             #   newPlayer.movePlayer()  # move right
            #elif key[pygame.K_LEFT]:  # left key
             #   newPlayer.movePlayer()  # move left

