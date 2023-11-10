import pyautogui
import time

position = pyautogui.position()
print(position)

def open_paint():
    pyautogui.click(x = 229, y = 1051)
    pyautogui.typewrite(['p','a','i','n','t', 'enter'], interval = 0.5)
    #enlarge()

def enlarge():
    enlarge = pyautogui.locateOnScreen('paint_enlarge.png')
    print(enlarge)
    if enlarge != None:
        pyautogui.center(enlarge)


def draw():
    pyautogui.moveTo(500,400)
    pyautogui.dragTo(500,500, duration = 1)

def tutorial():
    total_distance = 300
    distance_change = 10
    duration = 0.1
    while total_distance > 0:
        pyautogui.dragRel(total_distance, 0, duration = duration)   # move right
        total_distance -= distance_change
        pyautogui.dragRel(0, total_distance, duration = duration)   # move down
        pyautogui.dragRel(-total_distance, 0, duration = duration)  # move left
        total_distance -= distance_change
        pyautogui.dragRel(0, -total_distance, duration = duration)  # move up

def close():
    pyautogui.moveTo(x = 1880, y = 20, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(x = 1015, y = 525, duration = 1)
    pyautogui.click()

def run():
    open_paint()
    #draw()
    pyautogui.moveTo(250,250)
    tutorial()



run()
time.sleep(2)
close()
