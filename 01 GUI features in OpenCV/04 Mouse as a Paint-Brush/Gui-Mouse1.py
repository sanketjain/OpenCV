# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:27:19 2016

http://docs.opencv.org/3.1.0/db/d5b/tutorial_py_mouse_handling.html#gsc.tab=0

Note: Press Left button to make circles
Press Escape to stop running and to quit window.
@author: sanketjain
"""

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


