# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:08:38 2016

@author: sanketjain
"""

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image2')

# create trackbars for color change
cv2.createTrackbar('R','image2',0,255,nothing)
cv2.createTrackbar('G','image2',0,255,nothing)
cv2.createTrackbar('B','image2',0,255,nothing)


# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image2',0,1,nothing)

while(1):
    cv2.imshow('image2',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image2')
    g = cv2.getTrackbarPos('G','image2')
    b = cv2.getTrackbarPos('B','image2')
    s = cv2.getTrackbarPos(switch,'image2')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()



