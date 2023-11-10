import pyautogui
import time
import datetime

bank2coal = [(1860, 78), (1794, 50), (1794, 50), (1800, 50), (1842, 60), (1828, 57), (1838, 61), (1808, 95)]
bank2iron = [(1860, 78), (1794, 50), (1794, 50), (1800, 50), (1842, 60), (1828, 57), (1838, 61), (1535, 121)]
coal2bank = [(1786, 270), (1737, 252), (1769, 269), (1769, 269), (1778, 270), (1808, 271), (1774, 269), (1750, 219)]

inventory_spaces = []

east_coal_colour = (47, 47, 27)
east_coal_position = (1331, 604)
south_coal_colour = (37, 37, 22)
south_coal_position = (1054, 772)

def position_and_colour():
    x, y = pyautogui.position()
    print('position and colour results')
    print("( x , y )= (",x,",",y,")\n","'x':",x,", 'y':",y,", 'colour':",pyautogui.pixel(x, y),'\n')

def test_colour():
    c1 = (0,0)
    c2 = (0,0)
    colour = (0,0,0)

    x1, y1 = C1
    x2, y2 = C2
    tolerance = 0
    for x in range(x1,x2):
        for y in range(y1,y2):
            if pyautogui.pixelMatchesColor(x, y, colour, tolerance = tolerance) == False:
                print('tolerance + 1')
                tolerance += 1
    print(tolerance)

def detect_tolerance(timer = 10, initial_tolerance = 0):
    i_x, i_y = pyautogui.position()
    i_colour = pyautogui.pixel(i_x, i_y)
    print('initial colour is',i_colour,'\n')
    tol = initial_tolerance
    while timer > 0:
        time.sleep(2)
        x, y = pyautogui.position()
        colour = pyautogui.pixel(x, y)
        print('compare colour to',colour)
        match = pyautogui.pixelMatchesColor(y, x, colour, tolerance = tol)
        while match == False:
            tol += 1
            match = pyautogui.pixelMatchesColor(y, x, colour, tolerance = tol)
        print('\nnew tolerance is',tol)

def oriantate(zoom = 'in'):
    if zoom == 'in':
        z = 10000
    elif zoom == 'out':
        z = -10000
    pyautogui.click(x = 1679, y = 68, duration = 1)
    pyautogui.moveTo(500,500)
    time.sleep(0.5)
    pyautogui.scroll(z,500,500)
    time.sleep(0.2)
    pyautogui.scroll(2*z,500,500)

def move_place(coordinates):
    oriantate()
    # Activate running
    #pyautogui.click(x = 1697, y = 250, wait = 0)
    print('\nMoving place')
    for xy in coordinates:
        x, y = xy
        pyautogui.click(x, y, duration = 1)
        time.sleep(17)
    # Dectivate running
    #pyautogui.click(x = 1697, y = 250, duration = 1)

def deposit():
    oriantate()
    print('depositing')
    pyautogui.click(x = 717, y = 515, duration = 1)
    if pyautogui.pixelMatchesColor(503, 208, (255, 0, 0)) == True:
        print('bank is locked')
        quit()
    else:
        pyautogui.click(x = 1049, y = 744, duration = 1)

def mine_rock(mine):
    try:
        pyautogui.click(x = mine['x'], y = mine['y'], duration = 0.5)
        mined = False

        # Move mouse away
        pyautogui.moveTo(x = 1000, y = 500, duration = 0.5)

        while mined == False:
            if pyautogui.pixelMatchesColor(mine['x'], mine['y'], mine['colour']) == False:
                mined = True
                print('Rock now empty')
    except:
        print('could not locate minable rock')

