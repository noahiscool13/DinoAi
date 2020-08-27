import pyautogui
import time
import PIL.ImageGrab as ImageGrab
from ctypes import *

GetForegroundWindow = windll.user32.GetForegroundWindow
GetWindowDC = windll.user32.GetWindowDC
GetPixel = windll.gdi32.GetPixel
ReleaseDC = windll.user32.ReleaseDC


restart_button = pyautogui.locateCenterOnScreen("restart.bmp")
pyautogui.click(restart_button)
pyautogui.sleep(1)

dino = pyautogui.locateCenterOnScreen("dino.png")

front_locs = [(dino[0]+75+i,dino[1]+15) for i in range(30)]


box_area1 = (dino[0]+85,dino[1]+10,dino[0]+200, dino[1]+100)

pyautogui.moveTo(front_locs[0])



while 1:
    time1 = time.time()
    box = ImageGrab.grab(box_area1)

    if any(box.getpixel((i*2,0))== (83,83,83) for i in range(1,5)):
        pyautogui.press("space")
        print("jump")
    # print(windll.gdi32.GetPixel(*front_locs[0]))



    # if any(pyautogui.pixel(*loc) == (83,83,83) for loc in front_locs):
    #     pyautogui.press("space")
    #     print("jump")

    time2 = time.time()
    print(1/(time2-time1))
    # print("!")


    # print(pyautogui.pixel(*loc))
    # print("!")

ReleaseDC(foreground_window, dc)



