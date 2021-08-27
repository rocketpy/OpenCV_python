# Using ImageHash
import imagehash
from PIL import Image


hash_1 = imagehash.average_hash(Image.open('image_name.jpg')) 
hash_2 = imagehash.average_hash(Image.open('image_name_2.jpg')) 

cutoff = 5  # maximum bits that could be different between the hashes. 

if hash_1 - hash_2 < cutoff:
  print('Images are similar')
else:
  print('Images are not similar')


#  without openCV
# IMPORTANT - if you have colored pictures you have to do this in all 3 dimensions or just compare a greyscaled version !!!
import numpy as np


pic_1 = np.random.rand(100, 100)
pic_2 = np.random.rand(100, 100)
pic_1_norm = pic_1/np.sqrt(np.sum(picture1**2))
pic_2_norm = pic_2/np.sqrt(np.sum(picture2**2))

# If compare similar pictures the sum will return 1
print(np.sum(pic_1_norm**2))
# result: 1.0

# If they aren't similar, we'll get a value between 0 and 1 (a percentage if you multiply by 100)
print(np.sum(pic_2_norm*pic_1_norm))
# result: 0.82362519392365335


# With OpenCV
import cv2
  
     
# test image
image = cv2.imread('cat.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([gray_image], [0],
                         None, [256], [0, 256])
  
# data1 image
image = cv2.imread('cat.jpeg')
gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram1 = cv2.calcHist([gray_image1], [0],
                          None, [256], [0, 256])
  
# data2 image
image = cv2.imread('food.jpeg')
gray_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram2 = cv2.calcHist([gray_image2], [0],
                          None, [256], [0, 256])

  
c1, c2 = 0, 0
  
# Euclidean Distance between data1 and test
i = 0
while i<len(histogram) and i<len(histogram1):
    c1+=(histogram[i]-histogram1[i])**2
    i+= 1
c1 = c1**(1 / 2)
  
 
# Euclidean Distance between data2 and test
i = 0
while i<len(histogram) and i<len(histogram2):
    c2+=(histogram[i]-histogram2[i])**2
    i+= 1
c2 = c2**(1 / 2)
  
if(c1<c2):
    print("data1.jpg is more similar to test.jpg as compare to data2.jpg")
else:
    print("data2.jpg is more similar to test.jpg as compare to data1.jpg")
  
  

