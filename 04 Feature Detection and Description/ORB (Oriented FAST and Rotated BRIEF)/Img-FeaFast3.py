# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:03:59 2016
http://docs.opencv.org/3.1.0/d1/d89/tutorial_py_orb.html
@author: sanketjain
"""



import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg', 0)

# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
plt.imshow(img2),plt.show()
