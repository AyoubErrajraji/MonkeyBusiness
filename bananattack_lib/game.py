'''
Created on Nov 25, 2017
@author: lexdewilligen
'''
import pygame
import pygame.locals
from bananattack_lib import config

class Game:
    def __init__(self, name, width, height, screen = None):
        self.width = width
        self.height = height
        self.on = True
        self.quit = False
        self.name = name
        if screen is None:
            self.new_screen(width, height)
        else:
            self.screen = screen
        pygame.font.init()

    def new_screen(self, width, height):
        self.screen = pygame.display.set_mode(
                # set the size
                (width, height),

                # use double-buffering for smooth animation
                pygame.locals.DOUBLEBUF |

                # apply alpha blending
                pygame.locals.SRCALPHA |

                # allow the window to be resizable
                pygame.locals.RESIZABLE)
        # set the title of the window
        pygame.display.set_caption(self.name)

    def main_loop(self):
        clock = pygame.time.Clock()
        keys = set()
        while True:
            clock.tick(config.FRAMES_PER_SECOND)

            newkeys = set()
            newclicks = set()
            for e in pygame.event.get():
                # did the user try to close the window?
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return

                # did the user just press the escape key?
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    if self.state == config.BA_CLEAR:
                        self.state = config.BA_PAUSE

                # track which keys are currently set
                if e.type == pygame.KEYDOWN:
                    keys.add(e.key)
                    newkeys.add(e.key)
                if e.type == pygame.KEYUP:
                    keys.discard(e.key)

                elif e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        for i, monkey in enumerate(self.rects):
                            if monkey.collidepoint(e.pos):
                                self.selected = i
                                self.selected_offset_x = monkey.x - e.pos[0]
                                self.selected_offset_y = monkey.y - e.pos[1]

                # track which mouse buttons were pressed
                if e.type == pygame.MOUSEBUTTONUP:
                    newclicks.add(e.button)
                    if e.button == 1:
                        self.selected = None

                # track the mouse's position
                if e.type == pygame.MOUSEMOTION:
                    mouse_pos = e.pos
                    if self.selected is not None:  # selected can be `0` so `is not None` is required
                        # move object
                        self.rects[self.selected].x = e.pos[0] + self.selected_offset_x
                        self.rects[self.selected].y = e.pos[1] + self.selected_offset_y
                        print(self.rects[self.selected].x)

                # update window size if resized
                if e.type == pygame.VIDEORESIZE:
                    self.new_screen(e.w, e.h)
                    self.screen.blit(pygame.transform.scale(pygame.image.load('data/bananattack/background.jpeg').convert(),(e.w, e.h)),(0, 0))

            if self.on:
                # Keep running bananattack.py game logic
                self.game_logic(keys)

                if self.quit == True:
                    pygame.quit()
                    return

                # Use the paint function defined in bananattack.py to draw the map, objects etc.
                self.paint(self.screen)

            pygame.display.flip()