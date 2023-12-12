#!/bin/sh
RPG_HOST_DIR=$1
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
sudo touch $XAUTH
sudo xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

# Check nVidia GPU docker support
# More info: http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration
NVIDIA_DOCKER_REQUIREMENT='nvidia-docker2'
GPU_OPTIONS=""
if dpkg --get-selections | grep -q "^$NVIDIA_DOCKER_REQUIREMENT[[:space:]]*install$" >/dev/null; then
  echo "Starting docker with nVidia support!"
  GPU_OPTIONS="--gpus all --runtime=nvidia"
fi

docker run --privileged --rm -it \
           --volume=$XSOCK:$XSOCK:rw \
           --volume=$XAUTH:$XAUTH:rw \
           --volume=/dev:/dev:rw \
           --volume=/var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket \
           ${GPU_OPTIONS} \
           --shm-size=1gb \
           --env="XAUTHORITY=${XAUTH}" \
           --env="DISPLAY=${DISPLAY}" \
           --env=TERM=xterm-256color \
           --env=QT_X11_NO_MITSHM=1 \
           -v "/home/lidia/py_ws/voxblox/bag:/catkin_ws/bag" \
           -v "/home/lidia/py_ws/voxblox/launch:/catkin_ws/launch" \
           --net=host \
           -u "voxblox"  \
           voxblox \
           bash
