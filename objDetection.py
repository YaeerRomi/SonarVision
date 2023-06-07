import time
from car import Picarx

car = Picarx()
class ObjectDetection:
    def __init__(self):
        pass
    def ultra_sensor(self):
        while True:
            distance = car.get_distance()
            print("Distance cm: ", distance)
            time.sleep(1)