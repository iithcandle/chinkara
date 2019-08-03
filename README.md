Chinkara - Donkeycar is a toy car based ADV research platform at CANDLE Research Lab, IIT Hyderbad.

Hardware used :

* Zed Stereo camera - 1
* Wide angle CSI camera - 1
* Logitech F710 game controller - 1
* Jetson Nano development kit - 1
* Raspberry PI 3B kit - 1
* IMU - 1
* GPS - 1
* LIDAR - 1
* Battery pack - 1
* Wifi Router (1Gbps) - 1
* Wireless keyboard + Mouse - 1

Software used :

* Nvidia Jetpack 4.2 / Ubuntu 18 on Jetson Nano
* Ubuntu 18 on Raspberry PI 3B
* Gnu C++ 11
* Python 3.6
* Robot Operating System (ROS) Melodic for Ubuntu 18


Topics Published:

Initial:

cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ rosnode list
/rosout
cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ rostopic list
/rosout
/rosout_agg

By CSI camera:

cs18resch01001@nano-ub18:~$ rostopic list
/csi_cam_0/camera_info
/csi_cam_0/image_raw
/csi_cam_0/image_raw/compressed
/csi_cam_0/image_raw/compressed/parameter_descriptions
/csi_cam_0/image_raw/compressed/parameter_updates
/csi_cam_0/image_raw/compressedDepth
/csi_cam_0/image_raw/compressedDepth/parameter_descriptions
/csi_cam_0/image_raw/compressedDepth/parameter_updates
/csi_cam_0/image_raw/theora
/csi_cam_0/image_raw/theora/parameter_descriptions
/csi_cam_0/image_raw/theora/parameter_updates
/rosout
/rosout_agg

cs18resch01001@nano-ub18:~$ rostopic hz /csi_cam_0/image_raw
subscribed to [/csi_cam_0/image_raw]
average rate: 20.538
        min: 0.043s max: 0.050s std dev: 0.00139s window: 21
average rate: 20.435
        min: 0.043s max: 0.050s std dev: 0.00101s window: 42
average rate: 20.404
        min: 0.043s max: 0.050s std dev: 0.00085s window: 62
average rate: 20.388
        min: 0.043s max: 0.051s std dev: 0.00078s window: 82
average rate: 20.379
        min: 0.043s max: 0.051s std dev: 0.00070s window: 103
average rate: 20.373
        min: 0.043s max: 0.051s std dev: 0.00064s window: 123
average rate: 20.369
        min: 0.043s max: 0.051s std dev: 0.00062s window: 143
average rate: 20.365
        min: 0.043s max: 0.051s std dev: 0.00058s window: 164
average rate: 20.362
        min: 0.043s max: 0.051s std dev: 0.00056s window: 184


By ZED Stereo camera:

