from crosstheroad_lib.rectangle import Rectangle
import pygame, json


def getMemory(key):
    with open("data/memory.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        return data[key]

class Monkey(Rectangle):
    def __init__(self, x, y, w, h, screen, config, amount, monkeyList):
        Rectangle.__init__(self, x, y, w, h)
        self.screen = screen
        self.config = config
        self.amount = amount
        self.monkeys = monkeyList

    def show(self):
        image = pygame.image.load("data/" + getMemory("monkey").replace(".png", "_top.png"))
        image = pygame.transform.scale(image, (self.config.grid, self.config.grid))
        self.screen.blit(image, (self.x, self.y))

        pygame.draw.circle(self.screen, self.config.yellow, (int(self.x + self.w), int(self.y)), self.config.circle_radius)
        font = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 20)

        amount = font.render(str(self.amount), False, self.config.black)
        self.screen.blit(amount, (int(self.x + self.w - amount.get_rect().width/2), int(self.y - amount.get_rect().height/2)))

    def place(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.monkeys.pop(0)

    def move(self, xdir, ydir):
        if xdir == -1:
            if not self.x == 0:
                self.x += xdir * self.config.grid
        elif xdir == 1:
            if not self.x == self.config.screenDim[0] - self.config.grid - self.config.sideMenu[0]:
                self.x += xdir * self.config.grid
        elif ydir == -1:
            if not self.y == 0:
                self.y += ydir * self.config.grid
        elif ydir == 1:
            if not self.y == self.config.screenDim[1] - self.config.grid:
                self.y += ydir * self.config.grid

