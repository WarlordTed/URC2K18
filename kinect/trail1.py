import numpy as np
import cv2
import sys
from scipy import signal


try:
    import libfreenect2
except Exception as e:
    print("hi")
finally:
    import pylibfreenect2
from pylibfreenect2 import Freenect2, SyncMultiFrameListener
from pylibfreenect2 import FrameType, Registration, Frame


try:
    from pylibfreenect2 import OpenCLPacketPipeline
    pipeline = OpenCLPacketPipeline()
except:
    try:
        from pylibfreenect2 import OpenGLPacketPipeline
        pipeline = OpenGLPacketPipeline()
    except:
        from pylibfreenect2 import CpuPacketPipeline
        pipeline = CpuPacketPipeline()
print("Packet pipeline:", type(pipeline).__name__)

fn = Freenect2()
num_devices = fn.enumerateDevices()
if num_devices == 0:
    print("No device connected!")
    sys.exit(1)

serial = fn.getDeviceSerialNumber(0)
device = fn.openDevice(serial, pipeline=pipeline)

types = 0
types |= (FrameType.Ir | FrameType.Depth)
listener = SyncMultiFrameListener(types)
device.setIrAndDepthFrameListener(listener)
device.startStreams(rgb=False, depth=True)
#registration = Registration(device.getIrCameraParams(),device.getColorCameraParams())

frames = listener.waitForNewFrame()
depth = frames["depth"]
dep=depth.asarray()
dep=dep[212:]
dep_display=dep / 4096.

seg=dep_display[0:212,416:512]
seg2=dep_display[0:212,96:192]

corr = signal.correlate2d(seg,seg2, boundary='symm', mode='same')

print(corr)
cv2.imshow("depth",corr/4096.)
cv2.imshow("seg",seg)
cv2.imshow("seg2",seg2)
k = cv2.waitKey() 
cv2.destroyAllWindows()







while True:
    frames = listener.waitForNewFrame()
    depth = frames["depth"]
    dep=depth.asarray()
    dep=dep[212:]
    dep_display=dep / 4096.

    seg=dep_display[0:212,416:512]
    print(dep_display.shape)
    cv2.imshow("depth",dep_display)
    cv2.imshow("seg",seg)






    listener.release(frames)

    key = cv2.waitKey(11)
    if key == ord('q'):
        break

device.stop()
device.close()

sys.exit(0)




