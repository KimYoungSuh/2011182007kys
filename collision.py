from pico2d import *

import game_framework
import title_state

from Witch import Witch # import Boy class from boy.py
from BG import Grass
from FireBall import FireBall1
from FireBall import FireBall2


name = "collision"

witch = None
FB1 = None
FB2 = None
FB3 = None
grass = None
balls = None
Fireballnum = 1
def create_world():
    global witch, grass, FB1, FB2, FB3
    witch = Witch()
    FB1 = [FireBall1() for i in range(Fireballnum)]
    FB2 = [FireBall2() for i in range(Fireballnum)]
    FB3 = FB1 + FB2
    grass = Grass()


def destroy_world():
    global witch, grass, FB1, FB2 , FB3

    del(witch)
    del(FB3)
    del(grass)
    del(FB2)



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


def update(frame_time):
    global Fireballnum
    witch.update(frame_time)
    for ball in FB3:
        ball.updata(frame_time)

    for ball in FB3 :
        if collide(witch, ball):
            FB3.remove(ball)
            witch.HP()



def draw(frame_time):
    clear_canvas()
    grass.draw()
    witch.draw()
    for ball in FB3:
        ball.draw()
 #   grass.draw_bb()
    witch.draw_bb()
    for ball in FB3 :
        ball.draw_bb()

    update_canvas()






