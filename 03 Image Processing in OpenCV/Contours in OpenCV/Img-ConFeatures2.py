

import cv2
import numpy as np

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/hand.jpg')
im2 = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/hand.jpg', 0)
img1 = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/hand.jpg')

ret,thresh = cv2.threshold(im2,127,255,0)
im3, contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# We added following to find length of contours:
for i in xrange(len(contours)):
   print str(i)+" "+str(len(contours[i]))

cnt = contours[0]

epsilon = 0.001*cv2.arcLength(cnt,True)

approx = cv2.approxPolyDP(cnt,epsilon,True)

cv2.drawContours(img, cnt, -1, (255,0,0), 12)
cv2.drawContours(img1, approx, -1, (255,0,0), 3)


cv2.imshow('modified1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('modified2', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


