#!/usr/bin/env python

import rospy
from nav_msgs.msg import OccupancyGrid
from enum import Enum
import math

def callback(grid):
    pass    
    #print grid.data[]

def map_listener():
    rospy.init_node('map_listener', anonymous=True)
    #pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    rospy.Subscriber('map', OccupancyGrid, callback, queue_size = 1)
    
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:
        map_listener()
    except rospy.ROSInterruptException:
        pass
