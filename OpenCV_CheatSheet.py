#  Good example at bellow !

#  Importing an image and viewing
import cv2


image = cv2.imread("file_name")  # or path to file 
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#  Saving the image
image = cv2.imread("file_name or Path to file")
cv2.imwrite("file_name", image)


#  IMPORTANT
# On reading images this way via openCV, it isn’t in RGB colorspace—it’s in BGR !!!
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


#  best practice using a method
def view_image(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 

#  Cropping
cropped = image[10:500, 500:2000]
view_image(cropped, "Image after cropping")
#  image[10:500, 500:2000] is image[y:y+h, x:x+w]


#  Resizing
#  for more info:   https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
percent = 20  # percent of original size
width = int(img.shape[1] * percent / 100)
height = int(img.shape[0] * percent / 100)
dimen = (width, height)
resized = cv2.resize(img, dimen, interpolation = cv2.INTER_AREA)
view_image(resized, "Result after resizing with 20%")


#  Rotating
(h, w, d) = image.shape
center = (w // 2, h // 2)
MATRIX = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, MATRIX, (w, h))
view_image(rotated, "Image after rotation")


#  Grayscaling and Thresholding it's a black & white effects
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(im, 127, 255, 0)
view_image(gray_image, "Image in gray-scale")
view_image(threshold_image, "Black & White image")


#  Example , with path and directories
import os
import cv2  
  
    
# image path
image_path = r'C:\Users\Rajnish\Desktop\GeeksforGeeks\geeks.png' 
# image directory
directory = r'C:\Users\Rajnish\Desktop\GeeksforGeeks'  
  
img = cv2.imread(image_path) 
  
# change the current directory to specified directory  
os.chdir(directory) 
  
# files and directories in 'C:/Users/...'   
print("Before saving image: ")   
print(os.listdir(directory))   
  
filename = 'saved_image.jpg'
# saving the image 
cv2.imwrite(filename, img) 
  
# files and directories in 'C:/Users/...'   
print("After saving image: ")   
print(os.listdir(directory)) 
print('Successfully saved !') 
 
