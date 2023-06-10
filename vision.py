import cv2
import numpy as np
from ultralytics import YOLO

# ADD LANE DETECTION TO THIS FILE

class Vision: 
    def __init__(self):

        self.cam = cv2.VideoCapture(0)
        self.model = YOLO("best.pt")

    def __del__(self):
        self.cam.release()

    def findStopSigns(self):
        res,frame=self.cam.read()

        results = self.model.track(source=frame, conf=0.8)
        if len(results[0].boxes) > 0:
            return True
        return False

