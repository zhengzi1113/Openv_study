import cv2
import numpy as np

img = cv2.imread('img/shudu.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


'''
# Harris角点检测
# 返回角点像一个，每一个像素都可以计算出一个角点响应
dst = cv2.cornerHarris(gray, blockSize=5, ksize=3, k=0.04)

# 显示角点
# 设定阈值
img[dst > (0.01 * dst.max())] = [0, 0, 255]
'''

corners = cv2.goodFeaturesToTrack(gray, maxCorners=0,  qualityLevel=0.01, minDistance=10)
corners = np.int0(corners)
for i in corners:
    print(i)
    # i 相当于corners中的每一行数据
    # ravel 把二维数据变一维
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (250, 0, 1), -1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()