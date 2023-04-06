import cv2
import numpy
import matplotlib.pyplot as plt

img = plt.imread('/home/xiang/OpenCV/img/1.jpg')
# 浅
img2 = img
# 深
img3 = img.copy()

img[10:100, 10:100] = [0, 0, 255]

cv2.imshow('img', img)
cv2.imshow('img3', img3)
cv2.imshow('img2', img2)

cv2.waitKey()