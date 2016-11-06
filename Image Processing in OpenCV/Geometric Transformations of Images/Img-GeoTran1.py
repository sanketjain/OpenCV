# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:56:36 2016

@author: sanketjain
"""

import cv2
import numpy as np

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg')

# res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imwrite('doublesize.jpg', res)