cs18resch01001@nano-ub18:~$ rostopic list
/diagnostics
/rosout
/rosout_agg
/tf
/tf_static
/zed/joint_states
/zed/zed_node/confidence/camera_info
/zed/zed_node/confidence/confidence_image
/zed/zed_node/confidence/confidence_image/compressed
/zed/zed_node/confidence/confidence_image/compressed/parameter_descriptions
/zed/zed_node/confidence/confidence_image/compressed/parameter_updates
/zed/zed_node/confidence/confidence_image/compressedDepth
/zed/zed_node/confidence/confidence_image/compressedDepth/parameter_descriptions
/zed/zed_node/confidence/confidence_image/compressedDepth/parameter_updates
/zed/zed_node/confidence/confidence_image/theora
/zed/zed_node/confidence/confidence_image/theora/parameter_descriptions
/zed/zed_node/confidence/confidence_image/theora/parameter_updates
/zed/zed_node/confidence/confidence_map
/zed/zed_node/depth/camera_info
/zed/zed_node/depth/depth_registered
/zed/zed_node/depth/depth_registered/compressed
/zed/zed_node/depth/depth_registered/compressed/parameter_descriptions
/zed/zed_node/depth/depth_registered/compressed/parameter_updates
/zed/zed_node/depth/depth_registered/compressedDepth
/zed/zed_node/depth/depth_registered/compressedDepth/parameter_descriptions
/zed/zed_node/depth/depth_registered/compressedDepth/parameter_updates
/zed/zed_node/depth/depth_registered/theora
/zed/zed_node/depth/depth_registered/theora/parameter_descriptions
/zed/zed_node/depth/depth_registered/theora/parameter_updates
/zed/zed_node/disparity/disparity_image
/zed/zed_node/imu/data
/zed/zed_node/imu/data_raw
/zed/zed_node/left/camera_info
/zed/zed_node/left/image_rect_color
/zed/zed_node/left/image_rect_color/compressed
/zed/zed_node/left/image_rect_color/compressed/parameter_descriptions
/zed/zed_node/left/image_rect_color/compressed/parameter_updates
/zed/zed_node/left/image_rect_color/compressedDepth
/zed/zed_node/left/image_rect_color/compressedDepth/parameter_descriptions
/zed/zed_node/left/image_rect_color/compressedDepth/parameter_updates
/zed/zed_node/left/image_rect_color/theora
/zed/zed_node/left/image_rect_color/theora/parameter_descriptions
/zed/zed_node/left/image_rect_color/theora/parameter_updates
/zed/zed_node/left_raw/camera_info
/zed/zed_node/left_raw/image_raw_color
/zed/zed_node/left_raw/image_raw_color/compressed
/zed/zed_node/left_raw/image_raw_color/compressed/parameter_descriptions
/zed/zed_node/left_raw/image_raw_color/compressed/parameter_updates
/zed/zed_node/left_raw/image_raw_color/compressedDepth
/zed/zed_node/left_raw/image_raw_color/compressedDepth/parameter_descriptions
/zed/zed_node/left_raw/image_raw_color/compressedDepth/parameter_updates
/zed/zed_node/left_raw/image_raw_color/theora
/zed/zed_node/left_raw/image_raw_color/theora/parameter_descriptions
/zed/zed_node/left_raw/image_raw_color/theora/parameter_updates
/zed/zed_node/odom
/zed/zed_node/parameter_descriptions
/zed/zed_node/parameter_updates
/zed/zed_node/path_map
/zed/zed_node/path_odom
/zed/zed_node/point_cloud/cloud_registered
/zed/zed_node/pose
/zed/zed_node/pose_with_covariance
/zed/zed_node/rgb/camera_info
/zed/zed_node/rgb/image_rect_color
/zed/zed_node/rgb/image_rect_color/compressed
/zed/zed_node/rgb/image_rect_color/compressed/parameter_descriptions
/zed/zed_node/rgb/image_rect_color/compressed/parameter_updates
/zed/zed_node/rgb/image_rect_color/compressedDepth
/zed/zed_node/rgb/image_rect_color/compressedDepth/parameter_descriptions
/zed/zed_node/rgb/image_rect_color/compressedDepth/parameter_updates
/zed/zed_node/rgb/image_rect_color/theora
/zed/zed_node/rgb/image_rect_color/theora/parameter_descriptions
/zed/zed_node/rgb/image_rect_color/theora/parameter_updates
/zed/zed_node/rgb_raw/camera_info
/zed/zed_node/rgb_raw/image_raw_color
/zed/zed_node/rgb_raw/image_raw_color/compressed
/zed/zed_node/rgb_raw/image_raw_color/compressed/parameter_descriptions
/zed/zed_node/rgb_raw/image_raw_color/compressed/parameter_updates
/zed/zed_node/rgb_raw/image_raw_color/compressedDepth
/zed/zed_node/rgb_raw/image_raw_color/compressedDepth/parameter_descriptions
/zed/zed_node/rgb_raw/image_raw_color/compressedDepth/parameter_updates
/zed/zed_node/rgb_raw/image_raw_color/theora
/zed/zed_node/rgb_raw/image_raw_color/theora/parameter_descriptions
/zed/zed_node/rgb_raw/image_raw_color/theora/parameter_updates
/zed/zed_node/right/camera_info
/zed/zed_node/right/image_rect_color
/zed/zed_node/right/image_rect_color/compressed
/zed/zed_node/right/image_rect_color/compressed/parameter_descriptions
/zed/zed_node/right/image_rect_color/compressed/parameter_updates
/zed/zed_node/right/image_rect_color/compressedDepth
/zed/zed_node/right/image_rect_color/compressedDepth/parameter_descriptions
/zed/zed_node/right/image_rect_color/compressedDepth/parameter_updates
/zed/zed_node/right/image_rect_color/theora
/zed/zed_node/right/image_rect_color/theora/parameter_descriptions
/zed/zed_node/right/image_rect_color/theora/parameter_updates
/zed/zed_node/right_raw/camera_info
/zed/zed_node/right_raw/image_raw_color
/zed/zed_node/right_raw/image_raw_color/compressed
/zed/zed_node/right_raw/image_raw_color/compressed/parameter_descriptions
/zed/zed_node/right_raw/image_raw_color/compressed/parameter_updates
/zed/zed_node/right_raw/image_raw_color/compressedDepth
/zed/zed_node/right_raw/image_raw_color/compressedDepth/parameter_descriptions
/zed/zed_node/right_raw/image_raw_color/compressedDepth/parameter_updates
/zed/zed_node/right_raw/image_raw_color/theora
/zed/zed_node/right_raw/image_raw_color/theora/parameter_descriptions
/zed/zed_node/right_raw/image_raw_color/theora/parameter_updates
/zed/zed_node/stereo/image_rect_color
/zed/zed_node/stereo/image_rect_color/compressed
/zed/zed_node/stereo/image_rect_color/compressed/parameter_descriptions
/zed/zed_node/stereo/image_rect_color/compressed/parameter_updates
/zed/zed_node/stereo/image_rect_color/compressedDepth
/zed/zed_node/stereo/image_rect_color/compressedDepth/parameter_descriptions
/zed/zed_node/stereo/image_rect_color/compressedDepth/parameter_updates
/zed/zed_node/stereo/image_rect_color/theora
/zed/zed_node/stereo/image_rect_color/theora/parameter_descriptions
/zed/zed_node/stereo/image_rect_color/theora/parameter_updates
/zed/zed_node/stereo_raw/image_raw_color
/zed/zed_node/stereo_raw/image_raw_color/compressed
/zed/zed_node/stereo_raw/image_raw_color/compressed/parameter_descriptions
/zed/zed_node/stereo_raw/image_raw_color/compressed/parameter_updates
/zed/zed_node/stereo_raw/image_raw_color/compressedDepth
/zed/zed_node/stereo_raw/image_raw_color/compressedDepth/parameter_descriptions
/zed/zed_node/stereo_raw/image_raw_color/compressedDepth/parameter_updates
/zed/zed_node/stereo_raw/image_raw_color/theora
/zed/zed_node/stereo_raw/image_raw_color/theora/parameter_descriptions
/zed/zed_node/stereo_raw/image_raw_color/theora/parameter_updates


