import pyautogui
import time

timer = 10

while timer > 0:
    pyautogui.PAUSE = 1
    position = pyautogui.position()
    print(position)
    time.sleep(2)
    timer += -1
