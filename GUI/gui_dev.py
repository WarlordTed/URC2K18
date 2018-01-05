from PyQt5.uic import loadUiType
from PyQt5 import QtGui
from PyQt5 import  QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication

from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

import socket
import random
import sys

Ui_MainWindow, QMainWindow = loadUiType('gui_dev.ui')

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self,):
        super(Main,self).__init__()
        self.setupUi(self)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname() 
        port = 8500
        self.s.connect((host, port))
        
        #self.list_alt = [random.randint(0, 10) for i in range(5)]
        self.item = []

        self.getdata()
        figure = Figure(facecolor='white')
        self.canvas = FigureCanvas(figure)
        self.sensorgraph.addWidget(self.canvas)
        self.canvas.draw()

        self.plotgraph = figure.add_subplot('111', axisbg='white')
        self.plotgraph.clear()
        self.plotgraph.plot(self.item,'g')

        self.update_label()

    def getdata(self):
        self.data = self.s.recv(1024).decode()
        self.item = [i for i in self.data.split(',')]
        QtCore.QTimer.singleShot(1000, lambda: self.getdata())

    def update_label(self):
        self.label1.setText(self.item[0])
        self.label2.setText(self.item[1])
        self.label3.setText(self.item[2])
        self.label4.setText(self.item[3])
        self.label5.setText(self.item[4])
        QtCore.QTimer.singleShot(1000, lambda: self.update_label())

if __name__ == '__main__' :
    app=QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())