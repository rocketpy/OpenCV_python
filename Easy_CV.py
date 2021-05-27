#  Easy_CV is a easy Computer Vision solution for making project faster

# Github: https://github.com/Shaswatadatta7/Easy_CV

#  pip install Easy-CV

# Easy_CV uses a number of open source projects to work properly:
# Open CV
# Meadipipe

import time
import cv2
from Easy_CV import HandTracker, handDetector


pTime = 0
cTime = 0

cap = cv2.VideoCapture(0)
detector = handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
               (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

