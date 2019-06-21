from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (480,400)
    dinasaur = (246, 371)
def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')

def imageGrab(): 
    box = (Cordinates.dinasaur[0]+60, Cordinates.dinasaur[1], Cordinates.dinasaur[0]+100, Cordinates.dinasaur[1]+30) 
    image = ImageGrab.grab(box) 
    grayImage = ImageOps.grayscale(image) 
    a = array(grayImage.getcolors()) 
    print(a.sum()) 
    return(a.sum())


def basla():
    restartGame()
    while True:
        if(imageGrab()!= 1447):
            pressSpace()
            time.sleep(0.2)

basla()