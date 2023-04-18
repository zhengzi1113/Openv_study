# 加载视频
import cv2
import numpy as np

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture('.video/video.mp4')
print(cap)

while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('video', frame)
    
    key = cv2.waitKey(40)
    # 按Esc推出
    if (key & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
