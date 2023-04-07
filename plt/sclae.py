import cv2
import numpy as np

img = cv2.imread('/home/xiang/OpenCV/img/2.jpg')
# 缩放
# new = cv2.resize(img, (400,  400))
# new2 = cv2.resize(img, None, fx= 1.3, fy =1.3)


# 翻转
# new = cv2.flip(img, 1)
# new2 = cv2.flip(img, -1)


# 旋转
new = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
new2 = cv2.rotate(img, cv2.ROTATE_180)


cv2.imshow('img', img)
cv2.imshow('new', new)
cv2.imshow('new2', new2)

cv2.waitKey(0)
