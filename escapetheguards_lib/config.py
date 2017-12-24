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
w = 1280
h = 720
screen_width = w
screen_height = h
screenDim = (screen_width, screen_height)
screen = pygame.display.set_mode(screenDim)
gs_width = 880
gs_height = 720
player_width = 70
player_height = 70


### CLOCK: ###

clock = pygame.time.Clock()

### IMAGES: ###


    ### INTRO: ###

backgroundintro = pygame.image.load('/data/escapetheguards/bgintro.png').convert()
backgroundintro = pygame.transform.scale(backgroundintro, (screen_width, screen_height))
monkeyImg = pygame.image.load('/data/escapetheguards/monkey.png').convert_alpha()


    ### LEVEL 1 & 2 ###


logoImg = pygame.image.load('/data/escapetheguards/logo.png')

player_left = pygame.image.load('/data/escapetheguards/player_left.png')
player_left = pygame.transform.scale(player_left, (70, 70))
player_right = pygame.image.load('/data/escapetheguards/player_right.png')
player_right = pygame.transform.scale(player_right, (70, 70))
player_up = pygame.image.load('/data/escapetheguards/player_up.png')
player_up = pygame.transform.scale(player_up, (70, 70))
player_down = pygame.image.load('/data/escapetheguards/player_down.png')
player_down = pygame.transform.scale(player_down, (70, 70))

containerImg = pygame.image.load('/data/escapetheguards/container1.png').convert_alpha()

barrelsideImg = pygame.image.load('/data/escapetheguards/barrelside.png')
barrelsideImg = pygame.transform.scale(barrelsideImg, (200, 250))

tableImg = pygame.image.load('/data/escapetheguards/picknicktable.png').convert_alpha()

cageImg = pygame.image.load('/data/escapetheguards/cage.png').convert_alpha()
cage2Img = pygame.image.load('/data/escapetheguards/cage2.png').convert_alpha()
cage2Img = pygame.transform.scale(cage2Img, (260,250))
cage3Img = pygame.image.load('/data/escapetheguards/cage3.png').convert_alpha()
cage3Img = pygame.transform.scale(cage3Img, (250,200))
cagedoorImg = pygame.image.load('/data/escapetheguards/cagedoor.png').convert_alpha()

carImg = pygame.image.load('/data/escapetheguards/car.png').convert_alpha()
car1Img = pygame.image.load('/data/escapetheguards/car1.png').convert_alpha()
car1Img = pygame.transform.scale(car1Img, (300, 200))

excavatorImg = pygame.image.load('/data/escapetheguards/excavator.png').convert_alpha()
truckImg = pygame.image.load('/data/escapetheguards/truck.png').convert_alpha()

bananaImg = pygame.image.load('/data/escapetheguards/bananapoint.png').convert_alpha()
bananaImg = pygame.transform.scale(bananaImg, (30,30))

pickupImg = pygame.image.load('/data/escapetheguards/pickup.png').convert_alpha()

guard_rightImg = pygame.image.load('/data/escapetheguards/guards_right.png').convert_alpha()
guard_rightImg = pygame.transform.scale(guard_rightImg, (100,100))
guard_leftImg = pygame.image.load('/data/escapetheguards/guards_left.png').convert_alpha()
guard_leftImg = pygame.transform.scale(guard_leftImg, (400,250))
guard_topImg = pygame.image.load('/data/escapetheguards/guards_top.png').convert_alpha()
guard_topImg = pygame.transform.scale(guard_topImg, (280, 350))
guard_bottomImg = pygame.image.load('/data/escapetheguards/guards_bottom.png').convert_alpha()
guard_bottomImg = pygame.transform.scale(guard_bottomImg, (100,100))



