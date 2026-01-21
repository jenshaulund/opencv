import cv2
import numpy as np

# Load image
img = cv2.imread("balls_grey_table.jpg")

# Convert Image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Image binary threshold
_, threshold = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

# Show image and threshold
cv2.imshow("Threshold", threshold)
cv2.imshow("Image", img)
cv2.imshow("Gray", gray)
cv2.waitKey(0)