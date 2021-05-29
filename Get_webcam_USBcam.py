#  open webcam
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

#  access to USB camera 
# Important , by default with computers which come with an integrated camera , 
# the camera index most of the time is 0 !!! But it's can be 1 or 2 ...

import cv2
import numpy as np


all_indx_available = []

for indx in range(5):
    cap = cv2.VideoCapture(indx)
    if cap.isOpened():
        print(f'Camera index available: {indx}')
        all_indx_available.append(indx)
        cap.release()
        
