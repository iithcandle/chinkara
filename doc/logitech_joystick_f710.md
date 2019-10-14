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

