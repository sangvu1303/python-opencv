import cv2
import numpy as np



img = cv2.imread("tree3.jpg")
kernel = np.ones((5, 5), np.uint8)
cv2.imshow('default', img)

# 1: tách kênh màu
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
min_do = np.array([166, 63, 175])
max_do = np.array([179, 160, 255])
mask = cv2.inRange(hsv_img, min_do, max_do)
img1 = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('s', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()