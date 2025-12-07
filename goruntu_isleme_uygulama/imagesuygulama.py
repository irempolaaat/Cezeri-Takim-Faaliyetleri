import cv2
import numpy as np

img =cv2.imread('fourballs.jpeg', cv2.IMREAD_COLOR)
hsv =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([11, 70, 90])
upper_yellow = np.array([35, 255, 255])

mask = cv2.inRange(hsv,lower_yellow,upper_yellow )
kernel = np.ones((5,5), np.uint8)
median = cv2.medianBlur(mask,13)
res = cv2.bitwise_and(img, img, mask= median)

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)


contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    largest_contour = max(contours, key = cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  

cv2.imshow('img', img)
cv2.imshow('res', res)
cv2.imshow('opening', opening)

cv2.waitKey(0)
cv2.destroyAllWindows()