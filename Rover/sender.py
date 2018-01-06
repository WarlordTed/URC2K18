import socket
import sys
TCP_PORT = int(sys.argv[1])


TCP_IP = '192.168.43.243' # this IP of my pc. When I want raspberry pi 2`s as a server, I replace it with its IP '169.254.54.195'

BUFFER_SIZE = 20 # Normally 1024, but I want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

"""*
 *     w
 * a       d
 *     s
 * 
 * p-stop
 * q-speed inc
 * e-speed dec
 * 
 *"""


conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
  try:
    s=getch.getch()
    data=s.encode()
    conn.send(data)  
  except Exception, e:
    conn.close()
    conn.send("bye") 
    print  "BYE BYE"
    exit()
    #raise e
  
conn.close()