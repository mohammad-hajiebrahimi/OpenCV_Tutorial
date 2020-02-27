import  cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("out.avi", fourcc, 24.0, (640, 480))

while True:
    _,frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow("Webcam", color)
    if ((cv2.waitKey(5) & 0xFF) == 27):
        break

cap.release()
cv2.destroyAllWindows()