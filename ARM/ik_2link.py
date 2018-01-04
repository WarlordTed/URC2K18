import ikpy
import numpy as np
from ikpy import plot_utils
import matplotlib.pyplot as plt
from matplotlib import animation


ax = plot_utils.init_3d_figure()


def get_angles(xyz):
        x=xyz[0]
        y=xyz[1]
        z=xyz[2]
        my_chain = ikpy.chain.Chain.from_urdf_file("robot_2link.URDF")
        target_vector = [x,y,z]
        target_frame = np.eye(4)
        target_frame[:3, 3] = target_vector
        #print("The angles of each joints are : ", my_chain.inverse_kinematics(target_frame))
        real_frame = my_chain.forward_kinematics(my_chain.inverse_kinematics(target_frame))
       #print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))


        ax = plot_utils.init_3d_figure()
        my_chain.plot( [ 0,0,0,0,0],ax, target=target_vector)
        my_chain.plot(my_chain.inverse_kinematics(target_frame), ax, target=target_vector)
        angles=my_chain.inverse_kinematics(target_frame)
        angles[1]=(angles[1]*180)/3.14
        angles[2]=(angles[2]*180)/3.14
        angles[3]=(angles[3]*180)/3.14
        #print(angles)
        #plt.xlim(-1,1)
        #plt.ylim(-1,1)
        #plt.show()
       
        return angles

def get_position(angles):
        real_frame1=[0,0,0]
        my_chain = ikpy.chain.Chain.from_urdf_file("robot_2link.URDF")
        real_frame = my_chain.forward_kinematics(angles)
        real_frame1[0]=real_frame[0][3]
        real_frame1[1]=real_frame[1][3]
        real_frame1[2]=real_frame[2][3]
        return real_frame1
#x=get_position(get_angles(0,0.4,0.0))
#print(x)

