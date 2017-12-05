from crosstheroad_lib import crosstheroad, config
import pygame, pygame.locals


def main():
    # Setup the window
    pygame.init()
    #set screen
    screen = pygame.display.set_mode((config.screenDim[0], config.screenDim[1]), pygame.locals.DOUBLEBUF | pygame.locals.SRCALPHA)
    # set the title of the window
    pygame.display.set_caption(config.name)

    game = crosstheroad.Crosstheroad(screen, config)
    game.run()


main()