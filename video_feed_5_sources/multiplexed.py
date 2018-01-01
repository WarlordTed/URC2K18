'''print('Enter code: ')
a=int(input())
'''

from multiprocessing import Process
import sys
import main_port1
import main_port2
import main_port3
import main_port4
import main_port5

a=b=c=d=e=1

def func1():
	if __name__ == '__main__':
		main_port1.app.run(host='0.0.0.0', debug=True, threaded=True, port=80)

def func2():
	if __name__ == '__main__':
		main_port2.app.run(host='0.0.0.0', debug=True, threaded=True, port=5600)

def func3():
	if __name__ == '__main__':
		main_port3.app.run(host='0.0.0.0', debug=True, threaded=True, port=5800)

def func4():
	if __name__ == '__main__':
		main_port4.app.run(host='0.0.0.0', debug=True, threaded=True, port=4400)

def func5():
	if __name__ == '__main__':
		main_port5.app.run(host='0.0.0.0', debug=True, threaded=True, port=4800)



if __name__ == '__main__':
	if(a==1):
   		p1 = Process(target = func1)
   		p1.start()
   	if(b==1):
   		p2 = Process(target = func2)
   		p2.start()
   	if(c==1):
   		p3 = Process(target = func3)
   		p3.start()
	if(d==1):
		p4 = Process(target = func4)
   		p4.start()
   	if(e==1):
		p5 = Process(target = func5)
   		p5.start()