import cv2 as cv
import numpy

img = cv.imread("C:\Users\slgzo\OneDrive\Resimler\Özgür SELAĞZI Resim (2).jpg")
cv.imshow('Özgür SELAĞZI Resim (2)', img)

b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

for i in range(0, 360):

    for a in range(0, 450):

        if r[i, a] > 100:

            r[i, a] = 20

merged = cv.merge([b, g, r])
cv.imshow('Merged Image ', merged)

cv.waitKey(0)