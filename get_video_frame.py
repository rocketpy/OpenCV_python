import cv2


some_video = 'name_video.avi'
cap = cv2.VideoCapture(some_video)

# number of frames in the video
# print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
current_frame = 0

ret, frame = cap.read()

while ret:
    cv2.imwrite('frames/frame' + str(current_frame) + '.jpg', frame)
    current_frame += 1
    ret, frame = cap.read()

cap.release()
 
