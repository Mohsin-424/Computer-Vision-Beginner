from ultralytics import YOLO
import cv2
import numpy as np
import cvzone
import numpy as np


cap = cv2.VideoCapture("bicep.mp4")



while True:
    rt,frame=cap.read()
    frame = cv2.resize(frame,(600,480))
    
    
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
    
