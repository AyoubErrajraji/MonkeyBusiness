from crosstheroad_lib.rectangle import Rectangle
import pygame

class Car(Rectangle):
    def __init__(self, x, y, w, h, screen, config, speed, img):
        Rectangle.__init__(self, x, y, w, h)
        self.screen = screen
        self.config = config
        self.speed = speed
        self.img = img

    def update(self):
        self.x = self.x + self.speed

        if self.x > self.config.screenDim[0] - self.config.sideMenu[0] and self.speed > 0:
            self.x = - self.w

        if self.x + self.w < 0 and self.speed < 0:
            self.x = self.config.screenDim[0] + self.w - self.config.sideMenu[0]

    def show(self):
        if self.img == 'none':
            cr = pygame.Rect(self.x, self.y, self.w, self.h)
            pygame.draw.rect(self.screen, self.config.green, cr)
        else:
            img = pygame.image.load(self.img).convert_alpha()
            self.screen.blit(img, (self.x, self.y))

