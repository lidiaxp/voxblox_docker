# import rospy
# from geometry_msgs.msg import PoseStamped, TransformStamped
# from sensor_msgs.msg import PointCloud2
# # from rosgraph_msgs.msg import Clock
 
# import tf

# ODOM_FRAME_ID = "uav"
# LIDAR_FRAME_ID = "point_cloud_from_unity"
# # ODOM_FRAME_ID = "uav1/fcu"
# # LIDAR_FRAME_ID = "uav1/stable_origin"

# def sendBroadcast(frame_id, child_frame_id, timestamp=None):
#     if timestamp == None:
#         timestamp = rospy.get_rostime()

#     br = tf.TransformBroadcaster()
#     transform = TransformStamped()
#     transform.header.stamp = timestamp
#     transform.header.frame_id = frame_id
#     transform.child_frame_id = child_frame_id
#     transform.transform.translation.x = 0.0  
#     transform.transform.translation.y = 0.0
#     transform.transform.translation.z = 0.0
#     quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)  
#     transform.transform.rotation.x = quaternion[0]
#     transform.transform.rotation.y = quaternion[1]
#     transform.transform.rotation.z = quaternion[2]
#     transform.transform.rotation.w = quaternion[3]
#     br.sendTransformMessage(transform)


# def mainTfCallback(data):
#     # br = tf.TransformBroadcaster()
#     # transform = TransformStamped()
#     # transform.header.stamp = rospy.get_rostime()
#     # transform.header.frame_id = "world"
#     # transform.child_frame_id = "uav"
#     # transform.transform.translation.x = 0.0  
#     # transform.transform.translation.y = 0.0
#     # transform.transform.translation.z = 0.0
#     # quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)  
#     # transform.transform.rotation.x = quaternion[0]
#     # transform.transform.rotation.y = quaternion[1]
#     # transform.transform.rotation.z = quaternion[2]
#     # transform.transform.rotation.w = quaternion[3]
#     # br.sendTransformMessage(transform)

#     # br = tf.TransformBroadcaster()
#     # transform = TransformStamped()
#     # transform.header.stamp = rospy.get_rostime()
#     # transform.header.frame_id = "map"
#     # transform.child_frame_id = "uav"
#     # transform.transform.translation.x = 0.0  
#     # transform.transform.translation.y = 0.0
#     # transform.transform.translation.z = 0.0
#     # quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)  
#     # transform.transform.rotation.x = quaternion[0]
#     # transform.transform.rotation.y = quaternion[1]
#     # transform.transform.rotation.z = quaternion[2]
#     # transform.transform.rotation.w = quaternion[3]
#     # br.sendTransformMessage(transform)

#     sendBroadcast("map", ODOM_FRAME_ID)
#     sendBroadcast("map", LIDAR_FRAME_ID)
#     sendBroadcast(ODOM_FRAME_ID, LIDAR_FRAME_ID)
#     # sendBroadcast("map", "uav")
#     # sendBroadcast("uav", "point_cloud_from_unity")
#     # sendBroadcast(LIDAR_FRAME_ID, "point_cloud_from_unity")
#     print('sent')


# # def velodyneTfCallback(data):
# #     # br = tf.TransformBroadcaster()
# #     # transform = TransformStamped()
# #     # transform.header.stamp = rospy.get_rostime()
# #     # # transform.header.stamp = data.header.stamp
# #     # transform.header.frame_id = "uav" 
# #     # transform.child_frame_id = "point_cloud_from_unity"  
# #     # transform.transform.translation.x = 0.0  
# #     # transform.transform.translation.y = 0.0
# #     # transform.transform.translation.z = 0.0
# #     # transform.transform.rotation.x = 0.0  
# #     # transform.transform.rotation.y = 0.0
# #     # transform.transform.rotation.z = 0.0
# #     # transform.transform.rotation.w = 1.0
# #     # br.sendTransformMessage(transform)

# #     sendBroadcast("uav", "point_cloud_from_unity")


