import pygame
import json
from os.path import join
from menu_lib import slidemenu

def main():

    # === CONFIG === (UPPER_CASE names)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    RED = (255, 0, 0)

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    FPS = 60

    APPRENTICE_MONKEY = 1000
    NINJA_MONKEY = 1200

    # === CLASSES === (CamelCase names)

    class Button():

        def __init__(self, text='OK', pos=(0, 0), size=(100, 50), command=None):
            font = pygame.font.SysFont(None, 35)

            self.text = text
            self.rect = pygame.Rect((0, 0), size)

            self.image_normal = pygame.Surface(size)
            self.image_normal.fill(WHITE)
            txt_image = font.render(self.text, True, RED)
            txt_rect = txt_image.get_rect(center=self.rect.center)
            self.image_normal.blit(txt_image, txt_rect)

            self.image_hover = pygame.Surface(size)
            self.image_hover.fill(RED)
            txt_image = font.render(self.text, True, WHITE)
            txt_rect = txt_image.get_rect(center=self.rect.center)
            self.image_hover.blit(txt_image, txt_rect)

            self.rect.topleft = pos

            self.hover = False

            if command:
                self.command = command

        def draw(self, screen):
            if self.hover:
                screen.blit(self.image_hover, self.rect)
            else:
                screen.blit(self.image_normal, self.rect)

        def handle_event(self, event):
            if event.type == pygame.MOUSEMOTION:
                self.hover = self.rect.collidepoint(event.pos)

            if self.hover and self.command:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.command()

        def command(self):
            print("Click")


    # === FUNCTIONS === (lower_case names)

    def back():
        mymenu = slidemenu.run()
        mymenu.runm()

    def default_select():
        setMemory("monkey", "default_monkey.png")

    def apprentice_select():
        setMemory("monkey", "apprentice_monkey.png")
    def apprentice_buy():
        setMemory("balance", getMemory("balance") - APPRENTICE_MONKEY)
        bought = getMemory("bought")
        bought.append("apprentice_monkey.png")
        setMemory("bought", bought)
    def apprentice_sell():
        if getMemory("monkey") == "apprentice_monkey.png":
            setMemory("monkey","default_monkey.png")
        setMemory("balance", getMemory("balance") + (APPRENTICE_MONKEY // 2))
        bought = getMemory("bought")
        bought.remove("apprentice_monkey.png")
        setMemory("bought", bought)

    def ninja_select():
        setMemory("monkey","ninja_monkey.png")
    def ninja_buy():
        setMemory("balance",getMemory("balance") - NINJA_MONKEY)
        bought = getMemory("bought")
        bought.append("ninja_monkey.png")
        setMemory("bought",bought)
    def ninja_sell():
        if getMemory("monkey") == "ninja_monkey.png":
            setMemory("monkey","default_monkey.png")
        setMemory("balance", getMemory("balance") + (NINJA_MONKEY//2))
        bought = getMemory("bought")
        bought.remove("ninja_monkey.png")
        setMemory("bought", bought)

    def getMemory(key):
        with open("data/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            return data[key]

    def setMemory(key, value):
        with open("data/memory.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            data[key] = value

            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()


    # === MAIN === (lower_case names)

    # --- (global) variables ---
    user = getMemory("player")
    balance = getMemory("balance")
    monkey = getMemory("monkey")
    bought = getMemory("bought")

    font = pygame.font.Font(join('data/menu/FEASFBRG.ttf'), 45)

    # --- init ---

    pygame.init()
    pygame.display.set_caption("Store")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_rect = screen.get_rect()

    # --- objects ---

    # - buttons -

    back = Button(text="Back", pos=(50, 450), command=back)

    selected_default_monkey = Button(text="Selected", pos=(840, 40))
    select_default_monkey = Button(text="Select", pos=(840, 40), command=default_select)

    price_apprentice_monkey = Button(text=str(APPRENTICE_MONKEY), pos=(840, 100))
    selected_apprentice_monkey = Button(text="Selected", pos=(840, 100))
    select_apprentice_monkey = Button(text="Select", pos=(840, 100), command=apprentice_select)
    buy_apprentice_monkey = Button(text="Buy", pos=(840,100), command=apprentice_buy)
    sell_apprentice_monkey = Button(text="Sell", pos=(1110, 100), command=apprentice_sell)

    price_ninja_monkey = Button(text=str(NINJA_MONKEY), pos=(840, 160))
    selected_ninja_monkey = Button(text="Selected", pos=(840, 160))
    select_ninja_monkey = Button(text="Select", pos=(840, 160), command=ninja_select)
    buy_ninja_monkey = Button(text="Buy", pos=(840, 160), command=ninja_buy)
    sell_ninja_monkey = Button(text="Sell", pos=(1110, 160), command=ninja_sell)

    # --- mainloop ---

    clock = pygame.time.Clock()
    is_running = True

    while is_running:

        # --- events ---

        for event in pygame.event.get():

            # --- global events ---

            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    selected = None

            # --- objects events ---

            back.handle_event(event)

            if "default_monkey.png" == monkey:
                selected_default_monkey.handle_event(event)
            else:
                select_default_monkey.handle_event(event)

            if "apprentice_monkey.png" == monkey:
                selected_apprentice_monkey.handle_event(event)
            elif "apprentice_monkey.png" in bought:
                select_apprentice_monkey.handle_event(event)
            elif balance > APPRENTICE_MONKEY:
                buy_apprentice_monkey.handle_event(event)
            else:
                price_apprentice_monkey.handle_event(event)
            if "apprentice_monkey.png" in bought:
                sell_apprentice_monkey.handle_event(event)

            if "ninja_monkey.png" == monkey:
                selected_ninja_monkey.handle_event(event)
            elif "ninja_monkey.png" in bought:
                select_ninja_monkey.handle_event(event)
            elif balance > NINJA_MONKEY:
                buy_ninja_monkey.handle_event(event)
            else:
                price_ninja_monkey.handle_event(event)
            if "ninja_monkey.png" in bought:
                sell_ninja_monkey.handle_event(event)

        # --- updates ---

        user = getMemory("player")
        balance = getMemory("balance")
        monkey = getMemory("monkey")
        bought = getMemory("bought")

        # --- draws ---

        screen.fill(BLACK)
        screen.blit(pygame.image.load('data/menu/bg.png').convert(), (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load('data/%s' % (monkey)).convert_alpha(), (300, 300)), (300, 360))

        back.draw(screen)

        if "default_monkey.png" == monkey:
            selected_default_monkey.draw(screen)
        else:
            select_default_monkey.draw(screen)
        screen.blit(pygame.transform.scale(pygame.image.load('data/default_monkey_top.png').convert_alpha(), (50, 50)),(1000, 40))

        if "apprentice_monkey.png" == monkey:
            selected_apprentice_monkey.draw(screen)
        elif "apprentice_monkey.png" in bought:
            select_apprentice_monkey.draw(screen)
        elif balance > APPRENTICE_MONKEY:
            buy_apprentice_monkey.draw(screen)
        else:
            price_apprentice_monkey.draw(screen)
        screen.blit(pygame.transform.scale(pygame.image.load('data/apprentice_monkey_top.png').convert_alpha(), (50, 50)), (1000, 100))
        if "apprentice_monkey.png" in bought:
            sell_apprentice_monkey.draw(screen)

        if "ninja_monkey.png" == monkey:
            selected_ninja_monkey.draw(screen)
        elif "ninja_monkey.png" in bought:
            select_ninja_monkey.draw(screen)
        elif balance > NINJA_MONKEY:
            buy_ninja_monkey.draw(screen)
        else:
            price_ninja_monkey.draw(screen)
        screen.blit(pygame.transform.scale(pygame.image.load('data/ninja_monkey_top.png').convert_alpha(), (50, 50)),(1000, 160))
        if "ninja_monkey.png" in bought:
            sell_ninja_monkey.draw(screen)

        screen.blit(font.render('Username: %s' % (user), 1, (255, 255, 255)), (50, 300))
        screen.blit(font.render('Balance: %d' % (balance), 1, (255, 255, 255)), (50, 350))

        pygame.display.update()

        # --- FPS ---

        clock.tick(FPS)

    # --- the end ---

    pygame.quit()
