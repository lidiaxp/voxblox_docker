import rospy
import tf
from tf.msg import tfMessage

def tf_callback(data):
    for transform in data.transforms:
        # if transform.header.frame_id == "uav1/fcu" or transform.child_frame_id == "uav1/fcu":
        # if transform.header.frame_id == "uav1/fcu" and transform.child_frame_id == "uav1/stable_origin":
        if transform.header.frame_id == "uav1/front_rgbd/link":# and transform.child_frame_id == "uav1/front_rgbd/aligned_depth_to_color":
            print(transform)
            # print(f"Frame ID: {transform.header.frame_id}, Child Frame ID: {transform.child_frame_id}")
            # print(f"Frame ID: {transform.header.frame_id}, Child Frame ID: {transform.child_frame_id}")

def listener():
    rospy.init_node('tf_listener')
    tf_sub = rospy.Subscriber("/tf", tfMessage, tf_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
