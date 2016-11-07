# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:04:01 2016
http://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html#gsc.tab=0
@author: sanketjain
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg')

blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

