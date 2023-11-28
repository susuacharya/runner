# player class, initialized at the start of every run
class player:
    def __init__(self, coords=[150,470]):
        # initial coordinates of the player, middle lane, 0 - left lane, 200 - right lane
        self.coords = [100,430]
        
        # variable that tracks airtime
        self.jump_timer = -1

        # sprite variables required during run
        self.sprites = ["images/sprites/pleft.png", "images/sprites/pright.png"]
        self.jmp = "images/sprites/pjmp.png"

        # setting initial sprite
        self.sprite = self.sprites[1]

    def __repr__(self):
        return str(self.coords)
    
    # change lanes, move left
    def move_left(self):
        self.coords[0] -= 100

    # change lanes, move right
    def move_right(self):
        self.coords[0] += 100

    # one tick/game cycle, called at every iteration of the main loop
    def step(self):
        
        # checking if player is in the air, then set the correct sprite
        if self.jump_timer >= 0: #one extra step worth of air time
            self.sprite = self.jmp
            
            # reduce air time by one so player eventually lands
            self.jump_timer -= 1
        
        else:
            
            # if not airbound, then set sprite to one of the grounded ones
            if self.sprite == self.jmp:
                self.sprite = self.sprites[0]
            
            # toggle sprites between left and right
            # if current sprite is right, set it to left, otherwise right
            self.sprite = self.sprites[1] if self.sprite == self.sprites[0] else self.sprites[0]
    
    # add 3 to airtime, so player stays airbound for next 3 ticks
    def jump(self):
        self.jump_timer = 3
        