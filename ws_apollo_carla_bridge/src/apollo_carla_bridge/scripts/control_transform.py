#!/usr/bin/env python

import rospy
from pb_msgs.msg import ControlCommand
from std_msgs.msg import String

CARLA_CONTROL_TOPIC = '/carla_control'
APOLLO_CONTROL_TOPIC = '/apollo/control'

def callback(data, pub):
	"""
    Forwards apollo control command to carla control relay

    :param data: apollo control command 
    :type data: ControlCommand
	:param pub: publisher for carla control topic
	:type pub: rospy.Publisher
    """
	msg = String()
	msg.data = str(data.steering_target) + " " \
				+ str(data.throttle) + " " \
				+ str(data.brake)
	pub.publish(msg)

def setup():
	"""
    Setup of the subscribers and publishers

    """
	pub = rospy.Publisher(CARLA_CONTROL_TOPIC, String, queue_size=10)
	rospy.Subscriber(APOLLO_CONTROL_TOPIC, ControlCommand, callback, pub)

def listener():
	"""
	Initialize node control_transformer and run setup

	"""
	rospy.init_node('control_transformer')
	setup()
	rospy.spin()

if __name__ == '__main__':
	listener()

