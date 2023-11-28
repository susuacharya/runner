import pygame

# importing required pygame keyboard and event constants 
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

class pauseState:
    def __init__(self, window):
        # parent window passed down from the main script
        self.window = window

        # pause flag that is checked every tick/cycle, if false, resume gameplay
        self.pause = True
        # was getting scanned even for pause even though its only supposed to be in running. so permanently set it to false
        self.dead = False

    # return current state's name
    def __repr__(self):
        return "Paused State"
    

    def update_game(self):
        # very simple update to the main screen
        self.window.fill([0,0,0])
        self.pause = True
        
        # Processing the event queue
        for event in pygame.event.get():
            # Quit on clicking close button
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # if escape is pressed again, resume gameplay
                    self.pause = False

            if event.type == QUIT:
                pygame.quit()
                return
               
        # temp screen that'll hold things to be pased on the main window
        pause_screen = pygame.Surface((300,520))
        pause_screen.fill((255,255,255))

        # adding the text GAME PAUSED to the temp screen
        myfont = pygame.font.Font("Quinquefive.ttf", 20)
        label = myfont.render("GAME PAUSED",1,(0,0,0),(255,255,255))
        pause_screen.blit(label, (150 - label.get_width()//2, 240))

        # adding temp screen to main screen
        self.window.blit(pause_screen,(0,0))
        
        # Flip the display
        pygame.display.flip()
        pygame.time.wait(500)