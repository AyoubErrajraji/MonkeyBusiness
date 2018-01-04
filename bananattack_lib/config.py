'''
Created on Nov 25, 2017
@author: lexdewilligen
'''

# COLORS #
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
SAND = (255,255,100)

# Screen #
NAME = "BananAttack"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FRAMES_PER_SECOND = 60
BG_COLOR = (154, 180, 61)
O_COLOR = (27, 143, 30)
FONT = "data/bananattack/FEASFBRG.ttf"
FONT_SIZE = 36
FONT_BIG_SIZE = 72
FONT_COLOR = (255, 255, 255)
SELECTED_O_COLOR = (225, 225, 55)
SELECTED_O_WIDTH = 2

# Info Box #
INFO_BOX_BG_COLOR = (0, 200, 0)

# States #
BA_PAUSE = 10 # game is paused
BA_PLAYING = 20 # wave in progress
BA_CLEAR = 30 # in between waves
BA_FAILURE = 40
BA_SUCCESS = 50

# Display #
DISPLAY_FONT = "data/bananattack/FEASFBRG.ttf"
DISPLAY_FONT_SIZE = 18
DISPLAY_FONT_COLOR = (27, 143, 30)
DISPLAY_X = 360
DISPLAY_Y = 538
DISPLAY_O_COLOR = O_COLOR
DISPLAY_BG_COLOR = BG_COLOR
DISPLAY_HEIGHT = 132
DISPLAY_WIDTH = 223
DISPLAY_MARGIN_LEFT = 5
DISPLAY_MARGIN_TOP = 5
DISPLAY_NO_IMG_HEIGHT = 32
DISPLAY_NO_IMG_WIDTH = 32

# Hardware Buttons #
MOUSE_LEFT = 1
MOUSE_MIDDLE = 2
MOUSE_RIGHT = 3

# Wave #
WAVE_X = 950
WAVE_Y = 20

# Money #
STARTING_MONEY = 100
MONEY_X = 950
MONEY_Y = 60

# State #
STATE_X = 950
STATE_Y = 100

# Lives #
LIVES_X = 950
LIVES_Y = 140
LIVES = 100

# StartWave Button
BUTTON_STARTWAVE_IMG = "data/bananattack/buttons/startWave.png"
BUTTON_STARTWAVE_HOVER_IMG = "data/bananattack/buttons/startWaveHover.png"
BUTTON_STARTWAVE_WIDTH = 300
BUTTON_STARTWAVE_HEIGHT = 100
BUTTON_STARTWAVE_X = 950
BUTTON_STARTWAVE_Y = 400

BUTTON_PLAYGAME_IMG = "data/bananattack/buttons/continueButton.png"
BUTTON_PLAYGAME_HOVER_IMG = "data/bananattack/buttons/continueButtonHover.png"
BUTTON_PLAYGAME_WIDTH = 100
BUTTON_PLAYGAME_HEIGHT = 100
BUTTON_PLAYGAME_X = 480
BUTTON_PLAYGAME_Y = 350

BUTTON_EXITGAME_IMG = "data/bananattack/buttons/exitToMenuButton.png"
BUTTON_EXITGAME_HOVER_IMG = "data/bananattack/buttons/exitToMenuButtonHover.png"
BUTTON_EXITGAME_WIDTH = 100
BUTTON_EXITGAME_HEIGHT = 100
BUTTON_EXITGAME_X = 680
BUTTON_EXITGAME_Y = 350

BUTTON_RESTARTGAME_IMG = "data/bananattack/buttons/replayButton.png"
BUTTON_RESTARTGAME_HOVER_IMG = "data/bananattack/buttons/replayButtonHover.png"
BUTTON_RESTARTGAME_WIDTH = 100
BUTTON_RESTARTGAME_HEIGHT = 100
BUTTON_RESTARTGAME_X = 580
BUTTON_RESTARTGAME_Y = 350

BUTTON_MONKEYBUTTON_IMG = "data/bananattack/buttons/monkeyButton.png"
BUTTON_MONKEYBUTTON_HOVER_IMG = "data/bananattack/buttons/monkeyButtonHover.png"
BUTTON_MONKEYBUTTON_WIDTH = 100
BUTTON_MONKEYBUTTON_HEIGHT = 100
BUTTON_MONKEYBUTTON_X = 950
BUTTON_MONKEYBUTTON_Y = 200

# Kind of draw
KIND_BUTTON = 36
KIND_ENEMY = 37
KIND_BULLET = 38

# ENEMY #
DEFAULT_HEALTH = 100
DEFAULT_SPEED = 70
DEFAULT_WIDTH = 30
DEFAULT_HEIGHT = 30
DEFAULT_IMAGE = "data/bananattack/sprites/truck_right.png"
DEFAULT_DELAY = 100
DEFAULT_PRICE = 50
DEFAULT_KILLVALUE = 20
DEFAULT_HEALTH_RADIUS = 10

# BULLET #
BULLET_WIDTH = 20
BULLET_HEIGHT = 20
BULLET_IMAGE = "data/bananattack/sprites/bullet.png"
BULLET_DAMAGE = 10
BULLET_SPEED = 150

# MONKEY #
MONKEY_SIZE = 50
MONKEY_IMAGE = "data/default_monkey.png"
MONKEY_IMAGE_TOP = "data/default_monkey_top.png"
MONKEY_RADIUS = 100
MONKEY_ATTACK_SPEED = 1.4

# WAYPOINTS #
STARTPOINT = (0, 311)

# [order, pos_x, pos_y]
WAYPOINTS = [
                [1, 168, 311],
                [2, 167, 168],
                [3, 312, 167],
                [4, 311, 504],
                [5, 120, 503],
                [6, 119, 598],
                [7, 792, 598],
                [8, 791, 456],
                [9, 552, 455],
                [10, 551, 360],
                [11, 792, 359],
                [12, 791, 000]
            ]






