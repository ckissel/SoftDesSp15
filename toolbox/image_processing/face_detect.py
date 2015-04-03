""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('/home/caleb/Downloads/haarcascade_frontalface_alt.xml')


kernel = np.ones((21,21),'uint8')

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    for (x,y,w,h) in faces:
    	frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
    	cv2.circle(frame,(x+60,y+50),30,(225,0,0))
    	cv2.circle(frame,(x+160,y+50),30,(225,0,0))
    	cv2.rectangle(frame,(x+10,y+150),(x+180, y+190),(255,0,0))

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()