import game_framework

from pico2d import *


import collision


name = "Char_sellect"
image = None
image_CharA = None
image_CharB = None
image_CharC = None
image_Wand = None
def enter():
    global image, image_CharA,image_CharB,image_CharC,image_Wand
    image = load_image('FL_BG.png')
    image_CharA = load_image('FL_WITCH_RED_CHAR.png')
    image_CharB = load_image('FL_WITCH_BLACK_CHAR.png')
    image_CharC = load_image('FL_ANIME_CHAR.png')
    image_Wand = load_image('Magic_wand.png')

def exit():
    global image, image_CharA,image_CharB,image_CharC,image_Wand
    del(image)
    del(image_CharA)
    del (image_CharB)
    del (image_CharC)
    del (image_Wand)

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
                game_framework.change_state(collision)



def update(frame_time):
    pass


def draw(frame_time):
    global image, image_CharA,image_CharB,image_CharC,image_Wand
    clear_canvas()
    image.draw(400, 300)
    image_CharA.draw(200,400)
    image_CharB.draw(400,400)
    image_CharC.draw(600,400)
    image_Wand.draw(200,340)


    update_canvas()



