# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket
#import serial
#from time import sleep
import random
import pickle

#ser=serial.Serial('Enter the port here', 9600)  # establishing the connection with specified port  

s=socket.socket()
host=socket.gethostname()
port=5672
s.bind((host,port))

s.listen(5)
while True:
    c,addr=s.accept()
    print("Got Connection from",addr)
    l=list()
    """for i in range(0,25):
        l.append(ser.readline()) #reading 25 different sensor data from the arduino output
        sleep(.1) # Delay for one tenth of a second same should be in arduino code """

    for i in range (0,25):
        l.append(random.randint(65,122))
        
    data=pickle.dumps(l)
    c.sendall(data)
    c.close()