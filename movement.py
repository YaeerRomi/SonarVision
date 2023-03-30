import RPi.GPIO as GPIO
import time

left_motor_pin = ""
right_motor_pin = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor_pin, GPIO.OUT)
GPIO.setup(right_motor_pin, GPIO.OUT)

def move_forward():
    GPIO.output(left_motor_pin, GPIO.HIGH)
    GPIO.output(right_motor_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(left_motor_pin, GPIO.LOW)
    GPIO.output(right_motor_pin, GPIO.LOW)

while True:
    command = input("Enter a command: ")
    if command == "go":
        move_forward()
    else:
        print("Invalid command. Try again.")
