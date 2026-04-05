"""
Tracking an Object Based on Color in OpenCV
This file explores how to track an object based on color. 
We will use trackbars to train the model, and then will create masks to select only the object of the desired color. 
I will show you step-by-step instruction, and I do not assume you are already an expert..

"""
import cv2
import numpy as np
import cam_utils as cu

width = 640
height = 360
hueLow = 10
hueHigh = 20
satLow = 10
satHigh = 250
valLow = 10
valHigh = 250

cam = cu.create_camera(width, height, fps=30)
cv2.namedWindow('my WEBcam')

cv2.namedWindow('myTracker')
cv2.moveWindow('myTracker', width,0)

cv2.createTrackbar('Hue Low', 'myTracker', 10,179, cu.onTrack1)
cv2.createTrackbar('Hue High', 'myTracker', 20,179, cu.onTrack2)
cv2.createTrackbar('Sat Low', 'myTracker', 10,255, cu.onTrack3)
cv2.createTrackbar('Sat High', 'myTracker', 250,255, cu.onTrack4)
cv2.createTrackbar('Val Low', 'myTracker', 10,255, cu.onTrack5)
cv2.createTrackbar('Val High', 'myTracker', 250,255, cu.onTrack6)

while True:
    # reading camera output
    ignore, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound = np.array([cu.hueLow, cu.satLow, cu.valLow])
    upperBound = np.array([cu.hueHigh, cu.satHigh, cu.valHigh])

    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    myMask = cv2.bitwise_not(myMask)
    myObject = cv2.bitwise_and(frame, frame, mask=myMask)
    myObjectSmall = cv2.resize(myObject, (int(width/2), int(height/2)))
    cv2.imshow('My Object', myObjectSmall)
    cv2.moveWindow('My Object', int(width/2), int(height))

    myMaskSmall = cv2.resize(myMask, (int(width/2), int(height/2)))
    cv2.imshow('My Mask', myMaskSmall)
    cv2.moveWindow('My Mask', 0, height)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    # Render main window
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows(),