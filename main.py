import pydirectinput as pg
import keyboard
import pyautogui
import time as t
import PIL

#config
time = 1

def search():
    k1 = pyautogui.locateOnScreen("./img/q.png",region=(1548,502,56,51))
    if k1 == None:
        print('Could not locate the image Q')
        k2()
    else:
        pg.keyDown('q')
        pg.keyUp('q')
        print(f'pressing Q',{k1})
def k2():
    k2 = pyautogui.locateOnScreen("./img/w.png",region=(1546,493,64,56))
    if k2 == None:
        print('Could not locate the image W')
        k3()
    else:
        pg.keyDown('w')
        pg.keyUp('w')
        print(f'pressing W',{k2})
def k3():
    k3 = pyautogui.locateOnScreen("./img/s.png",region=(1549,498,53,50))
    if k3 == None:
        print('Could not locate the image S')
        k4()
    else:
        pg.keyDown('s')
        pg.keyUp('s')
        print(f'pressing S',{k3})

def k4():
    k4 = pyautogui.locateOnScreen("./img/rr2.png",region=(1549,498,53,50))
    if k4 == None:
        print('Could not locate the image R')
    else:
        pg.keyDown('r')
        pg.keyUp('r')
        print(f'pressing R',{k4})
        
start = input(str('Type Start : '))
i = 0
round = 999 + 1 
for i in range(1,round,1): 
    if start == 'start':
        print(f'starting Round {int(i)} / {round}')
        t.sleep(time)
        search()