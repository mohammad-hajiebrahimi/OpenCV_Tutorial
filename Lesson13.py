import cv2
import numpy as np

img = cv2.imread("corner.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)

corner = cv2.goodFeaturesToTrack(img_gray, 200, 0.1, 20)
corner = np.int0(corner)

for c in corner:
    x,y = c.ravel()
    print(c)
    cv2.circle(img, (x,y), 5, (0,255,0), 1)

cv2.imshow("corner", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
