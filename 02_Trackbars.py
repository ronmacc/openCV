"""
Creating and Using Trackbars in OpenCV
"""
import cv2
import cam_utils as cu

width = 1280
height = 720
# xPos = int(width/2)
# yPos = int(height/2)
xPos = 0
yPos = 0
myRad = 25
myThick = 7

# cam = cu.create_camera(width, height, fps=30)
# cv2.namedWindow('myTrackbars')
# cv2.resizeWindow('myTrackbars', 400, 150)
# cv2.moveWindow('myTrackbars', width, 0)
# cv2.createTrackbar('xPos', 'myTrackbars', xPos, 640, cu.mycallBack1)
# cv2.createTrackbar('yPos', 'myTrackbars', yPos, 360, cu.mycallBack2)
# cv2.createTrackbar('radius', 'myTrackbars', myRad, int(height/2), cu.mycallBack3)
# cv2.createTrackbar('thick', 'myTrackbars', myThick, 7, cu.mycallBack4)

# while True:
#     # reading camera output
#     ignore, frame = cam.read()

#     # add circle
#     cv2.circle(frame, (cu.xPos, cu.yPos), cu.myRad, (0,0,255), cu.mythick)

#     # Render main window
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam', 0,0)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
# cam.release()

# assignment 

cam = cu.create_camera(width, height, fps=30)
cv2.namedWindow('my WEBcam', cv2.WINDOW_NORMAL)

cv2.namedWindow('my trackbars')
cv2.moveWindow('my trackbars', width, 0)
cv2.resizeWindow('my trackbars', 400, 150)

cv2.createTrackbar('xPos', 'my trackbars', 0, 2000, cu.mycallBack1)
cv2.createTrackbar('yPos', 'my trackbars', 0, 1000, cu.mycallBack2)
cv2.createTrackbar('myWidth', 'my trackbars', width, 1920, cu.mycallBack3)


while True:
    ignore, frame = cam.read()

    if not ignore:
        break

    frame = cv2.flip(frame, 1)

    cv2.imshow('my WEBcam', frame)
    cv2.resizeWindow('my WEBcam', cu.myWidth, cu.myHeight)
    cv2.moveWindow('my WEBcam', cu.xPos, cu.yPos)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()