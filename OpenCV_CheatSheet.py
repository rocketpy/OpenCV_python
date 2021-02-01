#  importing an image and viewing
import cv2


image = cv2.imread("file_name")  # or path to file 
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


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
percent = 20  # percent of original size
width = int(img.shape[1] * percent / 100)
height = int(img.shape[0] * percent / 100)
dimen = (width, height)
resized = cv2.resize(img, dimen, interpolation = cv2.INTER_AREA)
view_image(resized, "Result after resizing with 20%")

