import cv2

# cam=cv2.VideoCapture(0)
# while True:
#     ignore, frame = cam.read()
#     grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     # cv2.imshow('my WEBcam',frame)
#     cv2.imshow('my WEBcam',grayframe)
#     cv2.moveWindow('my WEBcam', 0,0)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
# cam.release()

# assignment
cam=cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # red=cv2.cvtColor(frame,cv2.COLOR_BGR2BLUE)

    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam', 0,0)
    cv2.imshow('my WEBcam2',frame)
    cv2.moveWindow('my WEBcam2', 640,480)

    cv2.imshow('my gWEBcam',gray)
    cv2.moveWindow('my gWEBcam', 640,0)
    cv2.imshow('my g2WEBcam',gray)
    cv2.moveWindow('my g2WEBcam', 0,480)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()

