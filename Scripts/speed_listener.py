#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def callback(data):
    pass
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def speed_listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('speed_listener', anonymous=True)
    rospy.Subscriber('speed_publisher', Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    speed_listener()
