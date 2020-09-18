# Plotting data of the microcontroller temperature
# AHAC 2020 Workshop
# Matthew E. Nelson

import time
import microcontroller

while True:
    # Just keep emitting three random numbers in a Python tuple.
    time.sleep(0.05)
    print(((microcontroller.cpu.temperature),))
