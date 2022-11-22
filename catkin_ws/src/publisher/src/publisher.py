#!/usr/bin/env python3
# license removed for brevity
import cv2
import norfair
import rospy
from cv_bridge import CvBridge
from norfair import Detection, Paths, Tracker, Video
from sensor_msgs.msg import Image


def talker():
    pub = rospy.Publisher("camera/rgb/image_raw", Image, queue_size=1)
    rospy.init_node("talker")
    rate = rospy.Rate(10)  # 10hz
    video = Video(input_path="marvel.mp4")

    bridge = CvBridge()

    for frame in video:
        image_message = bridge.cv2_to_imgmsg(frame, encoding="rgb8")

        pub.publish(image_message)
        rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
