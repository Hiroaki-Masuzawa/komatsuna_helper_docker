FROM ros:noetic-robot-focal

### speedup download
# https://genzouw.com/entry/2019/09/04/085135/1718/
RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list

# RUN apt update -q -qq && \
#     DEBIAN_FRONTEND=noninteractive apt install -q -qq -y ros-noetic-depth-image-proc python3-pip && \
#     apt clean && \
#     rm -rf /var/lib/apt/lists/
RUN apt update -q -qq && \
    DEBIAN_FRONTEND=noninteractive apt install -q -qq -y python3-catkin-tools \
    ros-noetic-cv-bridge ros-noetic-image-transport ros-noetic-pcl-conversions ros-noetic-pcl-ros ros-noetic-pcl-ros ros-noetic-resource-retriever && \
    apt clean && \
    rm -rf /var/lib/apt/lists/
RUN sed -i.bk -e '6i if [ -e /catkin_ws/devel/setup.bash ]; then' -e '6i source /catkin_ws/devel/setup.bash' -e '6i fi' /ros_entrypoint.sh
