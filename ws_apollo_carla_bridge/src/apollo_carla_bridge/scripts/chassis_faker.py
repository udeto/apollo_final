#!/usr/bin/env python
import rospy

from modules.canbus.proto.chassis_pb2 import Chassis
# from pb_msgs.msg import ChassisDetail
# from pb_msgs.msg import Eps
# from pb_msgs.msg import CheckResponseSignal

APOLLO_CHASSIS_TOPIC = '/apollo/canbus/chassis'
# APOLLO_CHASSIS_DETAIL_TOPIC = '/apollo/canbus/chassis_detail'

def setup():
    pub = rospy.Publisher(APOLLO_CHASSIS_TOPIC, Chassis, queue_size=10)
    msg = Chassis()
    msg.engine_started = True
    msg.driving_mode = 1
    return [pub, msg]

def main():
    rospy.init_node('chassis_faker')

    pub = rospy.Publisher(APOLLO_CHASSIS_TOPIC, Chassis, queue_size=10)
    msg = Chassis()
    msg.engine_started = True
    msg.driving_mode = 1

    # pub = rospy.Publisher(APOLLO_CHASSIS_DETAIL_TOPIC, ChassisDetail, queue_size=10)
    # msg = ChassisDetail()
    # e = Eps()
    # e.is_eps_fail = False
    # e.eps_control_state = 2 # TODO: Try 1 if it doesn't work
    # msg.eps.CopyFrom(e)

    # crs = CheckResponseSignal()
    # crs.is_eps_online = True

    # msg.check_response.CopyFrom(crs)

    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    main()