import pygame

# importing button class
from button import button

# importing required events and keyboard constants from pygame
from pygame.locals import (
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
    KEYDOWN,
    QUIT,
)

# color constants established
WHITE = (255,255,255)
BLACK = (0,0,0)

class optionState:
    def __init__(self, window):
        # window passed from the main script
        self.window = window

        # flag that'll be set to indicate return to main menu
        self.go_back = 0

        # variable required to generation live bg
        self.road_pos = 10

        # bg image loaoded once to prevent excessive memory uasge
        self.bg = pygame.image.load("images/road_bg.png")

        # different components of the options page
        self.title = button("OPTIONS",size=20,fg=BLACK)
        self.prompt = button("Set player name",size=15,fg=BLACK)
        self.save = button("SAVE",size=18,fg=BLACK)

        # fetching current player name
        with open("scores.dat","r") as file:
            self.inputtext = file.readline()[:-1]
        self.input = button(self.inputtext,size=18,bg=WHITE,fg=BLACK)
        
        # input field active status
        self.active = False
        
    def __repr__(self):
        return "Options"

    def update_game(self):
        # live background
        self.window.blit(self.bg, (0,(-30+self.road_pos%20)))
        self.road_pos += 10

        # have to create and render these labels every frame
        options_text = pygame.Surface((300,520),pygame.SRCALPHA)
        options_text.fill((255,255,255,100))

        # text field
        pygame.draw.rect(options_text, WHITE, pygame.Rect(75,225,150,30))

        # painting all components
        self.title.paint(options_text,150,100)
        self.prompt.paint(options_text,150,200)
        self.input.text=self.inputtext      # setting textfield value before setting
        self.input.paint(options_text,150,250)
        self.save.paint(options_text,150,300)
        
        self.window.blit(options_text,(0,0))

        # Processing the event queue
        for event in pygame.event.get():
            # Quit on clicking close button
            if event.type == QUIT:
                pygame.quit()

            # Mouse clicks
            if event.type == MOUSEBUTTONDOWN: 

                # checking clicks on input field
                if pygame.Rect(self.input.get_rect()).collidepoint(event.pos): 
                    self.active = True
                else: 
                    self.active = False

                # checking clicks on save button
                if pygame.Rect(self.save.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.save.bg = WHITE
                    if self.inputtext != "":
                        #write code to update current user in .dat
                        with open("scores.dat","a+") as file:
                            file.seek(0)
                            temp=file.readlines()
                            temp[0] = self.inputtext+"\n"
                            file.truncate(0)
                            file.writelines(temp)

                        self.go_back = 1

            # button highlight
            if event.type == MOUSEMOTION:
                if pygame.Rect(self.save.get_rect()).collidepoint(pygame.mouse.get_pos()):
                    self.save.bg = WHITE
                else:
                    self.save.bg = None

            # processing text inputs
            if event.type == KEYDOWN and self.active: 
                if event.key == pygame.K_BACKSPACE: 
                    self.inputtext = self.inputtext[:-1] 
                elif len(self.inputtext)<6: 
                    self.inputtext += event.unicode


        # Flip the display
        pygame.display.flip()
        pygame.time.wait(100)