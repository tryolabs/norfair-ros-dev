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
    # Load parameters
    publishers = rospy.get_param("publisher_publishers")
    image_publisher = publishers["images"]
    publisher_setup = rospy.get_param("publisher_setup")

    pub = rospy.Publisher(image_publisher["topic"], Image, queue_size=image_publisher["queue_size"])
    rospy.init_node("publisher_node")
    rate = rospy.Rate(1)  # Adapt the hz value to your needs
    video = Video(input_path=publisher_setup["input_video"])

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
