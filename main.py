from vision import Vision
import time

import keyboard
v = Vision()

print("Started")
""" 
HOW PROGRAM SHOULD FLOW
while True:
    if v.findStopSigns():
        STOP THE CAR FOR X AMOUNT OF TIME
        THEN GO FORWARD ONCE CLEAR
    if v.findStopLight():
        STOP THE CAR FOR X AMOUNT OF TIME
        THEN GO FORWARD ONCE CLEAR
    curve = getLaneCurve()
    set servo to curve angle to stay in lane

    at first intersection turn ____
    at second intersection turn ____
    at third intersection turn _____
    and so on
    at exit stop
"""