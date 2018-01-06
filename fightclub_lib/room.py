import pygame


class Wall(pygame.sprite.Sprite):
    """
    Walls can't be passed by player.
    """
    def __init__(self, x, y, width, height, color, screen):
        # Init.
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.screen = screen
        # Create
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height], 0)