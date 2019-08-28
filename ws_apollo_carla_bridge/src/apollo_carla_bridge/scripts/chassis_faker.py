#!/usr/bin/env python
import rospy

from modules.canbus.proto.chassis_pb2 import Chassis
from modules.control.proto.pad_msg_pb2 import PadMessage
from pb_msgs.msg import ChassisDetail
from pb_msgs.msg import Eps
from pb_msgs.msg import CheckResponseSignal

APOLLO_CHASSIS_TOPIC = '/apollo/canbus/chassis'
APOLLO_CHASSIS_DETAIL_TOPIC = '/apollo/canbus/chassis_detail'
APOLLO_CONTROL_PAD_TOPIC = '/apollo/control/pad'

def setup():
    pub = rospy.Publisher(APOLLO_CHASSIS_TOPIC, Chassis, queue_size=10)
    msg = Chassis()
    msg.engine_started = True
    msg.driving_mode = 1

    return [pub, msg]

def main():
    #rospy.init_node('chassis_faker')
    
    pub1 = rospy.Publisher(APOLLO_CHASSIS_TOPIC, Chassis, queue_size=10)
    msg1 = Chassis()
    msg1.engine_started = True
    msg1.driving_mode = 1

    """     
    pub2 = rospy.Publisher(APOLLO_CONTROL_PAD_TOPIC, PadMessage, queue_size=10)
    msg2 = PadMessage()
    msg2.action = 1
    msg2.driving_mode = 1 
    """
    
    """ 
    pub3 = rospy.Publisher(APOLLO_CHASSIS_DETAIL_TOPIC, ChassisDetail, queue_size=10)
    msg3 = ChassisDetail()
    e = Eps()
    e.is_eps_fail = False
    e.eps_control_state = 1 # TODO: Try 1 if it doesn't work
    msg3.eps.CopyFrom(e) 

    crs = CheckResponseSignal()
    crs.is_eps_online = True

    msg3.check_response.CopyFrom(crs) 
    

    while not rospy.is_shutdown():
        pub1.publish(msg1)
        pub2.publish(msg2)
        pub3.publish(msg3)
    """

if __name__ == '__main__':
        main() 
