import pyautogui

restart_button = pyautogui.locateCenterOnScreen("restart.bmp")
dino = pyautogui.locateCenterOnScreen("dino.png")
print(dino)
print(restart_button)

# pyautogui.click(475,196)
pyautogui.click(restart_button)

loc = (dino[0]+60,dino[1]+5)

pyautogui.moveTo(loc)
pyautogui.sleep(3)

while 1:

    if pyautogui.pixel(*loc) != (255,255,255):
        pyautogui.press("space")
    # print(pyautogui.pixel(*loc))




