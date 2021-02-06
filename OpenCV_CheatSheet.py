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
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # it's a grayscale one-channel version 
ret, threshold_image = cv2.threshold(im, 127, 255, 0)  # threshold made darker (smaller) than 127 to 0 and all brighter (greater) to 255
view_image(gray_image, "Image in gray-scale")
view_image(threshold_image, "Black & White image")
#  ret, threshold = cv2.threshold(im, 150, 200, 10)  # shades be a smaller than 150 to 10 and all greater to 200


#  Writing some text on an image
result = image.copy()
cv2.putText(result, "Write here any ...", (1500, 3600), cv2.FONT_HERSHEY_SIMPLEX, 15, (30, 105, 210), 40) 
view_image(output, "New image with some text")


#  Blurring or Smoothing
blurred_img = cv2.GaussianBlur(image, (51, 51), 0)
view_image(blurred_img, "Blurred image")


#  Drawing a rectangle on an image
result = image.copy()
cv2.rectangle(result, (2600, 800), (4100, 2400), (0, 255, 255), 10)
view_image(result, "New image with a rectangle") 
"""
The rectangle function takes 5 parameters:
    The first parameter is the image.
    The second parameter is x1, y1 — Top Left Corner.
    The third parameter is x2, y2 — Bottom Right Corner.
    The fourth parameter is the rectangle color (GBR/RGB, depending on how you imported your image).
    The fifth parameter is the rectangle line thickness.
"""
 
    
#  Using transpose() method , like rotate
import cv2 
  

path = r'C:\Users\user\Desktop\image_name.png'
img = cv2.imread(path) 
window_name = 'Image' 
trans_image = cv2.transpose(img) 
cv2.imshow(window_name, trans_image) 
cv2.waitKey(0) 


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
 
