# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:15:53 2016
Gui Features in OpenCV
Getting Started with Images
http://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html#gsc.tab=0

@author: sanketjain
"""



import numpy as np
import cv2

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg', 0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()











