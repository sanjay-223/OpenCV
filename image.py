import cv2 as cv
import numpy as np

img = cv.imread("test.jpg")

img2 = np.copy(img)

def Padd(a,b):
    x = ((a//2)+(b//2))
    #print(a,b,"\t",x)
    return x

for i in range(img.shape[0]):
    for j in range(0,img.shape[1],2):
        img2[i][j//2] = Padd(img[i][j],img[i][j+1])

img3 = np.copy(img2)

for i in range(img2.shape[1]):
    for j in range(0,img2.shape[0]-1,2):
        img3[j//2][i] = Padd(img2[j][i],img2[j+1][i])

#for i in range(img.shape[1]-1):
    #print(img[0][i],img[0][i+1],"\t",img2[0][i])

cv.imshow('img',img)
cv.waitKey(0)

cv.imshow('img',img2)
cv.waitKey(0)

img3 = img3[0:img.shape[0]//2,0:img.shape[1]//2]
#img3 = cv.resize(img, (img.shape[1],img.shape[0]), interpolation = cv.INTER_AREA)

cv.imshow('img',img3)
cv.waitKey(0)

cv.destroyAllWindows()

cv.imwrite("testr.jpg", img3)