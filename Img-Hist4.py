# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:20:21 2016
http://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html#gsc.tab=0
@author: sanketjain
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/hist.jpg', 0)

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)