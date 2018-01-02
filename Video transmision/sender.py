import numpy as np
import matplotlib as plt
import cv2
cap = cv2.VideoCapture(0)#"192.168.43.55:5000")#'http://192.168.43.185:8080/video')

while 1:
    ret ,img = cap.read()
    print(img.shape)
    cv2.imwrite("dev.bmp",img)
    cv2.imshow('img',img)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
