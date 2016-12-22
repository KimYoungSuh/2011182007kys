from pico2d import *
import random
import game_framework
import title_state
import Game_over
import char_sellect
import WITCH
from WITCH import Witch # import Boy class from boy.py
from WITCH import Witch_R
from WITCH import Witch_B
from BG import Grass
from FireBall import FireBall1
from FireBall import FireBall2
from FireBall import FireBall3
from FireBall import FireBall4
from WAND import Wand
from item import Coin
from item import Potion

name = "collision"
wand = None
FB1 = []
FB2 = []
FB3 = []
FB4 = []
FB5 = []
grass = None
balls = None
font = None
item = []
potion = []
Time = 0.0
GameScore = 0

bgm = None
class Timer:
    def __init__(self):
        self.Whattime = 0
        self.itemtime = 0
        self.potintime =0
        self.Scoretime = 0
    def update(self, frame_time):
        self.Whattime +=  frame_time
        self.itemtime += frame_time
        self.Scoretime += frame_time
        self.potintime += frame_time
        self.add()
    def add(self):
        if self.Whattime >= 1.3:
            new_fireball1 = FireBall1()
            FB5.append(new_fireball1)
            new_fireball2 = FireBall2()
            FB5.append(new_fireball2)
            new_fireball3 = FireBall3()
            FB5.append(new_fireball3)
            new_fireball4 = FireBall4()
            FB5.append(new_fireball4)
            self.Whattime = 0
        if self.potintime >= 3.3 :
            new_potion = Potion()
            potion.append(new_potion)
            self.potintime =0
        if self.itemtime >= 2:
            new_item = Coin()
            item.append(new_item)
            self.itemtime = 0

def create_world():
    global witch, grass, FB1, FB2, FB3 ,wand ,FB4, Fireballnum, timer, FB5,GameScore, bgm, select_witch, font
    timer = Timer()
    wand = Wand()
    GameScore =0
    font = load_font('ENCR10B.TTF')
    if char_sellect.select_witch == 1 :
        witch = Witch_R()
        bgm = load_music('FL_BGM_C.mp3')
        bgm.set_volume(64)
        bgm.repeat_play()
    elif char_sellect.select_witch == 2 :
        witch = Witch_B()
        bgm = load_music('FL_BGM_D.mp3')
        bgm.set_volume(64)
        bgm.repeat_play()
    elif char_sellect.select_witch == 3 :
        witch = Witch()
        bgm = load_music('FL_BGM_E.mp3')
        bgm.set_volume(64)
        bgm.repeat_play()
    FB1 = []
    FB2 = []
    FB3 = []
    FB4 = []
    FB5 = []
    grass = Grass()


def destroy_world():
    global witch, grass, FB5  , timer, bgm
    del(witch)
    del(FB5)
    del(grass)
    del(bgm)



def enter():

    game_framework.reset_time()
    create_world()



def exit():
    destroy_world()


def pause():
    pass


def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                witch.handle_event(event)




def collide(a, b):
    left_a, bottom_a,right_a, top_a = a.get_bb()
    left_b, bottom_b,right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True
def get_time(frame_time):
    global Time, Fireballnum

    Time += frame_time
    return Time

def update(frame_time):
    for Score in item :
        Score.update(frame_time)
    for Score in potion:
        Score.update(frame_time)


    for ball in FB5:
        ball.update(frame_time)

    for ball in FB5 :
        if collide(ball, witch):
            FB5.remove(ball)
            witch.HP()

    for Score in item:
        if collide(Score, witch):
            item.remove(Score)
            witch.eat(Score)
    for Score in potion:
        if collide(Score, witch):
            potion.remove(Score)
            witch.eat_p(Score)

    witch.update(frame_time)
    timer.update(frame_time)




def draw(frame_time):
    clear_canvas()
    grass.draw()
    witch.draw()
    font.draw(620,580,'life = %d' %(witch.life))
    font.draw(620,560, 'Score = %d'%(witch.Score))

    for Score in item :
        Score.draw()

    for Score in potion :
        Score.draw()
    for ball in FB5:
        ball.draw()

 #   grass.draw_bb()
    witch.draw_bb()
    for ball in FB5 :
        ball.draw_bb()

    update_canvas()


