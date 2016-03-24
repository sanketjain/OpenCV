
import cv2
import numpy as np

img1 = cv2.imread('Pictures/libertyblending.jpg')
img2 = cv2.imread('Pictures/newyorkblending.jpg')


for i in range (0,100):
    dst = cv2.addWeighted(img1, i/100.0, img2, (100-i)/100.0, 0)
    image = 'image' + str(i)+'.jpg'
    cv2.imwrite(image, dst)







