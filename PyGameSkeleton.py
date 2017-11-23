import sys, pygame


pygame.init()

width = 900
height = 700
screenDim = (width, height)
gameName = "Monkey Royale"


screen = pygame.display.set_mode(screenDim)
pygame.display.set_caption(gameName)
print("Game succefully launched!")
finished = False
while not finished:
    #processing all the events
    for event in pygame.event.get():
        #do appropriate things with events
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()

            sys.exit()

        
    pygame.display.flip()#Update method / load next screen
