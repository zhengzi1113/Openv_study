import cv2
import numpy as np

# img = cv2.imread('./img/高斯函数.jpg')
img = cv2.imread('./img/1.jpg')
cv2.resizeWindow('img', 200, 200)

'''
# sobel 算子
    # 计算x轴方向的梯度, 只有垂直方向的边缘
    dx = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0, ksize=5)
    # 计算y轴方向的梯度, 只有水平方向的边缘
    dy = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1, ksize=5)
    # 使用sobel算子, 需要把x, y合并
    dst = cv2.add(dx, dy)
    cv2.imshow("img", img)
    cv2.imshow('img1', np.hstack((img, dst)))
    cv2.imshow('img2', np.hstack((img, dx)))
    cv2.imshow('img3', np.hstack((img, dy)))
'''

'''
# Scharr
    dx = cv2.Scharr(img, cv2.CV_64F, dx=1, dy=0)
    dy = cv2.Scharr(img, cv2.CV_64F, dx=0, dy=1)
    dst = cv2.add(dx, dy)
    cv2.imshow("img", img)
    cv2.imshow('img1', np.hstack((img, dst)))
'''

'''
# Laplacian
    dst = cv2.Laplacian(img, -1, ksize=3)
cv2.imshow('img', np.hstack((img, dst)))
'''

#阈值越小， 细节越丰富
lena1 = cv2.Canny(img, 64, 128)
lena2 = cv2.Canny(img, 100, 200)



cv2.imshow('img', np.hstack((lena1, lena2)))

cv2.waitKey(0)
cv2.destroyAllWindows()