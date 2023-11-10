import pyautogui as pyag
import time
import datetime
import math

screenshot = pyag.screenshot();
print(pyag.position())
try:
    print(screenshot.getpixel(pyag.position()));
except:
    print("Can't get pixel colour");

# Colours
blue1 = (25,188,222);
green2 = (126, 158, 46);
red3 = (227, 63, 127);
covered = (126, 212, 255);
blank = (253, 253, 253);

topLeftX, topLeftY = (594, 211);
bottomRightX, bottomRightY = (1319, 941);
boardLength = 9;

pyag.moveTo(topLeftX,topLeftY);
pyag.moveTo(bottomRightX,bottomRightY);

def distanceBetweenSquares(A,B,boardLength):
    distance = (A - B) / (boardLength-1);
    print("distance is:",distance,math.floor(distance));
    distance = math.floor(distance);
    return(distance);

distanceBetweenSquaresVertical = distanceBetweenSquares(bottomRightY, topLeftY, boardLength);
distanceBetweenSquaresHorizontal = distanceBetweenSquares(bottomRightX, topLeftX, boardLength);

position = [];
grid = [];

def stateCheck(j, i, attempt=0):
    rgb = screenshot.getpixel((j,i));
    if pyag.pixelMatchesColor(j,i, covered, tolerance = 5):
        #print("covered", rgb);
        return(9)
    elif pyag.pixelMatchesColor(j,i, blue1, tolerance = 10):
        #print("blue1", rgb);
        return(1)
    elif pyag.pixelMatchesColor(j,i, green2, tolerance = 20):
        #print("green2", rgb);
        return(2)
    elif pyag.pixelMatchesColor(j,i, red3, tolerance = 10):
        #print("red3", rgb);
        return(3)
    elif attempt < 5:
        return(stateCheck(j+2,i,attempt+1));
    else:
        #print("probably blank")
        return(0)
def checkboard():
    for n, i in enumerate(range(topLeftY, bottomRightY, distanceBetweenSquaresVertical)):
        position.append([]);
        grid.append([]);
        for m, j in enumerate(range(topLeftX, bottomRightX, distanceBetweenSquaresHorizontal)):
            position[n].append([j,i]);
            grid[n].append(stateCheck(j-4,i));
        print(grid[n])
    return(grid);
#grid = checkboard();

############################################################

grid = [[9, 9, 9, 9, 9, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 1, 1],
        [9, 9, 1, 0, 0, 1, 1, 2, 9],
        [9, 2, 1, 0, 0, 1, 9, 9, 9],
        [9, 2, 0, 0, 0, 1, 1, 1, 9],
        [9, 2, 0, 0, 0, 0, 0, 1, 9],
        [9, 2, 2, 1, 1, 0, 0, 1, 9],
        [9, 9, 9, 9, 2, 1, 0, 1, 1],
        [9, 9, 9, 9, 9, 1, 0, 0, 0]];

def printGrid(grid):
    print(" ")
    for n in range(0, boardLength):
        print(grid[n])
    print(" ")

printGrid(grid)

#############################################################

def inspectRow(y,x):
    if x == 0:
        row = ['x', grid[y][x], grid[y][x+1]];
    elif x == 8:
        row = [grid[y][x-1], grid[y][x], 'x'];
    else:
        row = [grid[y][x-1], grid[y][x], grid[y][x+1]];
    return(row);

def inspectSurroundings(y,x,g):
    surroundings = []
    if y == 0:
        if x == 0:
            return(['x','x','x','x',g[x,y],g[x+1,y],'x',g[x,y+1],g[x+1,y+1]])
        elif x == boardLength-1:
            return(['x','x','x',g[x-1,y],g[x,y],'x',g[x-1,y+1],g[x,y+1],'x'])
        else:
            return(['x','x','x',g[x-1,y],g[x,y],'x',g[x-1,y+1],g[x,y+1],'x'])
    elif y == boardLength-1:
        if x == 0:
            return(['x',g[x,y-1],g[x+1,y-1],'x',g[x,y],g[x+1,y],'x','x','x'])

        elif x == boardLength-1:
        return([g[x-1,y-1],g[x,y-1],'x',g[x-1,y],g[x,y],'x','x','x','x')


def Direction(v):
    if v == 0:
        i, j = -1, -1
    elif v == 1:
        i, j = -1, 0
    elif v == 2:
        i, j = -1, 1
    elif v == 3:
        i, j = 0, -1
    elif v == 4:
        i, j = 0, 0
    elif v == 5:
        i, j = 0, 1
    elif v == 6:
        i, j = 1, -1
    elif v == 7:
        i, j = 1,0
    elif v == 8:
        i, j = 1,1
    return(i,j)

def temp(surroundings):
    v = surroundings[4]

v=1;

for n in range(0, boardLength):
    for m in range(0, boardLength):
        if grid[n][m] == v:
            print('\n',n,", ",m)
            s = inspectSurroundings(n,m,grid);
            for r in s:
                print(r)