$ rostopic hz /zed/zed_node/right_raw/image_raw_color
subscribed to [/zed/zed_node/right_raw/image_raw_color]
average rate: 30.849
        min: 0.013s max: 0.034s std dev: 0.00386s window: 29
average rate: 30.404
        min: 0.013s max: 0.034s std dev: 0.00273s window: 59
average rate: 30.264
        min: 0.013s max: 0.034s std dev: 0.00223s window: 89
average rate: 30.198
        min: 0.013s max: 0.034s std dev: 0.00194s window: 119
average rate: 30.158
        min: 0.013s max: 0.035s std dev: 0.00176s window: 149

cs18resch01001@nano-ub18:~$ rostopic list | grep -i imu
/zed/zed_node/imu/data
/zed/zed_node/imu/data_raw

cs18resch01001@nano-ub18:~$ rostopic hz /zed/zed_node/imu/data
subscribed to [/zed/zed_node/imu/data]
average rate: 100.059
        min: 0.009s max: 0.011s std dev: 0.00045s window: 95
average rate: 100.037
        min: 0.009s max: 0.011s std dev: 0.00046s window: 195
average rate: 100.008
        min: 0.009s max: 0.011s std dev: 0.00046s window: 295
average rate: 100.013
        min: 0.009s max: 0.011s std dev: 0.00046s window: 395
