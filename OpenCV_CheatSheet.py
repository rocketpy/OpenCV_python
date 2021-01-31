#  importing an image and viewing
import cv2


image = cv2.imread("file_name")  # or path to file 
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

