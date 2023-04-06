import cv2
import numpy as np
import matplotlib.pyplot as plt



# 设置鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse', 640, 360)


#设置鼠标回调
cv2.setMouseCallback('mouse', mouse_callback, "123")

imgs = np.zeros((360, 640, 3), np.uint8)
# img = plt.imread("/home/xiang/OpenCV/img/5.gif",1)

while True:

    cv2.imshow('mouse', imgs)

    key = cv2.waitKey(1)
    if(key & 0xFF == ord('q')):
        break

#释放资源
cv2.destroyAllWindows()