import rospy

import numpy as np
import argparse
import os

from visualization_msgs.msg import MarkerArray
from std_srvs.srv import Trigger, Empty
from std_msgs.msg import Float32
from nav_msgs.msg import Odometry
from voxblox_msgs.srv import FilePath, FilePathRequest
# from geograpihc_msgs.msg import GeoPoint

class CenterFlight:
    def __init__(self):
        self.tunnel_name = 'here_tunnel_'
        # self.call_load_map_service(f'/catkin_ws/bag/{self.tunnel_name}.vxblx')
        # self.call_generate_mesh_service()
        self.call_save_map_service(f'/home/voxblox/catkin_ws/bag/{self.tunnel_name}.vxblx')

        exit()


    def call_save_map_service(self, file_path):
        rospy.wait_for_service('/voxblox_node/save_map')
        try:
            request = FilePathRequest()
            request.file_path = file_path

            save_map_service = rospy.ServiceProxy('/voxblox_node/save_map', FilePath)
            save_map_service(request)
        except rospy.ServiceException as e:
            print(f"Service call failed: {e}")


    def call_generate_mesh_service(self):
        rospy.wait_for_service('/voxblox_node/generate_mesh')
        try:
            generate_mesh_service = rospy.ServiceProxy('/voxblox_node/generate_mesh', Empty)
            response = generate_mesh_service()
            return response
        except rospy.ServiceException as e:
            print(f"Service call failed: {e}")


    def call_load_map_service(self, file_path):
        rospy.wait_for_service('/voxblox_node/load_map')
        try:
            request = FilePathRequest()
            request.file_path = file_path

            load_map_service = rospy.ServiceProxy('/voxblox_node/load_map', FilePath)
            load_map_service(request)
        except rospy.ServiceException as e:
            print(f"Service call failed: {e}")


def main():
    rospy.init_node("flying_center")
    CenterFlight()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


if __name__ == "__main__":
    main()
