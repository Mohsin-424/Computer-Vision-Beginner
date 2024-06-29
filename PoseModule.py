import cv2
import mediapipe as mp
import math



class poseDetector():
    def __init__(self,mode=False,modelComp=1,smoothlm=True,segment=False,smoothsegment=True,detectionCon=0.5, trackingCon=0.5):
         
       self.mode=mode
       self.modelComp=modelComp
       self.smoothlm=smoothlm
       self.segment=segment
       self.smoothsegment=smoothsegment
       self.detectionCon = detectionCon
       self.trackingCon = trackingCon

       self.mpDraw = mp.solutions.drawing_utils
       self.mpPose = mp.solutions.pose
       self.pose = self.mpPose.Pose(self.mode,self.modelComp,self.smoothlm,self.segment,self.smoothsegment,self.detectionCon,self.trackingCon)
 

    def findPose(self,frame, draw=True):
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(frameRGB)
        if self.results.pose_landmarks:
           if draw:
              self.mpDraw.draw_landmarks(frame, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return frame

    def findPosition(self,frame,draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id , lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = frame.shape
                cx , cy = int(lm.x*w), int(lm.y*h)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(frame,(cx,cy),5,(0,0,255),cv2.FILLED)
        return self.lmList

    def findAngle(self, frame , p1, p2, p3, draw = True):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]
        
        radians = math.atan2(y3-y2,x3-x2) - math.atan2(y1-y2,x1-x2)
        angle = math.degrees(radians)
        if angle < 0:
            angle = angle + 360
        if angle > 180:
            angle = 360 - angle 
    
        if draw:
            cv2.circle(frame,(x1,y1),5,(0,0,255),cv2.FILLED)
            cv2.circle(frame,(x1,y1),10,(0,0,255),2)
            cv2.circle(frame,(x2,y2),5,(0,0,255),cv2.FILLED)
            cv2.circle(frame,(x2,y2),10,(0,0,255),2)
            cv2.circle(frame,(x3,y3),5,(0,0,255),cv2.FILLED)
            cv2.circle(frame,(x3,y3),10,(0,0,255),2)
            cv2.putText(frame, str(int(angle)), (x2,y2), cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,0),2)
        return angle


def main():
    cap = cv2.VideoCapture("Man Skipping.mp4")
    detector = poseDetector()

    while True:
       ret, frame = cap.read()
       resized = cv2.resize(frame,(400,600))
       resized1 = detector.findPose(resized)
       #lmList = detector.findPosition(resized,draw=False)
       #cv2.circle(resized,(lmList[14][1],lmList[14][2]),15,(0,0,255),cv2.FILLED)
       #print(lmList[14])
       cv2.imshow("biceps", resized1)
    
       if cv2.waitKey(1) == ord('q'):
           break
         
    # Release camera and close windows
    cap.release()
    cv2.destroyAllWindows() 


if __name__ == "__main__":
    main()