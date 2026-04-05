"""
Creating and Using Trackbars in OpenCV
"""
import cv2
import cam_utils as cu

width = 640
height = 360
xPos = int(width/2)
yPos = int(height/2)
myRad = 25
myThick = 7

cam = cu.create_camera(width, height, fps=30)
cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars', 400, 150)
cv2.moveWindow('myTrackbars', width, 0)
cv2.createTrackbar('xPos', 'myTrackbars', xPos, 640, cu.mycallBack1)
cv2.createTrackbar('yPos', 'myTrackbars', yPos, 360, cu.mycallBack2)
cv2.createTrackbar('radius', 'myTrackbars', myRad, int(height/2), cu.mycallBack3)
cv2.createTrackbar('thick', 'myTrackbars', myThick, 7, cu.mycallBack4)

while True:
    # reading camera output
    ignore, frame = cam.read()

    # add circle
    cv2.circle(frame, (cu.xPos, cu.yPos), cu.myRad, (0,0,255), cu.mythick)

    # Render main window
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()