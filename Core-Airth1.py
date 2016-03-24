# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:42:22 2016

@author: sanketjain
"""



import cv2
import numpy as np

img1 = cv2.imread('Pictures/libertyblending.jpg')
img2 = cv2.imread('Pictures/newyorkblending.jpg')

dst = cv2.addWeighted(img1,0.2,img2,0.4,0.6)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


