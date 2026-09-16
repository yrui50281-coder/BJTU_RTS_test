cmake_minimum_required(VERSION 3.20)

project(OpenCVDemo LANGUAGES NONE)

find_package(Python3 REQUIRED COMPONENTS Interpreter)

add_custom_target(run_opencv_demo
    COMMAND "${Python3_EXECUTABLE}" "${CMAKE_CURRENT_SOURCE_DIR}/opencv_demo.py"
    WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    COMMENT "Running OpenCV image processing demo"
)
