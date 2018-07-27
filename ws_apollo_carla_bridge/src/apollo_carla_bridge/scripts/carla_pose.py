#!/usr/bin/env python

import rospy
from pb_msgs.msg import LocalizationEstimate
from pb_msgs.msg import Pose
from std_msgs.msg import String
from math import radians

POSE_TOPIC = "/apollo/localization/pose"
PLAYER_VEHICLE_TOPIC = '/player_vehicle'

def callback(data, pub):
    msg = LocalizationEstimate()
    p = Pose()

    arr = data.data.split()

    p.position.x = float(arr[0])
    p.position.y = -float(arr[1])
    p.position.z = float(arr[2])

    # heading / yaw
    h = float(arr[3])
    # transform carla heading into apollo
    p.heading = radians(360-h if h>0 else -h)

    msg.pose.CopyFrom(p)

    pub.publish(msg)

def main():
    pub = rospy.Publisher(POSE_TOPIC, LocalizationEstimate, queue_size=10)
    rospy.init_node('carla_to_apollo_pose')
    rospy.Subscriber(PLAYER_VEHICLE_TOPIC, String, callback, pub, queue_size=10)
    
    rospy.spin()

if __name__ == '__main__':
    main()
