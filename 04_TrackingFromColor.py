"""
Description Here
"""
import cv2
import cam_utils as cu

width = 1280
height = 720

cam = cu.create_camera(width, height, fps=30)
cv2.namedWindow('my WEBcam')

while True:
    # reading camera output
    ignore, frame = cam.read()
    frame = cv2.flip(frame, 1)

    # Render main window
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()