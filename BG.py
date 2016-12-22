import random

from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('FL_BG.png')


    def draw(self):
        self.image.draw(400, 300)

