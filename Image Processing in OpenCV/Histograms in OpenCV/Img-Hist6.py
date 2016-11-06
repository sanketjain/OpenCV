# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:37:56 2016

@author: sanketjain
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/proscia.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.imshow(hist,interpolation = 'nearest')
plt.show()

