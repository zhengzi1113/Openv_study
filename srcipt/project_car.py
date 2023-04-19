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
        blur = cv2.GaussianBlur(gray, (3, 3), 5)
    
        # 调用mog
        fgmask = mog.apply(blur)

        # 腐蚀， 膨胀
        erode = cv2.erode(fgmask, kernel)
        dialte = cv2.dilate(erode, kernel)

        # 消除内部小块 闭运算
        close = cv2.morphologyEx(dialte, cv2.MORPH_CLOSE, kernel)

        # 展示视频
        cv2.resizeWindow('video', 800, 600)
        cv2.imshow('video', close)

        key = cv2.waitKey(100)
        # 按Esc推出
        if(key & 0xFF == ord('q')):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
