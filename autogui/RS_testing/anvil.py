import pyautogui
import time

pause = 1
pyautogui.PAUSE = pause

def position_and_colour():
    x, y = pyautogui.position()
    print('position and colour results')
    print("( x , y )= (",x,",",y,")\n","'x':",x,", 'y':",y,", 'colour':",pyautogui.pixel(x, y),'\n')

def collect_from_bank(mouse_time = 0.5):
    print('collect from bank')
    pyautogui.PAUSE = 0

    # Get Hammer
    pyautogui.click(872 ,402, duration = mouse_time)
    # Right click on bars
    pyautogui.click(590,340, duration = mouse_time, button = 'right')
    # Get all bars
    pyautogui.click(580,500, duration = mouse_time)

    pyautogui.PAUSE = pause

def oriantate(zoom = 'in'):
    if zoom == 'in':
        z = 10000
    elif zoom == 'out':
        z = -10000
    pyautogui.click(x = 1679, y = 68, duration = 0.5)
    pyautogui.moveTo(500,500)
    time.sleep(0.5)
    pyautogui.scroll(z,500,500)
    time.sleep(0.2)
    pyautogui.scroll(2*z,500,500)

position_and_colour()

def cycle(total_cycles = 1):
    cycles = 1
    while cycles <= total_cycles:

        print('cycle number:', cycles)

        if cycles == 1:
            #oriantate()
            # Open bank
            pyautogui.click(916 ,684, duration = 0.5)

        collect_from_bank()
        # To Anvil
        pyautogui.click(1779 ,248, duration = 0.5)
        time.sleep(21-pause)
        # Click on Anvil
        pyautogui.click(902 ,856, duration = 0.5)
        # Click on thing to make
        pyautogui.click(683 ,326, duration = 0.5, button = 'right')
        # Click "make all"
        pyautogui.click(615 ,455, duration = 0.5)
        # Wait to make all items
        time.sleep(33-pause)
        # Back to bank
        pyautogui.click(1813 ,76, duration = 0.5)
        # Wait to move to bank
        time.sleep(21-pause)
        # Open bank
        pyautogui.click(916 ,684, duration = 1)
        # Deposit all in inventory
        pyautogui.click(x = 1049, y = 744, duration = 0.5)

        cycles += 1

time.sleep(1)
cycle()
