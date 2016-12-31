# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:42:22 2016
http://docs.opencv.org/3.1.0/d0/d86/tutorial_py_image_arithmetics.html
This code imports 2 images and put one over another with weights. 
@author: sanketjain
"""

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')



import cv2
import numpy as np

img1 = cv2.imread('/Users/sanketjain/Documents/OpenCV/02 Core Operations/Arithmetic Operations on Images/libertyblending.jpg')
img2 = cv2.imread('/Users/sanketjain/Documents/OpenCV/02 Core Operations/Arithmetic Operations on Images/newyorkblending.jpg')

dst = cv2.addWeighted(img1,0.2,img2,0.4,0.6)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


