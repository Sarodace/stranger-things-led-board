import board
import neopixel
from time import sleep

BLANK = (0, 0, 0)
RED = (0, 255, 0)
YELLOW = (150, 255, 0)
CYAN = (255, 0, 255)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (0, 180, 255)

pixels = neopixel.NeoPixel(board.D21, 26, brightness = 0.1, auto_write=True)
pixels.fill(BLANK)
sleep (0.5)

for i in range(len(pixels)):
	sleep (0.1)
	if i in range(0,26)[0::7]:
		pixels[i] = RED
	if i in range(0,26)[1::7]:
		pixels[i] = YELLOW
	if i in range(0,26)[2::7]:
		pixels[i] = CYAN
	if i in range(0,26)[3::7]:
		pixels[i] = GREEN
	if i in range(0,26)[4::7]:
		pixels[i] = BLUE
	if i in range(0,26)[5::7]:
		pixels[i] = PURPLE