import cv2
import numpy as np




class Vision: 

    def __init__(self):
        self.stop_data = cv2.CascadeClassifier('stop_data.xml')
        self.cam = cv2.VideoCapture(0)

    def __del__(self):
        self.cam.release()

    def findStopSigns(self):
        ret,frame=self.cam.read()
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        found = self.stop_data.detectMultiScale(gray_frame, minSize =(20, 20))
        
        if len(found) != 0:
            return (True, found)
    