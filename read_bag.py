import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2

class PointCloudSubscriber(Node):
    def __init__(self):
        super().__init__('point_cloud_subscriber')
        self.subscription = self.create_subscription(
            PointCloud2,
            '/camera/depth_registered/points',
            self.point_cloud_callback,
            10  # QoS profile
        )
        self.subscription

    def point_cloud_callback(self, msg):
#         std_msgs/Header header
# uint32 height
# uint32 width
# sensor_msgs/PointField[] fields
# bool is_bigendian
# uint32 point_step
# uint32 row_step
# uint8[] data
# bool is_dense
        print(msg.fields)
        # print(msg.data.index('R'))
        # print(msg.data.index('G'))
        # print(msg.data.index('B'))
        print(msg.data[:20])
        print(msg.data[-20:])
        # Process the point cloud data here
        # You can access the data using the pc2 library
        # for point in pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True):
        #     x, y, z = point
            # Do something with x, y, and z

def main(args=None):
    rclpy.init(args=args)
    node = PointCloudSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
