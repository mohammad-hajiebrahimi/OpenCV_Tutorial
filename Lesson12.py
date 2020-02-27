import cv2
import numpy as np


mario = cv2.imread("Mario.png")
mario_gray = cv2.cvtColor(mario,cv2.COLOR_BGR2GRAY)

coin = cv2.imread("Coin.png",0)
W, H = coin.shape[0:2]

res = cv2.matchTemplate(mario_gray, coin, cv2.TM_CCOEFF_NORMED)

thereshhold = 0.8
loc = np.where(res >= thereshhold)
print(*loc[::-1])
for pt in zip(*loc[::-1]):
    print(pt)
    cv2.rectangle(mario, pt, (pt[0]+W,pt[1]+H), (0,0,255), 1)

cv2.imshow("detect", mario)
cv2.waitKey(0)
cv2.destroyAllWindows()
