
import cv2

img = cv2.imread("livingroom.jpg")  # Provide the correct path to your image file

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()