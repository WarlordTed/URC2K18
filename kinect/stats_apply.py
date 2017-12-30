import numpy as np
from numpy import genfromtxt
import cv2
a = np.asarray([[1,2,3],[4,1,3],[4,5,6]])
b= np.asarray([[1,2,4],[5,1,3],[4,9,6]])
data = genfromtxt('dev.csv', delimiter=',')
data.shape
print(data.shape)
"""
x=data[0:140,0:128]
a.shape
y=data[0:140,412:512]
y.shape
print(x.std(),y.std())
"""
y=data[0:140,384:512]
print(y.std())
print("other")
for i in range(0,512,128):    
    x=data[0:140,i:i+128]
    cv2.imshow("x",x/4500)
    print("std ", end =" " ,x.std())
    dist = np.linalg.norm(x-y)
    print("dis linalg",dist)
    distance=np.sqrt(np.sum((x-y)**2))
    print("dis sqrt",distance)
    cv2.waitKey()

    
cv2.imshow("depth",data/4500)

cv2.imshow("y",y/4500)
cv2.waitKey()
cv2.destroyAllWindows()

