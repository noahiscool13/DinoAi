import pyautogui
import time
import PIL.ImageGrab as ImageGrab

restart_button = pyautogui.locateCenterOnScreen("restart.bmp")
pyautogui.click(restart_button)
pyautogui.sleep(1)
dino = pyautogui.locateCenterOnScreen("dino.png")

front_locs = [(dino[0]+75+i,dino[1]+15) for i in range(30)]

box_area1 = (dino[0]+85,dino[1]+10,dino[0]+95, dino[1]+15)

pyautogui.moveTo(front_locs[0])



while 1:
    time1 = time.time()
    box = ImageGrab.grab(box_area1)

    if any(box.getpixel((i*2,2))== (83,83,83) for i in range(1,5)):
        pyautogui.press("space")
        print("jump")

    time2 = time.time()
    print(1/(time2-time1))

    # if any(pyautogui.pixel(*loc) == (83,83,83) for loc in front_locs):
    #     pyautogui.press("space")
    #     print("jump")
    # print(pyautogui.pixel(*loc))
    # print("!")




