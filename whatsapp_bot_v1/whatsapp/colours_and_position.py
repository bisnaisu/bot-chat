import pyautogui as pt
from time import sleep

while True:
    posXY = pt.position()
    print(posXY)
    sleep(0.4)
    if(posXY[0] == 0):
        break