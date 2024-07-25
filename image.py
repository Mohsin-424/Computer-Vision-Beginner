# Prepeare Data(Data preprocessing)
# Train / Test Split
# Train Classifier
# Test Performance 

import numpy as np
import cv2
import os
from skimage.io import imread
from skimage.transform import resize



# 1. Prepeare Data(Data preprocessing)

input_dir = 'G:\Computer Vision\Computer-Vision-Beginner\Image-Classification\clf-data' # change data path accordingly
categories = ['empty','non_empty']




# Initializing Data Containers for Iamges
data = []
labels= []

# Loading and Processing Images
for category_idex ,category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir,category)):
        img_path = os.path.join(input_dir,category,file)
        img = imread(img_path)
        img = resize(img,(15,15))
        data.append(img.flatted())
        labels.append(category_idex)


# Converting Lists to Arrays
data = np.asarray(data)
labels = np.asarray(labels) 
        

        

