import pygame
import math
import json
import time
from bananattack_lib import config
from bananattack_lib import bullet

class Monkey():
    def __init__(self):
        self.x = pygame.mouse.get_pos()[0]-(config.MONKEY_SIZE // 2)
        self.y = pygame.mouse.get_pos()[1]-(config.MONKEY_SIZE // 2)

        self.radius = config.MONKEY_RADIUS
        self.closest = 1000
        self.closest_pos = (self.x, self.y - 100)

        self.bullets = []

        self.last_attack = 0

    def calc_center(self):
        px = self.x
        py = self.y
        cx, cy = px + .5 * config.DEFAULT_WIDTH, py + .5 * config.DEFAULT_HEIGHT
        return (int(cx), int(cy))

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def paint(self, surface, color=(255, 255, 255, 255), range=True):
        if range:
            pygame.draw.circle(surface, color, (self.x + (config.MONKEY_SIZE//2), self.y + (config.MONKEY_SIZE//2)), config.MONKEY_RADIUS, 3)

        image = pygame.image.load("data/" + self.getMemory("monkey").replace(".png","_top.png"))
        image = pygame.transform.scale(image, (config.MONKEY_SIZE, config.MONKEY_SIZE))
        image = self.rot_center(image, self.getAngle(self.closest_pos))
        surface.blit(image, (self.x, self.y))

    def getMemory(self, key):
        with open("data/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            return data[key]

    def collidepoint(self, mouse_pos):
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + (config.MONKEY_SIZE):
            return True
        if mouse_pos[1] > self.y and mouse_pos[1] < self.y + (config.MONKEY_SIZE):
            return True
        else:
            return False

    def getDistance(self, position):
        px, py = position
        cx, cy = (self.x + (config.MONKEY_SIZE//2), self.y + (config.MONKEY_SIZE//2))
        distance = ((px - cx) ** 2 + (py - cy) ** 2) ** .5
        return distance

    def attack(self, target):
        b = bullet.Bullet(self.calc_center(), config.BULLET_WIDTH, config.BULLET_HEIGHT, config.BULLET_IMAGE, config.BULLET_DAMAGE, config.BULLET_SPEED)
        b.set_target(target)
        self.bullets.append(b)
        self.last_attack = time.time()

    def paint_bullets(self, surface):
        for bullet in self.bullets:
            if bullet.alive == 1:
                bullet.paint(surface)

    def can_attack(self):
        return time.time() - self.last_attack >= 1.0 / config.MONKEY_ATTACK_SPEED

    def game_logic(self):
        for bullet in self.bullets:
            bullet.game_logic()

    def getAngle(self, position):
        px, py = position
        cx, cy = (self.x + (config.MONKEY_SIZE // 2), self.y + (config.MONKEY_SIZE // 2))

        if px < cx:
            overstaand = cx - px
        else:
            overstaand = px - cx

        if py < cy:
            aanliggend = cy - py
        else:
            aanliggend = py - cy

        angle = math.degrees(math.atan(overstaand/aanliggend)) if aanliggend != 0 else 0

        if px < cx and py > cy:
            # 1
            return -angle - 180
        elif px < cx and py < cx:
            # 2
            return angle
        elif px > cx and py < cx:
            # 3
            return -angle
        else:
            # 4
            return angle - 180

    def canPlace(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]

        if x >= 0 and x <= 192 and y >= 287 and y <= 335:
            return False
        elif x >= 144 and x <= 192 and y >= 143 and y <= 287:
            return False
        elif x >= 192 and x <= 336 and y >= 143 and y <= 191:
            return False
        elif x >= 288 and x <= 336 and y >= 191 and y <= 528:
            return False
        elif x >= 96 and x <= 288 and y >= 479 and y <= 528:
            return False
        elif x >= 96 and x <= 144 and y >= 528 and y <= 622:
            return False
        elif x >= 144 and x <= 816 and y >= 576 and y <= 622:
            return False
        elif x >= 768 and x <= 816 and y >= 432 and y <= 576:
            return False
        elif x >= 528 and x <= 768 and y >= 432 and y <= 480:
            return False
        elif x >= 528 and x <= 576 and y >= 335 and y <= 432:
            return False
        elif x >= 576 and x <= 768 and y >= 335 and y <= 384:
            return False
        elif x >= 768 and x <= 816 and y >= 0 and y <= 384:
            return False
        else:
            return True

