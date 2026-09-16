cmake_minimum_required(VERSION 3.0.2)
project(message_subscriber)

find_package(catkin REQUIRED COMPONENTS
  message_publisher
  rospy
)

catkin_package(
  CATKIN_DEPENDS message_publisher rospy
)

catkin_install_python(
  PROGRAMS
  scripts/subscriber.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
