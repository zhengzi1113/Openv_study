# 加载视频
import cv2
import numpy as np

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 800, 600)
cap = cv2.VideoCapture('video/video1.mp4')


min_w = 50
min_h = 50
max_w = 150
max_h = 150

line_hight = 550

# 偏移量
offset = 6

cars = []
carcount = 0

def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = int(x) + x1
    cy = int(y) + y1
    return cx, cy


# 创将mog对象， 去背景算法
mog = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

while True:
    ret, frame = cap.read()
    if ret == True:

        # 灰度化， 去噪声
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), sigmaX=10)
        # 调用mog
        fgmask = mog.apply(blur)

        # 腐蚀， 膨胀
        erode = cv2.erode(fgmask, kernel, iterations=1)
        dialte = cv2.dilate(erode, kernel, iterations=3)

        # 消除内部小块 闭运算
        close = cv2.morphologyEx(dialte, cv2.MORPH_CLOSE, kernel)

        # 查找轮廓
        contours, hierachy = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # 画线
        cv2.line(frame, (10, line_hight), (1200, line_hight), (0,0,255), 3)

        # 画出轮廓
        for contour in contours:
            # 最大外接矩形
            (x, y, w, h) = cv2.boundingRect(contour)
             # 通过宽高大小过滤小的
            if w >= min_w and h >= min_h and w <= max_w and h <= max_h:
                cv2.rectangle(frame, (int(x), int(y)), (int(x+w), int(y+h)), (0, 0, 255), 2)
                cpiont = center(x, y, w, h)
                cars.append(cpiont)
                cv2.circle(frame, (cpiont), 5, (0, 0, 200), -1)
                for (x, y) in cars:
                    if y > line_hight - offset and y < line_hight + offset:
                        carcount += 1
                        cars.remove((x, y))
               
        
        # 展示
        cv2.putText(frame, 'CAR Count : '+ str(carcount), (300, 60) , cv2.FONT_HERSHEY_DUPLEX, 2, (200, 233, 0), 5) 
        cv2.imshow('video', frame)

        key = cv2.waitKey(100)
        # 按Esc推出
        if(key & 0xFF == ord('q')):
            break
             
    else:
        break

cap.release()
cv2.destroyAllWindows()

