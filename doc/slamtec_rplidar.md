# By Slamtec RPLidar:

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

