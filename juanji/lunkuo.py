import cv2
import numpy as np

img = cv2.imread('./img/hello.jpg')

# 变灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, dst = cv2.threshold(gray, 110, 250, cv2.THRESH_BINARY)
# 轮廓查找
cont, hier = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓直接修改原图
# 可copy一份
img_copy = img.copy()
cv2.drawContours(img_copy, cont, 1, (0,0,255), 2)

'''
#  面积， 周长
area = cv2.contourArea(cont[1])
pre = cv2.arcLength(cont[1], closed=True)

# 多边形逼近， 近似模拟手的轮廓
approx = cv2.approxPolyDP(cont[0], 20, closed=True)
# approx 是一个轮廓数据
cv2.drawContours(img_copy, [approx], 0, (0,255,0), 2)

# 凸包
hull = cv2.convexHull(cont[0])
cv2.drawContours(img_copy, [hull], 0, (255,0,0), 2)
'''

'''
# 最小外接矩形
# rect是一个Rotated Rect 旋转的矩形， 矩形的起始坐标(x, v)，矩形的长宽，矩形旋转角度
rect = cv2.minAreaRect(cont[1])
box = cv2.boxPoints(rect)
# 坐标必须是整数
box = np.int0(box)
cv2.drawContours(img_copy, [box], 0, (255,0,0), 2)
'''

#  最大外接矩形
x, y, w, h= cv2.boundingRect(cont[1])
cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)



# print("面积：", area, "周长：", pre)
cv2.imshow("img_copy", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()