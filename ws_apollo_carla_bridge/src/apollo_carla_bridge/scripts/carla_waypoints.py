#!/usr/bin/env python

import rospy
import json
from pb_msgs.msg import RoutingRequest, LaneWaypoint, RoutingResponse
from modules.control.proto.pad_msg_pb2 import PadMessage
from nav_msgs.msg import Path
from std_msgs.msg import String
from std_msgs.msg import Int32



APOLLO_WAYPOINTS_TOPIC = '/apollo/routing_request'
APOLLO_PAD_TOPIC = '/apollo/control/pad'
CALRA_WAYPOINTS_TOPIC = '/carla_route'
CARLA_PLAYER_VEHICLE_TOPIC = '/player_vehicle'

def on_player_vehicle_input(data):
    """
    Read x and y coordinates of the current position from player_vahicle topic

    :param data: player_vehicle input
    :type data: String
    """
    arr = data.data.split()
    global position_x    
    position_x = float(arr[0])
    global position_y
    position_y = float(arr[1])
    global position_recieved
    position_recieved = True

def on_waypoint_input(data):
    """
    Read waypoints for the current route and create routing request

    :param data: route number
    :type data: Int32
    """

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
    #route.waypoint[0].s = float(0)
    route.waypoint[0].pose.x = position_x
    route.waypoint[0].pose.y = position_y + 182.5
    print("set first waypoint as Position", position_x, position_y)
    
    #load json current route from json file
    route_no = "route_0" + str(data.data)
    print("publish", route_no)
    with open('/apollo/routes_str.json') as json_file:
	wp = json.load(json_file)

    #add waypoints of the current rout eto the routing request
    i = 1
    for pose in wp[route_no]:
	route.waypoint.add()
	route.waypoint[i].id = pose['waypoint']["id"]
	route.waypoint[i].s = pose['waypoint']["s"]
	route.waypoint[i].pose.x = pose['waypoint']['pose']["x"]
	route.waypoint[i].pose.y = pose['waypoint']['pose']["y"]
	i = i+1

    publish_route(route)

def publish_route(route):
    """
    Publish the routing request

    :param route: routing request for the current route
    :type data: RoutingRequest
    """
    pub_route = rospy.Publisher(APOLLO_WAYPOINTS_TOPIC, RoutingRequest, queue_size=10)
    print("publish route")
        
    for i in range(2):
        pub_route.publish(route)
        rospy.sleep(1)
    
    control_reset()

def control_reset():
    """
    Publish pad message to trigger reset of the control module

    """
    pub2 = rospy.Publisher(APOLLO_PAD_TOPIC, PadMessage, queue_size=10)
    msg2 = PadMessage()
    msg2.action = 2
    msg2.driving_mode = 1 
    
    rospy.sleep(1)

    for i in range(4):
        pub2.publish(msg2)
        rospy.sleep(2)
        print("--publish pad message--")
        print("driving action: ", msg2.action)
        print("driving mode: ", msg2.driving_mode)
        print("--published pad message--")
    
def setup():
    """
    Setup the subscribers

    """
    rospy.Subscriber(CALRA_WAYPOINTS_TOPIC, Int32, on_waypoint_input)
    rospy.Subscriber(CARLA_PLAYER_VEHICLE_TOPIC, String, on_player_vehicle_input)

def main():
    """
    run setup

    """
    setup()

if __name__ == "__main__":
    main()
