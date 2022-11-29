FROM ros:noetic

RUN sudo apt -y update && \
    sudo apt-get install -y python3-pip && \
    sudo apt-get install -y xorg-dev && \
    sudo apt-get install -y libopencv-dev  && \
    sudo apt-get install -y ros-noetic-cv-bridge && \
    sudo apt-get install -y ros-noetic-image-transport && \
    sudo apt-get install -y git

RUN pip install norfair

# create a basic workspace
WORKDIR /root/catkin_ws/src
