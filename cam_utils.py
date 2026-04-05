from multiprocessing import Value
from xml.etree.ElementTree import XMLPullParser
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

evt = None
pnt = None
pnt1 = None
pnt2 = None
xPos = 860
yPos = 540
myRad = 25
mythick = 1

def mouseClick(event, xPos, yPos, flags, params):
    global pnt1, pnt2, evt, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        pnt1 = (xPos, yPos)
        pnt2 = (xPos, yPos)
        evt = event

    elif event == cv2.EVENT_LBUTTONUP:
        pnt2 = (xPos, yPos)
        evt = event
        
def mouseClickAddCircle(event, xPos, yPos, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global evt, pnt
        print("Mouse Event Was: ", event)
        print('at Position ', xPos, yPos)
        pnt=(xPos, yPos)
        evt=event
    if event == cv2.EVENT_LBUTTONUP:
        print("Mouse Event Was: ", event)
        print('at Position ', xPos, yPos)
        evt=event
    if event == cv2.EVENT_RBUTTONUP:
        print('Right Button up: ', event)
        pnt=(xPos, yPos)
        evt=event

def mycallBack1(val):
    global xPos
    xPos = val

def mycallBack2(val):
    global yPos
    yPos = val

def mycallBack3(val):
    global myRad
    myRad = val

def mycallBack4(val):
    global mythick
    mythick = val