# def cloudUnityCallback(data):
#     # sendBroadcast("map", "uav")
#     # sendBroadcast("uav", "point_cloud_from_unity")
#     sendBroadcast("map", LIDAR_FRAME_ID)
#     sendBroadcast(ODOM_FRAME_ID, LIDAR_FRAME_ID)


# # def clock_callback(data):
# #     global cur_time
# #     cur_time = data.clock


# def mainTfCallback2(data):
#     sendBroadcast("world", "map")
#     sendBroadcast("map", ODOM_FRAME_ID)
#     # sendBroadcast("map", LIDAR_FRAME_ID)
#     # sendBroadcast(ODOM_FRAME_ID, LIDAR_FRAME_ID)
#     print('sent')


# if __name__ == '__main__':
#     rospy.init_node('tf_broadcaster_unity')

#     # rospy.Subscriber('/unity/imu', PoseStamped, imu_callback)
#     # rospy.Subscriber('/velodyne_points', PointCloud2, velodyne_callback)
#     # rospy.Subscriber('/uav1/os_cloud_nodelet/points', PointCloud2, velodyneTfCallback)
#     rospy.Subscriber('/cloud_unity', PointCloud2, cloudUnityCallback)
#     # rospy.Subscriber('/clock', Clock, clock_callback)
    
#     # rospy.Timer(rospy.Duration(0.0001), mainTfCallback)
#     # rospy.Timer(rospy.Duration(0.01), velodyneTfCallback)
#     rospy.Timer(rospy.Duration(0.0001), mainTfCallback2)

#     rospy.spin()











# import rospy
# from geometry_msgs.msg import PoseStamped, TransformStamped
# from sensor_msgs.msg import PointCloud2
# from rosgraph_msgs.msg import Clock
# from nav_msgs.msg import Odometry
# from visualization_msgs.msg import Marker
 
# # import tf
# import tf2_ros
# # import tf2_geometry_msgs

# ODOM_FRAME_ID = "uav"
# LIDAR_FRAME_ID = "point_cloud_from_unity"
# # ODOM_FRAME_ID = "uav1/fcu"
# # LIDAR_FRAME_ID = "point_cloud_from_unity"

# def sendBroadcast(frame_id, child_frame_id, timestamp=None):
#     if timestamp == None:
#         timestamp = rospy.Time.now()
#         # timestamp = rospy.get_rostime()

#     # tf_buffer = tf2_ros.Buffer()
#     # tf_listener = tf2_ros.TransformListener(tf_buffer)

#     br = tf2_ros.TransformBroadcaster()

#     # br = tf.TransformBroadcaster()
#     transform = TransformStamped()
#     transform.header.stamp = timestamp
#     transform.header.frame_id = frame_id
#     transform.child_frame_id = child_frame_id
#     transform.transform.translation.x = 0.0  
#     transform.transform.translation.y = 0.0
#     transform.transform.translation.z = 0.0
#     # quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)  
#     quaternion = [0.0, 0.0, 0.0, 1.0]
#     transform.transform.rotation.x = quaternion[0]
#     transform.transform.rotation.y = quaternion[1]
#     transform.transform.rotation.z = quaternion[2]
#     transform.transform.rotation.w = quaternion[3]
#     # br.sendTransformMessage(transform)
#     br.sendTransform(transform)


# def cloudUnityCallback(data):
#     # sendBroadcast("map", LIDAR_FRAME_ID)
#     # sendBroadcast(ODOM_FRAME_ID, LIDAR_FRAME_ID)
#     sendBroadcast("world_env", ODOM_FRAME_ID)
#     sendBroadcast(ODOM_FRAME_ID, LIDAR_FRAME_ID)
#     sendBroadcast("map", ODOM_FRAME_ID)
#     sendBroadcast("map", LIDAR_FRAME_ID)
#     print('sent')



# def publishClock():
#     clock_publisher = rospy.Publisher('/clock', Clock, queue_size=10)
#     # current_time = rospy.get_rostime()
#     current_time = rospy.Time.now()

#     clock_msg = Clock()
#     clock_msg.clock = current_time

#     clock_publisher.publish(clock_msg)


