#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:09:55 2017

@author: sarthak
"""
import socket
import pickle               

s = socket.socket()         
host = socket.gethostname() 
port = 5672               

s.connect((host, port))

data=s.recv(1024)
data_arr = pickle.loads(data)
s.close
print (data_arr)
    
class sensor:
    def __init__(self):
        self.a=data_arr[0]
        self.b=data_arr[1]
        self.c=data_arr[2]
        self.d=data_arr[3]
        self.e=data_arr[4]
        self.f=data_arr[5]
        self.g=data_arr[6]
        self.h=data_arr[7]
        self.i=data_arr[8]
        self.j=data_arr[9]
        self.k=data_arr[10]
        self.l=data_arr[11]
        self.m=data_arr[12]
        self.n=data_arr[13]
        self.o=data_arr[14]
        self.p=data_arr[15]
        self.q=data_arr[16]
        self.r=data_arr[17]
        self.s=data_arr[18]
        self.t=data_arr[19]
        self.u=data_arr[20]
        self.v=data_arr[21]
        self.w=data_arr[22]
        self.x=data_arr[23]
        self.y=data_arr[24]
    