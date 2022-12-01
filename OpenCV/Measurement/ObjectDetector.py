import cv2

net = cv2.dnn.readNet(r'C:\Users\Pravin P B\Documents\GitHub\iQube\OpenCV\Measurement\dnn_model\yolov4-tiny.weights',r'C:\Users\Pravin P B\Documents\GitHub\iQube\OpenCV\Measurement\dnn_model\yolov4-tiny.cfg')
model = cv2.dnn_DetectionModel()
cap = cv2.VideoCapture('http://192.168.21.63:8080/shot.jpg')

while True:
    ret, frame = cap.read()

    cv2.imshow('Frame',frame)
    cv2.waitKey(1)