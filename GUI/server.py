import socket                                         
import time
from random import randint

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 8502

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           
c,addr = serversocket.accept()      
while True:
    # establish a connection
    d=str(randint(0,9)) + "," + str(randint(0,9)) + "," + str(randint(0,9)) + "," + str(randint(0,9))+"," + str(randint(0,9))
    d=d.encode()
    c.send(d)
    time.sleep(1)

c.close()
