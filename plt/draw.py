import cv2
import numpy as np

#画直线， 坐标点（x， y）
img = np.zeros((600, 600, 3), np.uint8)

cv2.line(img, (10,10), (100, 150), (0,0,222),5 ,4)

#画矩形
cv2.rectangle(img, (10,10), (100, 100), (0, 0, 255), -1)

#画园
cv2.circle(img, (320, 240), 5, (0,0,255))
# cv2.circle(img, (320, 240), 100, (0,0,255), -1)

# 画椭圆
cv2.ellipse(img, (320, 240),(100, 50), 90, 0, 90, (0,0,255), -1)

# 画多边形
pts = np.array([(300, 10), (150, 150), (450, 100)], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 255))
# 多边形填充（特殊）
cv2.fillPoly(img, [pts], (122,22, 2))

# 画文本



cv2.imshow('draw', img)
cv2.waitKey(0)