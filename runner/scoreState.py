import pygame

# importing required mouse and event constants
from pygame.locals import (
    MOUSEBUTTONDOWN,
    QUIT,
)

class scoreState:
    def __init__(self, window, current = 0 ):
        # parent window passed from main script
        self.window = window

        # flags required to go back to menu
        self.go_back = 0

        # variables required for live background
        self.road_pos = 10
        self.bg = pygame.image.load("images/road_bg.png")

        # initializing required font, * just once *
        self.myfont = pygame.font.Font("Quinquefive.ttf", 20)

    def __repr__(self):
        return "High Scores"

    def update_game(self):
        # live bg
        self.window.blit(self.bg, (0,(-30+self.road_pos%20)))
        self.road_pos += 10

        # creating temporary screen with high scores to be updated onto main
        game_menu = pygame.Surface((300,520),pygame.SRCALPHA)
        game_menu.fill((255,255,255,100))

        # adding title to screen
        title = self.myfont.render(f"HIGH SCORES",1,(255,0,0),None)
        coords = [150 - title.get_width()//2, 30]
        game_menu.blit(title, coords)

        # fetching highscores as a list sorted on scores
        with open("scores.dat","r") as file:
             scores = file.readlines()[1:]
             scores.sort(key=lambda s: int(s.split()[1]),reverse=True)
        lh = 35

        # rendering top 10 scores one by one
        for i in range(len(scores[:10])):
            score = self.myfont.render(f"{scores[i][:-1]}",1,(255,0,0),None)
            coords = [150 - score.get_width()//2, (100+lh*i)]
            game_menu.blit(score, coords)
        
        # moving temp screen to main
        self.window.blit(game_menu,(0,0))

        # Processing the event queue
        for event in pygame.event.get():
            # Quit on clicking close button
            if event.type == QUIT:
                pygame.quit()
                
            # go back to main menu if clicked anywhere
            if event.type == MOUSEBUTTONDOWN:
                    self.go_back= 1
        
        # Flip the display
        pygame.display.flip()
        pygame.time.wait(100)