import cv2 as cv
import numpy as np


img = cv.imread("photos/cats.jpg")
capture = cv.VideoCapture('videos/dog.mp4')

blank = np.zeros(img.shape,dtype="uint8")
cv.imshow("blank",blank)


cv.imshow("cats",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
#cv.imshow("blur",blur)

#canny = cv.Canny(blur,125,175)
#cv.imshow("Canny",canny)

ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow("thresh",thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank,contours,-1,(0,255,255),thickness=1)
cv.imshow("draw contours",blank)





cv.waitKey(0)