# # def odometryAgilicious(data):
# #     sendBroadcast("world", "map", data.header.stamp)
# #     sendBroadcast("map", ODOM_FRAME_ID, data.header.stamp)
# #     sendBroadcast("map", LIDAR_FRAME_ID, data.header.stamp)
# #     sendBroadcast(ODOM_FRAME_ID, LIDAR_FRAME_ID, data.header.stamp)
# #     publishClock()
# #     print('sent')


# def mainTfCallback2(data):
#     # sendBroadcast("world", "map")
#     sendBroadcast("map", ODOM_FRAME_ID)
#     sendBroadcast("map", LIDAR_FRAME_ID)
#     sendBroadcast(ODOM_FRAME_ID, LIDAR_FRAME_ID)
#     # publishClock()
#     print('sent')


# if __name__ == '__main__':
#     rospy.init_node('tf_broadcaster_unity')

#     # rospy.Subscriber('/kingfisher/agiros_pilot/odometry', Odometry, odometryAgilicious)
#     # rospy.Subscriber('/uav1/estimation_manager/odom_main', Odometry, cloudUnityCallback)
#     rospy.Subscriber('/cloud_unity', PointCloud2, cloudUnityCallback)
    
#     # rospy.Subscriber('/motion_detector/visualization/detections/object/static', Marker, cloudUnityCallback)
#     # rospy.Timer(rospy.Duration(0.01), mainTfCallback2)
    

#     rospy.spin()



import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry

ODOM_FRAME_ID = "uav"
LIDAR_FRAME_ID = "point_cloud_from_unity"


# class StaticTransformPublisher:
#     def __init__(self):
#         self.tfb = tf2_ros.StaticTransformBroadcaster()
#         self.tf_buffer = tf2_ros.Buffer()
#         self.listener = tf2_ros.TransformListener(self.tf_buffer)

#     def publish_static_transform(self, frame_id, child_frame_id, translation=[0.0, 0.0, 0.0], rotation=[0.0, 0.0, 0.0, 1.0]):
#         static_transformStamped = TransformStamped()

#         static_transformStamped.header.stamp = rospy.Time.now()
#         static_transformStamped.header.frame_id = frame_id
#         static_transformStamped.child_frame_id = child_frame_id
#         static_transformStamped.transform.translation.x = translation[0]
#         static_transformStamped.transform.translation.y = translation[1]
#         static_transformStamped.transform.translation.z = translation[2]
#         static_transformStamped.transform.rotation.x = rotation[0]
#         static_transformStamped.transform.rotation.y = rotation[1]
#         static_transformStamped.transform.rotation.z = rotation[2]
#         static_transformStamped.transform.rotation.w = rotation[3]

#         self.tfb.sendTransform(static_transformStamped)

#     def wait_for_transform(self, target_frame, source_frame):
#         if not self.tf_buffer.can_transform(target_frame, source_frame, rospy.Time(), rospy.Duration(1.0)):
#             rospy.logwarn("Transform from " + source_frame + " to " + target_frame + " not available, waiting...")
#             rospy.sleep(1.0)

# class OdometryHandler:
#     def __init__(self):
#         self.pub = rospy.Publisher('/kingfisher/agiros_pilot/odometry_', Odometry, queue_size=10)
#         rospy.Subscriber('/kingfisher/agiros_pilot/odometry', Odometry, self.odometry_callback)

#     def odometry_callback(self, data):
#         data.header.frame_id = ODOM_FRAME_ID
#         self.pub.publish(data)


# def sendBroadcast(frame_id, child_frame_id, timestamp=None):
#     if timestamp == None:
#         timestamp = rospy.Time.now()
#         # timestamp = rospy.get_rostime()

#     # tf_buffer = tf2_ros.Buffer()
#     # tf_listener = tf2_ros.TransformListener(tf_buffer)

#     br = tf2_ros.TransformBroadcaster()

