# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:24:25 2016

@author: sanketjain
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/proscia.png', 0)


# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)


equ = cv2.equalizeHist(img)
res = np.hstack((cl1,equ)) #stacking images side-by-side
cv2.imwrite('clahe_2.jpg',res)
