import cv2

rows = int(input('How many rows do you want? '))
columns = int(input('How many columns do you want? '))

width = 1280
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

horizontal_padding = 0
vertical_padding = 30

while True:
    ignore, frame = cam.read()
    if not ignore:
        break

    original_height, original_width = frame.shape[:2]

    tile_width = int(width / columns)
    scale = tile_width / original_width
    tile_height = int(original_height * scale)

    frame_resized = cv2.resize(frame, (tile_width, tile_height))

    for i in range(rows):
        for j in range(columns):
            windName = 'Window' + str(i) + ' x ' + str(j)
            cv2.imshow(windName, frame_resized)
            cv2.moveWindow(
                windName,
                j * (tile_width + horizontal_padding),
                i * (tile_height + vertical_padding)
            )

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()