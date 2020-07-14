# LIBRARIES
import board
import neopixel
import random
import sys
from time import sleep

# VARIABLES
# LED colors
BLANK = (0, 0, 0)
RED = (0, 255, 0)
YELLOW = (150, 255, 0)
CYAN = (255, 0, 255)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (0, 180, 255)
PINK = (0, 255, 200)

# Alphabet
## When I trim the LED strip, I'll handle this by subtracting 96 from it's ASCII.
alphabet = ( ["A",0],
["B",1],
["C",2],
["D",3],
["E",4],
["F",5],
["G",6],
["H",7],
["I",10],
["J",11],
["K",12],
["L",13],
["M",14],
["N",15],
["O",16],
["P",17],
["Q",18],
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

# Clear any LED colors
def clearLEDs():
	pixels.fill(BLANK)
	sleep(0.5)

# Fill LEDs with appropriate colors
def displayChristmasLEDS():
    for i in range(len(pixels)):
        if i in {0,7,16,25}:
            pixels[i] = RED
        if i in {1,10,17,26}:
            pixels[i] = PURPLE
        if i in {2,11,18,27}:
            pixels[i] = CYAN
        if i in {3,12,21,28}:
            pixels[i] = PINK
        if i in {4,13,22,29}:
            pixels[i] = BLUE
        if i in {5,14,23}:
            pixels[i] = YELLOW
        if i in {6,15,24}:
            pixels[i] = GREEN

        sleep (0.1)

# Flicker the LEDs to alert the user of a received message
def demogorgonNearby(selectedLED):
    shortDelay = int(random.uniform(0,1))
    longDelay = int(random.uniform(2.5,10.0))

    # FLICKER
    for i in range(0,2):
        pixels[selectedLED] = BLANK
        sleep(0.1)
        pixels[selectedLED] = GREEN
        sleep(0.1)
        pixels[selectedLED] = BLANK
        sleep(0.15)
        pixels[selectedLED] = GREEN
        sleep(0.15)
        pixels[selectedLED] = BLANK
        sleep(0.12)
        pixels[selectedLED] = GREEN
        sleep(0.12)
        pixels[selectedLED] = BLANK
        sleep(0.8)
        pixels[selectedLED] = GREEN
        sleep(0.8)

    pixels[selectedLED] = BLANK

    for i in range(0,3):
        pixels[selectedLED - 1] = BLANK
        sleep(0.1)
        pixels[selectedLED - 1] = GREEN
        sleep(0.1)
        pixels[selectedLED] = BLANK
        sleep(0.1)
        pixels[selectedLED] = GREEN
        sleep(0.1)

    pixels[selectedLED] = BLANK
    pixels[selectedLED - 1] = BLANK

# Seperate message into underlying characters and display them
## THIS DOESN'T ACCOUNT FOR SKIPPING LEDS JUST YET
def deconstructMessage(message):
    for char in message:
        if char.isalpha():
            for item in alphabet:
                if char in item[0]:
                    print(char + " " +  str(item[1]))
                    pixels[item[1]] = GREEN
                    sleep(0.5)
                    clearLEDs()


clearLEDs()

#while True:
# 	demogorgonNearby(int(random.uniform(0,30)))

displayChristmasLEDS()

if len(sys.argv) == 2:
    deconstructMessage(str(sys.argv[1]))

# TODO: RECEIVE SMS MESSAGE USING TWILIO OR SOME KIND OF IRC
# TODO: (RELATED TO ABOVE) RANDOMLY PICK FROM MANY FLICKER FUNCTIONS
