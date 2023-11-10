import pyautogui as pyag
import time
import datetime
import math

# Colours
blue1 = (25,188,222);
green2 = (101,132,27);

topLeftY = 655;
topLeftX = 221;
bottomRightY = 221;
bottomRightX = 845;
boardLength = 9;

distanceBetweenSquares = math.floor((bottomRightX - topLeftX) / boardLength);
print("distanceBetweenSquares is:",distanceBetweenSquares)

print(pyag.locateCenterOnScreen("blank.png"))

for i in range(topLeftX, bottomRightX, distanceBetweenSquares):
    print(i);
    pyag.moveTo(topLeftY, i, 1);
