cmake_minimum_required(VERSION 2.8.3)
project(jsk_ik_server)

find_package(catkin REQUIRED COMPONENTS rostest)

catkin_package(
    DEPENDS 
    CATKIN-DEPENDS 
    INCLUDE_DIRS 
    LIBRARIES 
)

install(DIRECTORY test
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
  PATTERN ".svn" EXCLUDE
  )

## add_rostest(test/test-sample-robot.test)
