#!/usr/bin/env python
# Publishing hand status value of Raspi SenseHAT

import rospy
import sys

from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int32MultiArray
from sense_hat import SenseHat
from time import sleep
#from sensor_msgs.mgs import Imu
#from sensor_msgs.msg import Imu

SH = SenseHat()

# 0, 0 = Top left
# 7, 7 = Bottom right
UP_PIXELS = [[3, 0], [4, 0]]
DOWN_PIXELS = [[3, 7], [4, 7]]
LEFT_PIXELS = [[0, 3], [0, 4]]
RIGHT_PIXELS = [[7, 3], [7, 4]]
CENTER_PIXELS = [[3, 3], [4, 3], [3, 4], [4, 4]]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]


def set_pixels(pixels, col):
    for p in pixels:
        SH.set_pixel(p[0], p[1], col[0], col[1], col[2])

def hand_status():
    node_name = rospy.get_name()
    pub = rospy.Publisher('hand_command', Float32MultiArray, queue_size=1)    

    rate = rospy.Rate(10) # 10hz

    x=0
    y=0
    z=0  
    
    while not rospy.is_shutdown():
        x_p = x
        y_p = y
        z_p = z

        x, y, z = SH.get_accelerometer_raw().values()

        x = 0.5*x + 0.5*x_p;
        y = 0.5*y + 0.5*y_p;
        z = 0.5*z + 0.5*z_p;

        x = round(x, 3)
        y = round(y, 3)
        z = round(z, 3)

        if x > 0.2:
            set_pixels(DOWN_PIXELS, WHITE)
            set_pixels(UP_PIXELS, BLACK)
#        set_pixels(CENTER_PIXELS, BLACK)
#        Dir_turn = "R"
#        SH.show_message("R")
        elif x < -0.2:
            set_pixels(UP_PIXELS, WHITE)
            set_pixels(DOWN_PIXELS, BLACK)
#        set_pixels(CENTER_PIXELS, BLACK)
#        Dir_turn = "L"
#       SH.show_message("L")
        else: 

            set_pixels(UP_PIXELS, BLACK)
            set_pixels(DOWN_PIXELS, BLACK)
#        set_pixels(CENTER_PIXELS, WHITE)
    
        if y > 0.2:
            set_pixels(RIGHT_PIXELS, WHITE)
            set_pixels(LEFT_PIXELS, BLACK)
#        set_pixels(CENTER_PIXELS, BLACK)
#        Dir_go = "F"
#        SH.show_message("F")
        elif y < -0.2:
            set_pixels(LEFT_PIXELS, WHITE)
            set_pixels(RIGHT_PIXELS, BLACK)             
#        set_pixels(CENTER_PIXELS, BLACK)
        else: 
            set_pixels(LEFT_PIXELS, BLACK)
            set_pixels(RIGHT_PIXELS, BLACK)
#        set_pixels(CENTER_PIXELS, WHITE)
#        Dir_go = "B"
 #       SH.show_message("B")
#    set_pixels(CENTER_PIXELS, WHITE)

        print ("x=%.3f, y=%.3f, z=%.3f" % (x, y, z))

        #hand_angle = Float32MultiArray (x, y, z)

        hand_angle = Float32MultiArray();
        hand_angle.data = [x, y, z]
        pub.publish(hand_angle)
        rate.sleep()

if __name__ == '__main__':
    try:
        for i in range(0,8):
            for j in range(0,8):
                SH.set_pixel(i, j, BLACK)
        rospy.init_node('hand_status', anonymous=True)
        hand_status()
    except rospy.ROSInterruptException:
        pass








