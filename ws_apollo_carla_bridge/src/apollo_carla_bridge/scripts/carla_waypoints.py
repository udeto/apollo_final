#!/usr/bin/env python

import rospy
from pb_msgs.msg import RoutingRequest, LaneWaypoint, RoutingResponse
from nav_msgs.msg import Path

APOLLO_WAYPOINTS_TOPIC = '/apollo/routing_request'
CALRA_WAYPOINTS_TOPIC = '/carla/ego_vehicle/waypoints'


def on_waypoint_input(data, publisher):
    route = RoutingRequest()
    i=0

    route.header.timestamp_sec = float(rospy.get_rostime().secs)
    route.header.module_name = "dreamview"
    route.header.sequence_num = 1
    
    for pose in data.poses:
        route.waypoint.add()
        route.waypoint[i].id = "2_1_-1"
        route.waypoint[i].s = float(rospy.get_rostime().secs)
        route.waypoint[i].pose.x = pose.pose.position.x
        route.waypoint[i].pose.y = pose.pose.position.y + 182.5
        i = i+1

    pub = publisher
    for i in range(10):    
        pub.publish(route)
        rospy.sleep(5)

    

def setup():
    pub = rospy.Publisher(APOLLO_WAYPOINTS_TOPIC, RoutingRequest, queue_size=10)
    rospy.Subscriber(CALRA_WAYPOINTS_TOPIC, Path, on_waypoint_input, pub)

def main():
    #rospy.init_node("carla_waypoints_to_apollo") 
    setup()
    rospy.spin()   

if __name__ == "__main__":
    main()