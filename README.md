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



