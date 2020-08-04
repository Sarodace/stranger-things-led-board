## LIBRARIES
import board
import neopixel
import random
import sys
from time import sleep


## VARIABLES
# LED colors
BLANK = (0, 0, 0)
RED = (0, 255, 0)
YELLOW = (150, 255, 0)
CYAN = (255, 0, 255)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (0, 180, 255)
PINK = (0, 255, 200)

# Alphabetical characters and their respective LEDs
alphabet = (["A",0],
["B",1],
["C",2],
["D",3],
["E",4],
["F",5],
["G",6],
["H",7],
["I",18],
["J",17],
["K",16],
["L",15],
["M",14],
["N",13],
["O",12],
["P",11],
["Q",10],
["R",21],
["S",22],
["T",23],
["U",24],
["V",25],
["W",26],
["X",27],
["Y",28],
["Z",29] )

# Define LEDs that will be used
pixels = neopixel.NeoPixel(board.D21, 30, brightness = 0.1, auto_write=True)


## FUNCTIONS 
# Set all LEDs to off
def clearLEDs():
	pixels.fill(BLANK)

# Return appropriate color for given LED
def getLEDColor(index):
    if index in {0,7,16,25}:
        return RED
    if index in {1,10,17,26}:
        return PURPLE
    if index in {2,11,18,27}:
        return CYAN
    if index in {3,12,21,28}:
        return PINK
    if index in {4,13,22,29}:
        return BLUE
    if index in {5,14,23}:
        return YELLOW
    if index in {6,15,24}:
        return GREEN
    else:
        return BLANK

# Fill in LEDs, starting from A to Z
def displayChristmasLEDs():
    for i in range(len(pixels)):
        pixels[i] = getLEDColor(i)
        sleep(0.1)

# Fill in LED with appropriate color
def lightLED(index):
    pixels[index] = getLEDColor(index)

# Seperate message into underlying characters and display them
def deconstruct_message(message):
    for char in message:
        if char.isalpha(): # this if statement should probably be removed
            for item in alphabet:
                if char in item[0]:
                    clearLEDs()
                    print(char + " " +  str(item[1]))
                    lightLED(item[1])
                    sleep(0.75)
    clearLEDs()


## FLICKERING ANIMATIONS
# The following functions willl be used to alert the user of a received message by flickering the LEDs
def firstFlicker(selectedLED):
    for i in range(0, 2):
        pixels[selectedLED] = BLANK
        sleep(0.1)
        lightLED(selectedLED)
        sleep(0.1)
        pixels[selectedLED] = BLANK
        sleep(0.1)
        lightLED(selectedLED)
        sleep(0.15)
        pixels[selectedLED] = BLANK
        sleep(0.1)
        lightLED(selectedLED)
        sleep(0.12)
        pixels[selectedLED] = BLANK
        sleep(0.1)
        lightLED(selectedLED)
        sleep(0.4)

    pixels[selectedLED] = BLANK

def secondFlicker(selectedLED):
    for i in range(0, 3):
        pixels[selectedLED - 1] = BLANK
        sleep(0.1)
        lightLED(selectedLED - 1)
        sleep(0.1)
        pixels[selectedLED] = BLANK
        sleep(0.1)
        lightLED(selectedLED)
        sleep(0.1)

    pixels[selectedLED] = BLANK
    pixels[selectedLED - 1] = BLANK

def thirdFlicker(selectedLED):
    for i in range(0, 10):
        pixels[selectedLED - 1] = BLANK
        sleep(1.01 - 0.1 * i)
        lightLED(selectedLED - 1)
        sleep(1.01 - 0.1 * i)


clearLEDs()

# This'll change a bunch as I'm playing around with the flickering animations
if __name__ == "__main__":
    # TODO: RANDOMLY PICK FROM MANY FLICKER FUNCTIONS

    while True:
        firstFlicker(16)
        secondFlicker(16)
        thirdFlicker(16)
        print("loop done!")
        sleep(2)