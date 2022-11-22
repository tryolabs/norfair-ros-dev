# Dev repo to create a Norfair ROS node

## How to use

Build the Docker Image and run the container

```
docker-compose build
docker-compose up
```

Inside the Docker container run the following commands

```sh
# Set environment variables used by ROS
source /opt/ros/noetic/setup.bash
# Compile
cd /root/catkin_ws && catkin_make
# Set environment variables used by ROS
. devel/setup.bash
```
