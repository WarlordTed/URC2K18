from PyQt5.uic import loadUiType
from PyQt5 import QtGui
from PyQt5 import  QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication

from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

import socket
import random
import sys
import cv2
import numpy as np
Ui_MainWindow, QMainWindow = loadUiType('gui_dev.ui')

class Video():
    def __init__(self,capture):
        self.capture = capture
        self.currentFrame=np.array([])
 
    def captureNextFrame(self):
        
        ret, readFrame=self.capture.read()
        if(ret==True):
            self.currentFrame=cv2.cvtColor(readFrame,cv2.COLOR_BGR2RGB)
 
    def convertFrame(self):
        
        try:
            height,width=self.currentFrame.shape[:2]
            img=QtGui.QImage(self.currentFrame,
                              width,
                              height,
                              QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self,):
        super(Main,self).__init__()
        self.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname() 
        port = 8500
        self.s.connect((host, port))
        
        #self.list_alt = [random.randint(0, 10) for i in range(5)]
        self.item = []
        self.vol=[]
        self.getdata()
        figure = Figure(facecolor='white')
        self.canvas = FigureCanvas(figure)
        self.sensorgraph.addWidget(self.canvas)
        self.canvas.draw()

        self.plotgraph = figure.add_subplot('111', axisbg='white')
        self.plotgraph.clear()
        #self.plotgraph.plot(self.item,'g')
        self.update_label()
        self.graph  ()

        self.video = Video(cv2.VideoCapture(0))#'http://192.168.0.101:8160'))
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)

    def getdata(self):
        self.data = self.s.recv(1024).decode()
        self.item = [i for i in self.data.split(',')]
        self.vol.append(self.item[0])
        QtCore.QTimer.singleShot(1000, lambda: self.getdata())

    def update_label(self):
        self.label1.setText(self.item[0])
        self.label2.setText(self.item[1])
        self.label3.setText(self.item[2])
        self.label4.setText(self.item[3])
        self.label5.setText(self.item[4])
        QtCore.QTimer.singleShot(1000, lambda: self.update_label())
    
    def play(self):
        try:
            self.video.captureNextFrame()
            self.videoFrame.setPixmap(
                self.video.convertFrame())
            self.videoFrame.setScaledContents(True)
        except TypeError:
            print ("No frame")
    def graph(self):
        if len(self.vol)>5:
            del(self.vol[0])
            self.canvas.draw()
            self.plotgraph.clear()
            self.plotgraph.plot(self.vol,'b')
            self.plotgraph.axes.get_xaxis().set_visible(True)
            self.plotgraph.axes.get_yaxis().set_visible(True)
            #self.label_22.setText(data[3])
        else:
            self.canvas.draw()
            self.plotgraph.clear()
            self.plotgraph.plot(self.vol,'b')
            self.plotgraph.axes.get_xaxis().set_visible(True)
            self.plotgraph.axes.get_yaxis().set_visible(True)
        QtCore.QTimer.singleShot(500, lambda: self.graph())


if __name__ == '__main__' :
    app=QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
