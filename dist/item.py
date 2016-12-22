import random

from pico2d import *

FB1 = []
FBnum =1
class Coin:

    image = None

    def __init__(self):
        self.x, self.y = random.randint(50,700), random.randint(0, 600)
        self.frame = random.randint(0,5)
        if Coin.image == None:
            Coin.image = load_image('FL_COIN.png')

    def update(self,frame_time):

        self.frame = (self.frame + 1) % 5



    def draw(self):
        self.image.clip_draw(self.frame*24, 0, 24, 40, self.x, self.y)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-10 , self.y-10, self.x+10, self.y+10

class Potion :
    image = None

    def __init__(self):
        self.x, self.y = random.randint(50, 700), random.randint(0, 600)
        self.frame = random.randint(0, 5)
        if Potion.image == None:
            Potion.image = load_image('FL_potion.png')

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 5

    def draw(self):
        self.image.clip_draw(self.frame * 25, 0, 24, 30, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

