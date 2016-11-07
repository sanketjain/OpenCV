# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:11:00 2016
http://docs.opencv.org/3.1.0/d4/d73/tutorial_py_contours_begin.html#gsc.tab=0
@author: sanketjain
"""

import cv2
import numpy as np

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/spot.png')
2 = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/spot.png', 0)


ret,thresh = cv2.threshold(im2,127,255,0)
thresh=im2
#im3, contours,hierarchy = cv2.findContours(thresh, 1, 2)
im3, contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#Note: There is an error in document.

# We added following to find length of contours:
for i in xrange(len(contours)):
   print str(i)+" "+str(len(contours[i]))

cnt = contours[28]
M = cv2.moments(cnt)
print M

#cx = int(M['m10']/M['m00'])
#cy = int(M['m01']/M['m00'])

area = cv2.contourArea(cnt)

perimeter = cv2.arcLength(cnt,True)

epsilon = 0.1*cv2.arcLength(cnt,True)

approx = cv2.approxPolyDP(cnt,epsilon,True)


hull = cv2.convexHull(cnt)


#img2 = img

cv2.drawContours(img, approx, -1, (255,0,0), 12)
cv2.drawContours(im2, cnt, -1, (255,0,0), 12)

cv2.imshow('modified', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('modified2', im2)
cv2.waitKey(0)
cv2.destroyAllWindows()



