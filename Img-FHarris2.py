# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:00:45 2016

@author: sanketjain
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:40:16 2016
http://docs.opencv.org/3.1.0/dc/d0d/tutorial_py_features_harris.html#gsc.tab=0
@author: sanketjain
"""

import cv2
import numpy as np

filename = '/Users/sanketjain/Documents/Opencv/pictures/chess.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

th3= np.float32(th3)
dst = cv2.cornerHarris(th3,2,5,0.04)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

