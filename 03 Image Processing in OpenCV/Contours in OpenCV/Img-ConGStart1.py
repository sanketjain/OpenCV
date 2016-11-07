# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:51:29 2016
http://docs.opencv.org/3.1.0/d4/d73/tutorial_py_contours_begin.html#gsc.tab=0
@author: sanketjain
"""


import numpy as np
import cv2

im = cv2.imread('/Users/sanketjain/Documents/Opencv/Pictures/messi5.jpg')
img = cv2.imread('/Users/sanketjain/Documents/Opencv/Pictures/messi5.jpg')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#http://docs.opencv.org/3.1.0/d3/dc0/group__imgproc__shape.html#ga4303f45752694956374734a03c54d5ff&gsc.tab=0
#http://docs.opencv.org/3.1.0/d9/d8b/tutorial_py_contours_hierarchy.html#gsc.tab=0

cv2.drawContours(img, contours, -1, (0,255,0), 3)
#cv2.drawContours(img, contours, 3, (0,255,0), 3)
#cnt = contours[4]
#cv2.drawContours(img, [cnt], 0, (0,255,0), 3)


cv2.imshow('modified', img)


cv2.waitKey(0)
cv2.destroyAllWindows()




