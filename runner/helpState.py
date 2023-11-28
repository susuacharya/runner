import pygame

# importing required mouse and event constants
from pygame.locals import (
    MOUSEBUTTONDOWN,
    QUIT,
)

class helpState:
    def __init__(self, window):
        # parent window passed from main script
        self.window = window

        # flag to return to menu
        self.go_back = 0

        # variables require for live background
        self.road_pos = 10
        self.bg = pygame.image.load("images/road_bg.png")
        
    def __repr__(self):
        return "Help"

    def update_game(self):
        # live background
        self.window.blit(self.bg, (0,(-30+self.road_pos%20)))
        self.road_pos += 10

        # content of the help screen that'll be put on the main screen
        help_text = pygame.Surface((300,520),pygame.SRCALPHA)
        help_text.fill((255,255,255,100))

        # help info created as an image, so much easier than rendering realtime
        image = pygame.image.load("images/control.png")
        
        # updating help info to main screen
        help_text.blit(image,(10,20))
        self.window.blit(help_text,(0,0))

        # Processing the event queue
        for event in pygame.event.get():
            # Quit on clicking close button
            if event.type == QUIT:
                pygame.quit()
            
            # go back to main menu when clicked on the screen
            if event.type == MOUSEBUTTONDOWN:
                self.go_back = 1
        
        # Flip the display
        pygame.display.flip()
        pygame.time.wait(500)