import cv2 as cv

# MODIFYING A VIDEO OR IMG -SCALING- ALWAYS AIM TO REDUCE NOT SCALE UP
def rescaleFrame(frame, scale=0.75):
    """
    works on images, videos and live video
    """
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width,heigth)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    """
    only works for live video
    """
    capture.set(3, width)
    capture.set(4, height)

# READING VIDEOS
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()