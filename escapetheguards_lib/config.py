import pygame

### COLORS: ###
black = (0, 0, 0)
light_black = (43,39,39)
white = (255, 255, 255)
green = (15,213,88)
dark_green = (14,104,47)
gray = (206,206,206)
brown = (102,51,0)
yellow = (204,204,0)


### SCREEN: ###
display_width = 1280
display_height = 720

barrelsideImg = pygame.image.load('barrelside.png')
barrelsideImg = pygame.transform.scale(barrelsideImg, (200,250))