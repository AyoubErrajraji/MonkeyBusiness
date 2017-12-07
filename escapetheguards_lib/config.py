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
screen_width = 1280
screen_height = 720


screenDim = (screen_width, screen_height)

screen = pygame.display.set_mode(screenDim)

backgroundintro = pygame.image.load('bgintro.png').convert()
backgroundintro = pygame.transform.scale(backgroundintro, (screen_width,screen_height))
logoImg = pygame.image.load('logo.png')
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (70,70))
containerImg = pygame.image.load('container1.png')
barrelsideImg = pygame.image.load('barrelside.png')
barrelsideImg = pygame.transform.scale(barrelsideImg, (200,250))