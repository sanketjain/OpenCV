# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:06:47 2016
http://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html#gsc.tab=0
@author: sanketjain
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/hist.jpg', 0)

hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]


hist1,bins = np.histogram(img2.flatten(),256,[0,256])
cdf1 = hist1.cumsum()
cdf_normalized1 = cdf1 * hist1.max()/ cdf1.max()

plt.plot(cdf_normalized1, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()



cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

