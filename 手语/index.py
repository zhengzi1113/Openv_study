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

def draw_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

def draw_styled_landmarks(image,results):
    # Draw face connections
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS, 
                            mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                            mp_drawing.DrawingSpec(color=(88,256,121), thickness=1, circle_radius=1))
    # Drow pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                            mp_drawing.DrawingSpec(color=(80,220,10), thickness=2, circle_radius=4),
                            mp_drawing.DrawingSpec(color=(80,4,121), thickness=2, circle_radius=2))
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                            mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                            mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2))
    # Draw right hand conections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                            mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                            mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

#获取视频设备
cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as holistic:
 
    # 判断摄像头是否打开
    while cap.isOpened():

        #从摄像头读视频帧
        ret, frame = cap.read()
        #检测
        image, results = mediapipe_datection(frame, holistic)
        # print( len(results.left_hand_landmarks.landmark))
        #绘制
        draw_styled_landmarks(image, results)
        if ret == True:
            cv2.imshow("video", image)
            key = cv2.waitKey(10)
            if(key & 0xFF == ord('q')):
                break
        else:
            break


#释放资源
cap.release()