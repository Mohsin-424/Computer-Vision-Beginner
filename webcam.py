import numpy as np
import cv2
from pyzbar.pyzbar import decode

# Load the image directly
image_path = 'G:\\Computer Vision\\PortFolio\\img-1.jpeg'
frame = cv2.imread(image_path)

if frame is None:
    print("Failed to load image")
else:
    qr_info = decode(frame)
    
    if len(qr_info) > 0:
        for qr in qr_info:
            data = qr.data.decode('utf-8')
            rect = qr.rect
            polygon = qr.polygon
            
            cv2.putText(frame, data, (rect.left, rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 5)
            
            if len(polygon) > 0:
                pts = np.array(polygon, dtype=np.int32)
                pts = pts.reshape((-1, 1, 2))
                frame = cv2.polylines(frame, [pts], True, (255, 0, 0), 5)

    cv2.imshow('webcam', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
