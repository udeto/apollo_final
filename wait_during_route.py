#!/usr/bin/env python  

import sys
import rospy
from std_msgs.msg import String

def on_route_end (data):
    """
    Recieve end request

    :param data: request for ending of the current route
    :type data: String
    """
    print("ending")
    rospy.signal_shutdown("end of route")
    print("shutting down complete")
    sys.exit()

def setup ():
    """
    Setup subscriber

    """
    rospy.Subscriber("end_route", String, on_route_end)

def main():
    """
    Init node and run setup

    """
    rospy.init_node("wait_during_route")
    setup()
    rospy.spin()

if __name__ == '__main__':
    main()