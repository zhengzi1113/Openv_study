from cmath import log
import cv2
import numpy as np


img = cv2.imread('/home/xiang/OpenCV/img/2.jpg')

logo = np.zeros((200, 200,3), np.uint8)
mask = np.zeros((200, 200), np.uint8)

logo[100:120, 20:80] = [0, 200,0]
logo[120:170, 100:150] = [0, 0,100]

mask[100:120, 20:80] = 200
mask[120:170, 100:150] = 100

# 对mask按取反
m = cv2.bitwise_not(mask)

# 选择img添加logo的位置
roi = img[0:200, 0:200]

#与m进行与操作（单层）
tmp = cv2.bitwise_and(roi, roi, mask =m)

dst = cv2.add(tmp, logo)

img[0:200, 0:200] = dst


# cv2.imshow('mask', mask)
# cv2.imshow('logo', logo)
# cv2.imshow('m', m)
# cv2.imshow('roi', roi)
# cv2.imshow('tmp', tmp)
# cv2.imshow('dst', tmp)
cv2.imshow('img', img)



cv2.waitKey(0)