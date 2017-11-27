import pygame
import sys

pygame.init()
pygame.display.set_caption("MonkeyWar")

class run(object):
    def runm(self):
        screen = pygame.display.set_mode((1280, 720))
        bg = pygame.image.load("data/monkeywar/bg.jpg")

        black = (0,0,0)
        white = (255,255,255)

        clock = pygame.time.Clock()

        crashed = False

        while not crashed:
        #menu functies
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True


        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
        pygame.quit()
        quit()