#!/usr/bin/env python

import rospy
from pb_msgs.msg import RoutingRequest, LaneWaypoint, RoutingResponse
from nav_msgs.msg import Path
from std_msgs.msg import String



APOLLO_WAYPOINTS_TOPIC = '/apollo/routing_request'
APOLLO_PAD_TOPIC = '/apollo/control/pad'
CALRA_WAYPOINTS_TOPIC = '/carla/ego_vehicle/waypoints'
CARLA_PLAYER_VEHICLE_TOPIC = '/player_vehicle'

def on_player_vehicle_input(data):
    arr = data.data.split()
    global position_x    
    position_x = float(arr[0])
    global position_y
    position_y = float(arr[1])
    global position_recieved
    position_recieved = True

def on_waypoint_input(data):
    global carla_route
    carla_route = data

def setup():
    rospy.Subscriber(CALRA_WAYPOINTS_TOPIC, Path, on_waypoint_input)
    rospy.Subscriber(CARLA_PLAYER_VEHICLE_TOPIC, String, on_player_vehicle_input)

def main():
    #rospy.init_node("carla_waypoints_to_apollo") 
    setup()

    route = RoutingRequest()
    i=1
    
    #wait for position input
    ready = False
    while not ready:
        try:
            ready = position_recieved
            print("position recieved")
        
        except:
            print("position not ready")
            rospy.sleep(2)
            
        

    #set first waypoint with the current position
    route.header.timestamp_sec = float(rospy.get_rostime().secs)
    route.header.module_name = "dreamview"
    route.header.sequence_num = 1

    route.waypoint.add()
    route.waypoint[0].s = float(rospy.get_rostime().secs)
    route.waypoint[0].pose.x = position_x
    route.waypoint[0].pose.y = position_y + 182.5
    print("set first waypoint as Position", position_x, position_y)
    
    try:
        #read waypoints from carla and add them to the route
        for pose in carla_route.poses:
            route.waypoint.add()
            route.waypoint[i].id = "2_1_-1"
            route.waypoint[i].s = float(rospy.get_rostime().secs)
            route.waypoint[i].pose.x = pose.pose.position.x
            route.waypoint[i].pose.y = pose.pose.position.y + 182.5
            i = i+1

        #publish the waypoints to apollo
        pub_route = rospy.Publisher(APOLLO_WAYPOINTS_TOPIC, RoutingRequest, queue_size=10)
        for i in range(2):    
            pub_route.publish(route)
            print("route published")
            print("sleep 3 sec")
            rospy.sleep(3)
            print("sleep done")

    except:
        pass
 

if __name__ == "__main__":
    main()