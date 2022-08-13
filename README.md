# ORB-SLAM3 for ROS Noetic, Ubuntu 20

<p align="center">
  <img
    src="/images/ORB_SLAM3.gif"
  >
</p>

ORBSLAM3 adapted for Ubuntu 20 and ROS Noetic if neccesary.

# Install modified Pangolin
I added Pangolin version compatible with Ubuntu 20 and ORB_SLAM3, so, we need to install it.

=== Required Dependencies ===

* C++11

* OpenGL (Desktop / ES / ES2)

* Glew
 * (win) built automatically
 * (deb) sudo apt-get install libglew-dev
 * (mac) sudo port install glew

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

# Install ORB_SLAM3
I added ORB_SLAM3 version compatible with Ubuntu 20 and ORB_SLAM3, so, for install and use just follow official steps at: https://github.com/UZ-SLAMLab/ORB_SLAM3 (except clone official ORBSLAM3, or you can test it too)

# Test:
Here is a [video](https://www.youtube.com/watch?v=Q9igtfsPSs0&t=1s) testing it:

[![IMAGE ALT TEXT HERE](/images/ORB_SLAM3.gif)](https://www.youtube.com/watch?v=Q9igtfsPSs0&t=1s)
