import cv2
import numpy as np

face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray)
    eyes = eye.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    if ((cv2.waitKey(5) & 0xFF) == 27):
        break
    cv2.imshow("cap", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()