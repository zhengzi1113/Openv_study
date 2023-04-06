import cv2
import numpy as np
import matplotlib.pyplot as plt

def callback():
    pass

cv2.namedWindow('color')

img = plt.imread('/home/xiang/OpenCV/img/5.gif')

colorspaces = [cv2.COLOR_BGR2RGBA,cv2.COLOR_BGR2BGRA,
                cv2.COLOR_BGR2GRAY,cv2.COLOR_BGR2HSV,
                cv2.COLOR_BGR2YUV]

cv2.createTrackbar("curcolor", 'color', 0,len(colorspaces), callback)


while True:
    
    v = cv2.getTrackbarPos('curcolor', 'color')


    #颜色空间转换API
    cut_img = cv2.cvtColor(img, colorspaces[v])

    cv2.imshow('color', cut_img)

    key = cv2.waitKey(1)

    if(key & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()