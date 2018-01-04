from PyQt5.uic import loadUiType
import sys 
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
#from PyQt5 import QtGui
from PyQt5 import  QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import  QApplication
import time
import numpy as np
import cv2





Ui_MainWindow, QMainWindow = loadUiType('ploting.ui')


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
    list_main=[]
    list_pre=[]
    list_tem=[]
    i=0
    k=0
    value=1
 
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        #graph initiallisation start
        fig1 = Figure(facecolor='white', edgecolor='red')
        fig2 = Figure(facecolor='white', edgecolor='red')
        fig3 = Figure(facecolor='white', edgecolor='red')
    
        self.canvas1 = FigureCanvas(fig1)
        self.canvas2 = FigureCanvas(fig2)#temp
        self.canvas3 = FigureCanvas(fig3)#pre
        
        self.mainplt.addWidget(self.canvas1)
        self.temprature.addWidget(self.canvas2)#temp
        self.pressure.addWidget(self.canvas3)
        
        self.plot_main = fig1.add_subplot('111', axisbg='white')
        self.plot_temp = fig2.add_subplot(111)#temp
        self.plot_pre = fig3.add_subplot(111)#pre
        self.make_temp()
        self.make_pre()
        self.p_but.mousePressEvent=self.change
        #graph initiallisation  complete
        
        self.video = Video(cv2.VideoCapture(0))#'http://192.168.0.101:8160'))
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()
        
    def play(self):
        try:
            self.video.captureNextFrame()
            self.videoFrame.setPixmap(
                self.video.convertFrame())
            self.videoFrame.setScaledContents(True)
        except TypeError:
            print ("No frame")
            
    def change(self,event):
        self.value+=1
        self.value=self.value%2
        self.plot_main.clear()
        
            
    def make_temp(self):
        f=open("data.txt",'r')
        yo=[j for j in f]
        data=[x for x in yo[0].split(',')]
        print(data)
        f.close()
        if len(self.list_tem)>5:
            del(self.list_tem[0])
            #print(self.list_alt)
            self.canvas2.draw()
            self.plot_temp.clear()
            self.plot_temp.plot(self.list_tem,'g')
            self.plot_temp.axes.get_xaxis().set_visible(False)
            self.plot_temp.axes.get_yaxis().set_visible(False)
            #self.label_22.setText(data[3])
            
            self.list_tem.append(int(data[3]))
        else:
            self.canvas2.draw()
            self.plot_temp.clear()
            self.plot_temp.plot(self.list_tem,'g')
            self.list_tem.append(int(data[3]))
            #self.label_22.setText(data[3])
            self.plot_temp.axes.get_xaxis().set_visible(False)
            self.plot_temp.axes.get_yaxis().set_visible(False)
            
        if self.value == 0:
            if len(self.list_tem)>5:
                self.canvas1.draw()
                self.plot_main.clear()
                self.plot_main.set_title('Temprature')
                self.plot_main.set_xlabel('Time in sec')
                self.plot_main.set_ylabel('Temprature in K')
                self.plot_main.plot(self.list_tem,'g')
                self.plot_main.text(0.9, 0.9, 'Temprature %s K'%str(data[3]), horizontalalignment='right',verticalalignment='top',transform=self.plot_main.transAxes)
            else:
                self.canvas1.draw()
                self.plot_main.clear()
                self.plot_main.set_title('Temprature')
                self.plot_main.set_xlabel('Time in sec')
                self.plot_main.set_ylabel('Temprature in K')
                self.plot_main.plot(self.list_tem,'g')
                self.plot_main.text(0.9, 0.9, 'Temprature %s K'%str(data[3]), horizontalalignment='right',verticalalignment='top',transform=self.plot_main.transAxes)
                
        QtCore.QTimer.singleShot(500, lambda: self.make_temp())

        
    def make_pre(self):
        f=open("seds_temp.txt",'r')
        yo=[j for j in f]
        data=[x for x in yo[0].split(',')]
        print(data)
        f.close()
        if len(self.list_pre)>5:
            del(self.list_pre[0])
            #print(self.list_alt)
            self.canvas3.draw()
            self.plot_pre.clear()
            self.plot_pre.plot(self.list_pre,'b')
            self.plot_pre.axes.get_xaxis().set_visible(False)
            self.plot_pre.axes.get_yaxis().set_visible(False)
            #self.label_22.setText(data[3])
            
            self.list_pre.append(int(data[3]))
        else:
            self.canvas3.draw()
            self.plot_pre.clear()
            self.plot_pre.plot(self.list_pre,'b')
            self.list_pre.append(int(data[3]))
            #self.label_22.setText(data[3])
            self.plot_pre.axes.get_xaxis().set_visible(False)
            self.plot_pre.axes.get_yaxis().set_visible(False)
        if self.value == 1:
            if len(self.list_pre)>5:
                
                self.canvas1.draw()
                self.plot_main.clear()
                self.plot_main.set_title('Pressure')
                self.plot_main.set_xlabel('Time in sec')
                self.plot_main.set_ylabel('Pressure in Pascal')
                self.plot_main.plot(self.list_pre,'b')
                self.plot_main.text(0.9, 0.9, 'Pressure %s Pa'%str(data[2]), horizontalalignment='right',verticalalignment='top',transform=self.plot_main.transAxes)
                
            else :
                self.canvas1.draw()
                self.plot_main.clear()
                self.plot_main.set_title('Pressure')
                self.plot_main.set_xlabel('Time in sec')
                self.plot_main.set_ylabel('Pressure in P')
                self.plot_main.plot(self.list_pre,'b')
                self.plot_main.text(0.9, 0.9, 'Pressure %s P'%str(data[2]), horizontalalignment='right',verticalalignment='top',transform=self.plot_main.transAxes)
             
                

            
        
        
        QtCore.QTimer.singleShot(500, lambda: self.make_pre())
    
        


if __name__ == '__main__':
    app =QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
