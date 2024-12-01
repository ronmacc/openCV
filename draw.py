import cv2 as cv
import numpy as np

# blank = np.zeros((500,500), dtype='uint8')
# cv.imshow('Black', blank)

# # 1. Paint the image a certain colour
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# cv.waitKey(0)

# PAINT 
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Black', blank)

# # 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# DRAW A RECTANGLE
# cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=2)
# cv.rectangle(blank, (0,0), (250,500), (0,250,0), thickness=-1)
# cv.rectangle(blank, (0,0), (250,500), (0,250,0), thickness=cv.FILLED)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,250,0), thickness=-1)
cv.imshow('Rectangle', blank)

#DRAW A CIRCLE
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# DRAW A LINE   
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# write text on an image
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)