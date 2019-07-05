from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    replayBtn = (470, 370)
    dinosaur = (236, 375)
    #x coordinate 287
    #y 392
    #927 = wala
    #1010 = meron
def restartGame():
    pyautogui.click(Coordinates.replayBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')


def imageGrab():
    box = (Coordinates.dinosaur[0]+51, Coordinates.dinosaur[1], Coordinates.dinosaur[0]+91, Coordinates.dinosaur[1]+17)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())


def main():
    restartGame()
    while True:
        if imageGrab() != 927:
            pressSpace()
            time.sleep(0.5)

main()