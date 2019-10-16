# Chinkara 

Chinkara - Donkeycar is a toy car based ADV research platform at CANDLE Research Lab, IIT Hyderbad.

## Hardware used :

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

## Software used :

* Nvidia Jetpack 4.2 / Ubuntu 18 on Jetson Nano
* Ubuntu 18 on Raspberry PI 3B
* Gnu C++ 11
* Python 3.6
* Robot Operating System (ROS) Melodic for Ubuntu 18


## Procudure to Build & Run :


```
$ git clone https://github.com/iithcandle/chinkara --recurse-submodules
$ cd chinkara/src
$ catkin_init_workspace
$ cd ..
$ catkin_build
$ source /opt/ros/melodic/setup.bash
$ source devel/setup.bash
$ roslaunch donkeycar donkeycar_nano_manual.launch
```

## Citation
```
@techreport { ref114,
	title            = "Hardware-Software Stack for an RC car for testing autonomous driving algorithms",
	year             = "2019",
	author           = "Kakul Shrivastava and Maruthi Inukonda and Sparsh Mittal",
	institution      = "IIT Hyderabad",
	number           = "2019-CSE-CANDLE-01",
	doi              = "10.13140/RG.2.2.14768.30728",
	url              = "https://www.researchgate.net/publication/336411476_Hardware-Software_Stack_for_an_RC_car_for_testing_autonomous_driving_algorithms",
	abstract         = "In this paper, we report our ongoing work on developing hardware and software support for a toy RC car.
	                    This toy car can be used as a platform for evaluating algorithms and accelerators for autonomous driving
						vehicles (ADVs). We describe different sensors and actuators used and interfacing of them with two processors,
						viz., Jetson Nano and Raspberry Pi. Where possible, we have used ROS nodes for interfacing.  We discuss the
						advantages and limitations of different sensors and processors and issues related to their compatibility.
						We include both software (e.g., python code, linux commands) and hardware (e.g., pin configuration) information
						which will be useful for reproducing the experiments. This paper will be useful for robotics enthusiasts
						and researchers in the area of  autonomous driving. "}
```

## Disclaimer

This code published is work-in-progress, and shared under AGPLv3 (no warranty, no guarantee).
Any issues reported will be fixed on best-effort basis.
