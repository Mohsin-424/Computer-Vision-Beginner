import mediapipe as mp

import cv2

# Read Image

# img_path = './data/testImg.png'
img_path = './data/testNoFace.jpg'

img = cv2.imread(img_path)

H , W, _ = img.shape
# Detect Faces
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection = 0,min_detection_confidence = 0.5  ) as face_detection:
    # pass
    img_rgb = cv2.cvtColor( img , cv2.COLOR_BGR2RGB)
    out = face_detection.process( img_rgb )
    # To detect a Human face if not any face then there wll be noneType as result 
    print( out.detections )  # Just to print output for keypoints
    
    
    if out.detections in out.detections:
       for detection in out.detections:
        
        location_data = detection.location_data
        
        bbox = location_data.relative_bounding_box
        
        x1 , y1, w, h = bbox.xmin , bbox.ymin , bbox.width,  bbox.height
        
        x1 = int( x1 * W)
        y1 = int( y1 * W)
        w = int( w * W)
        h = int( h * W)
        
        cv2.rectangle( img , ( x1 , y1) , (x1 * w ,  y1 * h ) , ( 0 , 255, 0 ) , 10 )
        
# Blur Faces




# Save Images
