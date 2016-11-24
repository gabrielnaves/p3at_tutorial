#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def speed_publisher():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('speed_publisher', anonymous=True)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        vel_lin = 1
        vel_ang = 0

        speed = Twist()
        speed.linear = Vector3(vel_lin,0,0)
        speed.angular = Vector3(0,0,vel_ang)
        rospy.loginfo(speed)
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        speed_publisher()
    except rospy.ROSInterruptException:
        pass
