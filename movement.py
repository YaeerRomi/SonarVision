import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

speed = 0
acceleration = 0.1

IN1 = 16
IN2 = 18
ENA = 22
IN3 = 11
IN4 = 13
ENB = 15



GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

direct  = (input("Input Direction: ")).lower()
speed = int(input("Input Speed:"))

pwn = GPIO.PWN(ENA, 50)

if direct == "right":
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)
elif direct == "left":
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)
    
try:
    while True:
        pwn.start(speed)
        
except KeyboardInterrupt:
    pwn.stop()
    GPIO.cleanup()
    