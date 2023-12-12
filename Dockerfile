FROM ros:melodic

ENV USERNAME voxblox
ENV HOME /home/$USERNAME

# nvidia-container-runtime. Adds support to Nvidia drivers inside the container.
# for this to work, you need to install nvidia-docker2 in your host machine.
# More info: http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

RUN useradd -m $USERNAME && \
        echo "$USERNAME:$USERNAME" | chpasswd && \
        usermod --shell /bin/bash $USERNAME && \
        usermod -aG sudo $USERNAME && \
        mkdir -p /etc/sudoers.d && \
        echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME && \
        chmod 0440 /etc/sudoers.d/$USERNAME && \
        # Replace 1000 with your user/group id
        usermod  --uid 1000 $USERNAME && \
  groupmod --gid 1000 $USERNAME

USER voxblox
WORKDIR /home/${USERNAME}

RUN sudo apt-get update

# Other dependencies
RUN sudo apt-get install -y tmux git python-wstool python-catkin-tools ros-melodic-cmake-modules protobuf-compiler
RUN sudo apt-get install -y autoconf rsync libtool automake pkg-config libtool-bin qtbase5-dev libqt5opengl5-dev wget
RUN sudo apt-get install -y ros-melodic-eigen-conversions ros-melodic-tf ros-melodic-tf-conversions ros-melodic-rviz 
RUN sudo apt-get install -y ros-melodic-pcl-conversions ros-melodic-pcl-ros ros-melodic-cv-bridge 

# Libraries
RUN sudo apt-get install -y libyaml-cpp-dev libeigen3-dev libgoogle-glog-dev ccache tmux  net-tools iputils-ping nano wget usbutils htop gdb psmisc screen

RUN sudo apt-get update

RUN /bin/bash -c "source /opt/ros/melodic/setup.bash \
    && sudo mkdir -p /catkin_ws/src \
    && cd /catkin_ws \
    && sudo catkin init \
    && sudo catkin config --extend /opt/ros/melodic \
    && sudo catkin config --cmake-args -DCMAKE_BUILD_TYPE=Release \
    && sudo catkin config --merge-devel"

RUN /bin/bash -c "cd /catkin_ws/src \
    && sudo git clone https://github.com/ethz-asl/voxblox.git \
    && sudo wstool init . ./voxblox/voxblox_https.rosinstall \
    && sudo wstool update" 

RUN /bin/bash -c "cd /catkin_ws \
    && sudo catkin build voxblox_ros"

RUN sudo apt update && sudo apt install -y python3-pip ros-melodic-depth-image-proc
RUN pip3 install pyyaml numpy rospkg paho-mqtt

USER root

# COPY out.sh /root/out.sh
# RUN echo "alias out='bash /root/out.sh'" >> /root/.bashrc

USER voxblox

COPY fluffy.launch /catkin_ws/src/voxblox/voxblox_ros/launch/fluffy.launch
# COPY tunnel.launch /catkin_ws/src/voxblox/voxblox_ros/launch/tunnel.launch
# COPY data.bag /catkin_ws/data.bag
# COPY f450_nano_ufscar_150721.bag /catkin_ws/f450_nano_ufscar_150721.bag
# COPY teste_1.bag /catkin_ws/teste_1.bag
# COPY teste_2.bag /catkin_ws/teste_2.bag
# COPY teste_3.bag /catkin_ws/teste_3.bag
# COPY depth_to_pc.launch /catkin_ws/src/voxblox/voxblox_ros/launch/depth_to_pc.launch
# COPY fake_tf_world.launch /catkin_ws/src/voxblox/voxblox_ros/launch/fake_tf_world.launch

# Give permissions to use tty to user
RUN sudo usermod -a -G tty $USERNAME
RUN sudo usermod -a -G dialout $USERNAME

RUN echo "source /catkin_ws/devel/setup.bash" >> /home/voxblox/.bashrc

COPY out.sh /home/voxblox/out.sh
RUN echo "alias out='bash /home/voxblox/out.sh'" >> /home/voxblox/.bashrc

ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/melodic/setup.bash && source /catkin_ws/devel/setup.bash && /bin/bash"]
