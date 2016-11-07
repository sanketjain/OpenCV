# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:06:01 2016
http://docs.opencv.org/3.1.0/d3/df2/tutorial_py_basic_ops.html
@author: sanketjain
"""

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('Pictures/blending.jpg')

replicate = cv2.copyMakeBorder(img1,10,10,10,50,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,200,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,200,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()

