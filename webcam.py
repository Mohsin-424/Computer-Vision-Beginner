import numpy as np
import cv2
from pyzbar.pyzbar import decode

def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def draw_text(image, text, position, font, font_scale, color, thickness, max_width):
    words = text.split()
    line = ""
    y = position[1]

    for word in words:
        test_line = line + word + ' '
        (w, h), _ = cv2.getTextSize(test_line, font, font_scale, thickness)
        if w > max_width:
            cv2.putText(image, line, (position[0], y), font, font_scale, color, thickness)
            line = word + ' '
            y += h + 10
        else:
            line = test_line

    cv2.putText(image, line, (position[0], y), font, font_scale, color, thickness)

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
            binary_data = text_to_binary(data)  # Convert the text to binary
            
            # Print the decoded data and its binary format to the terminal
            print(f"Decoded data: {data}")
            print(f"Binary format: {binary_data}")
            
            rect = qr.rect  # Rectangle bounding the QR code
            polygon = qr.polygon  # Polygon points for the QR code
            
            # Display the binary data above the QR code
            draw_text(frame, binary_data, (rect.left, rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, rect.width)

            # Draw a rectangle around the QR code
            frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 2)
            
            # Draw the polygon around the QR code
            if len(polygon) > 0:
                pts = np.array(polygon, dtype=np.int32)  # Convert polygon points to integer array
                pts = pts.reshape((-1, 1, 2))  # Reshape points for cv2.polylines
                frame = cv2.polylines(frame, [pts], True, (255, 0, 0), 2)  # Color: Red, Thickness: 2

    # Resize the frame
    frame_resized = cv2.resize(frame, (800, 600))  # Adjust the width and height as needed
    
    cv2.imshow('webcam', frame_resized)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
