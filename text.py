# imports to add

import matplotlib.pyplot as plt # type: ignore
import easyocr # type: ignore
import cv2 # type: ignore



# read image

img_path = 'F:\Utorrent downloads\Projects\data\test1.png'

img = cv2.imread(img_path)

# (Instance text detector)

reader = easyocr.Reader( ['en']  , gpu = False )
# Detect image text

text_ = reader.readtext(img)
print(text_)

threshold = 0.25
for i in text_:
    print(i)

    bbox , text , score = i 
    
    if score > threshold:
        cv2.rectangle(img , bbox [0] , bbox[2] , (0,255,0), 5 )
        cv2.putText( img , text, bbox[0] , cv2.FONT_HERSHEY_COMPLEX , 1 , ( 255 , 0, 8) , 2 )





plt.imshow( cv2.cvtColor( img , cv2.COLOR_BGR2RGB ))

plt.show()






# Draw box and text show
