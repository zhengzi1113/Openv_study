from multiprocessing.connection import wait
import matplotlib.pyplot as plt
import cv2

#创建Videowriter为写多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
vm = cv2.VideoWriter("/home/xiang/OpenCV/video/out.mp4", fourcc, 25 ,(1280, 720))

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 360)

#获取视频设备
cap = cv2.VideoCapture(0)

#获取视频文件
# cap = cv2.VideoCapture("/home/zheng/Openv_study/video/out.mp4")

# 判断摄像头是否打开
while cap.isOpened():

    #从摄像头读视频帧
    ret, frame = cap.read()

    if ret == True:

        cv2.imshow("video", frame)
        # cv2.resizeWindow('video', 640, 360)

        #写数据到多媒体文件
        # vm.write(frame)

        key = cv2.waitKey(40)
        if(key & 0xFF == ord('q')):
            break
    else:
        break

#释放资源
cap.release()
vm.release()
cv2.destroyAllWindows()



