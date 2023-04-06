import cv2
import numpy as np

def callback():
    pass

cv2.namedWindow('trackbar')

# 创建trackbar
cv2.createTrackbar("R", 'trackbar', 0, 255, callback)
cv2.createTrackbar("G", 'trackbar', 0, 255, callback)
cv2.createTrackbar("B", 'trackbar', 0, 255, callback)

imgs = np.zeros((360, 640, 3), np.uint8)

while True:
    
    # 获取当前trackbar的值
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')

    imgs[:] = [b, g, r]
    cv2.imshow('trackbar', imgs)

    key = cv2.waitKey(1)

    if(key & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()