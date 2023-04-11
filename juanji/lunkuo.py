import cv2
import numpy as np

img = cv2.imread('./img/24.jpg')

# 变灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, dst = cv2.threshold(gray, 110, 250, cv2.THRESH_BINARY)
# 轮廓查找
cont, hier = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(cont)
cv2.waitKey(0)
cv2.destroyAllWindows()