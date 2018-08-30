#!/usr/bin/env python

import rospy
from pb_msgs.msg import ControlCommand
from std_msgs.msg import String

CARLA_CONTROL_TOPIC = '/carla_control'
APOLLO_CONTROL_TOPIC = '/apollo/control'

def callback(data, pub):
	msg = String()
	msg.data = str(data.steering_target) + " " \
				+ str(data.throttle) + " " \
				+ str(data.brake)
	pub.publish(msg)

def setup():
	pub = rospy.Publisher(CARLA_CONTROL_TOPIC, String, queue_size=10)
	rospy.Subscriber(APOLLO_CONTROL_TOPIC, ControlCommand, callback, pub)

def listener():
	rospy.init_node('control_transformer')
	setup()
	rospy.spin()

if __name__ == '__main__':
	listener()

