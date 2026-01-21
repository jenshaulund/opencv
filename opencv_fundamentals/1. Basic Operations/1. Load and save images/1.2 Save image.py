import cv2

img = cv2.imread("1. Load and save images/livingroom.jpg")
cv2.imwrite("1. Load and save images/livingroom_copy.jpg", img)

# Display Images
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()