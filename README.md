# ros-app-tb3-hand-motion-teleop
* This code uses Raspberry Pi3(RASP3) and Sense HAT module.
* Accelerometer on Sense HAT module senses the angles (Pitch and Roll) of hand to control the TurtleBot3 

# Package configuration
* hand_motion package 
  * Publishing package of RASP3 on Hand 
  * Sensing the 3-axis acceleration in G-dimension (1G = 9.8m/s^2)
  * Publishing topic : hand-command, consisting of 3 axis acceleratioin values
* hand_sub package 
  * Subscribing & Publisching package of RASP3 on Turtlebot3
  * Transfoming the acceleration to Linear & Angular velocity command (topic cmd_vel)
  * Subscribing topic : hand_cammand
  * Publishing topic : cmd_vel
 
