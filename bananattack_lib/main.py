from bananattack_lib import bananattack
from bananattack_lib import config
import pygame
import pygame.locals

def main():
    # Setup the window
    screen = pygame.display.set_mode(
        # set the size
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT),

        # use double-buffering for smooth animation
        pygame.locals.DOUBLEBUF |

        # apply alpha blending
        pygame.locals.SRCALPHA)
    # set the title of the window
    pygame.display.set_caption(config.NAME)

    td = bananattack.BananAttack(config.NAME, config.SCREEN_WIDTH, config.SCREEN_HEIGHT, screen)
    td.main_loop()
