import cv2
import numpy as np

# Load video
cap = cv2.VideoCapture("cars_highway.mp4")

# Get first frame from video
_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

# Show first frame
cv2.imshow("First Frame", first_frame)

while True:
    # Get frames in realtime
    ret, frame = cap.read()
    if ret is False:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Absolute difference between first and current frames
    diff = cv2.absdiff(first_gray, gray)

    # Show frame and absolute difference
    cv2.imshow("Frame", frame)
    cv2.imshow("Diff", diff)

    key = cv2.waitKey(33)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()