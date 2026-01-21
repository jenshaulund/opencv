import cv2
import numpy as np

# Load images
img = cv2.imread("images/frame_71.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("images/frame_164.jpg", cv2.IMREAD_GRAYSCALE)

# Absolute difference between the 2 images
diff = cv2.absdiff(img, img2)

# Show images and the absolute difference
cv2.imshow("Diff", diff)
cv2.imshow("Img1", img)
cv2.imshow("Img2", img2)
cv2.waitKey(0)