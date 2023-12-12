#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import PoseStamped, TransformStamped
from sensor_msgs.msg import PointCloud2
# from rosgraph_msgs.msg import Clock
 
import tf
# import turtlesim.msg

global cur_time 
ODOM_FRAME_ID = "uav1/fcu"
LIDAR_FRAME_ID = "uav1/gps_origin"
# LIDAR_FRAME_ID = "uav1/stable_origin"


def sendBroadcast(frame_id, child_frame_id, timestamp=None):
    if timestamp == None:
        timestamp = rospy.get_rostime()

    br = tf.TransformBroadcaster()
    transform = TransformStamped()
    transform.header.stamp = timestamp
    transform.header.frame_id = frame_id
    transform.child_frame_id = child_frame_id
    transform.transform.translation.x = 0.0  
    transform.transform.translation.y = 0.0
    transform.transform.translation.z = 0.0
    quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)  
    transform.transform.rotation.x = quaternion[0]
    transform.transform.rotation.y = quaternion[1]
    transform.transform.rotation.z = quaternion[2]
    transform.transform.rotation.w = quaternion[3]
    br.sendTransformMessage(transform)

 
def mainTfCallback(data):
    br = tf.TransformBroadcaster()
    transform = TransformStamped()
    transform.header.stamp = rospy.get_rostime()
    # transform.header.stamp = data.header.stamp
    transform.header.frame_id = "map"
    transform.child_frame_id = ODOM_FRAME_ID
    transform.transform.translation.x = 0.0  
    transform.transform.translation.y = 0.0
    transform.transform.translation.z = 0.0
    quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)  
    transform.transform.rotation.x = quaternion[0]
    transform.transform.rotation.y = quaternion[1]
    transform.transform.rotation.z = quaternion[2]
    transform.transform.rotation.w = quaternion[3]
    br.sendTransformMessage(transform)
    
    br = tf.TransformBroadcaster()
    transform = TransformStamped()
    transform.header.stamp = rospy.get_rostime()
    # transform.header.stamp = data.header.stamp
    transform.header.frame_id = "map" 
    transform.child_frame_id = LIDAR_FRAME_ID  
    transform.transform.translation.x = 0.0  
    transform.transform.translation.y = 0.0
    transform.transform.translation.z = 0.0
    transform.transform.rotation.x = 0.0  
    transform.transform.rotation.y = 0.0
    transform.transform.rotation.z = 0.0
    transform.transform.rotation.w = 1.0
    br.sendTransformMessage(transform)


def mainTfCallback2(data):
    print('enter')
    sendBroadcast("map", ODOM_FRAME_ID)
    sendBroadcast("map", LIDAR_FRAME_ID)
    sendBroadcast(ODOM_FRAME_ID, LIDAR_FRAME_ID)
    # sendBroadcast("uav1/world_origin", ODOM_FRAME_ID)
    print('sent')


def velodyneTfCallback(data):
    br = tf.TransformBroadcaster()
    transform = TransformStamped()
    transform.header.stamp = rospy.get_rostime()
    transform.header.frame_id = ODOM_FRAME_ID
    transform.child_frame_id = LIDAR_FRAME_ID 
    transform.transform.translation.x = 0.0  
    transform.transform.translation.y = 0.0
    transform.transform.translation.z = 0.0
    transform.transform.rotation.x = 0.0  
    transform.transform.rotation.y = 0.0
    transform.transform.rotation.z = 0.0
    transform.transform.rotation.w = 1.0
    br.sendTransformMessage(transform)


# def clock_callback(data):
#     global cur_time
#     cur_time = data.clock


if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')

    # rospy.Subscriber('/unity/imu', PoseStamped, imu_callback)
    # rospy.Subscriber('/velodyne_points', PointCloud2, velodyne_callback)
    # rospy.Subscriber('/uav1/os_cloud_nodelet/points', PointCloud2, velodyneTfCallback)
    # rospy.Subscriber('/clock', Clock, clock_callback)
    
    # rospy.Timer(rospy.Duration(0.1), mainTfCallback)
    # rospy.Timer(rospy.Duration(0.1), velodyneTfCallback)

    rospy.Timer(rospy.Duration(0.01), mainTfCallback2)

    rospy.spin()