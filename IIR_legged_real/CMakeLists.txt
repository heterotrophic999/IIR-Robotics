cmake_minimum_required(VERSION 2.8.3)
project(IIR_legged_real)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
    roscpp
    geometry_msgs
    unitree_legged_msgs
    unitree_legged_real
)

catkin_package()

message("-- CMAKE_SYSTEM_PROCESSOR: ${CMAKE_SYSTEM_PROCESSOR}")
if("${CMAKE_SYSTEM_PROCESSOR}" MATCHES "x86_64.*")
  set(ARCH amd64)
else()
  set(ARCH arm64)
endif()

link_directories(${CMAKE_SOURCE_DIR}/unitree_legged_sdk/lib/cpp/${ARCH})

set(EXTRA_LIBS -pthread libunitree_legged_sdk.so)

set(CMAKE_CXX_FLAGS "-O3 -fPIC")

include_directories(
    include
    ${catkin_INCLUDE_DIRS}
    ${CMAKE_SOURCE_DIR}/unitree_legged_sdk/include
)

add_executable(ros_udp_wifi src/exe/ros_udp_wifi.cpp)
target_link_libraries(ros_udp_wifi ${EXTRA_LIBS} ${catkin_LIBRARIES})
add_dependencies(ros_udp_wifi ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

add_executable(voice_commands src/exe/voice_command.cpp)
target_link_libraries(voice_commands ${EXTRA_LIBS} ${catkin_LIBRARIES})
add_dependencies(voice_commands ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

