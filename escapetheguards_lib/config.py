import pygame

### COLORS: ###
black = (0, 0, 0)
light_black = (43, 39, 39)
white = (255, 255, 255)
green = (15, 213, 88)
dark_green = (14, 104, 47)
gray = (206, 206, 206)
brown = (102, 51, 0)
yellow = (204, 204, 0)


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


### LOADING THE IMAGES: ###

backgroundintro = pygame.image.load('bgintro.png').convert()
monkeyImg = pygame.image.load('monkey.png').convert_alpha()
logoImg = pygame.image.load('logo.png')
tableImg = pygame.image.load('picknicktable.png').convert_alpha()
cageImg = pygame.image.load('cage.png').convert_alpha()
cage2Img = pygame.image.load('cage2.png').convert_alpha()
cage3Img = pygame.image.load('cage3.png').convert_alpha()
cagedoorImg = pygame.image.load('cagedoor.png').convert_alpha()
bananaImg = pygame.image.load('bananapoint.png').convert_alpha()
guard_rightImg = pygame.image.load('guards_right.png').convert_alpha()
guard_leftImg = pygame.image.load('guards_left.png').convert_alpha()
guard_topImg = pygame.image.load('guards_top.png').convert_alpha()
guard_bottomImg = pygame.image.load('guards_bottom.png').convert_alpha()



exitgame = pygame.image.load('exitGame.png').convert_alpha()
exitgamehover = pygame.image.load('exitGameHover.png').convert_alpha()
pausegame = pygame.image.load('pauseGame.png').convert_alpha()
pausegamehover = pygame.image.load('pauseGameHover.png').convert_alpha()
playgame = pygame.image.load('playGame.png').convert_alpha()
playgamehover = pygame.image.load('playGameHover.png').convert_alpha()
replaygame = pygame.image.load('replayGame.png').convert_alpha()
replaygamehover = pygame.image.load('replayGameHover.png').convert_alpha()
startgame = pygame.image.load('startGame.png').convert_alpha()
startgamehover = pygame.image.load('startGameHover.png').convert_alpha()

pausewoodgame = pygame.image.load('pauseGamewood.png').convert_alpha()
pausewoodgamehover = pygame.image.load('pauseGameHoverwood.png').convert_alpha()
exitwoodgame = pygame.image.load('exitGamewood.png').convert_alpha()
exitwoodgamehover = pygame.image.load('exitGameHoverwood.png').convert_alpha()

acid = pygame.image.load("acid_monkey.png").convert_alpha()
apprentice = pygame.image.load("apprentice_monkey_top.png").convert_alpha()
default = pygame.image.load("default_monkey_top.png").convert_alpha()
dragon = pygame.image.load("dragon_monkey_top.png").convert_alpha()
engineer = pygame.image.load("engineer_monkey_top.png").convert_alpha()
farmer = pygame.image.load("farmer_monkey.png").convert_alpha()
ninja = pygame.image.load("ninja_monkey_top.png").convert_alpha()
robo = pygame.image.load("robo_monkey_top.png").convert_alpha()
roboflat = pygame.image.load("robo_monkey.png").convert_alpha()
superMonkey = pygame.image.load("super_monkey_top.png").convert_alpha()
mainImg = pygame.image.load('monkey1.png').convert_alpha()
charwFlagImg = pygame.image.load('charwflag.png').convert_alpha()
flagImg = pygame.image.load("flag.png").convert_alpha()
noFlagImg = pygame.image.load("noflag.png").convert_alpha()
targetImg = pygame.image.load("target.png").convert_alpha()



# Transforming Characters
acid = pygame.transform.scale(acid, (70,70))
apprentice = pygame.transform.scale(apprentice, (70,70))
default = pygame.transform.scale(default, (70,70))
pygame.transform.scale(dragon, (70,70))
engineer = pygame.transform.scale(engineer, (70,70))
farmer = pygame.transform.scale(farmer, (70,70))
ninja = pygame.transform.scale(ninja, (70,70))
robo = pygame.transform.scale(robo, (70,70))
acid = pygame.transform.scale(acid, (150, 300))
backgroundintro = pygame.transform.scale(backgroundintro, (screen_width, screen_height))
bananaImg = pygame.transform.scale(bananaImg, (30,30))
exitgame = pygame.transform.scale(exitgame, (270,135))
exitgamehover = pygame.transform.scale(exitgamehover, (270,135))
cage2Img = pygame.transform.scale(cage2Img, (260,250))
cage3Img = pygame.transform.scale(cage3Img, (250,200))
guard_rightImg = pygame.transform.scale(guard_rightImg, (100,100))
monkeyImg = pygame.transform.scale(monkeyImg, (500, 600))
guard_leftImg = pygame.transform.scale(guard_leftImg, (400,250))
guard_bottomImg = pygame.transform.scale(guard_bottomImg, (100,100))
guard_topImg = pygame.transform.scale(guard_topImg, (280, 350))
noFlagImg = pygame.transform.scale(noFlagImg, (70,70))
roboflat = pygame.transform.scale(roboflat, (100,120))

playgame = pygame.transform.scale(playgame, (50,50))
playgamehover = pygame.transform.scale(playgamehover, (50,50))
startgame = pygame.transform.scale(startgame, (50,50))
startgamehover = pygame.transform.scale(startgamehover, (50,50))
pausegame = pygame.transform.scale(pausegame, (50,50))
pausegamehover = pygame.transform.scale(pausegamehover, (50,50))
replaygame = pygame.transform.scale(replaygame, (50,50))
replaygamehover = pygame.transform.scale(replaygamehover, (50,50))
exitgame = pygame.transform.scale(exitgame, (50,50))
exitgamehover = pygame.transform.scale(exitgamehover, (50,50))
exitwoodgame = pygame.transform.scale(exitwoodgame, (280,100))
exitwoodgamehover = pygame.transform.scale(exitwoodgamehover, (280,100))














