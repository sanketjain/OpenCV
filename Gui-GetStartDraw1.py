# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:18:50 2016
Gui Features in OpenCV
Drawing Functions in OpenCV

http://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html#gsc.tab=0
@author: sanketjain
"""

import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(100,100),(400,400),(255,0,0),0)

cv2.rectangle(img,(20,20),(51,12),(0,255,0),3)

cv2.circle(img,(447,63), 63, (150,150,150), -1)

cv2.ellipse(img,(256,256),(100,50),45,0,360,255,-1)


pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

