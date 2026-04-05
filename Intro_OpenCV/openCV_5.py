import cv2
import numpy as np

width = 640
height = 360
myRadius = 25
myColor = (0,0,0)
myThick = 2
myText = "Window Testing LALA"

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) # zero represents the list item for the cameras available in your pc so if you have two should be 1
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) # a moving jpg

while True:
    ignore, frame = cam.read()
    frame[140:220, 250:390]=(255,0,0) # slice the cam output window and manipulate the pixels.
    cv2.rectangle(frame, (250,140), (390,220), (0,255,0), 5)
    cv2.circle(frame, (int(width/2), int(height/2)), myRadius, myColor, myThick)
    cv2.putText(frame, myText, (60,60), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()