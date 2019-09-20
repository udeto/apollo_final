#!/usr/bin/env python  
import rospy

import tf

def world_to_localization():
    world_localization = tf.TransformBroadcaster()
    world_localization.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "localization",
                     "world")

def localization_to_novatel():
    localization_nvatel = tf.TransformBroadcaster()
    localization_nvatel.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "novatel",
                     "localization")

def novatel_to_velodyne64():
    novatel_velodyne64 = tf.TransformBroadcaster()
    novatel_velodyne64.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "velodyne64",
                     "novatel")

def novatel_to_velodyne16():
    novatel_velodyne16 = tf.TransformBroadcaster()
    novatel_velodyne16.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "velodyne16",
                     "novatel")

def velodyne64_to_short_camera():
    velodyne64_short_camera = tf.TransformBroadcaster()
    velodyne64_short_camera.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "short_camera",
                     "velodyne64")

def velodyne64_to_radar_front():
    velodyne64_radar_front = tf.TransformBroadcaster()
    velodyne64_radar_front.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "radar_front",
                     "velodyne64")

def short_camera_to_radar():
    short_camera_radar = tf.TransformBroadcaster()
    short_camera_radar.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "radar",
                     "short_camera")

def camera_short_to_radar():
    short_camera_radar = tf.TransformBroadcaster()
    short_camera_radar.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "radar",
                     "short_camera")

def short_camera_to_long_camera():
    short_camera_long_camera = tf.TransformBroadcaster()
    short_camera_long_camera.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "long_camera",
                     "short_camera")

if __name__ == '__main__':
    rospy.init_node('test_tf_broadcaster')

    rate=rospy.Rate(100) #100hz

    while not rospy.is_shutdown():
        #world_to_localization()
        localization_to_novatel()
        novatel_to_velodyne64()
        velodyne64_to_short_camera()
        velodyne64_to_radar_front()
        short_camera_to_radar()
        short_camera_to_long_camera()

        rate.sleep()