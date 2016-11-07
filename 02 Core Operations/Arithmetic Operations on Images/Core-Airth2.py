#http://docs.opencv.org/3.1.0/d0/d86/tutorial_py_image_arithmetics.html
#Code to pick up only outline of OpenCV Logo and add it to Messi5 image

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')


import cv2
import numpy as np

# Load two images

img1 = cv2.imread('/Users/sanketjain/Documents/OpenCV/02 Core Operations/Arithmetic Operations on Images/sanket.jpg')
img2 = cv2.imread('/Users/sanketjain/Documents/OpenCV/02 Core Operations/Arithmetic Operations on Images/opencvlogo.png')
img3 = cv2.imread('/Users/sanketjain/Documents/OpenCV/02 Core Operations/Arithmetic Operations on Images/BalloonImages.jpg')



# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# http://docs.opencv.org/3.1.0/d7/d4d/tutorial_py_thresholding.html#gsc.tab=0
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
#cv2.imshow('mask',img1_bg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img3,mask = mask)
#cv2.imshow('foreground',img2_fg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