def locate_mines():
    located_mines = False
    located_south = False
    located_east = False
    while located_mines == False:
        if located_south == False:
            try:
                south_x , south_y = pyautogui.locateCenterOnScreen('south_coal_full.png')
                print('Found full south coal. Its location is: (',south_x,',',south_y,')')
                south = {'x': south_x , 'y': south_y , 'colour': (37, 37, 22)}
                located_south = True
            except:
                try:
                    south_x , south_y = pyautogui.locateCenterOnScreen('south_coal_empty.png')
                    south = {'x': south_x , 'y': south_y , 'colour': (37, 37, 22)}
                    located_south = True
                    print('Found empty south coal. Its location is: (',south_x,',',south_y,')')
                except:
                    print('error finding south rock')
                    quit()
        if located_east == False:
            try:
                east_x , east_y = pyautogui.locateCenterOnScreen('east_coal_full.png')
                print('Found full east coal. Its location is: (',east_x,',',east_y,')')
                east  = {'x': east_x , 'y': east_y , 'colour': (47, 47, 27)}
                located_east = True
            except:
                try:
                    print(pyautogui.locateCenterOnScreen('east_coal_empty.png'))
                    east_x , east_y = pyautogui.locateCenterOnScreen('east_coal_empty.png')
                    east = {'x': east_x , 'y': east_y , 'colour': (37, 37, 22)}
                    located_east = True
                    print('Found empty east coal. Its location is: (',east_x,',',east_y,')')
                except:
                    print('error finding east rock')
                    quit()
        #print('Located east:',located_east,'. Located south:', located_south)
        if located_east == True and located_south == True:
            located_mines = True
    return south, east

def check_if_full(message = 'Inventory is full', negative_message = '', tol = 5):
    empty_colour = (62, 53, 41)
    empty_x, empty_y = (1830, 930)
    coal_x, coal_y = (1830, 930)
    coal_colour = (12, 12, 8)
    if pyautogui.pixelMatchesColor(empty_x, empty_y, empty_colour, tolerance = tol) == True:
        if negative_message != '':
            print(negative_message)
        answer = False
    elif pyautogui.pixelMatchesColor(coal_x, coal_y, coal_colour, tolerance = tol) == True:
        print(message,'with coal\n')
        answer = True
    else:
        print('detected something else\n')
        answer = False
    return answer

def fill_inventory():
    oriantate()
    start_time = time.time()
    south, east = locate_mines()
    start_waiting = time.time()
    rock_mined_number = 0

    double_check = False
    while double_check == False:
        inventory_full = False
        while inventory_full == False:
            if pyautogui.pixelMatchesColor(south['x'], south['y'], south['colour'], tolerance = 5) == True:
                inventory_full = check_if_full()
                if inventory_full == False:
                    rock_mined_number += 1
                    print('Waited:',round(time.time() - start_waiting, 2),'before beginning to mine south rock. Number',rock_mined_number)
                    mine_rock(south)
                    start_waiting = time.time()
                    inventory_full = check_if_full()
            elif pyautogui.pixelMatchesColor( east['x'],  east['y'],  east['colour'], tolerance = 5) == True:
                inventory_full = check_if_full()
                if inventory_full == False:
                    rock_mined_number += 1
                    print('waited:',round(time.time() - start_waiting, 2),'before beginning to mine east rock. Number',rock_mined_number)
                    mine_rock(east)
                    start_waiting = time.time()
                    inventory_full = check_if_full()
            elif (time.time() - start_waiting) > 60:
                print('time out, restart fill_inventory')
                pyautogui.click(656, 644, 2)
                time.sleep(1)
                pyautogui.click(1218, 648, 2)
                fill_inventory()
            else:
                time.sleep(1)
        time.sleep(2)
        double_check = check_if_full('double check confirmed', 'second run through does not confirm\n', tol = 40)

def cycle(total_cycles = 1):
    cycles = 1
    if pyautogui.locateCenterOnScreen('south_coal_full.png') == None:
        print('cant find a full south coal')
        if pyautogui.locateCenterOnScreen('south_coal_empty.png') == None:
            print('cant find an empty south coal either')
            move_place(bank2coal)
    while cycles <= total_cycles:

        print('cycle number:', cycles)
        print('start time of cyle:',datetime.datetime.now(),'\n')
        fill_inventory()
        move_place(coal2bank)
        deposit()
        move_place(bank2coal)
        cycles += 1

def find_mine():
    timer = 10
    while timer > 0:
        print(pyautogui.locateCenterOnScreen('coal_on_map.png'))
        time.sleep(2)
        timer += -1


#pyautogui.moveTo((1830,930))
#position_and_colour()
#check_if_full()
cycle(5)
#detect_tolerance()
#find_mine()
