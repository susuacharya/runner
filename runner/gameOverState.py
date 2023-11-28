import pygame

# importing required pygame keyboard, mouse and event constants
from pygame.locals import (
    K_ESCAPE,
    K_w,
    K_UP,
    KEYDOWN,
    MOUSEBUTTONUP,
    QUIT,
)

class gameOverState:
    def __init__(self, window, score=0):
        # parent window passed from the main script
        self.window = window

        # score to be shown, obtained from running state
        self.score = score

        # flags that decide next course of action
        self.replay = False
        self.menu = False

        # variables for the live background
        self.road_pos = 10
        self.bg = pygame.image.load("images/road_bg.png")
        self.myfont = pygame.font.Font("Quinquefive.ttf", 20)

        # updating score to the scores list
        with open("scores.dat","r") as file:
            name = file.readline()[:-1] # reading first line for the current player name
        with open("scores.dat", "a+") as file:
            file.write(f"{name} {self.score}\n") # writing player name with score to the end of the file

    def __repr__(self):
        return "Game Over"

    def update_game(self):
        # live bg
        self.window.blit(self.bg, (0,(-30+self.road_pos%20)))
        self.road_pos += 10
        
        # Processing the event queue
        for event in pygame.event.get():
            # Quit on clicking close button
            if event.type == QUIT:
                pygame.quit()

            # restart game on clicking escape
            if event.type == KEYDOWN:
                # if escape is hit, go back to main menu
                if event.key == K_ESCAPE:
                    self.menu = True

                # if jump key hit, restart a run
                if event.key in (K_w,K_UP):
                    self.replay = True
            
            # if mouse clicked, restart a run
            if event.type == MOUSEBUTTONUP:
                    self.replay = True # set this to relf.menu = True if you want mouse click to go to menu instead

        # temp surface with all the text to be displayed
        game_over = pygame.Surface((300,520), pygame.SRCALPHA) # making it SRCALPHA because the bg has to be translucent
        game_over.fill((255,255,255, 100))

        # gmae over text followed by score label followed by actual score
        label = self.myfont.render(f"GAME OVER",1,(15,15,200),None)
        game_over.blit(label, (150 - label.get_width()//2, (game_over.get_height()-(label.get_height()))//2-20))
        
        label = self.myfont.render(f"You Scored",1,(15,15,200),None)
        game_over.blit(label, (150 - label.get_width()//2, (game_over.get_height())//2))
        
        label = pygame.font.Font("Quinquefive.ttf", 30).render(f"{self.score}",1,(0,150,0),None)
        game_over.blit(label, (150 - label.get_width()//2, (game_over.get_height()+(label.get_height()))//2+20))
        
        # help text to navigate out of the screen
        label = pygame.font.Font("Quinquefive.ttf", 10).render("Press ESC to go to menu",1,(0,0,0),None)
        game_over.blit(label,(10,480))

        label = pygame.font.Font("Quinquefive.ttf", 10).render("MB-1 or up to restart run",1,(0,0,0),None)
        game_over.blit(label,(0,500))

        # copying temp surface to main window
        self.window.blit(game_over,(0,0))
        
        # Flip the display
        pygame.display.flip()
        pygame.time.wait(100)