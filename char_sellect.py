import game_framework

from pico2d import *


import collision
from WAND import Wand # import Boy class from boy.py


name = "Char_sellect"
image = None
image_CharA = None
image_CharB = None
image_CharC = None
font = None
bgm2 = None
wand = None
sel = None
select_witch = None
def enter():
    global image, image_CharA,image_CharB,image_CharC,wand,font, bgm2, sel
    image = load_image('FL_BG.png')
    image_CharA = load_image('FL_WITCH_RED_CHAR.png')
    image_CharB = load_image('FL_WITCH_BLACK_CHAR.png')
    image_CharC = load_image('FL_ANIME_CHAR.png')
    font = load_font('ENCR10B.TTF')
    bgm2 = load_music('FL_BGM_A.mp3')
    bgm2.set_volume(64)
    bgm2.repeat_play()
    sel = Sellect()

    wand = Wand()


def exit():
    global image, image_CharA,image_CharB,image_CharC,wand,font, bgm2
    del(image)
    del(image_CharA)
    del (image_CharB)
    del (image_CharC)
    del (wand)
    del(font)
    del(bgm2)

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
                wand.handle_event(event)



def update(frame_time):
    global wand, sel, select_witch
    wand.update(frame_time)
    sel.update()
    select_witch = sel.Choice_num



def draw(frame_time):
    global image, image_CharA,image_CharB,image_CharC,wand
    clear_canvas()
    image.draw(400, 300)
    image_CharA.draw(200,400)
    font.draw(160,430,'WItch A') #RED
    font.draw(160, 370, 'HP : 30')
    font.draw(160,340, 'SPD : A')
    font.draw(160,310, 'Skill : Blank')

    image_CharB.draw(400,400)
    font.draw(360,430,'WItch B') #BLACK
    font.draw(360, 370, 'HP : 50')
    font.draw(360, 340, 'SPD : C')
    font.draw(360, 310, 'Skill : Shield')

    image_CharC.draw(600,400)
    font.draw(560,430,'WItch C') #BROWN
    font.draw(560, 370, 'HP : 80')
    font.draw(560, 340, 'SPD : B')
    font.draw(560, 310, 'Skill : heal')

    wand.draw();


    update_canvas()

class Sellect :
    def __init__(self):
        self.Choice_num = 0
    def update(self):
        self.Choice_num = wand.choice_num




