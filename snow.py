import time
import os
import random

clear = lambda: os.system('clear')

# Creates and returns a 2D array that represents the screen. Size is n rows by m columns
# filled with zeros
def buildScreen(n, m):
    res = []
    for x in range(n):
        col = []
        for y in range(m):
            col.append(0)
        res.append(col)
    return res

# Prints a given 2d array to the screen
# Expects the array to be filled with 0, 1, and 2
# Substitutes each 0, 1, and 2 with char0, char1, and char2 respectively
# Then prints those to the screen
def printScreen(screen, char0, char1, char2=None):
    for row in screen:
        for col in row:
            if col == 0:
                print(char0, end="")
            elif col == 1:
                print(char1, end="")
            else:
                print(char2, end=""),
        print("")


# Randomly places snow in the first row of the given 2D array
# with given frequency
def createSnow(screen, frequency):
    for pixel in range(len(screen[0])):
        r = random.random()*100
        if r <= frequency:
            screen[0][pixel] = 1

# Updates the snows position, but does not let the snow stack up
# on the bottom of the screen
def updateSnow(screen):
    # select each cell on the screen
    for x in range(len(screen)):
        # selects rows from the bottom up
        row = len(screen) - x - 1
        for y in range(len(screen[row])):
            # select cells from right to left
            col = len(screen[row]) - y - 1
            # check if there is snow in the current cell
            if screen[row][col] == 1:
                # empty the current cell
                screen[row][col] = 0
                # check if the next row is off of the screen
                if row < len(screen) - 1:
                    # fill the same cell in the next row
                    screen[row+1][col] = 1

# Updates the snows position, but the snow builds up
# on the bottom of the screen
def updateSnowStack(screen):
    # select each cell on the screen
    for x in range(len(screen)):
        # select rows from the bottom up
        row = len(screen) - x - 1
        for y in range(len(screen[row])):
            # select cells from right to left
            col = len(screen[row]) - y - 1
            # check if the current cell as snow
            if screen[row][col] == 1:
                # check if the next row is off of the screen
                if row < len(screen) - 1:
                    # if the cell below is empty, fall down
                    if screen[row+1][col] == 0:
                        screen[row+1][col] = 1
                        screen[row][col] = 0
                    # if the cell below is full, become solid and stay still
                    else:
                        screen[row][col] = 2
                        screen[row+1][col] = 2
                # if the next row would be off of the screen, become a solid block and stay still
                else:
                    screen[row][col] = 2

# creates an effect that looks like snow in an n x m screen,
# updates snow every 1/speed seconds
# creates snowflakes with a frequency of freq%
def snow(n, m, speed=4, freq=5):
    screen = buildScreen(n, m)
    while True:
        clear()
        printScreen(screen, " ", "*", u"\u2588")
        updateSnowStack(screen)
        createSnow(screen, freq)
        time.sleep(1 / speed)

# creates an effect that looks like rain in an n x m screen,
# updates rain every 1/speed seconds
# creates raindrops with a frequency of freq%
def rain(n, m, speed=20, freq=4):
    screen = buildScreen(n, m)
    while True:
        clear()
        printScreen(screen, " ", "|")
        updateSnow(screen)
        createSnow(screen, freq)
        time.sleep(1 / speed)


# allows the user to choose settings to run the app using
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
