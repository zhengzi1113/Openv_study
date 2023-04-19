# 加载视频
import cv2
import numpy as np

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 800, 600)
cap = cv2.VideoCapture('video/video1.mp4')
# 创将mog对象， 去背景算法
mog = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

while True:
    ret, frame = cap.read()
    if ret == True:

        # 灰度化， 去噪声
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.bilateralFilter(gray, 7, sigmaColor=30, sigmaSpace=50)
    
        # 调用mog
        fgmask = mog.apply(blur)

        # 腐蚀， 膨胀
        erode = cv2.erode(fgmask, kernel, iterations=2)
        dialte = cv2.dilate(erode, kernel, iterations=2)

        # 消除内部小块 闭运算
        close = cv2.morphologyEx(dialte, cv2.MORPH_CLOSE, kernel)

        # 查找轮廓
        contours, hierachy = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # 画出轮廓
        for contour in contours:
            # 最大外接矩形
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (int(x), int(y)), (int(x+w), int(y+h)), (0, 0, 255), 2)
            # 展示视 cv2.resizeWindow('video', 800, 600)
        cv2.imshow('video', frame)

        key = cv2.waitKey(100)
        # 按Esc推出
        if(key & 0xFF == ord('q')):
            break
             
    else:
        break

cap.release()
cv2.destroyAllWindows()
