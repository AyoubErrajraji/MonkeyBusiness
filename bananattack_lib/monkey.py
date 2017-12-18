import pygame

from bananattack_lib import config

class Monkey():
    def __init__(self):
        self.x = 0
        self.y = 0

    def paint(self, surface):
        image = pygame.image.load(config.MONKEY_IMAGE)
        image = pygame.transform.scale(image, (config.MONKEY_SIZE, config.MONKEY_SIZE))

        surface.blit(image, (self.x, self.y))

    def collidepoint(self, mouse_pos):
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + (config.MONKEY_SIZE):
            return True
        if mouse_pos[1] > self.y and mouse_pos[1] < self.y + (config.MONKEY_SIZE):
            return True
        else:
            return False


