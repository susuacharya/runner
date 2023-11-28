# required to generate random ID of the object in order to distinguish it from others
from random import randint

class obstacle:
    def __init__(self, location):
        
        # randomized ID, *very* less likely to be the same for two consecutive cars
        # required in order to remove the car later on for memory cleanup
        self.id = randint(0,9999)
        
        # position on screen, assigned by generator function in game loop
        self.coords = location

        # list of sprites available, can be extended later
        self.sprites = ["images/sprites/car1.png","images/sprites/car2.png","images/sprites/car3.png","images/sprites/car4.png"]
        
        # selecting a random sprite for this particular object
        self.sprite = self.sprites[randint(0,3)]

    def __repr__(self):
        return str(self.coords)

    def step(self):
        # moving sprite down by one distance unit to simulate player moving forward
        self.coords[1] += 50