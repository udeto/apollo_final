#!/usr/bin/env python

import rospy
from pb_msgs.msg import RoutingRequest, LaneWaypoint, RoutingResponse
from modules.control.proto.pad_msg_pb2 import PadMessage
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
    send_request()


def send_request():
    route = RoutingRequest()
    i=1
    #wait for position input
    ready = False
    rospy.sleep(10)
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
        for i in range(4):    
            pub_route.publish(route)
            rospy.sleep(2)
        
        control_reset()

    except:
        pass

def control_reset():
    pub2 = rospy.Publisher(APOLLO_PAD_TOPIC, PadMessage, queue_size=10)
    msg2 = PadMessage()
    msg2.action = 2
    msg2.driving_mode = 1 
    
    rospy.sleep(5)

    for i in range(20):
        pub2.publish(msg2)
        print("--publish pad message--")
        print("driving action: ", msg2.action)
        print("driving mode: ", msg2.driving_mode)

def setup():
    rospy.Subscriber(CALRA_WAYPOINTS_TOPIC, Path, on_waypoint_input)
    rospy.Subscriber(CARLA_PLAYER_VEHICLE_TOPIC, String, on_player_vehicle_input)

def main():
    #rospy.init_node("carla_waypoints_to_apollo") 
    setup()

    
 

if __name__ == "__main__":
    main()