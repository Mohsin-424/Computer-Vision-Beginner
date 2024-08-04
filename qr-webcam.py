import numpy as np
import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture image")
        break
    
    qr_info = decode(frame)
    
    if len(qr_info) > 0:
        for qr in qr_info:
            data = qr.data.decode('utf-8')  # Decode the data from bytes to string
            rect = qr.rect  # Rectangle bounding the QR code
            polygon = qr.polygon  # Polygon points for the QR code

            # Draw a rectangle around the QR code
            frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 5)
            
            # Draw the polygon around the QR code
            if len(polygon) > 0:
                pts = np.array(polygon, dtype=np.int32)  # Convert polygon points to integer array
                pts = pts.reshape((-1, 1, 2))  # Reshape points for cv2.polylines
                frame = cv2.polylines(frame, [pts], True, (255, 0, 0), 5)  # Color: Red, Thickness: 5

    cv2.imshow('webcam', frame)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
