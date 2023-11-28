import pygame

# importing state manager
from stateManager import stateManager

pygame.init()

# Set up the drawing window in X, Y: 50 per square would be ideal
window = pygame.display.set_mode([300, 520])

# setting window properties
pygame.display.set_caption("Gorilla Run")

pygame.display.set_icon(pygame.image.load("images/ico.png"))

# initializing state object, will be reassigned based on user interaction after each loop 
game = stateManager(window)

# endless loop that'll render a frame every iteration
while True:
    # handling crashes, python just sticks to the ram like glue when this crashes, might as well force it to end
    try:
        # active state of the game
        where = game.get_state()

        # each state has return codes/flags that'll be set based on user interaction
        # next course of action is taken based on these values
        if where == "Main Menu":
            if game.state.current == 1:
                game.set_state(1)
            elif game.state.current == 2:
                game.set_state(4)
            elif game.state.current == 3:
                game.set_state(5)
            elif game.state.current == 4:
                game.set_state(6)
            elif game.state.current == 5:
                game.set_state(7)
        
        elif where == "Help":
            if game.state.go_back == 1:
                game.set_state(0)

        elif where == "High Scores":
            if game.state.go_back == 1:
                game.set_state(0)
        
        elif where == "Options":
            if game.state.go_back == 1:
                game.set_state(0)

        elif where == "Running State":
            if game.state.pause == True:
                game.set_state(2)
            
            if game.state.dead == True:     #TO DO gets evaluated in pause state, dunno why, temp fix is declaring a "dead" varible in pause, leaving it at false
                game.set_state(3)

        elif where == "Paused State":
            if game.state.pause == False:
                game.set_state(1)

        elif where == "Game Over":
            if game.state.replay == True:
                game.set_state(1)

            elif game.state.menu == True:
                game.set_state(0)

        else: 
            print("Unexpected state: Terminating game.")
            break
        # all state classes have the method update_game() defined
        game.state.update_game()
    except:
        # exiting the loop to terminate the game
        break

# Properly terminate the game and pygame instance
pygame.quit()
