import cv2
import numpy as np

img = cv2.imread('./img/1.jpg')

# 分辨率减小的操作， 下采样
dst = cv2.pyrDown(img)
# 分辨率增加的操作， 上采样
dst2 = cv2.pyrUp(dst)

# 原图和高斯金字塔的差就是拉普拉斯金字塔
lap0 = img - dst2
cv2. imshow('img', img)
cv2. imshow('dst', dst)
cv2. imshow('lap0', lap0)
cv2.waitKey(0)
cv2.destroyAllWindows()