# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:26:28 2016
Gui Features in OpenCV
Getting Started with Videos
http://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html#gsc.tab=0
@author: sanketjain
"""


import numpy as np
import cv2

cap = cv2.VideoCapture('/Users/sanketjain/Movies/22JumpStreet.avi', 0)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



