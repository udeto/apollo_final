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


def main():
    rospy.init_node("pad_faker")    

    pub2 = rospy.Publisher(APOLLO_CONTROL_PAD_TOPIC, PadMessage, queue_size=10)
    msg2 = PadMessage()
    msg2.action = 2
    msg2.driving_mode = 1 
    
    print("sleep")
    #rospy.sleep(2)

    while not rospy.is_shutdown():
        pub2.publish(msg2)
        print("--publish pad message--")
        print("driving action: ", msg2.action)
        print("driving mode: ", msg2.driving_mode)
          
        

if __name__ == '__main__':
        main() 
