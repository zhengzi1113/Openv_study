import cv2
import matplotlib.pyplot as plt

cv2.namedWindow('new', cv2.WINDOW_NORMAL)

img = plt.imread("/home/xiang/OpenCV/img/5.gif",1)

# print(img)
# cv2.resizeWindow("new", 100, 222)

while True:
    cv2.imshow('new',img)

    # 显示时长
    key = cv2.waitKey(0)
    # ord() 转化为SACLL值 
    if(key == ord('q')):
        cv2.destroyAllWindows()
        break
    elif(key == ord('s')):
        cv2.imwrite("/home/xiang/OpenCV/img"+'.png', img)
exit()

