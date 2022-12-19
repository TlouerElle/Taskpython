import cv2
import numpy as np


def video_demo():
    # 调用摄像头
    capture = cv2.VideoCapture(0)
    while (True):
        # 读取我们摄像头里面的类容
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        # 显示每一帧
        face_patterns = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
        faces = face_patterns.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
        print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("jiemian", frame)
        c = cv2.waitKey(1)
        if c == 27:
            break


video_demo()
