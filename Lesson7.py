import cv2

img1 = cv2.imread("corner.jpg")
img2 = cv2.imread("corner.jpg")

add = img1 + img2
add = cv2.add(img1, img2)
add = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)

cv2.imshow("add", add)
cv2.waitKey(0)
cv2.destroyAllWindows()