#!/usr/bin/env python3
import rospy

from geometry_msgs.msg import PoseStamped
import numpy as np
import math

def talker():
	pub = rospy.Publisher('tp_note', PoseStamped, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(15) # 15hz
	msg = PoseStamped()
	print(msg)
	msg.header.frame_id="map"
	t = 0
	while not rospy.is_shutdown():
		
		while t <=  2*math.pi :	    
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(msg.pose.position.x)
			t = t + 0.1
		
			pub.publish(msg)
			rate.sleep()
			
		while t >=  0 :	    
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(- msg.pose.position.x)
			t = t - 0.1
		
			pub.publish(msg)
			rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass