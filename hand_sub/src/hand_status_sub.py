#!/usr/bin/env python
# Publishing hand status value of Raspi SenseHAT

import rospy
import sys

from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int32MultiArray
from time import sleep
#from sensor_msgs.mgs import Imu
#from sensor_msgs.msg import Imu

def callback(msg):
#    print msg.data[2]
    print ("x=%.3f, y=%.3f, z=%.3f" % msg.data)


def hand_status_sub():
    node_name = rospy.get_name()
    sub = rospy.Subscriber('hand_command', Float32MultiArray, callback)    
    rospy.spin()


if __name__ == '__main__':
    try:               
        rospy.init_node('hand_status_sub', anonymous=True)
        hand_status_sub()
    except rospy.ROSInterruptException:
        pass

