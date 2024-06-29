import mediapipe as mp
import cv2
import PoseModule as pm 



cap = cv2.VideoCapture("Man Skipping.mp4")
detector = pm.poseDetector()

while True:
       ret, frame = cap.read()
       resized = cv2.resize(frame,(400,600))
       resized1 = detector.findPose(resized)
       lmList = detector.findPosition(resized,draw=False)
       #cv2.circle(resized,(lmList[14][1],lmList[14][2]),15,(0,0,255),cv2.FILLED)
       print(lmList)
       if len(lmList) != 0:
             detector.findAngle(resized1,11,13,15)
             detector.findAngle(resized1,12,14,16)
             detector.findAngle(resized1,23,25,27)
             detector.findAngle(resized1,24,26,28)

    
       cv2.imshow("biceps", resized1)
    
       if cv2.waitKey(1) == ord('q'):
           break
         
    # Release camera and close windows
cap.release()
cv2.destroyAllWindows() 
