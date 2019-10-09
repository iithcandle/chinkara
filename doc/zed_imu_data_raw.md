ZED Stereo camera's /zed/zed_node/imu/data_raw topic:

```
cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ rostopic hz /zed/zed_node/imu/data_raw
subscribed to [/zed/zed_node/imu/data_raw]
average rate: 100.001
        min: 0.009s max: 0.011s std dev: 0.00044s window: 95
average rate: 99.986
        min: 0.009s max: 0.011s std dev: 0.00044s window: 195
average rate: 99.986
        min: 0.009s max: 0.011s std dev: 0.00044s window: 295
average rate: 99.997
        min: 0.009s max: 0.011s std dev: 0.00044s window: 395
average rate: 100.002
        min: 0.009s max: 0.011s std dev: 0.00044s window: 495
average rate: 99.994
        min: 0.009s max: 0.011s std dev: 0.00044s window: 595
average rate: 99.998
        min: 0.009s max: 0.011s std dev: 0.00044s window: 695
^Caverage rate: 99.992
        min: 0.009s max: 0.011s std dev: 0.00044s window: 725

cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ rostopic echo /zed/zed_node/imu/data_raw | head -100         
header:             
  seq: 827                                                                                                                      
  stamp:            
    secs: 1569896768
    nsecs: 933455811                                                                                                            
  frame_id: "zed_imu_link"
orientation:        
  x: 0.0            
  y: 0.0                  
  z: 0.0            
  w: 0.0            
orientation_covariance: [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
angular_velocity:
  x: -0.0117179091187
  y: -0.0106526446533                                                 
  z: 0.00852211572266
angular_velocity_covariance: [4.67164120267826e-06, 0.0, 0.0, 0.0, 4.2504259122283575e-06, 0.0, 0.0, -0.0, 5.530521675950478e-06]
linear_acceleration:
  x: -1.21297931671
  y: -0.642447531223
  z: 9.89560985565
linear_acceleration_covariance: [0.002115716924890876, 0.0, 0.0, 0.0, 0.0010369346709921956, 0.0, 0.0, -0.0, 0.0173085518181324]
---
header:
 seq: 828
```
