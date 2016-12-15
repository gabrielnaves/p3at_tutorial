#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
import math

def cartesianToPixel(x, y):
    return 4000*x + y

resolution = 0.05
position_index = {"red" : cartesianToPixel(1460-2000,2000-2000),
    "green" : cartesianToPixel(1550-2000,2000-2000),
    "blue" : cartesianToPixel(1640-2000,2000-2000), 
    "pink" : cartesianToPixel(1730-2000,2000-2000), 
    "yellow" : cartesianToPixel(1820-2000,2000-2000), 
    "purple" : cartesianToPixel(1910-2000,2000-2000), 
    "brown" : cartesianToPixel(2000-2000,2000-2000), 
    "orange" : cartesianToPixel(2090-2000,2000-2000),
    "black" : cartesianToPixel(2180-2000,2000-2000),
    "white" : cartesianToPixel(2270-2000,2000-2000)
}
robot_position = [0,0]

def convertPixelToMeter(pixel):
    global robot_position
    global resolution
    robot_position = [(pixel/4000)*resolution, (pixel%4000)*resolution]

def receiveColor(color):
    convertPixelToMeter(position_index[color.data])

last_time = 0
def dt():
    global last_time
    current_time = rospy.Time.now()
    time = (current_time.nsecs - last_time)/1000000000.0
    last_time = current_time.nsecs
    if time < 0:
        time = 0
    return time

def receiveVelocities(odom):
    global robot_position
    robot_position[0] = robot_position[0] + odom.twist.twist.linear.x*dt()
    robot_position[1] = robot_position[1] + odom.twist.twist.linear.y*dt()

def localization_node():
    rospy.init_node('localization_node', anonymous=True)
    rate = rospy.Rate(10)
    
    pub = rospy.Publisher('position', Vector3, queue_size=10)

    rospy.Subscriber('color', String, receiveColor, queue_size = 1)
    rospy.Subscriber('odom', Odometry, receiveVelocities, queue_size = 1)

    while not rospy.is_shutdown():
        pos = Vector3(robot_position[0], robot_position[1], 0)
        pub.publish(pos)
        rate.sleep()

if __name__ == '__main__':
    try:
        localization_node()
    except rospy.ROSInterruptException:
        pass
