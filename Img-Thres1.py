# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:10:32 2016
http://docs.opencv.org/3.1.0/d7/d4d/tutorial_py_thresholding.html#gsc.tab=0
@author: sanketjain
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#original = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/binarythres.jpg')
img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/binarythres.jpg', 0)

#Documentation: 
#http://docs.opencv.org/3.1.0/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a147222a96556ebc1d948b372bcd7ac59&gsc.tab=0
ret,thresh1 = cv2.threshold(img,7,200,cv2.THRESH_BINARY)
thresh1=thresh1.astype(float)
thresh1=thresh1/255
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()



