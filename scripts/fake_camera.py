#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import String
import math

resolution = 0.05
color_index = {(resolution*(1460-2000),resolution*(2000-2000)) : "red",
    (resolution*(1550-2000),resolution*(2000-2000)) : "green",
    (resolution*(1640-2000),resolution*(2000-2000)) : "blue", 
    (resolution*(1730-2000),resolution*(2000-2000)) : "pink", 
    (resolution*(1820-2000),resolution*(2000-2000)) : "yellow", 
    (resolution*(1910-2000),resolution*(2000-2000)) : "purple", 
    (resolution*(2000-2000),resolution*(2000-2000)) : "brown", 
    (resolution*(2090-2000),resolution*(2000-2000)) : "orange",
    (resolution*(2180-2000),resolution*(2000-2000)) : "black",
    (resolution*(2270-2000),resolution*(2000-2000)) : "white"
}
robot_position = [0,0]
color = ''

def processPosition(pose):
    global color_index
    global color
    for key in color_index:
        position = pose.pose.pose.position
        if position.x >= key[0] - 0.2 and position.x <= key[0] + 0.2:
            if position.y >= key[1] - 0.2 and position.y <= key[1] + 0.2:
                color = color_index[key]
    
def fake_camera_node():
    rospy.init_node('localization_node', anonymous=True)
    rate = rospy.Rate(10)
    
    pub = rospy.Publisher('color', String, queue_size=10)
    rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, processPosition, queue_size = 1)

    global color

    while not rospy.is_shutdown():
        if color != '':
            print color
            pub.publish(color)
            color = ''
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_camera_node()
    except rospy.ROSInterruptException:
        pass
