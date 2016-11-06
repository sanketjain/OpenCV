# -*- coding: utf-8 -*-
"""
# Resize the display window

Created on Tue Mar  8 09:23:47 2016
@author: sanketjain

Note
There is a special case where you can already 
create a window and load image to it later. 
In that case, you can specify whether window 
is resizable or not. It is done with the function
 cv2.namedWindow(). By default, the flag is 
 cv2.WINDOW_AUTOSIZE. But if you specify flag
 to be cv2.WINDOW_NORMAL, you can resize window. 
 It will be helpful when image is too large in 
 dimension and adding track bar to windows.
 """

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/messi5.jpg', 0)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
