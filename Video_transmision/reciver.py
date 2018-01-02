import cv2
from time import sleep

import subprocess  
c=subprocess.Popen('python /home/devesh/Documents/urc/URC2K18/Video_transmision/sender.py', shell=True)  
print(c)

while True:
	sleep(0.01)
	dev = cv2.imread("dev.jpg",1)
	print(type(dev))
	try:
		cv2.imshow("y",dev)

	except Exception as e:
		a=e


	k = cv2.waitKey(60) & 0xff
	if k == 27:
		break
cv2.destroyAllWindows()
exit()