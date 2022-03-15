# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import cv2 as cv

img = cv.imread("photos/cats.jpg")
capture = cv.VideoCapture('videos/dog.mp4')

cv.imshow("cats",img)

# Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


# Blur image

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

# Edge Cascade

canny = cv.Canny(img,125,125)
cv.imshow("canny",canny)

# Dilating the image

dilated= cv.dilate(canny,(7,7),iterations=3)
cv.imshow("dilated",dilated)

# Eroded
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow("eroded",eroded)

# Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
cv.imshow("resized",resized)

# Cropping
cropped= img[50:200,200:400]
cv.imshow("Cropped",cropped)






#while True:
    #isTrue, frame = capture.read()

    #cv.imshow('video',frame)

    #if(cv.waitKey(20) & 0xFF==ord("d")):
    #    break

#capture.release()
#cv.destroyWindow()



cv.waitKey(0)





