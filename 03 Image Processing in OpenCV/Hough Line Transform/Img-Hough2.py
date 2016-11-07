# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:36:51 2016

@author: sanketjain
"""

import cv2
import numpy as np

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('houghlines5.jpg',img)
