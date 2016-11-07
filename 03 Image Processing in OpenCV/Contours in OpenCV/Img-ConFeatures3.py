
import cv2
import numpy as np

img = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/hand.jpg')
im2 = cv2.imread('/Users/sanketjain/Documents/Opencv/pictures/hand.jpg', 0)

ret,thresh = cv2.threshold(im2,127,255,0)
im3, contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

hull = cv2.convexHull(cnt)


cv2.imshow('modified2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img,center,radius,(255,0,0),2)

ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(255,255,0),2)

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img,(cols-1,righty),(0,lefty),(0,255,255),2)


cv2.imshow('modified2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

