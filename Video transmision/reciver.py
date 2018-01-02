import cv2
from time import sleep




while True:
	sleep(0.01)
	dev = cv2.imread("dev.jpg",1)
	try:
		cv2.imshow("y",dev)

	except Exception as e:
		a=e


	k = cv2.waitKey(60) & 0xff
	if k == 27:
		break
cv2.destroyAllWindows()
