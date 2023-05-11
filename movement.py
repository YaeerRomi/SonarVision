import time
import RPi.GPIO as GPIO
from robot_hat import motor
import keyboard

class Movement:
    def __init__(self):
        self.motor = motor.Motor()
        
    def forward(self, speed):
        self.motor.wheel(speed, motor=-1)
        
    def backward(self, speed):
        self.motor.wheel(-speed, motor=-1)

    def stop(self, speed):
        self.motor.wheel(0, motor=-1)

    def accelerate(self, start_speed, end_speed, duration):
        step = (end_speed - start_speed) / duration
        for speed in range(start_speed, end_speed, int(step)):
            self.forward(speed)
            time.sleep(0.1)
            
    def decelerate(self, start_speed, end_speed, duration):
        step = (start_speed - end_speed) / duration
        for speed in range(start_speed, end_speed, -int(step)):
            self.forward(speed)
            time.sleep(0.1)
            
    def turns(self, speed, angle):
        pass