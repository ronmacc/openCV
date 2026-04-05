import cv2
import numpy as np

# while True:
#     frame = np.zeros([1000,1000, 3], dtype=np.uint8)
#     frame[:,:] = [0,0,255]
#     frame[:,:500] = [0,255,0]
#     cv2.imshow('My Window',frame)
#     if cv2.waitKey(1) & 0xff==ord('q'):
#         break


# # assignment 
# rows = 8
# columns = 8
# width = 1000
# height = 1000

# while True:
#     frame = np.zeros([height,width], dtype=np.uint8)


#     tile_width = width // columns
#     tile_height = height // rows

#     for i in range(rows):
#         for j in range(columns):
            
#             x_start = j * tile_width
#             y_start = i * tile_height

#             x_end = x_start + tile_width
#             y_end = y_start + tile_height

#             if (i + j) % 2 == 0:
#                 frame[y_start:y_end, x_start:x_end] = 255
#             else:
#                 frame[y_start:y_end, x_start:x_end] = 0
#     cv2.imshow('My Window',frame)

#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break

# cv2.destroyAllWindows()

# === solution from tutorialsb

boardSize = int(input('What sixe is your board? '))
numSquares = int(input('And how many squares? '))
squareSize = int(boardSize/numSquares)

darkColor = (0,0,0)
lightColor = (0,0,255)
nowColor = darkColor

while True:
    x = np.zeros([boardSize,boardSize, 3], dtype=np.uint8)
    
    for row in range(0,numSquares):
        for column in range(0,numSquares):
            x[squareSize*row : squareSize*(row+1), squareSize*column : squareSize*(column+1)] = nowColor
            if nowColor == darkColor:
                nowColor =  lightColor
            else:
                nowColor = darkColor
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor = darkColor
                
    cv2.imshow('My checkerboard', x)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break