import cv2
import numpy as np


image = cv2.imread('2.jpg', 1)

# copying origin image
output = image.copy()

# change image to colorless
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100,
                           param1=250,
                           param2=50,
                           minRadius=10,
                           maxRadius=100)
# painting circles on image
circles2 = np.uint16(np.around(circles))

for i in circles2[0, :]:
    cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('image', output)
k = cv2.waitKey(0)  # & 0xFF

