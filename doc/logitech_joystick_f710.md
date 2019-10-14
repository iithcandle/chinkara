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

cs18resch01001@nano-ub18:~$ rostopic echo -n 8 /joy
header: 
  seq: 1
  stamp: 
    secs: 1571043170
    nsecs: 432888706
  frame_id: ''
axes: [0.0, -0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---
header: 
  seq: 2
  stamp: 
    secs: 1571043172
    nsecs: 171927397
  frame_id: ''
axes: [0.0, -0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
---
header: 
  seq: 3
  stamp: 
    secs: 1571043172
    nsecs: 443941147
  frame_id: ''
axes: [0.0, -0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---
header: 
  seq: 4
  stamp: 
    secs: 1571043198
    nsecs: 786762459
  frame_id: ''
axes: [0.0, -0.0, 0.0, -1.0, 0.07223731279373169, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---
header: 
  seq: 5
  stamp: 
    secs: 1571043198
    nsecs: 862758406
  frame_id: ''
axes: [0.0, -0.0, 0.0, -1.0, 0.10551854968070984, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---
header: 
  seq: 6
  stamp: 
    secs: 1571043198
    nsecs: 882795025
  frame_id: ''
axes: [0.0, -0.0, 0.0, -1.0, 0.13047948479652405, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---
header: 
  seq: 7
  stamp: 
    secs: 1571043198
    nsecs: 886806797
  frame_id: ''
axes: [0.0, -0.0, 0.0, -1.0, 0.17208102345466614, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---
header: 
  seq: 8
  stamp: 
    secs: 1571043198
    nsecs: 970816600
  frame_id: ''
axes: [0.0, -0.0, 0.0, -1.0, 0.13047948479652405, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---
header: 
  seq: 9
  stamp: 
    secs: 1571043198
    nsecs: 978774515
  frame_id: ''
axes: [0.0, -0.0, 0.0, -1.0, 0.12215916812419891, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---
header: 
  seq: 10
  stamp: 
    secs: 1571043198
    nsecs: 986762484
  frame_id: ''
axes: [0.0, -0.0, 0.0, -1.0, 0.10551854968070984, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---
header: 
  seq: 11
  stamp: 
    secs: 1571043198
    nsecs: 994774517
  frame_id: ''
axes: [0.0, -0.0, 0.0, -1.0, 0.0971982404589653, 0.0, 0.0, 0.0]
buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
---

```
