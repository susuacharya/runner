# a modular button object that can be used to quickly create an render a piece of text on screen
# much more efficient than the standard import-define-create-paint-place life-cycle of text renders in pygame
import pygame

# initializing pygame font sub-package
pygame.font.init()


class button:
    def __init__(self, text="Test", size=15, fg=(0,0,0), bg=None):
        # text displayed on the button
        self.text = text
        # colors of the button
        self.fg = fg
        self.bg = bg
        # font file's path, can be customized as per user's liking
        self.font = "Quinquefive.ttf"

        # size of the button
        self.size = size

        # position of the button on screen
        self.x = 0
        self.y = 0

        # variable that holds the Surface object created by Font.render() 
        self.render = None

    # function to render the button on screen
    def paint(self, surface, left, top):
        # initializing font
        myfont =  pygame.font.Font(self.font, self.size)
        # creating the Surface
        temp = myfont.render(f"{self.text}",1,self.fg,self.bg)

        # calculating actual coordinates based on the central coordinates provided and the button dimensions
        self.y = left-temp.get_width()//2
        self.x = top-temp.get_height()

        # placing the button render on the provided screen
        self.render = temp
        surface.blit(temp, (self.y, self.x))

    # returns an object formatted as the pygame Rect object
    def get_rect(self):
        return [self.y, self.x, self.render.get_width(),self.render.get_height()]
    