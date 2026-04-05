import cv2


def create_camera(width=640, height=360, fps=30):
    """
    Initializes and returns a configured OpenCV camera object.
    """

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    camera.set(cv2.CAP_PROP_FPS, fps)
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    return camera

# # =========== 01_Processing mouse click ===========

# pnt1 = None
# pnt2 = None
# xPos = 0
# yPos = 0
# camera = None
# evt = None
# pnt = None

# def mouseClick(event, xPos, yPos, flags, params):
#     global pnt1, pnt2, evt, drawing

#     if event == cv2.EVENT_LBUTTONDOWN:
#         pnt1 = (xPos, yPos)
#         pnt2 = (xPos, yPos)
#         evt = event

#     elif event == cv2.EVENT_LBUTTONUP:
#         pnt2 = (xPos, yPos)
#         evt = event

# def mouseClickAddCircle(event, xPos, yPos, flags, params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         global evt, pnt
#         print("Mouse Event Was: ", event)
#         print('at Position ', xPos, yPos)
#         pnt=(xPos, yPos)
#         evt=event
#     if event == cv2.EVENT_LBUTTONUP:
#         print("Mouse Event Was: ", event)
#         print('at Position ', xPos, yPos)
#         evt=event
#     if event == cv2.EVENT_RBUTTONUP:
#         print('Right Button up: ', event)
#         pnt=(xPos, yPos)
#         evt=event

# # =========== 02_Trackbars ===========

# xPos = 0
# yPos = 0
# myRad = 25
# mythick = 1
# myWidth = 0
# myHeight = 0

# def mycallBack1(val):
#     global xPos
#     xPos = val

# def mycallBack2(val):
#     global yPos
#     yPos = val

# def mycallBack3(val):
#     global myRad
#     myRad = val

# def mycallBack3(val):
#     global myWidth, myHeight
#     myWidth = val
#     myHeight = int(myWidth * 9 / 16)

# def mycallBack4(val):
#     global mythick
#     mythick = val

# =========== 03_HSVColorSpace ===========

evt = 0
xVal = 0
yVal = 0

def mouseClick(event, xPos, yPos, flags, params):
    global evt, xVal, yVal

    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        xVal=xPos
        yVal=yPos
        evt=event
    if event == cv2.EVENT_RBUTTONUP:
        evt.event
        print(event)
        

