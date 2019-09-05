#!/usr/bin/env python

import rospy
from pb_msgs.msg import ADCTrajectory


def on_planning(data):
    file = open("planning_log.txt","w")

    file.write('header:\n')
    file.write("timestamp_sec: " + str(data.header.timestamp_sec)+'\n')
    file.write("module name: " + data.header.module_name+'\n')
    file.write("sequence num: " + str(data.header.sequence_num)+'\n')
    file.write("lidar time: " + str(data.header.lidar_timestamp)+'\n')
    file.write("camera time: " + str(data.header.camera_timestamp)+'\n')
    file.write("radar time: " + str(data.header.radar_timestamp)+'\n')
    file.write("status" + str(data.header.status)+'\n')

def setup():
    rospy.Subscriber('/apollo/planning', ADCTrajectory, on_planning)

def main():
    rospy.init_node("Planning_debug")
    setup()
    rospy.spin()

if __name__ == "__main__":
    main()