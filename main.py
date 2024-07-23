import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while True:
    _ , frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    
    # For Red COLOR
    low_red = np.array([161,165,84])
    high_red = np.array([179,255,255])
    # Creating a mask 
    red_mask = cv2.inRange( hsv_frame , low_red , high_red )
    red = cv2.bitwise_and( frame , frame , mask = red_mask )
    
    # For Blue COLOR
    low_blue = np.array([94,80,20])
    high_blue = np.array([126,255,255])
    # Creating a mask 
    blue_mask = cv2.inRange( hsv_frame , low_blue , high_blue )
    blue = cv2.bitwise_and( frame , frame , mask = blue_mask )
    
    

    # For Green COLOR
    low_green = np.array([25,52,72])
    high_green = np.array([102,255,255])
    # Creating a mask 
    green_mask = cv2.inRange( hsv_frame , low_green , high_green )
    green = cv2.bitwise_and( frame , frame , mask = green_mask )
    
    # For all COLORs except White
    low = np.array([0,42,0])
    high = np.array([179,255,255])
    # Creating a mask 
    mask = cv2.inRange( hsv_frame , low , high )
    result = cv2.bitwise_and( frame , frame , mask = mask )
    
    
    
    
    
    
    
    
    # Running above  Masks
    

    # cv2.imshow( "Frame" , frame )
    
    # cv2.imshow( "Red Mask" , red )
    
    # cv2.imshow( "Blue Mask" , red )
    
    # cv2.imshow( "Green Mask" , red )
    
    cv2.imshow( "Result" , result )
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()


  

       
