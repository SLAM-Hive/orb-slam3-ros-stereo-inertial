### Build the ORB-SLAM3-ROS by Dockerfile
Firstly, git clone the algorithm Dockerfile repository to your computer, then:
```
cd orb-slam3-ros-stereo-inertial/
./install.sh
```
You can check whether the image is successfully built as follows:
```
docker images
```
you can see:
```
slam-hive-algorithm orb-slam3-ros-stereo-inertial [IMAGE ID] [CREATED] [SIZE]
```

For source code, we just change the places where used to save trajectory and mapping result files.

