import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread('./img/1.jpg')


# 统计直方图
## 用opencv的统计方法
# histb = cv2.calcHist([img], [0], None, [256], [0, 255])
# histg = cv2.calcHist([img], [1], None, [256], [0, 255])
# histr = cv2.calcHist([img], [2], None, [256], [0, 255])
# plt.plot(histb, color='b')
# plt.plot(histg, color='g')
# plt.plot(histr, color='r')

## 不用opencv的统计方法
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.hist(gray.ravel(), bins=256, range=[0, 255])


cv2.waitKey(0)
cv2.destroyAllWindows()