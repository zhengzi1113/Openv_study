import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./img/1.jpg')

'''
# 统计直方图
## 用opencv的统计方法
histb = cv2.calcHist([img], [0], None, [256], [0, 255])
histg = cv2.calcHist([img], [1], None, [256], [0, 255])
histr = cv2.calcHist([img], [2], None, [256], [0, 255])
plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.legend()
plt.show()

## 不用opencv的统计方法
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.hist(gray.ravel(), bins=256, range=[0, 255])
plt.legend()
plt.show()
'''
# 灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 掩膜图像
mask = np.zeros(gray.shape, np.uint8)
# 设置需要统计的图像
mask[50:150, 50:150] = 255
histmask = cv2.calcHist([img], [1], mask, [256], [0, 255])
histgray = cv2.calcHist([img], [2], None, [256], [0, 255])
plt.plot(histmask, color='b')
plt.plot(histgray, color='g')


cv2.imshow("gray", gray)
cv2.imshow("mask", mask)
# gray和gray做与运算结果还是gray，mask的做用，就是gray和gray先做与运算，结果再和mask做与运算
cv2.imshow("gray_mask", cv2.bitwise_and(gray, gray, mask=mask))
cv2.waitKey(0)
cv2.destroyAllWindows()