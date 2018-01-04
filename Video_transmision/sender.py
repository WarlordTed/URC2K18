from time import sleep
import cv2
cap = cv2.VideoCapture(0)#"192.168.43.55:5000")#'http://192.168.43.185:8080/video')

while 1:
    ret ,img = cap.read()
    #print(img.shape)
    cv2.imwrite("dev.jpg",img)
    #cv2.imshow('img',img)
    sleep(0.01)
    k = cv2.waitKey(120) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
