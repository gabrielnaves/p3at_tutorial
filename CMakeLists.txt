cmake_minimum_required(VERSION 2.8.3)
project(p3at_tutorial)

find_package(catkin REQUIRED COMPONENTS
  amcl
  base_local_planner
  base_local_planner
  gmapping
  move_base
  navfn
  roslaunch
  tf
  urdf
  xacro
  std_msgs
  sensor_msgs
  roscpp
)

add_definitions(-std=c++11)

find_package(Boost REQUIRED COMPONENTS system)

add_message_files(DIRECTORY msg FILES
  KeyboardMessage.msg)
generate_messages(DEPENDENCIES std_msgs)

catkin_package(
  CATKIN_DEPENDS
    message_runtime
  INCLUDE_DIRS
  LIBRARIES
)

catkin_package(
 INCLUDE_DIRS include
 # LIBRARIES radom_walk
 CATKIN_DEPENDS amcl base_local_planner base_local_planner gmapping move_base navfn roslaunch tf urdf xacro
 DEPENDS system_lib
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
  ${SDFormat_INCLUDE_DIRS}
)

link_directories(
  ${Boost_LIBRARY_DIRS}
  ${SDFormat_LIBRARY_DIRS}
)

## Declare a C++ library
add_library(random_walk src/random_walk.cpp)
target_link_libraries(random_walk ${catkin_LIBRARIES})

# Declare a C++ executable
add_executable(random_walk_node src/random_walk_node.cpp)
target_link_libraries(random_walk_node random_walk ${catkin_LIBRARIES})

add_library(keyboard_input src/keyboard_input.cpp)
target_link_libraries(keyboard_input ${catkin_LIBRARIES})

add_executable(keyboard_node src/keyboard_node.cpp)
target_link_libraries(keyboard_node keyboard_input ${catkin_LIBRARIES})