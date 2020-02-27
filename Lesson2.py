import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Mario.png", cv2.COLOR_BGR2GRAY)

cv2.imshow(img, camp ="gray", interpolation = 'bicubic')
plt.plot([600, 200], [200, 300], 'r', linewidth = 5)
plt.show()

cv2.imwrite("imgout.ppg", img)
