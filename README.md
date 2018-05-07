# ros-app-tb3-hand-motion-teleop
* This code uses Raspberry Pi3(RASP3) and Sense HAT module.
* Accelerometer on Sense HAT module senses the angles (Pitch and Roll) of hand to control the TurtleBot3 

# Package configuration
* hand_motion package 
  : Publishing package of RASP3 on Hand 
  : Sensing the 3-axis acceleration in G-dimension (1G = 9.8m/s^2) 
* Hand_sub package 
 - Subscribing package of RASP3 on Turtlebot3 
 - Trasfoming the acceleration to topic cmd_vel (Linear & Angular velocity) 
 
