import  cv2

cap = cv2.VideoCapture(0)


while True:
    _,frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.line(frame, (100,100), (200,200),(0,0,255), 10)
    cv2.rectangle(frame,(100,100), (200,200),(0,0,255), 10)
    

    cv2.imshow("Webcam", frame)
    if ((cv2.waitKey(5) & 0xFF) == 27):
        break

cap.release()
cv2.destroyAllWindows()