import random
import json
import os
import collision

from pico2d import *
import game_framework
import title_state
import Game_over
#import char_sellect
from FireBall import FireBall1
from WORLD import world
#font = load_font('ENCR10B.TTF')
#font.draw(self.x - 30, self.y + 20, 'HP : %3.2f' % self.life)
choice_witch = None

def choice():
    choice_witch = Wand.choice_num



class Wand:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    UP_RUN, RIGHT_RUN, LEFT_RUN,  DOWN_RUN, STAY = 0,1,2,3, 4

    def __init__(self):
        self.x, self.y = 300, 240
        self.xdir = 0
        self.ydir = 0
        self.choice_num = 3


        if Wand.image == None:
            Wand.image = load_image('Magic wand.png')
    def update(self, frame_time):
        distance = Wand.RUN_SPEED_PPS * frame_time
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)
        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)
        if self.x > 160:
            if self.x < 260:
                if self.y > 310:
                    if self.y < 420:
                        print('Witch 1')
                        self.choice_num = 1
                       # print('Choice_num = %d'%(self.choice_num))
        if self.x > 360:
            if self.x < 460:
                if self.y > 310:
                    if self.y < 420:
                        print('Witch 2')
                        self.choice_num = 2
                       # print('Choice_num = %d' % (self.choice_num))
        if self.x > 560:
            if self.x < 660:
                if self.y > 310:
                    if self.y < 420:
                        print('Witch 3')
                        self.choice_num = 3
                       # print('Choice_num = %d' % (self.choice_num))
    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                self.xdir = -1
                self.ydir = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                self.xdir = +1
                self.ydir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                self.ydir = +1
                self.xdir = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                self.ydir = -1
                self.xdir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                self.xdir = 0
                self.ydir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                self.xdir = 0
                self.ydir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
                self.ydir = 0
                self.xdir = 0

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
                self.ydir = 0
                self.xdir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.x >160:
                if self.x <260:
                    if self.y > 310:
                        if self.y < 420:
                            self.choice_num =1
                            game_framework.change_state(collision)
            if self.x > 360:
                if self.x < 460:
                    if self.y > 310:
                        if self.y < 420:
                            self.choice_num = 2
                            game_framework.change_state(collision)
            if self.x > 560:
                if self.x < 660:
                    if self.y > 310:
                        if self.y < 420:
                            self.choice_num = 3
                            game_framework.change_state(collision)
