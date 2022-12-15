import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


cap = cv2.VideoCapture(0)
 
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret , img = cap.read()

    img = cv2.flip(img,1)

    g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f = face_cascade.detectMultiScale(g,1.3,5)
    e = eye_cascade.detectMultiScale(g,1.3,5)

    c = 0
    d = 0

    for (a,b,c,d) in e:
        # print(x,y,w,h)
        cv2.rectangle(img, (a,b),(a+c,b+d),(0,255,0),4)
        c = 1

    for (x,y,w,h) in f:
        # print(x,y,w,h)
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),4)
        d = 1


        if c == 1:
            if d == 1:
                cv2.putText(img, "Eyes Open", (20,30), font, 1,(0,0,255),3, cv2.LINE_AA)
        else:
                cv2.putText(img, "Eyes Closed", (20,30), font, 1,(0,0,255),3, cv2.LINE_AA)

                
    cv2.imshow('img',img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


