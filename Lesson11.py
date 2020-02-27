import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_8U)
    sobelX = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)
    sobelY = cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize=5)
    canny = cv2.Canny(frame, 100, 200)

    cv2.imshow("org", frame)
    cv2.imshow("lap", laplacian)
    cv2.imshow("SobelX",sobelX)
    cv2.imshow("SobelY", sobelY)
    cv2.imshow("Canny", canny)

    if(cv2.waitKey(1) & 0xFF) ==27:
        break

cv2.destroyAllWindows()
cap.release()
