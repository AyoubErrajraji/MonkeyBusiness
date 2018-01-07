from crosstheroad_lib.rectangle import Rectangle
import pygame

class Button(Rectangle):
    def __init__(self, x, y, w, h, img, hvr_img, screen, tooltip='none'):
        Rectangle.__init__(self, x, y, w, h)
        self.img = img
        self.hvr_img = hvr_img
        self.screen = screen
        self.tooltip = tooltip
        self.font = pygame.font.Font("data/bananattack/FEASFBRG.ttf", 30)

    def show(self):
        # Check if the button has a img for on hover
        if self.hvr_img != 'none':
            # Check if cursor is on the button
            if self.x <= pygame.mouse.get_pos()[0] <= self.x + self.w and self.y <= pygame.mouse.get_pos()[1] <= self.y + self.h:
                # If so, set the img to the hover img
                img = pygame.image.load(self.hvr_img).convert_alpha()
                # Check if the button has a tooltip
                if self.tooltip != 'none':
                    tooltip = self.font.render(self.tooltip, 1, (255, 255, 255))
                    self.screen.blit(tooltip, (self.x + self.w/2 - tooltip.get_rect().width/2, self.y - tooltip.get_rect().height - 2))
            # Else set the img to the normal one
            else:
                img = pygame.image.load(self.img).convert_alpha()
        # Else set the img to the normal one
        else:
            img = pygame.image.load(self.img).convert_alpha()
            if self.x <= pygame.mouse.get_pos()[0] <= self.x + self.w and self.y <= pygame.mouse.get_pos()[1] <= self.y + self.h and self.tooltip != 'none':
                tooltip = self.font.render(self.tooltip, 1, (255, 255, 255))
                self.screen.blit(tooltip, (self.x + self.w/2 - tooltip.get_rect().width/2, self.y - tooltip.get_rect().height - 2))

        # Display button img
        self.screen.blit(img, (self.x, self.y))
