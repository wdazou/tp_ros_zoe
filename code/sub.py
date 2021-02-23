#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
from geomerty.msgs import PoseStamped
import numpy as np


def callback(data):

    print(data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('topic_sub_infini', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()