import cv2
import numpy as np

# Load video
cap = cv2.VideoCapture("cars_highway.mp4")

# Load MOG2 Background Subtractor
mog2 = cv2.createBackgroundSubtractorMOG2(history=500, detectShadows=True)

while True:
    # Extract frames in realtime
    ret, frame = cap.read()
    if ret is False:
        break

    # Get the mask
    mask = mog2.apply(frame)

    # Show frame and mask
    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(33)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()