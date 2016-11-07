# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:15:53 2016
Gui Features in OpenCV
Getting Started with Images
http://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html#gsc.tab=0

@author: sanketjain
"""

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')


import numpy as np
import cv2

img = cv2.imread('/Users/sanketjain/Documents/OpenCV/01 GUI features in OpenCV/01 Getting started with images/sanketincolor.jpg', 0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('sanketoutgray02.png',img)
    cv2.destroyAllWindows()











