# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:39:03 2016

@author: sanketjain
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg')

#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.hist(img.ravel(),256,[0,256]); plt.show()
# hist,bins = np.histogram(img.ravel(),256,[0,256])

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