#     # br = tf.TransformBroadcaster()
#     transform = TransformStamped()
#     transform.header.stamp = timestamp
#     transform.header.frame_id = frame_id
#     transform.child_frame_id = child_frame_id
#     transform.transform.translation.x = 0.0  
#     transform.transform.translation.y = 0.0
#     transform.transform.translation.z = 0.0
#     # quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)  
#     quaternion = [0.0, 0.0, 0.0, 1.0]
#     transform.transform.rotation.x = quaternion[0]
#     transform.transform.rotation.y = quaternion[1]
#     transform.transform.rotation.z = quaternion[2]
#     transform.transform.rotation.w = quaternion[3]
#     # br.sendTransformMessage(transform)
#     br.sendTransform(transform)


# if __name__ == '__main__':
#     rospy.init_node('static_transform_publisher')

#     transform_publisher = StaticTransformPublisher()
#     odometry_handler = OdometryHandler()

#     transform_publisher.publish_static_transform("map", ODOM_FRAME_ID)
#     sendBroadcast("map", ODOM_FRAME_ID)

#     transform_publisher.publish_static_transform("map", LIDAR_FRAME_ID)
#     sendBroadcast("map", LIDAR_FRAME_ID)

#     transform_publisher.publish_static_transform(ODOM_FRAME_ID, LIDAR_FRAME_ID)
#     sendBroadcast(ODOM_FRAME_ID, LIDAR_FRAME_ID)

#     rospy.spin()



import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped

class StaticTransformPublisher:
    def __init__(self):
        self.tfb = tf2_ros.StaticTransformBroadcaster()
        self.tf_buffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tf_buffer)

    def permission_enable(self, t=1.0):
        self.tf_buffer.can_transform(ODOM_FRAME_ID, "map", rospy.Time(), rospy.Duration(t))
        self.tf_buffer.can_transform(LIDAR_FRAME_ID, "map", rospy.Time(), rospy.Duration(t))
        self.tf_buffer.can_transform("map", LIDAR_FRAME_ID, rospy.Time(), rospy.Duration(t))
        self.tf_buffer.can_transform("map", ODOM_FRAME_ID, rospy.Time(), rospy.Duration(t))
        self.tf_buffer.can_transform(LIDAR_FRAME_ID, ODOM_FRAME_ID, rospy.Time(), rospy.Duration(t))

    def publish_static_transform(self, frame_id, child_frame_id, translation=[0.0, 0.0, 0.0], rotation=[0.0, 0.0, 0.0, 1.0]):
        static_transformStamped = TransformStamped()

        static_transformStamped.header.stamp = rospy.Time.now()
        static_transformStamped.header.frame_id = frame_id
        static_transformStamped.child_frame_id = child_frame_id
        static_transformStamped.transform.translation.x = translation[0]
        static_transformStamped.transform.translation.y = translation[1]
        static_transformStamped.transform.translation.z = translation[2]
        static_transformStamped.transform.rotation.x = rotation[0]
        static_transformStamped.transform.rotation.y = rotation[1]
        static_transformStamped.transform.rotation.z = rotation[2]
        static_transformStamped.transform.rotation.w = rotation[3]

        self.tfb.sendTransform(static_transformStamped)
        print('sent')

    def add_frame_to_tf_tree(self, parent_frame, new_frame, translation=[0.0, 0.0, 0.0], rotation=[0.0, 0.0, 0.0, 1.0]):
        self.publish_static_transform(parent_frame, new_frame, translation, rotation)

    def wait_for_transform(self, target_frame, source_frame):
        if not self.tf_buffer.can_transform(target_frame, source_frame, rospy.Time(), rospy.Duration(1.0)):
            rospy.logwarn("Transform from " + source_frame + " to " + target_frame + " not available, waiting...")
            rospy.sleep(1.0)


if __name__ == '__main__':
    rospy.init_node('static_transform_publisher')

    transform_publisher = StaticTransformPublisher()
    transform_publisher.permission_enable(0.01)

    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        transform_publisher.add_frame_to_tf_tree("map", "uav")
        transform_publisher.add_frame_to_tf_tree("map", LIDAR_FRAME_ID)

        transform_publisher.publish_static_transform("map", ODOM_FRAME_ID)
        transform_publisher.publish_static_transform("map", LIDAR_FRAME_ID)
        transform_publisher.publish_static_transform(ODOM_FRAME_ID, LIDAR_FRAME_ID)

        rate.sleep()
    # rospy.spin()

