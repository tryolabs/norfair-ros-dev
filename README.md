# Full environment to run the Norfair ROS node

This repo builds a dev environment for the development of the Norfair ROS node. It has 3 ROS packages: `darknet_ros`, `norfair_ros`, and `publisher`.

In the [`norfair-ros`](https://github.com/tryolabs/norfair-ros) repository you can find a piece of more detailed information about this package.

# Basic information

`publisher`: Iterate over a video and publishes each frame into the `camera/rgb/image_raw` topic, the `darknet_ros` node is subscribed to this topic.

`darknet_ros`: Yolo Detector publishes the detections on the `darknet_ros/bounding_boxes` topic.

`norfair_ros`: Norfair ROS node has a converter node to unify different types of input messages to the one accepted by Norfair. Internally Norfair is subscribe to the `norfair/converter` topic and publishes the Norfair tracking results on the `norfair/detections` topic.

# How to build

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
catkin_make
# Build ROS messages
. devel/setup.bash
```

# How to run all packages

If you like to start the three packages with only one command, you can run the following inside the docker container

```
roslaunch startup dev.launch
```

This command launches the 3 packages and starts the tracking process to the detections provided by the detector.

> :warning: Read the following section to set properly each package.

# How to run each package

Before running the `darknet_ros` you need to download the model weights with the following command:

```
wget http://pjreddie.com/media/files/yolov2-tiny.weights -P /root/catkin_ws/src/darknet_ros/darknet_ros/yolo_network_config/weights
```

After that you can start the `darknet_ros` package with the following command:

```
roslaunch darknet_ros darknet_ros.launch
```

If the execution is fine, you can start the `norfair_ros` package to generate the tracking process with the output of the detector.

To start the `norfair-ros` package run the following command:

```
roslaunch norfair_ros norfair_node.launch
```

At this time you can start the `publisher` package to publish into the detector topic and generate detections to be processed with the `norfair-ros` package.

To start the publisher package run the following command:

```
roslaunch publisher publisher_node.launch
```

Keep in mind that you need to upload a video inside the `publisher/src` folder and adapt the path in the `publisher.py` file.
