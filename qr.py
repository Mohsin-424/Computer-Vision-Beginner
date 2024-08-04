# Imports
import cv2  # OpenCV library for image processing
import pyzbar  # Library for reading QR codes and barcodes
import matplotlib.pyplot as plt  # For displaying images
import numpy as np  # For numerical operations on arrays
import os  # For file and directory operations
from pyzbar.pyzbar import decode  # QR code decoding function

# Define the path to the image file
input_dir = 'G:\\Computer Vision\\PortFolio\\img-1.jpeg'

# Check if the input path is a file and not a directory
if not os.path.isfile(input_dir):
    print(f"The file {input_dir} does not exist or is not a file.")
else:
    # Read the image from the specified path
    img = cv2.imread(input_dir)

    # Check if the image was loaded successfully
    if img is None:
        print(f"Failed to load image: {input_dir}")
    else:
        # Decode QR codes in the image
        qr_info = decode(img)

        # Iterate over each detected QR code
        for qr in qr_info:
            data = qr.data.decode('utf-8')  # Decode the data from bytes to string
            rect = qr.rect  # Rectangle bounding the QR code
            polygon = qr.polygon  # Polygon points for the QR code

            # Print QR code information
            print(f"Data: {data}")
            print(f"Rect: {rect}")
            print(f"Polygon: {polygon}")

            # Draw a rectangle around the QR code
            img = cv2.rectangle(img, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height),
                                (0, 255, 0), 2)  # Color: Green, Thickness: 2

            # Draw the polygon around the QR code
            if len(polygon) > 0:
                pts = np.array(polygon, dtype=np.int32)  # Convert polygon points to integer array
                pts = pts.reshape((-1, 1, 2))  # Reshape points for cv2.polylines
                img = cv2.polylines(img, [pts], True, (255, 0, 0), 2)  # Color: Red, Thickness: 2

        # Convert the image from OpenCV (BGR) to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Display the image using matplotlib
        plt.imshow(img_rgb)
        plt.axis('off')  # Hide axes
        plt.show()
