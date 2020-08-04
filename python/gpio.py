from gpiozero import Button
from time import sleep

display_button = Button(27)
power_button = Button(17)

while True:
    # Check for display_message button
    if display_button.is_pressed:
        print("Display message!")
    elif not display_button.is_pressed:
        print("Display button not pressed")

    # Check for power button 
    if power_button.is_pressed:
        print("Turn on/off!")
    elif not power_button.is_pressed:
        print("Power button not pressed")

    sleep(1)
