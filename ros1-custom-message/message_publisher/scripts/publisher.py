#!/usr/bin/env python3
import rospy
from message_publisher.msg import CustomMessage


def main():
    rospy.init_node("message_publisher")
    publisher = rospy.Publisher("custom_message", CustomMessage, queue_size=10)
    rate = rospy.Rate(1)
    sequence = 1

    while not rospy.is_shutdown():
        message = CustomMessage()
        message.sender = "yr"
        message.sequence = sequence
        message.text = "Hello from ROS1 publisher"
        publisher.publish(message)
        rospy.loginfo(
            "Sent: sender=%s, sequence=%d, text=%s",
            message.sender,
            message.sequence,
            message.text,
        )
        sequence += 1
        rate.sleep()


if __name__ == "__main__":
    main()
