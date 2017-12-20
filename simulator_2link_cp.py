from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import socket

s = socket.socket()
host = '192.168.43.122' #ip of raspberry pi
port = 12328
s.bind((host, port))

s.listen(5)
c, addr = s.accept()

print(addr)
def pulseWIdth(angle):
    x=angle
    out_min=650
    out_max=2350
    in_max=180
    in_min=0
    pluse_width = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    analog_value=int(float(pluse_width)/1000000*60*4096)
    print(analog_value)
    return analog_value


class SimpleRobotArm:

    def __init__(self):
        self.name= "Simple Robot Arm"
        self.shoulder = 0
        self.elbow = 225
        self.arm = 0.0
        self.wrist = 0.0
        self.shoulder1=45


    def run(self):

        glutInit(sys.argv) # initialise the system
        # Configure inital display mode
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

        # Set up and display initial window
        glutInitWindowSize(1000,1000)
        glutInitWindowPosition(100,100)
        glutCreateWindow(self.name)  # See the __init__ method for self.name

        # Initial colour and shading model
        glClearColor(0.0,0.0,0.0,0.0)
        glShadeModel(GL_FLAT)

        # Register callback methods. The arguments are the names of
        # methods defined below.
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        # glutMouseFunc(self.mouse) # not needed here
        glutKeyboardFunc(self.keys)
        #glutJoystickFunc(self.joystick,0)
        
        glutMainLoop()
        
        # Launch the OGL event processing loop
        

    def display(self):
        glClear (GL_COLOR_BUFFER_BIT);
        glPushMatrix();


        glTranslatef (0, -4, -4);
        glRotatef (self.shoulder, 0, 1, 0);
        glTranslatef (0, 0.0, 0.0);
        glPushMatrix();
        glScalef (10, 1, 5);
        glutWireCube(0.5)

        glPopMatrix();

        glTranslatef(0, 0.25, 0);
        glRotatef(self.shoulder1, 0, 0.0, 1);
        glTranslatef(1.2, 0, 0.0);
        glPushMatrix();
        glScalef(2.0, 0.2, 0.5);
        glutWireCube(1.2);
        glPopMatrix();

        glTranslatef (1.2, 0.0, 0.0);
        glRotatef (self.elbow, 0.0, 0.0, 1.0);
        glTranslatef (1, 0.0, 0.0);
        glPushMatrix();
        glScalef (2.0, 0.2, 0.5);
        glutWireCube (1);
        glPopMatrix();

        glTranslatef (0.6, 0.0, 0.0);
        glRotatef (self.wrist, 1, 0, 0);
        glTranslatef (0.5, 0.0, 0.0);
        glPushMatrix();
        glScalef (0.6, 0.7, 0.8);
        glutWireCube (0.5);
        glPopMatrix();


        
        glPopMatrix();
        glutSwapBuffers();

   

    def reshape(self,w,h):
        glViewport (0, 0, w, h)
        glMatrixMode (GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, w/h, 1.0, 20.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef (0.0, 0.0, -6.0)

    def keys(self,*args):
        key = args[0]
        
        if (key == 'a'.encode("utf-8")):
            self.shoulder = (self.shoulder+5) % 360

        elif (key==('d').encode("utf-8")):
            self.shoulder = (self.shoulder-5) % 360

        elif (key==('e').encode("utf-8")):
            self.elbow = (self.elbow+5) % 360

        elif (key==('E').encode("utf-8")):
            self.elbow = (self.elbow-5) % 360

        elif (key==('w').encode("utf-8")):
            self.arm = (self.arm+5) % 360

        elif (key==('W').encode("utf-8")):
            self.arm = (self.arm-5) % 360

        elif (key==('x').encode("utf-8")):
            self.wrist = (self.wrist-5) % 360

        elif (key==('X').encode("utf-8")):
            self.wrist = (self.wrist+5) % 360

        elif (key==('a').encode("utf-8")):
            self.finger2 = (self.finger2-5) % 360
      
        elif(key==('s').encode("utf-8")):
            self.shoulder1 = (self.shoulder1 + 5) % 360

        elif(key==('S').encode("utf-8")):
            self.shoulder1 = (self.shoulder1 - 5) % 360
        d=(str(self.shoulder)+" "+str(self.shoulder1)+" "+str(self.elbow)).encode()
        c.send(d)
     
        glutPostRedisplay()

    def joystick(self,*args):
        xaxis = args[1]/1000
        yaxis = args[2]/1000
        if(abs(xaxis)<0.1):
            xaxis=0
        if(abs(yaxis)<0.1):
            yaxis=0
        if(args[1]==16):
            self.shoulder=self.shoulder+5
        if (args[3] == 32):
            self.shoulder = self.shoulder + 5
        self.shoulder1=self.shoulder1+xaxis*5
        self.elbow = self.elbow + yaxis * 5
        print(xaxis,yaxis)
        print(self.shoulder1)

        glutPostRedisplay()


if __name__ == '__main__':
  app = SimpleRobotArm()
  app.run()
  



