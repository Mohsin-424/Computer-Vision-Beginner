import numpy as np
import cv2
from pyzbar.pyzbar import decode

# Load authorized users from whitelist
authorized_users = []
with open("./whitelist.txt", 'r') as f:
    authorized_users = [line.strip() for line in f.readlines() if len(line.strip()) > 0]

# Path to log file
log_path = './log.txt'

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture image")
        break
    
    qr_info = decode(frame)
    
    if qr_info:
        for qr in qr_info:
            data = qr.data.decode('utf-8')
            rect = qr.rect
            polygon = qr.polygon
            
            if data in authorized_users:
                status = "ACCESS GRANTED"
                color = (0, 255, 0)
            else:
                status = "ACCESS DENIED"
                color = (0, 0, 255)
                
            cv2.putText(frame, status, (rect.left, rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), color, 5)
            
            if polygon:
                pts = np.array(polygon, dtype=np.int32)
                pts = pts.reshape((-1, 1, 2))
                frame = cv2.polylines(frame, [pts], True, color, 5)

    frame_resized = cv2.resize(frame, (800, 600))
    
    cv2.imshow('webcam', frame_resized)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
