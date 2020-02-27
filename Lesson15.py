import cv2

cap = cv2.VideoCapture(0)

fg = cv2.createBackgroundSubtractorMOG2()

while True:
    _,frame = cap.read()
    fmask = fg.apply(frame)

    cv2.imshow("org", frame)
    cv2.imshow("fg", fmask)

    if((cv2.waitKey(5) & 0xFF)==27):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
