import cv2
import numpy as np

img1=cv2.imread('3D-Matplotlib.png')
img2=cv2.imread('mainsvmimage.png')

#add= img1+ img2
#add=cv2.add(img1,img2) #(155,211,79)+(50,170,200)=(205,381,279)...translated to (205,255,255)
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('add', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()