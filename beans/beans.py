import cv2
import numpy as np
from skimage.morphology import opening

img = cv2.imread("beans.jpg")
kernel = np.ones((5, 5), np.uint8)
cv2.imshow('default', img)

# 1: ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2: Làm mờ ảnh và phân ngưỡng ảnh
blur = cv2.GaussianBlur(gray, (9, 9), 1)
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, -5)
cv2.imshow('thresh', thresh)

# 3: lọc nhiễu ảnh với Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)

# 4: contour
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# kết quả
cv2.imshow('contours', img)
print("Count: " + str(len(contours)))
cv2.waitKey(0)
cv2.destroyAllWindows()