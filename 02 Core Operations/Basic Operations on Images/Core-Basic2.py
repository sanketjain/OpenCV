# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:42:22 2016
http://docs.opencv.org/3.1.0/d3/df2/tutorial_py_basic_ops.html
@author: sanketjain
"""



img1 = cv2.imread('ml.png')
img2 = cv2.imread('opencv_logo.jpg')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


