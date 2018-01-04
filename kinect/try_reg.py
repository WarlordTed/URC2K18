import numpy as np
import cv2
import sys
from scipy import signal
from time import sleep
import matplotlib.pyplot as plt
from drawnow import drawnow

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

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return(b_0, b_1)

def make_fig(x,y):
    plt.ion()  # enable interactivity
    fig = plt.figure() 
    plt.plot(x, y)





a=list(range(511))
while True:
    frames = listener.waitForNewFrame()
    depth = frames["depth"]
    dep=depth.asarray()
    dep=dep[212:]
    dep_display=dep / 4096.
    data = dep
    
    y=[]
    for i in a:
        d=estimate_coef(data[:,i],data[:,i+1])
        #plot_regression_line(data[:,1],data[:,2],d)
        #print (i)
    make_fig()


    cv2.imshow("depth",dep_display)
    listener.release(frames)

    key = cv2.waitKey(50)
    if key == ord('q'):
        break

device.stop()
device.close()

sys.exit(0)




