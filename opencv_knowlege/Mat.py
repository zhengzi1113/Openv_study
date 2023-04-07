import cv2
import numpy
import matplotlib.pyplot as plt

img = plt.imread('/home/xiang/OpenCV/img/5.gif').copy()
'''
# 浅
img2 = img
# 深
img3 = img.copy()
img[10:100, 10:100] = [0, 0, 255,4]
cv2.imshow('img', img)
cv2.imshow('img3', img3)
cv2.imshow('img2', img2)
'''

# shape属性 包含三个信息 ： 高度， 长度， 通道数
# size = 高度 * 长度 * 通道数
# dtype 元素位深

cv2.waitKey()