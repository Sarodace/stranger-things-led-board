# LIBRARIES
import board
import neopixel
import random
from time import sleep

# Potential LED colors
BLANK = (0, 0, 0)
RED = (0, 255, 0)
YELLOW = (150, 255, 0)
CYAN = (255, 0, 255)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (0, 180, 255)
PINK = (0, 255, 200)

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

clearLEDs()

#while True:
# 	demogorgonNearby(int(random.uniform(0,30)))
displayChristmasLEDS()

# TODO: MESSAGE DECOMP
# TODO: RECEIVE SMS MESSAGE USING TWILIO OR SOME KIND OF IRC
# TODO: CONVEY MESSAGE USING LEDs
# TODO: (RELATED TO ABOVE) RANDOMLY PICK FROM MANY FLICKER FUNCTIONS
