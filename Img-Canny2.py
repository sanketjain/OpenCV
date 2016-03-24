
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:36:07 2016
Trial 2 Example of Canny
@author: sanketjain
"""

import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = cv2.imread('/Users/sanketjain/Documents/Opencv/Pictures/messi5.jpg',0)
cv2.namedWindow('image')
messi = cv2.imread('/Users/sanketjain/Documents/Opencv/Pictures/messi5.jpg',0)
    

# create trackbars for color change
cv2.createTrackbar('min','image',0,255,nothing)
cv2.createTrackbar('max','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    minVal = cv2.getTrackbarPos('min','image')
    maxVal = cv2.getTrackbarPos('max','image')
    s = cv2.getTrackbarPos(switch,'image')
    edges = cv2.Canny(messi, minVal, maxVal)

    if s == 0:
        img[:] = 0
    else:
        img[:] = edges

cv2.destroyAllWindows()


