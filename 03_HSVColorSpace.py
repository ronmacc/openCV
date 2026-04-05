"""
Understanding the HSV Color Space
"""

import cv2
import numpy as np
import cam_utils as cu

width = 1280
height = 720

# cam = cu.create_camera(width, height, fps=30)
# cv2.namedWindow('my WEBcam')

# cv2.setMouseCallback('my WEBcam', cu.mouseClick)

# while True:
#     # reading camera output
#     ignore, frame = cam.read()
#     frame = cv2.flip(frame, 1)

#     if cu.evt == 1:
#         x = np.zeros([250,250,3], dtype=np.uint8)
#         clr = frame[cu.yVal][cu.xVal]
#         print(clr)
#         x[:,:] = clr
#         cv2.putText(x, str(clr), (0,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1)
#         cv2.imshow('Color Picker', x)
#         cv2.moveWindow('Color Picker', width, 0)
#         cu.evt = 0

#     # Render main window
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam', 0,0)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
# cam.release()

## assignment

x = np.zeros([256,720,3], dtype=np.uint8)
for row in range(0,256,1):
    for col in range(0,720,1):
        x[row,col] = (int(col/4),row,255)
x = cv2.cvtColor(x, cv2.COLOR_HSV2BGR)
while True:
    cv2.imshow('my HSV',x)
    cv2.moveWindow('my HSV', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# cam.release()
cv2.destroyAllWindows()