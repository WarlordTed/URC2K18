import cv2

while True:
	dev = cv2.imread("dev.bmp",1)
	cv2.imshow('img',dev)
	k = cv2.waitKey(60) & 0xff
	if k == 27:
		break
cv2.destroyAllWindows()
