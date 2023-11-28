import pygame

# importing button class
from button import button

from pygame.locals import (
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
    QUIT,
)

# declaring color constants, too tired of typing 0s and 255s at this point
BLACK = (0,0,0)
WHITE = (255,255,255)

class menuState:
    def __init__(self, window, current = 0 ):
        # parent window passed down from main script
        self.window = window

        # only state that also needs to keep track of current state in orfer to facilitate routing to multiple states
        self.current = current

        # variables for live background
        self.road_pos = 10
        self.bg = pygame.image.load("images/road_bg.png")
        self.myfont = pygame.font.Font("Quinquefive.ttf", 20)

        # initializing all the required buttons as button objects
        self.start = button("START",size=20, fg=BLACK)
        self.help = button("HELP",size=20, fg=BLACK)
        self.scores = button("HIGH SCORES",size=20, fg=BLACK)
        self.options = button("OPTIONS",size=20, fg=BLACK)
        self.quit = button("QUIT",size=20, fg=BLACK)

        # logo image loaded *just once*
        self.logo = pygame.image.load("images/logo.png")

    def __repr__(self):
        return "Main Menu"

    def update_game(self):
        # live bg
        self.window.blit(self.bg, (0,(-30+self.road_pos%30)))
        self.road_pos += 10

        # temp surface that'll hold all the menu content, to be copied to main window later
        game_menu = pygame.Surface((300,520),pygame.SRCALPHA)
        game_menu.fill((255,255,255,100))
        
        # adding the logo to temp screen
        game_menu.blit(self.logo,((game_menu.get_width()-self.logo.get_width())//2 ,65))

        # adding all the buttons to temp screen
        self.start.paint(game_menu,150,250)
        self.help.paint(game_menu,150,300)
        self.options.paint(game_menu,150,350)
        self.scores.paint(game_menu,150,400)
        self.quit.paint(game_menu,150,450)

        # copying temp screen to main window
        self.window.blit(game_menu,(0,0))

        # Processing the event queue
        for event in pygame.event.get():
            # Quit on clicking close button
            if event.type == QUIT:
                pygame.quit()
                return
            # processing mouse clicks
            if event.type == MOUSEBUTTONDOWN:
                # setting states based on where the clicks are registered
                # 1 = playing state, 2 = help menu state, 3 = highscores state, 
                # 4 = quit state, 5 = options state, 0 = stay right here!
                if pygame.Rect(self.start.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.current = 1
                elif pygame.Rect(self.help.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.current = 2
                elif pygame.Rect(self.scores.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.current = 3
                elif pygame.Rect(self.quit.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.current = 4
                elif pygame.Rect(self.options.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.current = 5
                else:
                    self.current = 0

            # processing mouse movement
            if event.type == MOUSEMOTION:
                # tracking mouse hover over the buttons, if detected, highlighting the buttons with a white bg
                # could be made more responsive by fore setting all the other buttons' bg's to None in each branch
                if pygame.Rect(self.start.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.start.bg = WHITE

                elif pygame.Rect(self.help.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.help.bg = WHITE

                elif pygame.Rect(self.scores.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.scores.bg = WHITE

                elif pygame.Rect(self.options.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.options.bg = WHITE

                elif pygame.Rect(self.quit.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.quit.bg = WHITE

                # resetting the white bg if hover isn't on any of the buttons
                else:
                    self.start.bg = None
                    self.help.bg = None
                    self.scores.bg = None
                    self.options.bg = None
                    self.quit.bg = None
        
        # Flip the display
        pygame.display.flip()
        pygame.time.wait(50)