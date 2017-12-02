import pygame, sys, config

pygame.init()

screenDim = (config.display_width,config.display_height)
screen = pygame.display.set_mode(screenDim)
pygame.display.set_caption('Escape The Guards')
clock = pygame.time.Clock()

backgroundintro = pygame.image.load('bgintro.png').convert()
backgroundintro = pygame.transform.scale(backgroundintro, (config.display_width,config.display_height))
logoImg = pygame.image.load('logo.png')
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (70,70))
containerImg = pygame.image.load('container1.png')
barrelsideImg = pygame.image.load('barrelside.png')
barrelsideImg = pygame.transform.scale(barrelsideImg, (200,250))

screen.blit(backgroundintro, (0,0))
screen.blit(logoImg, (300, 300))
screen.blit(logoImg, (730, 300))

def text_objects(text, font):
    textSurface = font.render(text, True, config.white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((config.display_width / 2), (config.display_height / 2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    main()

def crash():

    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("You Crashed!", largeText)
    TextRect.center = ((config.display_width / 2), (config.display_height / 2))
    screen.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(15)


def button():
    import Main
    Main.button()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "play":
                main()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "unpaused":
                unpause()
            elif action == "settings":
                settings_game()
            elif action == "leave":
                game_intro()


    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def unpause():
    global pause
    pause = False

def paused():
    myfont = pygame.font.SysFont("comicsansms", 115)
    label = myfont.render("Settings:", 1, (config.black))
    screen.blit(label, (490, 360))
    x = (config.display_width * 0.785)
    y = (config.display_height * 0.58)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        screen.fill(config.green)
        pygame.draw.rect(screen, config.dark_green, [980, 0, 300, 720])
        screen.blit(logoImg, (300, 300))

        button("Continue!", 980, 670, 100, 50, config.black, config.light_black, "unpaused")
        button("Settings!", 980, 670, 100, 50, config.black, config.light_black, "settings")
        button("Quit!", 1180, 670, 100, 50, config.black, config.light_black, "quit")

        pygame.display.update()
        clock.tick(15)

def game_intro():
    global pause
    intro = True

    x = (config.display_width * 0.785)
    y = (config.display_height * 0.58)

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        screen.blit(backgroundintro, (0, 0))

        myfont = pygame.font.SysFont("comicsansms", 80)
        label = myfont.render("Escape Those Guards!", 1, (config.black))
        screen.blit(label, (230,120))


        button("Let's Play!", 590, 350, 100, 50, config.black, config.light_black, "play")
        button("Settings!", 590, 450, 100, 50, config.black, config.light_black, "settings")
        button("Quit!", 590, 550, 100, 50, config.black, config.light_black, "quit")


        screen.blit(logoImg, (300, 300))
        screen.blit(logoImg, (730, 300))
        pygame.display.update()
        clock.tick(15)


def settings_game():
    global pause

    x = (config.display_width * 0.785)
    y = (config.display_height * 0.58)


    while settings_game:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(backgroundintro, (0, 0))


        myfont = pygame.font.SysFont("comicsansms", 80)
        label = myfont.render("Settings:", 1, (config.black))
        screen.blit(label, (470, 80))


        myfont = pygame.font.SysFont("comicsansms", 20)
        label = myfont.render("Resolution:", 1, (config.black))
        screen.blit(label, (470, 220))

        label = myfont.render("1280 x  720", 1, (config.black))
        screen.blit(label, (600, 220))

        label = myfont.render("1920 x 1080", 1, (config.black))
        screen.blit(label, (600, 250))

        label = myfont.render("Fullscreen", 1, (config.black))
        screen.blit(label, (600, 280))

        label = myfont.render("Controls:", 1, (config.black))
        screen.blit(label, (470, 310))

        label = myfont.render("Move forwards:", 1, (config.black))
        screen.blit(label, (600, 340))

        label = myfont.render("Move backwards:", 1, (config.black))
        screen.blit(label, (600, 370))

        label = myfont.render("Move Sideways:", 1, (config.black))
        screen.blit(label, (600, 400))

        label = myfont.render("Pause the game:", 1, (config.black))
        screen.blit(label, (600, 430))

        label = myfont.render("Key W", 1, (config.black))
        screen.blit(label, (780, 340))

        label = myfont.render("Key S", 1, (config.black))
        screen.blit(label, (780, 370))

        label = myfont.render("Key A (Left) and Key D (Right)", 1, (config.black))
        screen.blit(label, (780, 400))

        label = myfont.render("Key P", 1, (config.black))
        screen.blit(label, (780, 430))





        button("Back to Intro", 450, 670, 140, 50, config.black, config.light_black, "leave")
        button("Back to Game", 740, 670, 140, 50, config.black, config.light_black, "play")


        pygame.display.update()
        clock.tick(15)

def main():
    import Main
    Main.main()






game_intro()
settings_game()
main()
pygame.quit()
sys.exit()