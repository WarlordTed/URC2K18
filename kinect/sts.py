import numpy as np
from numpy import genfromtxt
import cv2
a = np.asarray([[1,2,3],[4,1,3],[4,5,6]])
b= np.asarray([[1,2,4],[5,1,3],[4,9,6]])
data = genfromtxt('rock.csv', delimiter=',')
data.shape
print(data.shape)
"""
x=data[0:140,0:128]
a.shape
y=data[0:140,412:512]
y.shape
print(x.std(),y.std())
"""
"""y=data[0:140,384:512]
print(y.std())
print("other")
for i in range(0,512,128):    
    x=data[0:140,i:i+128]
    cv2.imshow("x",x/4500)
    print "std " ,x.std()
    dist = np.linalg.norm(x-y)
    print "dis linalg",dist
    dist = np.corrcoef(np.ravel(x),np.ravel(y))
    print " corrcoef ",dist
    cv2.waitKey()
    print " " """


dev=data/4500

#dev=data/4500
#lap = cv2.Laplacian(data,cv2.CV_64F)
lap = cv2.Sobel(data,cv2.CV_64F,0,1,ksize=15)
cv2.imshow("depth",dev)
#cv2.imwrite("dd.bmp",dev)
#print (data)
cv2.imshow("dtry",lap/4500)

#edges = cv2.Canny(data,50,100)
#cv2.imshow('edges',edges/4500)   	
#cv2.imshow("y",y/4500)
cv2.waitKey()
cv2.destroyAllWindows()

