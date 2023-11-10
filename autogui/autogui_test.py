import pyautogui

# Show the current position of the mouse pointer
position = pyautogui.position()
print(position)

# Show the size of the screen (screen resolution)
size_of_screen = pyautogui.size()
print(size_of_screen)

# Check if coordinates are on the screen
x = 400
y = 500
XY_coordinates_on_screen = pyautogui.onScreen(x, y)
print(XY_coordinates_on_screen)

# Pause 2.5 seconds
pyautogui.PAUSE = 0.5

# move mouse to XY coordinates over num_second seconds
pyautogui.moveTo(x, y, duration = 1)

# move mouse relative to its current position
x_change = 100
y_change = 150
pyautogui.moveRel(x_change, y_change, duration = 1)

# Click!
# pyautogui.click( x = x, y = y, clicks = number_of_clicks, interval = time_between-clicks, button = 'left')
pyautogui.click()

# Holding a Click
pyautogui.mouseDown(x = x, y = y, button='left')
pyautogui.mouseUp(x = x, y = y, button='left')

# Scrolling
amount_to_scroll = 1
pyautogui.scroll(amount_to_scroll, x = x, y = y)

pyautogui.keyDown('shift')