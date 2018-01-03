from bananattack_lib import config
from bananattack_lib import draw
import time
import cmath

class Bullet(draw.Draw):
    def __init__(self, position, width=config.BULLET_WIDTH, height=config.BULLET_HEIGHT, image=config.BULLET_IMAGE,dmg=config.BULLET_DAMAGE, speed=config.BULLET_SPEED):
        draw.Draw.__init__(self, config.KIND_BULLET, position, width, height, image)
        self.dmg = dmg
        self.speed = speed
        self.target = None

        # frame rate independent data
        self.last_frame = time.time()
        self.dt = 0

        self.alive = 1

    def get_damage(self):
        return self.dmg

    def set_target(self, target):
        self.target = target

    # moves toward the target object if it exists
    def move(self):
        if self.target is None:
            return

        # move based on center points
        dest = self.target.get_center()
        curr = self.get_center()

        # calculate the direction to move
        direction = (dest[0] - curr[0], dest[1] - curr[1])
        x = direction[0] ** 2
        y = direction[1] ** 2

        # normalize the direction vector
        mag = (float(x) + float(y)) ** 0.5
        normalized = (direction[0] / mag, direction[1] / mag)

        # calculate how far to move in the direction
        # choosing to move as far/fast as allowed
        # or to move straight to the target if
        # it is closer
        dist = min(self.speed * self.dt, mag)
        self.position = (self.position[0] + dist * normalized[0], self.position[1] + dist * normalized[1])

    def game_logic(self):
        if self.alive == 1:
            # frame rate independent calculations
            t = time.time()
            self.dt = t - self.last_frame
            self.last_frame = t

            # move
            self.move()

            # if target no longer exists, send a message to the game
            if self.target is None or self.target.is_dead():
                self.target.kill()

            # if target exists and we collided with it
            # call the .hit() method of the target passing
            # the bullet's damage
            elif self.collide(self.target) or self.target.collide(self):
                self.target.hit(self.get_damage())
                self.alive = 0
                # send a message if the target took fatal damage
                if self.target.is_dead():
                    print("DEAD")