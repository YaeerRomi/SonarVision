import time
import math
import keyboard
from RPi.GPIO import GPIO
from gpiozero import Robot

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Left Motor
GPIO.setup(16, GPIO.OUT)
GPIO.steup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Right Motor
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# GPIOZERO METHOD

tesla = Robot(left=(16, 18), right=(11, 13))


def motors():
    tesla = Robot(left=(16, 18), right=(11, 13))

    while True:
        if keyboard.is_pressed('w'):

            tesla.forward()
        elif keyboard.is_pressed('s'):
            tesla.backward()

        else:
            tesla.stop()


motors()
