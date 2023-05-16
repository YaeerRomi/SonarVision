import cv2
import numpy as np

# Open the video feed
cap = cv2.VideoCapture(0) # 0 is the default camera. Change the number if you have multiple cameras.

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range for orange color
    lower_orange = np.array([5, 50, 50])
    upper_orange = np.array([15, 255, 255])

    # Threshold the HSV image to get only orange colors
    mask = cv2.inRange(hsv, lower_orange, upper_orange)


    # Apply dilation and erosion to remove small white regions
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.dilate(mask, kernel, iterations = 1)
    mask = cv2.erode(mask, kernel, iterations = 1)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)

    # Convert the result to grayscale
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    

    # Apply Canny edge detection
  
    edges = cv2.Canny(gray, 100, 200)

    # Define the region of interest
    height, width = frame.shape[:2]
    mask = np.zeros_like(edges)
    #full 
    polygon = np.array([[
    (0, height),
    (width, height),
    (width, 0),
    (0, 0)
]], np.int32)


    #mid to bot 
    """polygon = np.array([[
        (0, height),
        (width, height),
        (width, height/2),
        (0, height/2)
    ]], np.int32)"""
    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)

    # Apply Hough line transform
    lines = cv2.HoughLinesP(cropped_edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=100, maxLineGap=500)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
