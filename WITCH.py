import random
import json
import os

from pico2d import *
import game_framework
import title_state
import Game_over
from FireBall import FireBall1
from WORLD import world
#font = load_font('ENCR10B.TTF')
#font.draw(self.x - 30, self.y + 20, 'HP : %3.2f' % self.life)
Coin_Score = None
def Coin_S():
    Coin_Score = Witch.Score

class Witch:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 100

    image = None
    eat_sound = None
    UP_RUN, RIGHT_RUN, LEFT_RUN,  DOWN_RUN, STAY = 0,1,2,3, 4

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 1
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir =0
        self.state = self.STAY
        self.life = 30.0
        self.timer = 0
        self.Score = 0
        if Witch.image == None:
            Witch.image = load_image('FL_ANIME.png')
        if Witch.eat_sound == None :
            print("SOUND!")
            Witch.eat_sound = load_wav('FL_DROP.wav')
            Witch.eat_sound.set_volume(32)

    def eat(self, Score):
        self.eat_sound.play()
        self.Score += 100
    def eat_p(self,Score):
        self.eat_sound.play()
        self.life +=10

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))
        self.total_frames += Witch.FRAMES_PER_ACTION * Witch.ACTION_PER_TIME * frame_time
        distance = Witch.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame+1) %3
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)
        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)

    def print(self):
        print("Witch!")
    def HP(self):
        self.life -= 10.0
        if self.life <= 0  :
            game_framework.push_state(Game_over)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def draw(self):
        self.image.clip_draw(self.frame * 30, self.state * 32, 30, 32, self.x, self.y)
        #font.draw(self.x-30,self.y+20, 'HP : %3f' %self.life)
    def get_bb(self):
        return self.x-5, self.y-5, self.x+5, self.y+5

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_RUN, self.DOWN_RUN, self.STAY, self.UP_RUN):
                self.state = self.LEFT_RUN
                self.xdir = -1
                self.ydir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.LEFT_RUN, self.DOWN_RUN, self.STAY, self.UP_RUN):
                self.state = self.RIGHT_RUN
                self.xdir = +1
                self.ydir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RIGHT_RUN, self.DOWN_RUN, self.STAY, self.LEFT_RUN):
                self.state = self.UP_RUN
                self.ydir = +1
                self.xdir = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.RIGHT_RUN, self.UP_RUN, self.STAY, self.LEFT_RUN):
                self.state = self.DOWN_RUN
                self.ydir = -1
                self.xdir = 0




class Witch_B(Witch):
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 25.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    UP_RUN, RIGHT_RUN, LEFT_RUN, DOWN_RUN, STAY = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 1
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.state = self.STAY
        self.life = 50.0
        self.timer = 0.0
        self.Score = 0

        self.berrir = False
        if Witch_B.image == None:
            Witch_B.image = load_image('FL_WITCH_BLACK.png')
        if Witch.eat_sound == None :
            print("SOUND!")
            Witch.eat_sound = load_wav('FL_DROP.wav')
            Witch.eat_sound.set_volume(32)
    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))
        self.life_time += frame_time
        self.total_frames += Witch_B.FRAMES_PER_ACTION * Witch_B.ACTION_PER_TIME * frame_time
        distance = Witch_B.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame+1) %3
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)
        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)
        if self.life_time / 10 == 0 :
            world.make_item()
    def draw(self):
        self.image.clip_draw(self.frame * 30, self.state * 32, 30, 32, self.x, self.y)
        #font.draw(self.x-30,self.y+20, 'HP : %3f' %self.life)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-5, self.y-5, self.x+5, self.y+5
    def berrir_Action(self, frame_time):
        self.timer += frame_time
        if self.timer < 2.0 :
            return True

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_RUN, self.DOWN_RUN, self.STAY, self.UP_RUN):
                self.state = self.LEFT_RUN
                self.xdir = -1
                self.ydir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.LEFT_RUN, self.DOWN_RUN, self.STAY, self.UP_RUN):
                self.state = self.RIGHT_RUN
                self.xdir = +1
                self.ydir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RIGHT_RUN, self.DOWN_RUN, self.STAY, self.LEFT_RUN):
                self.state = self.UP_RUN
                self.ydir = +1
                self.xdir = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.RIGHT_RUN, self.UP_RUN, self.STAY, self.LEFT_RUN):
                self.state = self.DOWN_RUN
                self.ydir = -1
                self.xdir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):

                Witch.life = self.life



class Witch_R (Witch) :
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    UP_RUN, RIGHT_RUN, LEFT_RUN, DOWN_RUN, STAY = 0, 1, 2, 3, 4
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 1
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.state = self.STAY
        self.life = 40.0
        self.Score = 0

        if Witch.eat_sound == None :
            Witch.eat_sound = load_wav('FL_DROP.wav')
            Witch.eat_sound.set_volume(32)
        if Witch_R.image == None:
            Witch_R.image = load_image('FL_WITCH_RED.png')
    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))
        self.life_time += frame_time
        self.total_frames += Witch_R.FRAMES_PER_ACTION * Witch_R.ACTION_PER_TIME * frame_time
        distance = Witch_R.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame+1) %3
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)
        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)
        if self.life_time / 10 == 0 :
            world.make_item()
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def draw(self):
        self.image.clip_draw(self.frame * 30, self.state * 32, 30, 32, self.x, self.y)
        #font.draw(self.x-30,self.y+20, 'HP : %3f' %self.life)
    def get_bb(self):
        return self.x-5, self.y-5, self.x+5, self.y+5

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_RUN, self.DOWN_RUN, self.STAY, self.UP_RUN):
                self.state = self.LEFT_RUN
                self.xdir = -1
                self.ydir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.LEFT_RUN, self.DOWN_RUN, self.STAY, self.UP_RUN):
                self.state = self.RIGHT_RUN
                self.xdir = +1
                self.ydir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RIGHT_RUN, self.DOWN_RUN, self.STAY, self.LEFT_RUN):
                self.state = self.UP_RUN
                self.ydir = +1
                self.xdir = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.RIGHT_RUN, self.UP_RUN, self.STAY, self.LEFT_RUN):
                self.state = self.DOWN_RUN
                self.ydir = -1
                self.xdir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s): #blank
            if self.state == self.LEFT_RUN:
                if self.x >60 :
                    self.x -= 50
            elif self.state == self.RIGHT_RUN :
                if self.x < 740 :
                    self.x +=50
            elif self.state == self.DOWN_RUN :
                if self.y > 60 :
                    self.y -= 50
            elif self.state == self.UP_RUN :
                if self.y < 540 :
                    self.y += 50