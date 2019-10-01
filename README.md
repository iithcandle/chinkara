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


Procudure to Build & Run :


```
$ git clone https://bitbucket.org/maruthisi/chinkara -b donkeycar_1906 donkeycar_1906 --recurse-submodules
$ cd donkeycar_1906/src
$ catkin_init_workspace
$ cd ..
$ catkin_build
$ source /opt/ros/melodic/setup.bash
$ source devel/setup.bash
$ roslaunch donkeycar donkeycar_nano_manual.launch
```

Topics Published:

Initial:

```
cs18resch01001@nano-ub18:~$ rosnode list
/rosout
cs18resch01001@nano-ub18:~$ rostopic list
/rosout
/rosout_agg
```

By Logitech F710 joystick:

```
cs18resch01001@nano-ub18:~$ rosparam set joy_node/dev "/dev/input/js0"

cs18resch01001@nano-ub18:~$ rosrun joy joy_node
[ERROR] [1564965364.681140559]: Couldn't open joystick force feedback!
[ INFO] [1564965364.683083845]: Opened joystick: /dev/input/js0. deadzone_: 0.050000.

cs18resch01001@nano-ub18:~$ rostopic list
/diagnostics
/joy
/joy/set_feedback
/rosout
/rosout_agg

cs18resch01001@nano-ub18:~$ rosnode list
/joy_node
/rosout

cs18resch01001@nano-ub18:~$ rostopic hz /joy
subscribed to [/joy]
no new messages
no new messages
no new messages
no new messages
^Cno new messages

```

By CSI camera:

```
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
```

By ZED Stereo camera:

