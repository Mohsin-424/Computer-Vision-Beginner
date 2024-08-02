# Imports to add in Python

import cv2
import pyzbar # library to read qr codes and bar codes
import matplotlib as plt

import os 
from pyzbar.pyzbar import decode

# Steps for QR Reader

input_dir = '/G:\Computer Vision\PortFolio/img-1.jpeg'

for j in sorted( os.listdir ( input_dir )):
    # Imread always reads image....
    img = cv2.imread( os.path.join( input_dir ,j ))
    
    qr_info = decode(img)
    
    print(qr_info)
    
    
    
    
    
    