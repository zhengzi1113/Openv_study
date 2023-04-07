import cv2
import numpy as np

img =  cv2.imread('/home/xiang/OpenCV/img/1.jpg')

src = np.float32([[20,10], [10, 130], [80,20], [80, 100]])
dst = np.float32([[10,10], [10, 130], [80,10], [80, 130]])
M = cv2.getPerspectiveTransform(src, dst)
new = cv2.warpPerspective(img, M, (200, 200))

cv2.imshow('img', img)
cv2.imshow('new', new)
cv2.waitKey(0)

