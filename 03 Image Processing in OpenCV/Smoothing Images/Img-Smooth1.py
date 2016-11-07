# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:43:01 2016
http://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html#gsc.tab=0
@author: sanketjain
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


