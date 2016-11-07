# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:35:35 2016
http://docs.opencv.org/3.1.0/df/d0c/tutorial_py_fast.html#gsc.tab=0
@author: sanketjain
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg', 0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))

# Print all default params
print "Threshold: ", fast.getThreshold()
print "nonmaxSuppression: ", fast.getNonmaxSuppression()
print "neighborhood: ", fast.getType()
print "Total Keypoints with nonmaxSuppression: ", len(kp)
cv2.imwrite('fast_true.png',img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)

print "Total Keypoints without nonmaxSuppression: ", len(kp)
img3 = cv2.drawKeypoints(img, kp,None, color=(255,0,0))
cv2.imwrite('fast_false.png',img3)
