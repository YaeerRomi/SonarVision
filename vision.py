import cv2
import numpy as np
cam = cv2.VideoCapture(0)

# np.array([0,140,140]) LIGHT REDS
# lower mask (0-10) lower_red = np.array([0,70,53])

lower_red = np.array([0,130,60])
upper_red = np.array([10,255,255])


while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
    mask = cv2.inRange(hsv, lower_red, upper_red)


    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("camera", frame)
    cv2.imshow("Result", result)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()