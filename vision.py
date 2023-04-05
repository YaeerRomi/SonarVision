import cv2
import numpy as np
cam = cv2.VideoCapture(0)

stop_data = cv2.CascadeClassifier('stop_data.xml')


while True:
    ret,frame=cam.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    found = stop_data.detectMultiScale(gray_frame, 
                                   minSize =(20, 20))
    
    if len(found) != 0:
        for (x, y, width, height) in found:
            cv2.rectangle(frame, (x,y), (x + width,y + height), (0, 255, 0), 5)
    
    cv2.imshow("FRAME",frame)

    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
