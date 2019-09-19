import cv2


capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    raise Exception("Not open")

ret, frame = capture.read()
capture.release()



#  in Jupyter Notebook to display the picture 
"""
import sys
from matplotlib import pyplot as plt


frameRGB = frame[:,:,::-1] #  BGR to RGB
plt.imshow(frameRGB)
"""





