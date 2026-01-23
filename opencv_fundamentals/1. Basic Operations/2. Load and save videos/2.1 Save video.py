import cv2
import numpy as np

cap = cv2.VideoCapture("Rt25.mp4")
#cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('flipped.mp4', fourcc, 30.0, (1280, 720))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        break
    height, width, channels = frame.shape

    flipped_frame = cv2.flip(frame, 0)
    out.write(flipped_frame)

    cv2.imshow('Frame', frame)
    cv2.imshow("Flipped frame", flipped_frame)

    key = cv2.waitKey(33)
    if key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()