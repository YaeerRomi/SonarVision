import time
from gpriozero import Robot, Motor

car = Robot(leftMotor=(pin1, pin2), rightMotor=(pin3, pin4))


left_motor_pin = ""
right_motor_pin = ""

acceloration = 0.1
speed = 0
forward_maxSpeed = 100
backward_maxSpeed = 30

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor_pin, GPIO.OUT)
GPIO.setup(right_motor_pin, GPIO.OUT)

def move_forward(maxSpeed, speed, accelor):
    
    while speed <= maxSpeed:
        leftMotor.forward(speed)
        rightMotor.forward(speed)
        time.speed(0.5)
        speed += accelor
    
    moveForward = True
        
def move_backward(maxSpeed, speed, accelor):
    
    while speed >= maxSpeed:
        leftMotor.backward(speed)
        rightMotor.backward(speed)
        time.speed(0.5)
        speed -= accelor
    
        
        
    
    

while True:
    command = input("Enter a command: ")
    if command == "go":
        move_forward()
    else:
        print("Invalid command. Try again.")
