#blue-->(255,0,0)
#green-->(0,255,0)
#red-->(0,0,255)    BGR
#white-->(255,255,255)
#black-->(0,0,0)
import numpy as np
import cv2

img=cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150), (255,255,255), 4)
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)
cv2.circle(img, (100,63), 55, (0,0,255), -1)

font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'irem polat', (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
