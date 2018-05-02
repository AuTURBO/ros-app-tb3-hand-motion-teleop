#!/usr/bin/env python
# Publishing hand status value of Raspi SenseHAT

import rospy
import sys

from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist
from time import sleep

FWV = [0.05, 0.1, 0.2]
RTV = [0.1, 0.2, 0.3]

def callback(msg):
#   msg.data[0] : x-axis, right
#   msg.data[1] : y-axis, forward
#   msg.data[2] : z-axis, down
#    print msg.data[0]
    print ("x=%.3f, y=%.3f, z=%.3f" % msg.data)
    FW = msg.data[1]
    RT = msg.data[0]

    target_linear_vel = 0
    target_angular_vel = 0

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    # Forward moving velocity
    if FW > 0.2 and FW <= 0.4 :
        target_linear_vel = FWV[0]

    elif FW > 0.4 and FW <= 0.6 :
        target_linear_vel = FWV[1]

    elif FW > 0.6 :
        target_linear_vel = FWV[2]

    elif FW < -0.2 and FW >= -0.4 :
        target_linear_vel = -FWV[0]

    elif FW < -0.4 and FW >= -0.6 :
        target_linear_vel = -FWV[1]

    elif FW < -0.6 :
        target_linear_vel = -FWV[2]

    else:
        target_linear_vel = 0                

    # Rotating velocity
    if RT > 0.2 and RT <= 0.4 :
        target_angular_vel = RTV[0]

    elif RT > 0.4 and RT <= 0.6 :
        target_angular_vel = RTV[1]

    elif RT > 0.6 :
        target_angular_vel = RTV[2]

    elif RT < -0.2 and RT >= -0.4 :
        target_angular_vel = -RTV[0]

    elif RT < -0.4 and RT >= -0.6 :
        target_angular_vel = -RTV[1]

    elif RT < -0.6 :
        target_angular_vel = -RTV[2]

    else:
        target_angular_vel = 0     
           
    print ("Linear vel %.2f , Angular vel %.2f " % (target_linear_vel, target_angular_vel) )

    twist = Twist()
    twist.linear.x = target_linear_vel; twist.linear.y = 0; twist.linear.z = 0
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = target_angular_vel
    pub.publish(twist)

def hand_status_sub():
    node_name = rospy.get_name()
    sub = rospy.Subscriber('hand_command', Float32MultiArray, callback)    
    rospy.spin()

#def vels(target_linear_vel, target_angular_vel):
#    return "currently:\Linear vel %s\Angular vel %s " % (target_linear_vel,target_angular_vel)


if __name__ == '__main__':
    try:               
        rospy.init_node('hand_status_sub', anonymous=True)
        hand_status_sub()
    except rospy.ROSInterruptException:
        pass

