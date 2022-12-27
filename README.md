# Full environment to run the Norfair ROS node

This repo builds a dev environment for the development of the Norfair ROS package.

To build the environment Docker and Docker Compose are required.

We use the `ros:noetic` image. This image is built on `Ubuntu 20.04`.

In the [`norfair-ros`](https://github.com/tryolabs/norfair-ros) repository you can find a piece of more detailed information about this package.

# Basic information

This environment has 3 ROS packages: `publisher`, `darknet_ros`, and `norfair_ros`.

`publisher`: Iterate over a video and publishes each frame into the `camera/rgb/image_raw` topic, the `darknet_ros` node is subscribed to this topic.

`darknet_ros`: Yolo Detector publishes the detections on the `darknet_ros/bounding_boxes` topic.

`norfair_ros`: Norfair ROS node has a converter node to unify different types of input messages to the one accepted by Norfair. Internally Norfair is subscribe to the `norfair/input` topic and publishes the Norfair tracking results on the `norfair/output` topic.

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

# Setup

Before running the entire environment you need to load a video to process. Keep in mind that this environment is based on a video file and not on a camera. You can easily change the publisher loop to publish a frame from a camera.

To load a video you need to upload it to the `publisher/src` folder and adapt the parameter `input_video` in the [config file](/catkin_ws/src/publisher/config/publisher.yaml). Now, `mp4` and `avi` are supported.

Another required step is to download the model weights for the `darknet_ros` package. To do that you need to run the following command inside the docker container:

```
wget http://pjreddie.com/media/files/yolov2-tiny.weights -P /root/catkin_ws/src/darknet_ros/darknet_ros/yolo_network_config/weights
```

You can find more information to select other models in the [darknet_ros](https://github.com/leggedrobotics/darknet_ros) repository.

# How to run all packages

If you like to start the three packages with only one command, you can run the following inside the docker container

```
roslaunch startup dev.launch
```

This command launches the 3 packages and starts the tracking process to the detections provided by the detector.

> :warning: Make the setup before running this command.

# How to run each package

To start the `darknet_ros` package you can execute the following command:

```
roslaunch darknet_ros darknet_ros.launch
```

If the execution is fine, you can start the `norfair_ros` package to generate the tracking process with the output of the detector.

To start the `norfair_ros` package run the following command:

```
roslaunch norfair_ros norfair_node.launch
```

At this time you can start the `publisher` package to publish into the detector topic and generate detections to be processed with the `norfair_ros` package.

To start the publisher package run the following command:

```
roslaunch publisher publisher_node.launch
```
