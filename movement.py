import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Motor 1 Pins
IN1 = 16
IN2 = 18
ENA = 22

# Motor 2 Pins
IN3 = 11
IN4 = 13
ENB = 15


class Car:
    def __init__(self, IN1, IN2, ENA, IN3, IN4, ENB):
        # Initialize Motor 1
        self.GPIO.setup(IN1, GPIO.OUT)
        self.GPIO.setup(IN1, GPIO.OUT)
        self.GPIO.setup(ENA, GPIO.OUT)
        self.PWMA = GPIO.PWM(ENA, 100)
        self.PWMA.start(0)

        # Initialize Motor 2
        self.GPIO.setup(IN3, GPIO.OUT)
        self.GPIO.setup(IN4, GPIO.OUT)
        self.GPIO.setup(ENB, GPIO.OUT)
        self.PWMB = GPIO.PWM(ENB, 100)
        self.PWMB.start(0)
    
    def drive_forward(self, speed):
        # Motor 1 Speed
        self.PWMA.ChangeDutyCycle(speed)
        # Motor 2 Speed
        self.PWMB.ChangeDutyCycle(speed)
        
        # Motor 1 Forward
        self.GPIO.output(IN1, GPIO.HIGH)
        self.GPIO.output(IN2, GPIO.LOW)
        # Motor 2 Forward
        self.GPIO.output(IN3, GPIO.HIGH)
        self.GPIO.output(IN4, GPIO.LOW)
        
    def drive_backward(self, speed):
        # Motor 1 Speed
        self.PWMA.ChangeDutyCycle(speed)
        # Motor 2 Speed
        self.PWMB.ChangeDutyCycle(speed)
        
        # Motor 1 Reverse
        self.GPIO.output(IN1, GPIO.LOW)
        self.GPIO.output(IN2, GPIO.HIGH)
        # Motor 2 Reverse
        self.GPIO.output(IN3, GPIO.LOW)
        self.GPIO.output(IN4, GPIO.HIGH)
    
    def drive_stop(self):
        # Motor 1 Speed
        self.PWMA.ChangeDutyCycle(0)
        # Motor 2 Speed
        self.PWMB.ChangeDutyCycle(0)
        
        # Motor 1 Stop
        self.GPIO.output(IN1, GPIO.LOW)
        self.GPIO.output(IN2, GPIO.LOW)
        # Motor 2 Stop
        self.GPIO.output(IN3, GPIO.LOW)
        self.GPIO.output(IN4, GPIO.LOW)
        
        
        
car = Car(IN1, IN2, ENA, IN3, IN4, ENB)

forward = car.drive_forward()

reverse  = car.drive_backward()


