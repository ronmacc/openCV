"""
 Processing Mouse Clicks and Events in OpenCV
"""
import cv2
import cam_utils as cu


width = 640
height = 360

cam = cu.create_camera(width, height, fps=30)

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', cu.mouseClick)

# while True:
#     # reading camera output
#     ignore, frame = cam.read()
#     if cam_utils.evt == 1 or cam_utils.evt == 4:
#         cv2.circle(frame, cam_utils.pnt, 25, (255,0,0), 2)

#     # Render main window
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam', 0,0)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
# cam.release()


# assignment rectangle for ROI region of interest
while True:
    ignore, frame = cam.read()

    if cu.evt == 4:
        cv2.rectangle(frame, cu.pnt1, cu.pnt2, (0, 0, 255), 2)
        ROI = frame[cu.pnt1[1]:cu.pnt2[1], cu.pnt1[0]:cu.pnt2[0]]
        cv2.imshow('ROI', ROI)
        cv2.moveWindow('ROI', int(width*1.1), 0)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()