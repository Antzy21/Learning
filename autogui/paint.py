import pyautogui
import time
import pathlib

position = pyautogui.position()
print(position)

def open_paint():
    pyautogui.press("win")
    pyautogui.typewrite(['p','a','i','n','t', 'enter'], interval = 0.5)
    #enlarge()

def enlarge():
    square_location = pyautogui.locateOnScreen('small_square.png')
    print(square_location)
    if square_location != None:
        pyautogui.center(square_location)

def draw_line():
    pyautogui.moveTo(500,400)
    pyautogui.dragTo(500,500, duration = 1)

def draw_spiral():
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

def go_to_screen_centre():
    screensize = pyautogui.size()
    height = screensize.height/2
    width = screensize.width/2
    pyautogui.moveTo(width, height)

def close_and_save():
    # Close app
    pyautogui.keyDown("alt")
    pyautogui.press("f4")
    pyautogui.keyUp("alt")

    # Yes to save
    time.sleep(0.5)
    pyautogui.press("enter")

    # location
    time.sleep(0.5)
    new_file_name = f"{pathlib.Path().resolve()}\\my_spiral_drawing.png"
    pyautogui.write(new_file_name)
    
    # Yes to confirm save
    time.sleep(0.5)
    pyautogui.press("enter")

open_paint()
go_to_screen_centre()

time.sleep(2)

#draw_line()
draw_spiral()

time.sleep(2)
close_and_save()
