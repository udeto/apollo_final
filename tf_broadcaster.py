#!/usr/bin/env python  
import rospy
import math
import tf

def world_to_localization():
    """
    Send transform for frame world to frame localization
    """
    world_localization = tf.TransformBroadcaster()
    world_localization.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "localization",
                     "world")

def localization_to_novatel():
    """
    Send transform for frame localization to frame novatel
    """
    localization_nvatel = tf.TransformBroadcaster()
    localization_nvatel.sendTransform((0 , 0 , 0),
                     tf.transformations.quaternion_from_euler(0, 0, math.pi/2),
                     rospy.Time.now(),
                     "novatel",
                     "localization")

def novatel_to_velodyne64():
    """
    Send transform for frame novatel to frame velodyne64
    """
    novatel_velodyne64 = tf.TransformBroadcaster()
    novatel_velodyne64.sendTransform((0 , 0 , 2),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "velodyne64",
                     "novatel")

def novatel_to_velodyne16():
    """
    Send transform for frame novatel to frame velodyne16
    """
    novatel_velodyne16 = tf.TransformBroadcaster()
    novatel_velodyne16.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "velodyne16",
                     "novatel")

def novatel_to_short_camera():
    """
    Send transform for frame novatel to frame short_camera
    """
    novatel_short_camera = tf.TransformBroadcaster()
    novatel_short_camera.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "short_camera",
                     "novatel")

def velodyne64_to_radar_front():
    """
    Send transform for frame velodyne64 to frame radar_front
    """
    velodyne64_radar_front = tf.TransformBroadcaster()
    velodyne64_radar_front.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "radar_front",
                     "velodyne64")

def short_camera_to_radar():
    """
    Send transform for frame camera to frame radar
    """
    short_camera_radar = tf.TransformBroadcaster()
    short_camera_radar.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "radar",
                     "short_camera")

def short_camera_to_long_camera():
    """
    Send transform for frame short_camera to frame long_camera
    """
    short_camera_long_camera = tf.TransformBroadcaster()
    short_camera_long_camera.sendTransform((0 , 0 , 0),
                     (0.0 ,0.0 , 0.0, 1.0),
                     rospy.Time.now(),
                     "long_camera",
                     "short_camera")

if __name__ == '__main__':
    """
    Initialize node and send tfs at a rate of 100hz
    """
    rospy.init_node('tf_broadcaster')

    rate=rospy.Rate(100) #100hz

    while not rospy.is_shutdown():
        #world to loclaization is published by the localization module
        #world_to_localization() 
        localization_to_novatel()
        novatel_to_velodyne64()
        novatel_to_short_camera()
        velodyne64_to_radar_front()
        short_camera_to_radar()
        short_camera_to_long_camera()

        rate.sleep()