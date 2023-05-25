import pyautogui as pag
import random
import time
import keyboard

global PAUSE
global Loop

PAUSE = False 
Loop = True
count = 0
pag.FAILSAFE = False

PauseMap = {True:'On',False:'Off'}

def get_random_coords():
    screen = pag.size()
    width = screen[0]
    height = screen[1]

    return [  
        random.randint(100,width-200),
        random.randint(100,height-200)
    ]

def press_pause():
    global PAUSE
    PAUSE = not PAUSE
    print(f"Pause {PauseMap.get(PAUSE)} !")

def press_exit():
    global Loop
    print('Exit jiggler !')
    Loop = False    

keyboard.add_hotkey('ctrl+alt+p', press_pause) #ctrl+alt+p 로 포즈 토글
keyboard.add_hotkey('ctrl+alt+z', press_exit)  #ctrl+alt+z 로 종료

while Loop:

    if PAUSE == True:
        #print("Pause 실행중..")
        continue

    time.sleep(0.1)
    count +=1

    #x = random.randint(900,950)
    #y = random.randint(400,450)
    if count == 100:
        #현재위치
        x = pag.position().x
        y = pag.position().y

        #coord = get_random_coords()
        #x = coord[0]
        #y = coord[1]
        #pag.moveTo(x,y,0.2)

        #다이아몬드 
        x -= 15
        y += 15
        pag.moveTo(x,y,0.2)

        x += 15
        y += 15
        pag.moveTo(x,y,0.2)

        x += 15
        y -= 15
        pag.moveTo(x,y,0.2)

        x -= 15
        y -= 15
        pag.moveTo(x,y,0.2)

        #pag.click()
        pag.press('esc')
    
        count = 0

# 종료시 핫키 제거    
keyboard.remove_hotkey('ctrl+alt+p')
keyboard.remove_hotkey('ctrl+alt+z')
