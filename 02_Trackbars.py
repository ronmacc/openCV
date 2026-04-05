"""
Creating and Using Trackbars in OpenCV
"""
import cv2
import cam_utils as cu

width = 640
height = 360

cam = cu.create_camera(width, height, fps=30)
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', cu.mouseClick)

while True:
    # reading camera output
    ignore, frame = cam.read()

    # Render main window
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()