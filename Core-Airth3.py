# This code takes 2 images and gives them weight. Output is series of images with different weights.
# These images can be used to make a slide show which simply shows one image diminishes as other appears
import cv2
import numpy as np

img1 = cv2.imread('Pictures/libertyblending.jpg')
img2 = cv2.imread('Pictures/newyorkblending.jpg')


for i in range (0,100):
    dst = cv2.addWeighted(img1, i/100.0, img2, (100-i)/100.0, 0)
    image = 'image' + str(i)+'.jpg'
    cv2.imwrite(image, dst)







