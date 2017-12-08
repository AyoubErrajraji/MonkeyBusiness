import pygame

pygame.init()

width = 1280
height = 720

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Banana Fight Club')
clock = pygame.time.Clock()
done = False

#Loading Images
mainImg = pygame.image.load('monkey.png').convert_alpha()

flagImg = pygame.image.load("flag.png").convert_alpha()

bckImg =  pygame.image.load("background.png").convert()
bckImg = pygame.transform.scale(bckImg, (width, height))


def Background(x, y):
    gameDisplay.blit(bckImg, (x,y))

def Character(x, y):
    gameDisplay.blit(mainImg, (x, y))
x = (width * 0.8)
y = (height * 0.8)
x_change = 0
y_change = 0
character_speed = 0
def Flag(x, y):
    gameDisplay.blit(flagImg, (x,y))

#Game Loop
while done == False :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0


    x += x_change
    y += y_change

    Background(0,0)
    Character(x,y)
    Flag((1260/2), (700/2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

