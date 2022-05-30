import cv2
import numpy as np


img = cv2.imread("tree2.jpg")
kernel = np.ones((5, 5), np.uint8)
cv2.imshow('default', img)

# 1: tách kênh màu
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
min_do = np.array([166, 63, 150])
max_do = np.array([179, 160, 255])
mask = cv2.inRange(hsv_img, min_do, max_do)
img1 = cv2.bitwise_and(img, img, mask=mask)

# 2: ảnh xám
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# 3: Làm mờ ảnh và phân ngưỡng ảnh
blur = cv2.GaussianBlur(gray, (9, 9), 3)
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 0)
cv2.imshow('thresh', thresh)

# 4: lọc nhiễu ảnh với Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)

# 5: contour
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# kết quả
cv2.imshow('contours', img)
So_lương = int(len(contours))
San_luong = (So_lương / 25)
print("So luong: ", So_lương)
print('san luong :', San_luong, 'kg')


cv2.waitKey(0)
cv2.destroyAllWindows()