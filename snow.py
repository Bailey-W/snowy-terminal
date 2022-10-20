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

def printScreen(screen, char1, char2, char3=None):
    for row in screen:
        for col in row:
            if col == 0:
                print(char1, end="")
            elif col == 1:
                print(char2, end="")
            else:
                print(char3, end=""),
        print("")

def createSnow(screen, percentage):
    for pixel in range(len(screen[0])):
        r = random.random()*100
        if r <= percentage:
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
                    else:
                        screen[row][col] = 2
                        screen[row+1][col] = 2
                else:
                    screen[row][col] = 2

def snow(n, m, speed=4, freq=5):
    screen = buildScreen(n, m)
    while True:
        clear()
        printScreen(screen, " ", "*", u"\u2588")
        updateSnowStack(screen)
        createSnow(screen, freq)
        time.sleep(1 / speed)


def rain(n, m, speed=20, freq=4):
    screen = buildScreen(n, m)
    while True:
        clear()
        printScreen(screen, " ", "|")
        updateSnow(screen)
        createSnow(screen, freq)
        time.sleep(1 / speed)


if __name__ == "__main__":
    print("Choose:\n  1. Snow\n  2. Rain")
    choice = int(input())
    print("Speed?: ")
    speed = float(input())
    print("Frequency?: ")
    freq = float(input())
    if choice == 1:
        snow(30, 100, speed, freq)
    else:
        rain(30, 100, speed, freq)
