import socket
import serial
import sys
TCP_PORT = int(sys.argv[1])

TCP_IP = '192.168.43.243' # this IP of my pc. When I want raspberry pi 2`s as a client, I replace it with its IP '169.254.54.195'
#TCP_PORT = 5005
BUFFER_SIZE = 1024

ser = serial.Serial('/dev/ttyACM0',9600)  #Serial


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
    data = s.recv(BUFFER_SIZE)
    #serial
    ser.write(str(data).encode())
    #serial
    if data == "bye":
        conn.close()

    print(data)
    pass

s.close()

print ("received data:", data)





