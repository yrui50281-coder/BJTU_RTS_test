#!/usr/bin/env python3
import rospy
from message_publisher.msg import CustomMessage


def callback(message):
    rospy.loginfo(
        "Received: sender=%s, sequence=%d, text=%s",
        message.sender,
        message.sequence,
        message.text,
    )


def main():
    rospy.init_node("message_subscriber")
    rospy.Subscriber("custom_message", CustomMessage, callback)
    rospy.loginfo("Subscriber is waiting for messages...")
    rospy.spin()


if __name__ == "__main__":
    main()
