# Dev repo to create a Norfair ROS node

This repo is a dev environment for the development of the Norfair ROS node. It has 3 ROS packages: darknet_ros, norfair-ros, and publisher

`publisher`: Iterate over a video and publish it into the `camera/rgb/image_raw` topic, the `darknet_ros` node is subscribed to this topic.

`darknet_ros`: Yolo Detector publishes the detections on the `darknet_ros/bounding_boxes` topic.

`norfair-ros`: Norfair ROS node, subscribe to the `darknet_ros/bounding_boxes` topic and publish the Norfair tracking results on the `norfair/detections` topic.

## How to build

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
# Set environment variables used by ROS
. devel/setup.bash
```

## How to run

Before running the `darknet_ros` you need to download the model weights with the following command:

```
wget http://pjreddie.com/media/files/yolov2-tiny-voc.weights -P /root/catkin_ws/src/darknet_ros/darknet_ros/yolo_network_config/weights
```

After that you can start the `darknet_ros` node with the following command:

```
roslaunch darknet_ros darknet_ros.launch
```

If the execution is fine, you can start the `norfair-ros` node to generate the tracking process with the output of the detector.

To start the `norfair-ros` node run the following command:

```
rosrun norfair_ros run.py
```

At this time you can start the `publisher` node to publish into the detector topic and generate detections to be processed with the `norfair-ros` node.

To start the publisher node run the following command:

```
rosrun publisher publisher.py
```

Keep in mind that you need to upload a video inside the `publisher/src` folder and adapt the path in the `publisher.py` file.
