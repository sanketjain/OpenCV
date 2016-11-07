# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:40:16 2016
http://docs.opencv.org/3.1.0/dc/d0d/tutorial_py_features_harris.html#gsc.tab=0
@author: sanketjain
"""

import cv2
import numpy as np

filename = '/Users/sanketjain/Documents/Opencv/pictures/chess.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,5,0.04)

#result is dilated for marking the corners, not important
#dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0]=[0,0,255]
#I have modified the above command. We can use the exact one as it is 
#written in document

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

