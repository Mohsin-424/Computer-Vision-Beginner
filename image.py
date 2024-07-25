# Prepeare Data(Data preprocessing)
# Train / Test Split
# Train Classifier
# Test Performance 

import numpy as np
import cv2
import os
from skimage.io import imread
from skimage.transform import resize



# Prepeare Data(Data preprocessing)
input_dir = 'G:\Computer Vision\Computer-Vision-Beginner\Image-Classification\clf-data'
categories = ['empty','non_empty']

data = []
labels= []

for category in categories:
    for file in os.listdir(os.path.join(input_dir,category)):
        img_path = os.path.join(input_dir,category,file)
        img = imread(img_path)
        img = resize(img,(15,15))
        data.append(img.flatted())
        
        
        
        

