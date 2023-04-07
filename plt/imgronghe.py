from unittest import result
import cv2
import numpy as np

back = cv2.imread('/home/xiang/OpenCV/img/1.jpg')
smallcat = cv2.imread('/home/xiang/OpenCV/img/2.jpg')

result = cv2.addWeighted(smallcat, 0.9, back ,0.1, 0)
cv2.imshow('add', result)
cv2.waitKey(0)
