# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:17:09 2016

@author: sanketjain
"""

import cv2
import numpy as np

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg', 0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/4,rows/4),90,1)
#cols/2, rows/2 is center. It tells from where the images would be rotated
#Third parameter 0.5 is scaling factor
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



