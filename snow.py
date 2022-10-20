import time
import os
import random

clear = lambda: os.system('clear')

def buildScreen(n, m):
    res = []
    for x in range(n):
        col = []
        for y in range(m):
            col.append(0)
        res.append(col)
    return res

def printScreen(screen, char1, char2):
    for row in screen:
        for col in row:
            if col == 0:
                print(char1, end="")
            else:
                print(char2, end=""),
        print("")

def createSnow(screen):
    for pixel in range(len(screen[0])):
        r = random.randint(1, len(screen[0]))
        if r == 1:
            screen[0][pixel] = 1

def updateSnow(screen):
    for x in range(len(screen)):
        row = len(screen) - x - 1
        for y in range(len(screen[row])):
            col = len(screen[row]) - y - 1
            if screen[row][col] == 1:
                screen[row][col] = 0
                if row < len(screen) - 1:
                    screen[row+1][col] = 1

def updateSnowStack(screen):
    for x in range(len(screen)):
        row = len(screen) - x - 1
        for y in range(len(screen[row])):
            col = len(screen[row]) - y - 1
            if screen[row][col] == 1:
                if row < len(screen) - 1:
                    if screen[row+1][col] == 0:
                        screen[row+1][col] = 1
                        screen[row][col] = 0

def loop(screen):
    while True:
        clear()
        printScreen(screen, " ", "*")
        # screen = updateSnow(screen)
        updateSnowStack(screen)
        createSnow(screen)
        time.sleep(0.05)


snowScreen = buildScreen(20, 50)
loop(snowScreen)