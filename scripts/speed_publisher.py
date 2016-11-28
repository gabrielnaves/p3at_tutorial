#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from p3at_tutorial.msg import KeyboardMessage

def callback(data):
    rospy.loginfo('I heard %s', data.key)

def speed_publisher():
    rospy.init_node('speed_publisher', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    rospy.Subscriber('keyboard_topic', KeyboardMessage, callback, queue_size = 1)

    
    while not rospy.is_shutdown():
        vel_lin = 1
        vel_ang = 0

        speed = Twist()
        speed.linear = Vector3(vel_lin,0,0)
        speed.angular = Vector3(0,0,vel_ang)
        #rospy.loginfo(speed)
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        speed_publisher()
    except rospy.ROSInterruptException:
        pass
