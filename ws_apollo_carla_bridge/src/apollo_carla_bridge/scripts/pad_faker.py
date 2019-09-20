#!/usr/bin/env python
import rospy

from modules.canbus.proto.chassis_pb2 import Chassis
from modules.control.proto.pad_msg_pb2 import PadMessage
from pb_msgs.msg import ChassisDetail
from pb_msgs.msg import Eps
from pb_msgs.msg import CheckResponseSignal
from pb_msgs.msg import RoutingRequest

APOLLO_CHASSIS_TOPIC = '/apollo/canbus/chassis'
APOLLO_CHASSIS_DETAIL_TOPIC = '/apollo/canbus/chassis_detail'
APOLLO_CONTROL_PAD_TOPIC = '/apollo/control/pad'
APOLLO_ROUTING_REQUEST = '/apollo/routing_request'

def on_routing(data):
    pub2 = rospy.Publisher(APOLLO_CONTROL_PAD_TOPIC, PadMessage, queue_size=10)
    msg2 = PadMessage()
    msg2.action = 2
    msg2.driving_mode = 1 
    
    rospy.sleep(2)

    for i in range(20):
        pub2.publish(msg2)
        print("--publish pad message--")
        print("driving action: ", msg2.action)
        print("driving mode: ", msg2.driving_mode)

def setup():
    rospy.Subscriber(APOLLO_ROUTING_REQUEST, RoutingRequest, on_routing)

def main():
    #rospy.init_node("pad_faker")    
    setup()

if __name__ == '__main__':
        main() 
