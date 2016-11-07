# This code takes 2 images and gives them weight. Output is series of images with different weights.
# These images can be used to make a slide show which simply shows one image diminishes as other appears

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')


import cv2
import numpy as np

img1 = cv2.imread('/Users/sanketjain/Documents/OpenCV/02 Core Operations/Arithmetic Operations on Images/libertyblending.jpg')
img2 = cv2.imread('/Users/sanketjain/Documents/OpenCV/02 Core Operations/Arithmetic Operations on Images/newyorkblending.jpg')


for i in range (0,100):
    dst = cv2.addWeighted(img1, i/100.0, img2, (100-i)/100.0, 0)
    image = 'image' + str(i)+'.jpg'
    cv2.imwrite(image, dst)







