import os

os.system("docker load < /SLAM-Hive/slam_hive_algos/orb-slam3-ros-stereo-inertial/image.tar")
while True:
    # image_check = client.images.get("slam-hive-algorithm:orb-slam3-ros-stereo-inertial")
    ret = os.popen("docker images | grep orb-slam3-ros-stereo-inertial")
    if ret.read() != '':
        break
os.mkdir("/SLAM-Hive/slam_hive_algos/orb-slam3-ros-stereo-inertial/docker_loader_finish")

print("------ successful ------")
