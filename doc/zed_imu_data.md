ZED Stereo camera's /zed/zed_node/imu/data topic:

```
cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ rostopic hz /zed/zed_node/imu/data
subscribed to [/zed/zed_node/imu/data]
average rate: 99.972
        min: 0.009s max: 0.010s std dev: 0.00043s window: 95
average rate: 100.017
        min: 0.009s max: 0.011s std dev: 0.00044s window: 196
average rate: 99.986
        min: 0.009s max: 0.011s std dev: 0.00044s window: 296
average rate: 99.987
        min: 0.009s max: 0.011s std dev: 0.00044s window: 396
average rate: 99.994
        min: 0.009s max: 0.011s std dev: 0.00044s window: 496
average rate: 99.989
        min: 0.009s max: 0.011s std dev: 0.00044s window: 596
^Caverage rate: 99.994
        min: 0.009s max: 0.011s std dev: 0.00044s window: 651


cs18resch01001@nano-ub18:~/AllCode/Maruthi/chinkara/donkeycar_1906$ rostopic echo /zed/zed_node/imu/data | head -100                                                   
header:                                                                                                                                                                
  seq: 652                                                                                                                                                             
  stamp:                                                                                                                                                               
    secs: 1569896827                                                                                                                                                   
    nsecs: 538063849                                                                                                                                                   
  frame_id: "zed_imu_link"                                                                                                                                             
orientation:                                                                                                                                                           
  x: -0.0300474036485                                                                                                                                                  
  y: 0.0608215257525                                                                                                                                                   
  z: 0.000937639852054                                                                                                                                                 
  w: 0.997695863247                                                                                                                                                    
orientation_covariance: [0.0012802617878014295, 0.0001974645806649034, 5.7539290532412e-05, 0.0001974645988215175, 0.0019294516701135376, 0.0001977947223790398, 5.7539
28145410495e-05, 0.0001977947223790398, 0.0012747551046250007]                                                                                                         
angular_velocity:                                                                                                                                                      
  x: -0.01597896698                                                                                                                                                    
  y: -0.00639158679199                                                                                                                                                 
  z: 0.012783173584                                                                                                                                                    
angular_velocity_covariance: [4.67164120267826e-06, 0.0, 0.0, 0.0, 4.2504259122283575e-06, 0.0, 0.0, -0.0, 5.530521675950478e-06]                                      
linear_acceleration:                                                                                                                                                   
  x: -1.18181586266                                                                                                                                                    
  y: -0.594503700733                                                                                                                                                   
  z: 9.88602161407                                                                                                                                                     
linear_acceleration_covariance: [0.002115716924890876, 0.0, 0.0, 0.0, 0.0010369346709921956, 0.0, 0.0, -0.0, 0.0173085518181324]                                       
---                                                                                                                                                                    
header:                                                                                                                                                                
  seq: 653                               

```
