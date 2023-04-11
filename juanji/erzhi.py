import cv2
import numpy as np

img = cv2.imread('./img/23.jpg')

'''
# 全局阈值   
    # 二值化操作是对灰度值操作
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # threshold会返回与两个值， 一个是阈值， 一个是二值化处理后的图片
    thresh, dst = cv2.threshold(gray, 110, 200, cv2.THRESH_BINARY)
'''

'''
# 自适应阈值
    # 二值化操作是对灰度值操作
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 返回二值化处理后的图片
    dst = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)
'''
'''
# 腐蚀操作
    # 定义核
    kernel = np.ones((3, 3), np.uint8)
    dst = cv2.erode(img, kernel, iterations=1)
'''

'''
# 获取形态学卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
# 膨胀操作
dst = cv2.dilate(img, kernel, iterations=1)
'''

'''
# 开运算
# 用22.jpg， 方便理解
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
# 该方法为直接调用api， 也可用上面两个方法同时使用，但要注意迭代次数需要一致
dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=10)
'''

'''
# 闭运算
# 用23.jpg， 方便理解
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=10)
'''

'''
# 形态学梯度
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=1)
'''

'''
# 顶帽操作
# 用22.jpg， 方便理解
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
dst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=3)
'''

# 顶帽操作
# 用23.jpg， 方便理解
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
dst = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=3)


# cv2.imshow('img', dst)
cv2.imshow('img', np.hstack((img, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()