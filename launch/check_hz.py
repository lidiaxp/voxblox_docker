#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2

def topic_frequency(topic):
    rospy.init_node('topic_frequency_checker', anonymous=True)
    freq = rospy.Subscriber(topic, PointCloud2) 
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            data = rospy.wait_for_message(topic, PointCloud2, timeout=1) 
            print("Frequency of topic '{}': {} Hz".format(topic, 1))  
        except rospy.exceptions.ROSException:
            print("No messages received on topic '{}' within the last second.".format(topic))
        rate.sleep()

if __name__ == '__main__':
    topic_name = '/cloud_unity'  
    try:
        topic_frequency(topic_name)
    except rospy.ROSInterruptException:
        pass
