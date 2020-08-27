import time
from ctypes import *
import pyautogui


# time.sleep(1)
restart_button = pyautogui.locateCenterOnScreen("restart.bmp")
pyautogui.click(restart_button)
pyautogui.sleep(1)
dino = pyautogui.locateCenterOnScreen("dino.png")
GetForegroundWindow = windll.user32.GetForegroundWindow
GetWindowDC = windll.user32.GetWindowDC
GetPixel = windll.gdi32.GetPixel
ReleaseDC = windll.user32.ReleaseDC
foreground_window = GetForegroundWindow()
dc = GetWindowDC(foreground_window)
rgb = GetPixel(dc, 100, 200)
# ReleaseDC(foreground_window, dc)

r = rgb & 0xff
g = (rgb >> 8) & 0xff
b = (rgb >> 16) & 0xff
print("RGB(%d, %d, %d)" % (r, g, b))

#5460819



locs = [(dino[0]+90,dino[1]+i) for i in range(20, -13, -3)]
# loc = (1,1)
windll.user32.SetCursorPos(*locs[-1])
cnt = 0
windll.user32.keybd_event(81, 0, 0, 0)
time1 = time.time()
while 1:
    # rgb2 = GetPixel(dc, *loc)
    time2 = time.time()
    cnt+=1
    if cnt % 5 == 0:
        windll.user32.keybd_event(81, 0, 0, 0)
    if cnt % 5 == 3:
        windll.user32.keybd_event(81, 0, 0o2, 0)
    if any(GetPixel(dc, *loc) in [5460819, 181305, 16632377] for loc in locs):
        # pyautogui.press("space")
        windll.user32.keybd_event(0x20, 0, 0, 0)
        pyautogui.sleep(0.1)
        windll.user32.keybd_event(0x20, 0, 0x0002, 0)
        if((time1 - time2) >= 90):
            pyautogui.sleep(0.3)
            windll.user32.keybd_event(40, 0, 0, 0)
            pyautogui.sleep(0.1)
            windll.user32.keybd_event(40, 0, 0b10, 0)
        # r = rgb2 & 0xff
        # g = (rgb2 >> 8) & 0xff
        # b = (rgb2 >> 16) & 0xff
        # print("RGB(%d, %d, %d)" % (r, g, b))

    # if GetPixel(dc, *dino) !=