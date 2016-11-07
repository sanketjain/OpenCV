# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:13:51 2016

@author: sanketjain
"""


import cv2
import numpy as np

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg', 0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols+200,rows+150))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

