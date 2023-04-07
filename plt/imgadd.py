from cgitb import reset
from unittest import result
import cv2
import numpy as np

cv2.namedWindow('add', cv2.WINDOW_NORMAL)
imgs = cv2.imread("/home/xiang/OpenCV/img/HSL.jpg")
print(imgs.shape)
img = np.ones((791, 1520, 3), np.uint8) * 100
while True:

    cv2.imshow('add', imgs)
    #  A + B 位置随意
    result = cv2.add(imgs, img)
    # A - B 位置重要
    result2 = cv2.subtract(imgs, img)

    cv2.imshow('result', result)
    cv2.imshow('result', result2)

    key = cv2.waitKey(1)
    if(key & 0xFF == ord('q')):
        break

#释放资源
cv2.destroyAllWindows()