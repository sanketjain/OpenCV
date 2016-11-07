# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:26:26 2016
http://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html#gsc.tab=0

Note: Color image loaded by OpenCV is in BGR mode. 
But Matplotlib displays in RGB mode. 
So color images will not be displayed correctly in 
Matplotlib if image is read with OpenCV.

@author: sanketjain
"""

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/sanketjain/Documents/OpenCV/01 GUI features in OpenCV/01 Getting started with images/sanketincolor.jpg', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

