#!/usr/bin/env python3
# cv2 fix some CvBridge errors
import cv2
import rospy
from cv_bridge import CvBridge
from norfair import Video
from sensor_msgs.msg import Image


def talker():
    """
    Iterate over a video and publish each frame as a ROS Image message.
    """
    pub = rospy.Publisher("camera/rgb/image_raw", Image, queue_size=1)
    rospy.init_node("publisher_node")
    rate = rospy.Rate(1)  # Adapt the hz value to your needs
    video = Video(input_path="/root/catkin_ws/src/publisher/src/example.mp4")

    bridge = CvBridge()

    for frame in video:
        image_message = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        pub.publish(image_message)
        rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.loginfo("Publisher node terminated.")
