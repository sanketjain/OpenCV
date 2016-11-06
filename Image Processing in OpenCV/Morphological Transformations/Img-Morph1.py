# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 13:04:08 2016
http://docs.opencv.org/3.1.0/d9/d61/tutorial_py_morphological_ops.html#gsc.tab=0
@author: sanketjain
"""


import cv2
import numpy as np

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/coins.png', 0)

kernel = np.ones((15,15),np.uint8)
# erosion = cv2.erode(img,kernel,iterations = 1)
#dilation = cv2.dilate(img,kernel,iterations = 5)

#
i = 1
for i in range(1, 50): 
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    #closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    i = i+1

ret,thresh1 = cv2.threshold(opening,200,255,cv2.THRESH_BINARY)
#cv2.imshow('image', erosion)
#cv2.imshow('image', dilation)
cv2.imshow('image', thresh1)
#cv2.imshow('image', closing)


cv2.waitKey(0)
cv2.destroyAllWindows()


