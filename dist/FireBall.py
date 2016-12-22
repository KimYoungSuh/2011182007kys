import random

from pico2d import *

FB1 = []
FBnum =1
class FireBall1:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = random.randint(10,30)  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3
    image = None

    def __init__(self):
        self.x, self.y = random.randint(5,30), random.randint(0, 600)
        self.frame = random.randint(0,2)
        self.speed = 0
        self.total_frames = 0.0
        self.check = True

        if FireBall1.image == None:
            FireBall1.image = load_image('FL_FB_ANIME.png')

    def update(self,frame_time):

        self.speed = FireBall1.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 3
        self.total_frames += FireBall1.FRAMES_PER_ACTION * FireBall1.ACTION_PER_TIME * frame_time
        self.x += self.speed
        if self.x > 800:
            self.x = 10
            self.y = random.randint(0,600)
    def draw(self):
        self.image.clip_draw(self.frame*78, 70, 78, 60, self.x, self.y)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-10 , self.y-10, self.x+10, self.y+10

class FireBall2:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = random.randint(10, 30)  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3
    def __init__(self):
        self.x, self.y = random.randint(0, 800) , random.randint(5,30)
        self.frame = random.randint(0,2)
        self.speed = 0
        self.total_frames = 0.0
        self.FBnum = 1

        if FireBall2.image == None:
            FireBall2.image = load_image('FL_FB_ANIME.png')
    def update(self,frame_time):

        self.speed = FireBall2.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 3
        self.total_frames += FireBall2.FRAMES_PER_ACTION * FireBall2.ACTION_PER_TIME * frame_time
        self.y +=  self.speed
        self.frame = (self.frame+1) %3

        if self.y > 700:
            self.y = 10
            self.x = random.randint(0,800)
        if self.y > 350 :
            self.FBnum +=1
    def draw(self):
        self.image.clip_draw(self.frame*78, 0, 78, 60, self.x, self.y)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-10 , self.y-10, self.x+10, self.y+10


class FireBall3:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = random.randint(10,30)  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3
    image = None

    def __init__(self):
        self.x, self.y = random.randint(790,800), random.randint(0, 600)
        self.frame = random.randint(0,2)
        self.speed = 0
        self.total_frames = 0.0
        if FireBall3.image == None:
            FireBall3.image = load_image('FL_FB_ANIME.png')

    def update(self,frame_time):
        self.speed = FireBall3.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 3
        self.total_frames += FireBall3.FRAMES_PER_ACTION * FireBall1.ACTION_PER_TIME * frame_time

        self.x -= self.speed
        if self.x < 0:
            self.x = 800
            self.y = random.randint(0,600)

    def draw(self):
        self.image.clip_draw(self.frame*78, 140, 78, 60, self.x, self.y)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-10 , self.y-10, self.x+10, self.y+10

class FireBall4:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = random.randint(10, 30)  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3
    def __init__(self):
        self.x, self.y = random.randint(0, 800) , random.randint(690,700)
        self.frame = random.randint(0,2)
        self.speed = 0
        self.total_frames = 0.0

        if FireBall4.image == None:
            FireBall4.image = load_image('FL_FB_ANIME.png')
    def update(self,frame_time):

        self.speed = FireBall4.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 3
        self.total_frames += FireBall4.FRAMES_PER_ACTION * FireBall4.ACTION_PER_TIME * frame_time

        self.y -=  self.speed
        self.frame = (self.frame+1) %3

        if self.y < 0:
            self.y = 700
            self.x = random.randint(0,800)

    def draw(self):
        self.image.clip_draw(self.frame*78, 210, 78, 60, self.x, self.y)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-10 , self.y-10, self.x+10, self.y+10


