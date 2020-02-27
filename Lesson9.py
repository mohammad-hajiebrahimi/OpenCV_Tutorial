import cv2
import numpy as np

img = cv2.imread("Book")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thereshold = cv2.threshold(gray, 20, 30, cv2.THRESH_BINARY)

th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 0)

cv2.imshow('img', thereshold)
cv2.imshow('img1', img)
cv2.imshow("adpth", th)
cv2.waitKey(0)
cv2.destroyAllWindows()
