import cv2
import numpy as np

img = cv2.imread('./img/1.jpg')
'''
    # ketnel 必须是float
    # kernel = np.ones((5, 5), np.float32) /25
    # 不同卷积核心
    kernel = np.array([[-1,-1,-1], [-1,8,-1],[-1,-1,-1]])

    dst = cv2.filter2D(img, -1, kernel)
'''

'''
    方盒滤波
        # 不用手动创将卷积核， 只需要告诉方和滤波， 卷积核的大小是多少
        dst = cv2.boxFilter(img, -1, (5,5), normalize=True)
'''

'''
    # 均值滤波没有位深
        dst = cv2.blur(img,(5,5))
'''

'''
    高斯滤波
        # 指定sigma：
            # dst1 = cv2.GaussianBlur(img, (5,5), sigmaX=1)
            # dst2 = cv2.GaussianBlur(img, (5,5), sigmaX=10)
            # dst = cv2.GaussianBlur(img, (5,5), sigmaX=1000)
        # 没有sigma ，用ksize
            dst1 = cv2.GaussianBlur(img, (5,5), sigmaX=0)
            dst2 = cv2.GaussianBlur(img, (9,9), sigmaX=0)
            dst = cv2.GaussianBlur(img, (21,21), sigmaX=0)
'''

'''
    # 中值滤波
        dst =cv2.medianBlur(img, 5)

'''

# 双边滤波
# 双边滤波几乎对胡椒滤波没有效果
dst = cv2.bilateralFilter(img, 7, sigmaColor=30, sigmaSpace=50)

cv2.imshow('img1', np.hstack((img, dst)))
# cv2.imshow('img2', np.hstack((img, dst2)))

cv2.waitKey(0)
cv2.destroyAllWindows()