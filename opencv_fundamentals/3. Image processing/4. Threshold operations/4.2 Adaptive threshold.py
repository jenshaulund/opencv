import cv2
import numpy as np

# Load image
img = cv2.imread("balls_grey_table.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Adaptive Threshold
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, 5)

# Show image and threshold
cv2.imshow("Adaptive", adaptive)
cv2.imshow("Image", img)
cv2.imshow("Gray", gray)
cv2.waitKey(0)