from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import ik_2link
import socket
import sys
import math
import pygame
import pickle
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.103'
port = int(sys.argv[1])
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
print(addr, host)
'''
class SimpleRobotArm:
		def __init__(self):

				self.angles=[90,45,225] #base shoulder elbow
				self.config=[0,0] #(thetha,beta),(xy,zx)
				self.anglstep=5
				self.xyz=[0.5,0.2,0.05]
				self.xyzstep=0.025
				self.name = "Simple Robot Arm"
				self.mode="inverse" # inverse reverse combat mouse
				# thresholds = [[base_l,base_h],[shoulder........],[elbow........]]
				self.thresh = [[-5, 182], [1, 70], [201, 335]]
				self.r_max=1.32
				self.view="no_view"
				self.golax=0
				self.golay=0
				self.pos_c=[0,0]

		def run(self):

				glutInit(sys.argv)
				glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
				glutInitWindowSize(600, 800)
				glutInitWindowPosition(100, 100)
				glutCreateWindow(self.name)  
				glClearColor(0.0, 0.0, 0.0, 0.0)
				glShadeModel(GL_FLAT)
				glutDisplayFunc(self.display)
				glutReshapeFunc(self.reshape)
				glutKeyboardFunc(self.keys)
				glutMainLoop()

		def display(self):

				glClear(GL_COLOR_BUFFER_BIT);
				glPushMatrix();
				glTranslatef(0, -2, -4);
			
				glEnable(GL_BLEND)
				glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);
				glRotatef(self.golax, 0, 1, 0);
				glRotatef(self.golay, 1, 0, 0);
				glColor4f(0.0,0.0,1.0,1)
				if(self.dis(self.xyz)>self.r_max):
						glColor4f(1.0,0,0,0.5)	
				glPushMatrix();
				if(self.view=="view"):
						glutWireSphere(3.13*1.37,25,25)	
				glPopMatrix();
				glDisable(GL_BLEND)

				glColor4f(1.0,1.0,1.0,0.5)
				glTranslatef(0, 0, 0);
				if(self.angles[0]>self.thresh[0][1]-20 or self.angles[0]<self.thresh[0][0]+20):
						glColor4f(1.0,0,0,0.5)
				bbb = self.angles[0] - 90
				glRotatef(bbb, 0, 1, 0);
				glTranslatef(0, 0.0, 0.0);
				glPushMatrix();
				glScalef(10, 1, 5);
				glutWireCube(0.5)

				glPopMatrix();
				glColor4f(1.0,1.0,1.0,0.5)
				glTranslatef(0, 0.25, 0);
				if(self.angles[1]>self.thresh[1][1]-20 or self.angles[1]<self.thresh[1][0]+20):
						glColor4f(1.0,0,0,0.5)

				glRotatef(self.angles[1], 0, 0.0, 1);
				glTranslatef(1, 0, 0.0);
				glPushMatrix();
				glScalef(2.0, 0.2, 0.5);
				glutWireCube(1.1);
				glPopMatrix();

				glColor4f(1,1,1,0.5)
				glTranslatef(1.2, 0.0, 0.0);
				if(self.angles[2]>self.thresh[2][1]-20 or self.angles[2]<self.thresh[2][0]+20):
						glColor4f(1.0,0,0,0.5)
				glRotatef(self.angles[2], 0.0, 0.0, 1.0);
				glTranslatef(1.2, 0.0, 0.0);
				glPushMatrix();
				glScalef(2.0, 0.2, 0.5);
				glutWireCube(1.3);
				glPopMatrix();

				glPopMatrix();
				glutSwapBuffers();

		def reshape(self, w, h):

				glViewport(0, 0, w, h)
				glMatrixMode(GL_PROJECTION)
				glLoadIdentity()
				gluPerspective(65.0, w / h, 1.0, 20.0)
				glMatrixMode(GL_MODELVIEW)
				glLoadIdentity()
				glTranslatef(0.0, 0.0, -6.0)

		def recover(self,thresh):
				
				if(self.angles[0]<=thresh[0][0]):
					self.angles[0]=(self.angles[0]+5)%360
				elif(self.angles[0]>=thresh[0][1]):
					self.angles[0]=(self.angles[0]-5)%360
				
				if(self.angles[1]<=thresh[1][0]):
					self.angles[1]=(self.angles[1]+5)%360
				elif(self.angles[1]>=thresh[1][1]):
					self.angles[1]=(self.angles[1]-5)%360

				if(self.angles[2]<=thresh[2][0]):
					self.angles[2]=(self.angles[2]+5)%360
				elif(self.angles[2]>=thresh[2][1]):
					self.angles[2]=(self.angles[2]-5)%360


		def view_mode(self,keys):

				if(self.view=="view"):
							if(keys=='f'.encode("utf-8")):
									self.golax+=2
							elif(keys=='h'.encode("utf-8")):
									self.golax-=2
							elif(keys=='t'.encode("utf-8")):
									self.golay+=2
							elif(keys=='g'.encode("utf-8")):
									self.golay-=2

		def find_config(self,xyz): 
				#finding arm comfigurations, angles made by the inposition of line on y and z axis
				'''
				rxy=self.dis([self.xyz[0],self.xyz[1],0])
				rzx=self.dis([self.xyz[0],0,self.xyz[2]])
				self.config[1]=math.atan(self.xyz[1]/self.xyz[0])
				self.config[0]=math.atan(self.xyz[2]/self.xyz[0])	
				'''
				self.config[1]=((self.angles[0]-90)*3.14)/180
				alpha=-180+self.angles[2]
				beta=self.angles[1]
				a=180-(alpha+beta)
				self.config[0]=((a*3.14)/180)
				self.config[0]=(math.atan(self.xyz[2]/self.xyz[0]))
				print("Config",self.config)
				print("a",a,alpha,beta)	

		def apply(self,angles,xyz,angles_chg,xyz_chg):
				self.angles[0]=angles[0]+angles_chg[0]
				self.angles[1]=angles[1]+angles_chg[1]
				self.angles[2]=angles[2]+angles_chg[2]
				self.xyz[0]=xyz[0]+xyz_chg[0]
				self.xyz[1]=xyz[1]+xyz_chg[1]
				self.xyz[2]=xyz[2]+xyz_chg[2]

		def dis(self,xyz):
				x,y,z=xyz
				s=(x**2+y**2+z**2)**(1/2)
				
				return (s)
		def angle_check(self,angles):
				if(self.thresh[0][0]<angles[0]<self.thresh[0][1] and self.thresh[1][0]<angles[1]<self.thresh[1][1] and 
					self.thresh[2][0]<angles[2]<self.thresh[2][1]):
					return 1
				return 0

		def apply_ik(self,xyz):
				
				ik_angles = ik_2link.get_angles(self.xyz)
				ik_angles=ik_angles[1:-1]
				ik_angles1=[0,0,0]
				ik_angles1=ik_angles+[90,45,225]
				if(self.angle_check(ik_angles1) and self.dis(self.xyz)<self.r_max):
						self.apply([90,45,225],self.xyz,ik_angles,[0,0,0])
				else:
						print("Cannot Reach")

		def keys(self,*args):
				self.find_config(self.xyz)				
				
				keys=args[0]
				
				if(keys=='i'.encode("utf-8") or keys=='z'.encode("utf-8")):
						self.mode="inverse"
				elif(keys=='r'.encode("utf-8")):
						self.mode="reverse"
				elif(keys=='c'.encode("utf-8")):
						self.apply([90,45,225],[0.75,0,0],[0,0,0],[0,0,0])
				elif(keys=='v'.encode("utf-8")):
						self.view="view"
				elif(keys=='b'.encode("utf-8")):
						self.view="no_view"
				elif(keys=='V'.encode("utf-8")):
						self.mode="view"
				elif(keys=='C'.encode("utf-8")):
						self.golay=0
						self.golax=0
				elif(keys=='m'.encode("utf-8") or keys=='x'.encode("utf-8")):
						self.mode="combat"
						print(self.mode)
				elif(keys=='n'.encode("utf-8")):
						self.find_config(self.xyz)
						self.mode="battle"
				elif(keys=='+'.encode("utf-8")):
						self.xyzstep+=0.025
				elif(keys=='-'.encode("utf-8")):
						self.xyzstep-=0.025
				elif(keys=='j'.encode("utf-8")):
						self.mode="mouse"
			
				self.anglstep=self.xyzstep*100
				self.view_mode(keys)


				if(self.angle_check(self.angles)):
						
						if(self.mode=="inverse"):

								test=ik_2link.get_position([0,((self.angles[0]-90)*3.14)/180,((self.angles[1]-45)*3.14)/180,((self.angles[2]-225)*3.14)/180,0])
								self.xyz=test

								if(keys=='8'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,0],[self.xyzstep,0,0])
								elif(keys=='2'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,0],[-self.xyzstep,0,0])
								elif(keys=='4'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,0],[0,self.xyzstep,0])
								elif(keys=='7'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,0],[0,0,self.xyzstep])
								elif(keys=='3'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,0],[0,0,-self.xyzstep])

								elif(keys=='6'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,0],[0,-self.xyzstep,0])
								elif(keys=='5'.encode("utf-8")):
										self.apply([90,45,225],[0.6,0,0],[0,0,0],[0,0,0])

								self.apply_ik(self.xyz)

						elif(self.mode=="reverse"):
									
								if(keys=='q'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[self.anglstep,0,0],[0,0,0])
								elif(keys=='a'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[-self.anglstep,0,0],[0,0,0])
								elif(keys=='w'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,self.anglstep,0],[0,0,0])
								elif(keys=='s'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,-self.anglstep,0],[0,0,0])
								elif(keys=='e'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,self.anglstep],[0,0,0])
								elif(keys=='d'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,-self.anglstep],[0,0,0])
						
						elif(self.mode=="combat"):
							
								test=ik_2link.get_position([0,((self.angles[0]-90)*3.14)/180,((self.angles[1]-45)*3.14)/180,((self.angles[2]-225)*3.14)/180,0])
								self.xyz=test
								r=self.dis(self.xyz)
								print("R",r)
								z=self.xyz[2]

								if(keys=='8'.encode("utf-8")):
										r+=self.xyzstep
								elif(keys=='2'.encode("utf-8")):
										r-=self.xyzstep
								elif(keys=='7'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,0],[0,0,self.xyzstep])
								elif(keys=='3'.encode("utf-8")):
										self.apply(self.angles,self.xyz,[0,0,0],[0,0,-self.xyzstep])
							
								theta=self.config[0]
								beta=self.config[1]
								x=r*math.cos(theta)*math.cos(beta)
								y=r*math.cos(theta)*math.sin(beta)
								self.xyz=[x,y,self.xyz[2]]
								self.apply_ik(self.xyz)
							
						elif(self.mode=="mouse"):
								
								pickle_in = open('Frame.pickle','rb')
								clf = pickle.load(pickle_in)
								print("CLF",clf)
								self.xyz=[clf[0],clf[1],0]
								self.apply_ik(self.xyz)

				else:

						self.recover(self.thresh) #recovery from the worst case

				glutPostRedisplay()
				
				'''
				d = ""
				d = (str(int(self.angles[0])) + " " + str(int(self.angles[1])) + " " + str(int(self.angles[2])) + ".").encode()
				c.send(d)
				'''

				print("Mode:",self.mode)
				print("Angles:",self.angles)
				print("XYZ:",self.xyz)
				print("XYZStep:",self.xyzstep)
				print("Config",self.config)
				print("Distance:",self.dis(self.xyz))
				print("anglstep:",self.anglstep)
			

if __name__ == '__main__':
		app = SimpleRobotArm()
		app.run()
