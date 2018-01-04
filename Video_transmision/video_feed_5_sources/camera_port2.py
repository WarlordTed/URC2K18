# camera.py

import cv2

#
class VideoCamera1(object): 
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #self.video1 = cv2.VideoCapture(0)
        self.video1 = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.

    def __del__(self):
        self.video1.release()

    def get_frame1(self):
        success, image1 = self.video1.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        image1=cv2.resize(image1,(400,300),interpolation=cv2.INTER_LINEAR)
        ret, jpeg1 = cv2.imencode('.jpg', image1, [cv2.IMWRITE_JPEG_QUALITY, 90])
        return jpeg1.tobytes()