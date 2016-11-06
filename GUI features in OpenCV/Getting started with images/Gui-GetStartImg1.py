
"""
# Import, display and write an image

Gui Features in OpenCV
Getting Started with Images
http://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html

"""
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')


import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/sanket.jpg',1)

'''
imread('xyz' , (1, 0 or -1))
1 represents cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
0 represents cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
-1 represents cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

'''


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Press escape key ONCE to close window.


# cv2.imwrite('messigray.png',img)  #This command can write the image
#Try to find where the images is
#It will be located in pwd if you ran it from terminal. Try doing ls


