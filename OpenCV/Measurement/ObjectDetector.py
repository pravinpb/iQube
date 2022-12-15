# import cv2
# import matplotlib.pyplot as plt

# cap = cv2.VideoCapture(0)

# human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# while True:
#     ret,frame = cap.read()

#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     humans = human_cascade.detectMultiScale(gray,9,1)

#     for (x,y,w,h) in humans:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) == 81:
#         break


# import cv2
# import imutils
   
# # Initializing the HOG person
# # detector
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
   
# cap = cv2.VideoCapture('https://192.168.206.44.8080')
   
# while cap.isOpened():
#     # Reading the video stream
#     ret, image = cap.read()
#     if ret:
#         image = imutils.resize(image, 
#                                width=min(400, image.shape[1]))
   
#         # Detecting all the regions 
#         # in the Image that has a 
#         # pedestrians inside it
#         (regions, _) = hog.detectMultiScale(image,
#                                             winStride=(4, 4),
#                                             padding=(4, 4),
#                                             scale=1.05)
   
#         # Drawing the regions in the 
#         # Image
#         for (x, y, w, h) in regions:
#             cv2.rectangle(image, (x, y),
#                           (x + w, y + h), 
#                           (0, 0, 255), 2)
   
#         # Showing the output Image
#         cv2.imshow("Image", image)
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#     else:
#         break
  
# cap.release()
# cv2.destroyAllWindows()



# import cv2 
# import imutils 
   
# # Initializing the HOG person 
# hog = cv2.HOGDescriptor() 
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 
   
# # Reading the Image 
# image = cv2.imread('2.jpg') 
   
# # Resizing the Image 
# image = imutils.resize(image, 
#                        width=min(500, image.shape[1])) 
   
# # Detecting all humans 
# (humans, _) = hog.detectMultiScale(image,  
#                                     winStride=(5, 5), 
#                                     padding=(3, 3), 
#                                     scale=1.21)
# # getting no. of human detected
# print('Human Detected : ', len(humans))
   
# # Drawing the rectangle regions
# for (x, y, w, h) in humans: 
#     cv2.rectangle(image, (x, y),  
#                   (x + w, y + h),  
#                   (0, 0, 255), 2) 
  
# # Displaying the output Image 
# cv2.imshow("Image", image) 
# cv2.waitKey(0) 
   
# cv2.destroyAllWindows()












import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

img = cv2.imread('3.jpg')
bbox, label, conf = cv.detect_common_objects(img,confidence=0.7,model='yolov3-tiny')
for l,c in zip(label,conf):
    print(f'Detected {l} with confideance level {c}')

print(bbox)
img = draw_bbox(img,bbox,label,conf)
cv2.imshow('Image',img)

cv2.waitKey(0)
 

cv2.destroyAllWindows()



