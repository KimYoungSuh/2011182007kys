import game_framework
from pico2d import *


import collision
import char_sellect

name = "TitleState"
image = None
bgm = None
def enter():
    global image, bgm
    image = load_image('title.png')
    bgm = load_music('FL_BGM_A.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image, bgm
    del(image)
    del(bgm)

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
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(char_sellect)



def update(frame_time):
    pass


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()



