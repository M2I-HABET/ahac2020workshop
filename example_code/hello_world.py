# Hello World!
# AHAC 2020 Workshop
# Matthew E. Nelson

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    print("Hello World!")
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
