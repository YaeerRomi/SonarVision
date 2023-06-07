import time
from car import Picarx

class Movement:
    def __init__(self):
        self.car = Picarx()
        self.speed = 0
        self.max_speed = 100
        self.accelorator = 0.1
        
    def forward(self, speed):
        self.car.forward(speed)
        
    def backward(self, speed):
        self.car.backward(speed)

    def stop(self, speed):
        self.car.stop()

    def accelerate(self):
        while self.speed < self.max_speed:
            self.speed += self.accelorator
            self.accelorator *= 1.1  # Increase accelerator gradually
            if self.speed < self.max_speed:
                self.speed = 100
            self.car.set_motor_speed(self.speed)
            time.sleep(0.1)

            
        self.car.set_motor_speed(100)
            
    def decelerate(self):
        while self.speed > 0:
            self.speed -= self.accelorator
            self.accelorator *= 1.1  # Increase accelerator gradually
            if self.speed < 0:
                self.speed = 0
            self.car.set_motor_speed(self.speed)
            time.sleep(0.1)

            
    def turns(self, angle):
        # Max angles 50 to -50 degrees
        self.car.set_dir_servo_angle(angle)
        
    def camx(self, value):
        self.car.set_camera_servo1_angle(value)
        
    def camy(self, value):
        self.car.set_camera_servo2_angle(value)
        
        