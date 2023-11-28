# required to generate random ID of the object in order to distinguish it from others
from random import randint

class buff:
    def __init__(self, location):
        # randomized ID, very less likely to be the same for two consecutive buffs
        self.id = randint(0,9999)

        # position on screen, assigned by generator function in game loop
        self.coords = location

        # can be extended later to other sprites
        self.sprites = ["images/sprites/buff1.png"]

        # setting active sprite
        self.sprite = self.sprites[0]

    def __repr__(self):
        return str(self.coords)

    def step(self):
        # moving sprite down by one distance unit to simulate player moving forward
        self.coords[1] += 50