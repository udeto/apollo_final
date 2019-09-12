#!/usr/bin/env python

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('test_tf_listener')

    listener = tf.TransformListener()
    #buffer = tf.Buffer()

    while not rospy.is_shutdown():
        #print("All Frames running:")
        #print(listener.allFramesAsString())

        print("Check listener can Transform")
        print(listener.canTransform('/velodyne64', '/novatel', rospy.Time(0)))

        #print("Check buffer can Transform")
        #print(buffer.canTransform('/velodyne64', '/novatel', 10, rospy.Time(0)))
        try:
            (trans, rot) = listener.lookupTransform('/velodyne64', '/novatel', rospy.Time(0))

            print("Transform:", trans)
            print("Rotation:",rot)

        except:
            print("Could not get tf")
            continue

        rospy.sleep(1)