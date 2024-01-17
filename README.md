# ORB-SLAM3 for ROS Noetic, Ubuntu 20.04

<p align="center">
  <img
    src="/images/ORB_SLAM3.gif"
  >
</p>

ORBSLAM3 adapted for Ubuntu 20.04 and ROS Noetic.

# Install modified Pangolin
I added Pangolin version compatible with Ubuntu 20 and ORB_SLAM3, so, we need to install it.

=== Required Dependencies ===

* C++11

* OpenGL (Desktop / ES / ES2)

* Glew
 * (deb) sudo apt-get install libglew-dev

* CMake (for build environment)
 * (win) http://www.cmake.org/cmake/resources/software.html
 * (deb) sudo apt-get install cmake
 * (mac) sudo port install cmake

=== Building ===

1. Enter Pangolin path
    * cd ORB_SLAM3_NOETIC/Pangolin
2. Build Pangolin
    * mkdir build
    * cd build
    * cmake ..
    * make -j

3. Test Pangolin
    * cd ORB_SLAM3_NOETIC/Pangolin/examples/HelloPangolin
    * mkdir build
    * cd build
    * cmake ..
    * make -j
    * ./HelloPangolin

# Compile for ROS
## Build executibles
* Build orbslam by running `./build.sh`
* Set the ros package path 
  ```bash
  export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:PATH/ORB_SLAM3/Examples/ROS
  ```
* Build ROS executibles by `./build_ros.sh`


## Run Node
* Source the environment 
  ```bash
  source Examples/ROS/ORB_SLAM3/build/devel/setup.sh
  ```
* Start the node 
  ```
  rosrun ORB_SLAM3 Mono_Inertial Vocabulary/ORBvoc.txt Examples/Monocular-Inertial/EuRoC.yaml 
  ```

I added ORB_SLAM3 version compatible with Ubuntu 20 and ORB_SLAM3, so, for install and use just follow official steps at: https://github.com/UZ-SLAMLab/ORB_SLAM3 (except clone official ORBSLAM3, or you can test it too)

# Test:
Here is a [video](https://www.youtube.com/watch?v=Q9igtfsPSs0&t=1s) testing it:

[![IMAGE ALT TEXT HERE](/images/ORB_SLAM3.gif)](https://www.youtube.com/watch?v=Q9igtfsPSs0&t=1s)
