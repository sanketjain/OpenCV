# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:26:16 2016
http://docs.opencv.org/3.1.0/dc/d7d/tutorial_py_brief.html#gsc.tab=0
@author: sanketjain
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg', 0)

# Initiate FAST detector
star = cv2.xfeatures2d.StarDetector_create()

# Initiate BRIEF extractor
brief = cv2.BriefDescriptorExtractor_create()

# find the keypoints with STAR
kp = star.detect(img,None)

# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)

print brief.getInt('bytes')
print des.shape
