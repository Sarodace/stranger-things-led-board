import board
import neopixel
from time import sleep

pixels = neopixel.NeoPixel(board.D21, 26, brightness = 0.1)
pixels.fill((0, 0, 0))
sleep (2)
pixels.fill((255, 255, 255))
pixels.show()

print("Hello, world")