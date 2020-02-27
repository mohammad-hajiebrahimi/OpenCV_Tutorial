import cv2

img = cv2.imread("corner.jpg", cv2.IMREAD_COLOR)

part1= img[300:400, 100:200]

img[100:200,100,200] = part1

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
