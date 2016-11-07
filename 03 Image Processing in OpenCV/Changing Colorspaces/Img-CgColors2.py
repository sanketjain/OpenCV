# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:24:24 2016
http://docs.opencv.org/3.1.0/df/d9d/tutorial_py_colorspaces.html#gsc.tab=0
@author: sanketjain
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#Video Capture(0), 0 is index of camera. If we add more cameras there 
#would be more index

while(1):

    # Take each frame
    _, frame = cap.read()


    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])

    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])



    # Threshold the HSV image to get only blue colors
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res1 = cv2.bitwise_and(frame, frame, mask= mask1)
    res2 = cv2.bitwise_and(frame, frame, mask= mask2)
    res3 = cv2.bitwise_and(frame, frame, mask= mask3)
    
 
    res = cv2.add(res1, res2)
    res = cv2.add(res, res3)

    cv2.imshow('frame',frame)
#    cv2.imshow('mask',mask3)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


