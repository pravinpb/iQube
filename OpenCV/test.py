from tkinter import Frame
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAD_PROP_FPS,10)
while True:
    ret , Frame = cap.read()

    grey = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',grey)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()