import os
import datetime
import time

import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Load authorized users
with open('./whitelist.txt', 'r') as f:
    authorized_users = [l.strip() for l in f.readlines() if len(l) > 2]

log_path = './log.txt'

# Open the camera
cap = cv2.VideoCapture(0)  # Change index if needed

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

most_recent_access = {}
time_between_logs_th = 5

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    qr_info = decode(frame)

    if qr_info:
        qr = qr_info[0]
        data = qr.data.decode()
        rect = qr.rect
        polygon = qr.polygon

        if data in authorized_users:
            cv2.putText(frame, 'ACCESS GRANTED', (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            if data not in most_recent_access.keys() or time.time() - most_recent_access[data] > time_between_logs_th:
                most_recent_access[data] = time.time()
                with open(log_path, 'a') as f:
                    f.write('{},{}\n'.format(data, datetime.datetime.now()))
        else:
            cv2.putText(frame, 'ACCESS DENIED', (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 5)
        frame = cv2.polylines(frame, [np.array(polygon)], True, (255, 0, 0), 5)

    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
