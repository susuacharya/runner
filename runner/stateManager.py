import pygame

# import all the defined game states
from menuState import menuState # main menu
from helpState import helpState # help menu
from scoreState import scoreState # high scores menu
from optionState import optionState # options menu
from gameState import gameState # gameplay 
from pauseState import pauseState # pause menu
from gameOverState import gameOverState # game over screen

class stateManager:
    def __init__(self, window):
        # master window object
        self.window = window

        # state constants required
        self.running = gameState(self.window)
        self.paused = pauseState(self.window)
        self.help = helpState(self.window)

        # current state of the game
        self.state = menuState(self.window)
        
    def set_state(self, state):
        # 0 = menu, 1 = running, 2 = paused, 3 = game over, 4 = help menu, 5 = high score menu, 6 = quit, 7 = options menu
        if state == 0:
            # only gets here upon fresh launch of game or after a run, hence all variables will have to be reset
            # best way to do that? create a new object
            self.state = menuState(self.window)
    
        elif state == 1:
            # if running set to false, state changes to game over
            self.state = self.running

        elif state == 2:
            # if pause is true, switch to a frozen pause state, variables aren't affected
            self.state = self.paused
        
        elif state == 3:
            # game over, so setting a new game over window with the score
            # and running state to a new game state, resetting all the variables
            self.state = gameOverState(self.window, self.running.score)
            self.running = gameState(self.window)
        
        elif state == 4:
            # setting current state to the help window
            self.state = self.help
            
        elif state == 5:
            # setting current state to a new score window to make sure changes to the leaderboard if any, are reflected
            self.state = scoreState(self.window)
        
        elif state == 7:
            # setting current state to a new options window to make sure any changes to the options are reflected
            self.state = optionState(self.window)
            
        elif state == 6:
            # end game, not loop, but exception handling takes care of the rest
            pygame.quit()
    
    # to fetch current state in order to check for the required variables in main
    def get_state(self):
        return str(self.state)