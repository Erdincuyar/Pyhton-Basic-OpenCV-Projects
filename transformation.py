import cv2 as cv
import numpy as np

img = cv.imread("photos/cats.jpg")

cv.imshow("cats",img)

#translation
def translate(img,x,y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img,transMat,dimensions)

# -x ----> left
#  y ----> up
#  x ----> right
# -y ----> down

translated= translate(img,100,100)
cv.imshow('Translated',translated)

#rotating
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotmat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotmat,dimensions)

rotated= rotate(img,45)
cv.imshow("rotated",rotated)

# Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)

# Flipping
flip = cv.flip(img,0)
cv.imshow("flipped",flip)

# Cropping
cropped = img[200:400,300:500]
cv.imshow("cropped",cropped)




cv.waitKey(0)
