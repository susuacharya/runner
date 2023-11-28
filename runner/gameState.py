import pygame
import random
from obstacle import obstacle
from player import player
from buff import buff

# importing required mouse and keyboard constants
from pygame.locals import (
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_w,
    K_a,
    K_d,
    KEYDOWN,
    QUIT,
)

class gameState:
    def __init__(self, window, delay = 100, difficulty = 0.5):
        # window created in master being passed down the chain
        self.window = window
        
        # controls the frame rate. DELAY = 100 means ~10 frames every second
        self.DELAY = delay

        # alters variables such as DELAY and odds of obstacle generation
        self.difficulty = difficulty
        
        # set up list of obstacle objects to monitor their life cycle
        self.obstacles = []

        # set up list of powerups to moitor their life cycle
        self.buffs = []

        # initializing player object
        self.P1 = player()

        # game running state
        self.running = True

        # game pause state
        self.pause = False

        # duration of immunity form buff 
        self.immune = 0

        # game over flag
        self.dead = False

        # current run score
        self.score = 0

        # variable to calculate the road's new position every frame
        self.road_pos = 10

        # road background loaded at the beginning
        self.bg = pygame.image.load("images/road_bg.png")

        # initialize player character
        # pygame.draw.circle(self.window, self.P1.color,self.P1.coords,50)
        self.window.blit(pygame.transform.scale(pygame.image.load(self.P1.sprite),(100,100)),self.P1.coords)

    def __repr__(self):
        return "Running State"

    # generic method to detect collision of any 2 objects
    def test_collision(self,a,b):
        # object hitbox set to 50px radius by default, to be tweaked incase of observed early or delayed collisions
        if a.coords[0] in range(b.coords[0]-50,b.coords[0]+50) and a.coords[1] in range(b.coords[1]-50, b.coords[1]+50):
            return True
        else:
            return False
    
    # generate buffs randomly and assign to buffs array
    def generate_buffs(self):
        if len(self.buffs) == 0 and self.immune <= 0:
            #temporary array that houses the buffs in all three lanes, will be pushed to master buffs
            generator = []

            # create an object in a lane based on the odds defined
            if not random.randint(0,100):
                generator.append(buff([25,0]))
            if not random.randint(0,100):
                generator.append(buff([125,0]))
            if not random.randint(0,100):
                generator.append(buff([225,0]))
            
            #check if object already exists at said location, if yes remove it
            for j in self.obstacles:
                for i in generator:
                    if self.test_collision(i,j):
                        generator.remove(i)

            # push temporary objects into the main array to be rendered 
            self.buffs += generator

    # create objects randomly and update the obstacle array
    def generate_obstacles(self):
        #temporary array that houses the obstacles in all three lanes, will be pushed to master obstacles
        generator = []
        
        # difficulty factor, factor = 1 indicates odds of 1 in 10
        factor = self.difficulty

        # create an object in a lane based on the odds defined
        if not random.randint(0,10//factor):
            generator.append(obstacle([10,0]))
        if not random.randint(0,10//factor):
            generator.append(obstacle([110,0]))
        if not random.randint(0,10//factor):
            generator.append(obstacle([210,0]))
        
        #check if object already exists at said location, if yes remove it
        for j in self.obstacles:
            for i in generator:
                if self.test_collision(i,j):
                    generator.remove(i)

        # push temporary objects into the main array to be rendered 
        self.obstacles += generator

    def update_game(self):
        # live background
        self.window.blit(self.bg, (0,(-30+self.road_pos%20)))
        self.road_pos += 10

        # updating fixed variables
        self.score +=1
        self.immune-=1

        # game pause flag
        self.pause = False
        
        # generating/rolling for required objects for this pass
        self.generate_obstacles()
        self.generate_buffs()

        # Processing the event queue
        for event in pygame.event.get():
            # Quit on clicking close button
            if event.type == QUIT:
                self.running = False
                pygame.quit()
                return

            # Test key down
            if event.type == KEYDOWN:

                # if esc then pause
                if event.key == K_ESCAPE:
                    self.running = False
                    self.pause = True

                # if up is present, change player state via jump
                elif event.key in (K_UP, K_w):
                    self.P1.jump()

                # move right
                elif event.key in (K_RIGHT, K_d):
                    if self.P1.coords[0] <= 180:
                        self.P1.move_right()

                # move left
                elif event.key in (K_LEFT, K_a):
                    if self.P1.coords[0] >= 50:
                        self.P1.move_left()

        # update obstacles based on a copy since realtime editing of array causes flickering
        for i in self.obstacles.copy():
            # loading a randomized sprite decided by the obstacle object onto the screen
            # scaling to ensure proper functioning incase of wrong dimensions of sprites
            self.window.blit(pygame.transform.scale(pygame.image.load(i.sprite),(80,100)),i.coords)
        
            # obstacle class method
            i.step()

            # obstacle clean up, for memory efficiency
            if i.coords[1] > 620:
                self.obstacles.remove(i)
        
        while len(self.obstacles) == 0: # in the rare case there are no objects being generated, try toggling off once
            self.generate_obstacles()

        # update buffs based on a copy as well
        for i in self.buffs.copy():
            # loading buff sprite via the obstacle object onto the screen
            # transform.scale to ensure proper functioning incase of wrong dimensions of sprites
            self.window.blit(pygame.transform.scale(pygame.image.load(i.sprite),(50,50)),i.coords)
        
            # buff class method
            i.step()

            # buff cleanup
            if i.coords[1] > 620:
                self.buffs.remove(i)

        # adding all visual updates onto screen
        self.window.blit(pygame.transform.scale(pygame.image.load(self.P1.sprite),(100,100)),self.P1.coords)
        
        # collision checks for all objects
        for i in self.buffs:
            # check player collision against buffs to set immunity
            if self.test_collision(self.P1, i): 
                # setting immunity duration to 100, which means it CANNOT BE STACKED
                self.immune = 100
                self.buffs.remove(i)

        for i in self.obstacles:
            # check player collision against every object and if he's currently jumping and the effect of immune buff
            if self.test_collision(self.P1, i) and self.P1.jump_timer == -1 and self.immune<=0: 
                self.running = False
                self.dead = True
            # check player collision while immune to destroy obstacle
            if self.test_collision(self.P1, i) and self.P1.jump_timer == -1 and self.immune>0:
                i.sprite = "images/sprites/boom.png"
                self.score+=200
        
        # updating player variables
        self.P1.step()

        # immunity indicator
        immunometer = pygame.transform.scale(pygame.image.load("images/sprites/armor.png","(50,50)"),[50,50])
        immunometer.set_alpha(200*self.immune//100)
        self.window.blit(immunometer,(250,20))
        
        # score bar to be rendered every frame on top of the rest of the screen
        top_bar = pygame.Surface((300,20))
        top_bar.fill((255,255,255))

        myfont = pygame.font.Font("Quinquefive.ttf", 15)
        label = myfont.render("Score: "+str(self.score),1,(0,0,0),(255,255,255))
        top_bar.blit(label, ((top_bar.get_width()-label.get_width())//2, 0))

        # adding score bar to main screen
        self.window.blit(top_bar,(0,0))
        
        # Flip the display
        pygame.display.flip()
        pygame.time.wait(self.DELAY)