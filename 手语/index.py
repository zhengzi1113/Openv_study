import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time 
import mediapipe as mp

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def mediapipe_datection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 改变颜色通道
    image.flags.writeable = False                   # 使得图片不可写
    results = model.process(image)                  # 预测
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

#获取视频设备
cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as holistic:
 
    # 判断摄像头是否打开
    while cap.isOpened():

        #从摄像头读视频帧
        ret, frame = cap.read()
        #检测
        image, results = mediapipe_datection(frame, holistic)
        print(results)

        if ret == True:
            cv2.imshow("video", frame)
            key = cv2.waitKey(10)
            if(key & 0xFF == ord('q')):
                break
        else:
            break

#释放资源
cap.release()