```
cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ source devel/setup.bash
cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ roslaunch zed_wrapper zedm.launch
... logging to /mnt/home/cs18resch01001/.ros/log/86cc7dc4-e3f0-11e9-8c97-00044be5e429/roslaunch-nano-ub18-25925.log
Checking log directory for disk usage. This may take awhile.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://nano-ub18:36411/

SUMMARY
========

PARAMETERS
 * /rosdistro: melodic
 * /rosversion: 1.14.3
 * /zed/zed_description: <?xml version="1....
 * /zed/zed_node/auto_exposure: True
 * /zed/zed_node/camera_model: zedm
 * /zed/zed_node/confidence: 100
 * /zed/zed_node/depth/confidence_root: confidence
 * /zed/zed_node/depth/depth_stabilization: 1
 * /zed/zed_node/depth/depth_topic_root: depth
 * /zed/zed_node/depth/disparity_topic: disparity/dispari...
 * /zed/zed_node/depth/min_depth: 0.1
 * /zed/zed_node/depth/openni_depth_mode: 0
 * /zed/zed_node/depth/point_cloud_topic_root: point_cloud
 * /zed/zed_node/depth/quality: 1
 * /zed/zed_node/depth/sensing_mode: 0
 * /zed/zed_node/exposure: 100
 * /zed/zed_node/gain: 100
 * /zed/zed_node/general/base_frame: base_link
 * /zed/zed_node/general/camera_flip: False
 * /zed/zed_node/general/camera_frame: zed_camera_center
 * /zed/zed_node/general/frame_rate: 30
 * /zed/zed_node/general/gpu_id: -1
 * /zed/zed_node/general/left_camera_frame: zed_left_camera_f...
 * /zed/zed_node/general/left_camera_optical_frame: zed_left_camera_o...
 * /zed/zed_node/general/resolution: 2
 * /zed/zed_node/general/right_camera_frame: zed_right_camera_...
 * /zed/zed_node/general/right_camera_optical_frame: zed_right_camera_...
 * /zed/zed_node/general/self_calib: True
 * /zed/zed_node/general/serial_number: 0
 * /zed/zed_node/general/svo_compression: 4
 * /zed/zed_node/general/verbose: True
 * /zed/zed_node/general/zed_id: -1
 * /zed/zed_node/imu/imu_frame: zed_imu_link
 * /zed/zed_node/imu/imu_pub_rate: 100.0
 * /zed/zed_node/imu/imu_timestamp_sync: False
 * /zed/zed_node/imu/imu_topic_root: imu
 * /zed/zed_node/mapping/fused_pointcloud_freq: 1.0
 * /zed/zed_node/mapping/mapping_enabled: False
 * /zed/zed_node/mapping/resolution: 1
 * /zed/zed_node/mat_resize_factor: 1.0
 * /zed/zed_node/max_depth: 10.0
 * /zed/zed_node/point_cloud_freq: 10.0
 * /zed/zed_node/stream:
 * /zed/zed_node/svo_file:
 * /zed/zed_node/tracking/fixed_cov_value: 1e-6
 * /zed/zed_node/tracking/fixed_covariance: False
 * /zed/zed_node/tracking/fixed_z_value: 1.0
 * /zed/zed_node/tracking/floor_alignment: False
 * /zed/zed_node/tracking/imu_fusion: True
 * /zed/zed_node/tracking/init_odom_with_first_valid_pose: True
 * /zed/zed_node/tracking/initial_base_pose: [0.0, 0.0, 0.0, 0...
 * /zed/zed_node/tracking/map_frame: map
 * /zed/zed_node/tracking/odometry_db:
 * /zed/zed_node/tracking/odometry_frame: odom
 * /zed/zed_node/tracking/odometry_topic: odom
 * /zed/zed_node/tracking/path_max_count: -1
 * /zed/zed_node/tracking/path_pub_rate: 2.0
 * /zed/zed_node/tracking/pose_topic: pose
 * /zed/zed_node/tracking/publish_map_tf: True
 * /zed/zed_node/tracking/publish_pose_covariance: True
 * /zed/zed_node/tracking/publish_tf: True
 * /zed/zed_node/tracking/spatial_memory: True
 * /zed/zed_node/tracking/two_d_mode: False
 * /zed/zed_node/tracking/world_frame: map
 * /zed/zed_node/video/color_enhancement: True
 * /zed/zed_node/video/left_topic_root: left
 * /zed/zed_node/video/rgb_topic_root: rgb
 * /zed/zed_node/video/right_topic_root: right
 * /zed/zed_node/video/stereo_topic_root: stereo

NODES
  /zed/
    zed_node (zed_wrapper/zed_wrapper_node)
    zed_state_publisher (robot_state_publisher/robot_state_publisher)

ROS_MASTER_URI=http://localhost:11311

process[zed/zed_state_publisher-1]: started with pid [25940]
process[zed/zed_node-2]: started with pid [25941]
[ INFO] [1569895975.761048655]: Initializing nodelet with 4 worker threads.
[ INFO] [1569895976.422711237]: SDK version : 2.8.2
[ INFO] [1569895976.422846293]: *** PARAMETERS ***
[ INFO] [1569895976.423955955]:  * Camera Resolution            -> HD720
[ INFO] [1569895976.425000356]:  * Camera Framerate             -> 30
[ INFO] [1569895976.425914128]:  * Gpu ID                       -> -1
[ INFO] [1569895976.426776129]:  * Camera ID                    -> -1
[ INFO] [1569895976.427669223]:  * Verbose                      -> ENABLED
[ INFO] [1569895976.429337702]:  * Camera Flip                  -> DISABLED
[ INFO] [1569895976.431133370]:  * Self calibration             -> ENABLED
[ INFO] [1569895976.432922945]:  * Camera Model                 -> zedm
[ INFO] [1569895976.445124390]:  * Depth quality                -> PERFORMANCE
[ INFO] [1569895976.446152019]:  * Depth Sensing mode           -> STANDARD
[ INFO] [1569895976.447207618]:  * OpenNI mode                  -> DISABLED
[ INFO] [1569895976.448155922]:  * Depth Stabilization          -> ENABLED
[ INFO] [1569895976.449146311]:  * Minimum depth                -> 0.1
[ INFO] [1569895976.452845099]:  * Path rate                    -> 2 Hz
[ INFO] [1569895976.453764080]:  * Path history size            -> 1
[ INFO] [1569895976.455494018]:  * Odometry DB path             ->
[ INFO] [1569895976.457122287]:  * Spatial Memory               -> ENABLED
[ INFO] [1569895976.458715764]:  * IMU Fusion                   -> ENABLED
[ INFO] [1569895976.460377835]:  * Floor alignment              -> DISABLED
[ INFO] [1569895976.462000167]:  * Init Odometry with first valid pose data -> ENABLED
[ INFO] [1569895976.463637707]:  * Two D mode                   -> DISABLED
[ INFO] [1569895976.465784843]:  * Publish Pose Covariance      -> ENABLED
[ INFO] [1569895976.466676844]:  * Fixed covariance             -> DISABLED
[ INFO] [1569895976.467637232]:  * Fixed cov. value             -> 1e-06
[ INFO] [1569895976.469247271]:  * Mapping                      -> DISABLED
[ INFO] [1569895976.471394042]:  * IMU timestamp sync           -> DISABLED
[ INFO] [1569895976.472298335]:  * IMU data freq                -> 100 Hz
[ INFO] [1569895976.474581516]:  * SVO REC compression          -> HEVC (H265)
[ INFO] [1569895976.488895251]:  * world_frame                  -> map
[ INFO] [1569895976.488970045]:  * map_frame                    -> map
[ INFO] [1569895976.489036192]:  * odometry_frame               -> odom
[ INFO] [1569895976.489109527]:  * base_frame                   -> base_link
[ INFO] [1569895976.489160727]:  * camera_frame                 -> zed_camera_center
[ INFO] [1569895976.489209270]:  * imu_link                     -> zed_imu_link
[ INFO] [1569895976.489255625]:  * left_camera_frame            -> zed_left_camera_frame
[ INFO] [1569895976.489305886]:  * left_camera_optical_frame    -> zed_left_camera_optical_frame
[ INFO] [1569895976.489355627]:  * right_camera_frame           -> zed_right_camera_frame
[ INFO] [1569895976.489402191]:  * right_camera_optical_frame   -> zed_right_camera_optical_frame
[ INFO] [1569895976.489456984]:  * depth_frame                  -> zed_left_camera_frame
[ INFO] [1569895976.489519902]:  * depth_optical_frame          -> zed_left_camera_optical_frame
[ INFO] [1569895976.489572612]:  * disparity_frame              -> zed_left_camera_frame
[ INFO] [1569895976.489618446]:  * disparity_optical_frame      -> zed_left_camera_optical_frame
[ INFO] [1569895976.489672093]:  * confidence_frame             -> zed_left_camera_frame
[ INFO] [1569895976.489718969]:  * confidence_optical_frame     -> zed_left_camera_optical_frame
[ INFO] [1569895976.491582088]:  * Broadcast odometry TF        -> ENABLED
[ INFO] [1569895976.493155929]:  * Broadcast map pose TF        -> ENABLED
[ INFO] [1569895976.493978969]:  * [DYN] mat_resize_factor      -> 1
[ INFO] [1569895976.494773312]:  * [DYN] confidence             -> 100
[ INFO] [1569895976.495622083]:  * [DYN] max_depth              -> 10
[ INFO] [1569895976.496407466]:  * [DYN] exposure               -> 100
[ INFO] [1569895976.497172173]:  * [DYN] gain                   -> 100
[ INFO] [1569895976.497922243]:  * [DYN] auto_exposure          -> ENABLED
[ INFO] [1569895976.498705335]:  * [DYN] point_cloud_freq       -> 10 Hz
[ INFO] [1569895976.508737559]:  * Camera coordinate system     -> COORDINATE_SYSTEM_RIGHT_HANDED_Z_UP_X_FWD
ZED (Init) >> Depth mode: PERFORMANCE
ZED (Init) >> Video mode: HD720@30
[ INFO] [1569895979.038281282]: ZED connection -> SUCCESS
[ INFO] [1569895981.038694575]:  * CAMERA MODEL  -> ZED-M
[ INFO] [1569895981.038799525]:  * Serial Number -> 10027677
[ INFO] [1569895981.038854474]:  * FW Version    -> 1523
[ INFO] [1569895982.235600305]: Advertised on topic /zed/zed_node/rgb/image_rect_color
[ INFO] [1569895982.236539911]: Advertised on topic /zed/zed_node/rgb/camera_info
[ INFO] [1569895982.286610875]: Advertised on topic /zed/zed_node/stereo/image_rect_color
[ INFO] [1569895982.288291645]: Advertised on topic /zed/zed_node/pose
[ INFO] [1569895982.289720899]: Advertised on topic /zed/zed_node/pose_with_covariance
[ INFO] [1569895982.291031087]: Advertised on topic /zed/zed_node/odom
[ INFO] [1569895982.292678680]: Advertised on topic /zed/zed_node/path_odom
[ INFO] [1569895982.294187935]: Advertised on topic /zed/zed_node/path_map
[ INFO] [1569895982.295910269]: Advertised on topic /zed/zed_node/imu/data @ 100 Hz
[ INFO] [1569895982.297482495]: Advertised on topic /zed/zed_node/imu/data_raw @ 100 Hz
[ INFO] [1569895982.309392578]: Static transform Sensor to Base [zed_left_camera_frame -> base_link]
[ INFO] [1569895982.309493466]:  * Translation: {0.000,-0.030,0.000}
[ INFO] [1569895982.309556384]:  * Rotation: {0.000,-0.000,0.000}
[ INFO] [1569895982.309646699]: Static transform Sensor to Camera Center [zed_left_camera_frame -> zed_camera_center]
[ INFO] [1569895982.309712951]:  * Translation: {0.000,-0.030,0.000}
[ INFO] [1569895982.309762014]:  * Rotation: {0.000,-0.000,0.000}
[ INFO] [1569895982.309839204]: Static transform Camera Center to Base [zed_camera_center -> base_link]
[ INFO] [1569895982.309887434]:  * Translation: {0.000,0.000,0.000}
[ INFO] [1569895982.309932487]:  * Rotation: {0.000,-0.000,0.000}

cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ rosnode list
/rosout
/zed/zed_node
/zed/zed_state_publisher

With trimmed zed node
---------------------
cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ rostopic list
/diagnostics
/rosout
/rosout_agg
/tf
/tf_static
/zed/joint_states
/zed/zed_node/imu/data
/zed/zed_node/imu/data_raw
/zed/zed_node/odom
/zed/zed_node/parameter_descriptions
/zed/zed_node/parameter_updates
/zed/zed_node/path_map
/zed/zed_node/path_odom
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


With full zed node
------------------
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


cs18resch01001@nano-ub18:~$ rostopic list | grep -i imu
/zed/zed_node/imu/data
/zed/zed_node/imu/data_raw

```

By Slamtec RPLidar:

```
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
```