average rate: 100.008
        min: 0.009s max: 0.011s std dev: 0.00046s window: 496
average rate: 100.012
        min: 0.009s max: 0.011s std dev: 0.00046s window: 596
average rate: 100.007
        min: 0.009s max: 0.011s std dev: 0.00046s window: 696
^Caverage rate: 100.001
        min: 0.009s max: 0.011s std dev: 0.00046s window: 727

cs18resch01001@nano-ub18:~$ rostopic hz /zed/zed_node/imu/data_raw
subscribed to [/zed/zed_node/imu/data_raw]
average rate: 99.998
        min: 0.009s max: 0.011s std dev: 0.00045s window: 95
average rate: 99.975
        min: 0.009s max: 0.011s std dev: 0.00046s window: 195
average rate: 100.008
        min: 0.009s max: 0.011s std dev: 0.00046s window: 295
average rate: 99.995
        min: 0.009s max: 0.011s std dev: 0.00046s window: 395
^Caverage rate: 99.988
        min: 0.009s max: 0.011s std dev: 0.00045s window: 493

cs18resch01001@nano-ub18:~$ rosnode list
/rosout
/rplidarNode
/rviz

cs18resch01001@nano-ub18:~$ rostopic list
/initialpose
/move_base_simple/goal
/rosout
/rosout_agg
/scan
/tf
/tf_static
cs18resch01001@nano-ub18:~$ rostopic hz /initialpose
subscribed to [/initialpose]
no new messages
no new messages
no new messages
^Cno new messages

cs18resch01001@nano-ub18:~$ rosnode list
/rosout
/rplidarNode
/rviz

cs18resch01001@nano-ub18:~$ rostopic list
/initialpose
/move_base_simple/goal
/rosout
/rosout_agg
/scan
/tf
/tf_static

cs18resch01001@nano-ub18:~$ rostopic hz /initialpose
subscribed to [/initialpose]
no new messages
no new messages
no new messages
^Cno new messages

cs18resch01001@nano-ub18:~$ rostopic hz /move_base_simple/goal
subscribed to [/move_base_simple/goal]
no new messages
no new messages
^Cno new messages

cs18resch01001@nano-ub18:~$ rostopic hz /scan
subscribed to [/scan]
average rate: 7.496
        min: 0.128s max: 0.137s std dev: 0.00387s window: 7
average rate: 7.544
        min: 0.127s max: 0.137s std dev: 0.00403s window: 15
average rate: 7.544
        min: 0.127s max: 0.137s std dev: 0.00401s window: 22
average rate: 7.569
        min: 0.127s max: 0.137s std dev: 0.00403s window: 30
average rate: 7.564
        min: 0.127s max: 0.137s std dev: 0.00403s window: 37
^Caverage rate: 7.571
        min: 0.127s max: 0.137s std dev: 0.00403s window: 42

cs18resch01001@nano-ub18:~$ rostopic hz /tf
subscribed to [/tf]
no new messages
no new messages
^Cno new messages

cs18resch01001@nano-ub18:~$ rostopic hz /tf_static
subscribed to [/tf_static]
no new messages
no new messages
no new messages
^Cno new messages

