#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2

import carla_gps
import chassis_faker
import control_transform
import carla_waypoints

CARLA_LIDAR_TOPIC = '/lidar_0'
CARLA_CAMERA_LONG_TOPIC = '/camera_long/image_raw'
CARLA_CAMERA_SHORT_TOPIC = '/camera_short/image_raw'

APOLLO_LIDAR_TOPIC = '/apollo/sensor/velodyne64/compensator/PointCloud2'
APOLLO_CAMERA_LONG_TOPIC = '/apollo/sensor/camera/traffic/image_long'
APOLLO_CAMERA_SHORT_TOPIC = '/apollo/sensor/camera/obstacle/front_6mm'
APOLLO_CAMERA_SHORT_TOPIC2 = '/apollo/sensor/camera/traffic/image_short'

def forward_callback(data, pub):
    pub.publish(data)

def main():
    rospy.init_node('carla_to_apollo_data')

    carla_gps.setup()
    
    pub_lidar = rospy.Publisher(APOLLO_LIDAR_TOPIC, PointCloud2, queue_size=10)
    rospy.Subscriber(CARLA_LIDAR_TOPIC, PointCloud2, forward_callback, pub_lidar, queue_size=10)

    pub_cam_long = rospy.Publisher(APOLLO_CAMERA_LONG_TOPIC, Image, queue_size=10)
    rospy.Subscriber(CARLA_CAMERA_LONG_TOPIC, Image, forward_callback, pub_cam_long, queue_size=10)

    pub_cam_short = rospy.Publisher(APOLLO_CAMERA_SHORT_TOPIC, Image, queue_size=10)
    rospy.Subscriber(CARLA_CAMERA_SHORT_TOPIC, Image, forward_callback, pub_cam_short, queue_size=10)

    pub_cam_short = rospy.Publisher(APOLLO_CAMERA_SHORT_TOPIC2, Image, queue_size=10)
    rospy.Subscriber(CARLA_CAMERA_SHORT_TOPIC, Image, forward_callback, pub_cam_short, queue_size=10)

    control_transform.setup()
    chassis_faker.setup()
    carla_waypoints.setup()
    rospy.spin()

if __name__ == '__main__':
    main()
