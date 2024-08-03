# Imports to add in Python

import cv2
import pyzbar # library to read qr codes and bar codes
import matplotlib.pyplot as plt
import numpy as np


import os 
from pyzbar.pyzbar import decode

# Steps for QR Reader

# input_dir = '/G:/Computer Vision/PortFolio/img-1.jpeg'
input_dir = 'G:\Computer Vision\PortFolio\qr-reader-attendance-system-master\img-1.jpeg'

for j in sorted(os.listdir(input_dir)):
    # Imread always reads image....
    img = cv2.imread(os.path.join(input_dir,j ))
    
    qr_info = decode(img)
    
    # print(qr_info)
    
    for qr in qr_info:
        data = qr.data
        rect = qr.rect
        polygon = qr.polygon
        
            
        print(data)
        print(rect)
        print(polygon)
        
        
        img = cv2.rectangle(img , (rect.left , rect.top ) , (rect.left+ rect.width , rect.top + rect.height) , (0,255,0) , 5 )
        
        img = cv2.polygon( img , [np.array(polygon)] , True ,(255,0,0),5)
        
        
    
        
        plt.imshow( cv2.cvtColor(img , cv2.COLOR_BAYER_BG2BGR))
        plt.show()
        
        
        
    
    
    
    
    
    
    