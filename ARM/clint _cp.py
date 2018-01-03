import socket               

import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)


s = socket.socket()        
host = '192.168.1.103'# ip of raspberry pi 
port = 12328     
s.connect((host, port))

def get_angle(angle):
	x=angle
	out_min=650
	out_max=2350
	in_max=180
	in_min=0
	pluse_wide = (x - in_min) * (out_max - out_min) /(in_max -in_min) + out_min
	anlog_v=int(float(pluse_wide)/1000000*50*4096)
	print(anlog_v)
	return anlog_v



def get_servo_angles(base,shoulder,eldow):
	elb=abs(290-eldow-90)
	sh1=45-shoulder
	bas=base
	s=get_angle(sh1)
	e=get_angle(elb)
	b=get_angle(base)
	
	print("Shoulder:",shoulder,s,sh1)
	pwm.set_pwm(1,0,s)
	pwm.set_pwm(2,0,e)
	pwm.set_pwm(0,0,b)
	
	
	
while True:
    try:
        d=s.recv(1024).decode()
        print(d)
        d=d.split(" ")
        base=int(d[0])
        shoulder=int(d[1])
        eldow=int(d[2])
        get_servo_angles(base,shoulder,eldow)
        
        #d=input()
        #s.send(d).encode()
    except Exception as e:
        print(e)
        pass
s.close()

