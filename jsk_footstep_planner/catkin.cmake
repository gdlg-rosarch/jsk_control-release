cmake_minimum_required(VERSION 2.8.3)
project(jsk_footstep_planner)

find_package(catkin REQUIRED COMPONENTS jsk_footstep_msgs jsk_pcl_ros
  message_generation)

add_service_files(FILES
  ChangeSuccessor.srv)
generate_messages()
#catkin_python_setup()
catkin_package(
  DEPENDS
  CATKIN-DEPENDS  jsk_footstep_msgs jsk_pcl_ros
  INCLUDE_DIRS # TODO include
  LIBRARIES # TODO
  )

install(DIRECTORY euslisp launch scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
  PATTERN ".svn" EXCLUDE
  )
