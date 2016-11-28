#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from p3at_tutorial.msg import KeyboardMessage
from enum import Enum
import math

up = 119
down = 115
right = 100
left = 97

vel_lin = 0
vel_ang = 0

def callback(data):
    global vel_lin
    global vel_ang
    if data.key == up:
        vel_lin = 1;
        vel_ang = 0;
    if data.key == down:
        vel_lin = -1;
        vel_ang = 0;
    if data.key == right:
        vel_lin = 0;
        vel_ang = -math.pi/2;
    if data.key == left:
        vel_lin = 0;
        vel_ang = math.pi/2;

def speed_publisher():
    global vel_lin
    global vel_ang

    rospy.init_node('speed_publisher', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    rospy.Subscriber('keyboard_topic', KeyboardMessage, callback, queue_size = 1)
    
    while not rospy.is_shutdown():
        speed = Twist()
        speed.linear = Vector3(vel_lin,0,0)
        speed.angular = Vector3(0,0,vel_ang)
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        speed_publisher()
    except rospy.ROSInterruptException:
        pass
