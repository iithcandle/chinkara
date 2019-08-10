#!/usr/bin/env python

#
# Copyright (C) 2018-2019 Maruthi Seshidhar Inukonda - All Rights Reserved.
# maruthi.inukonda@gmail.com
#
# This file is released under the GPLv3 License.
#

import rospy
from sensor_msgs.msg import Joy
from servo_motor_controller import ServoMotorController

class DonkeyCarManualDriver:
    const_throttle = rospy.get_param("/CONST_THROTTLE")
    #Steering constants
    max_left_angle = rospy.get_param("/MAX_LEFT_ANGLE")
    min_right_angle = rospy.get_param("/MIN_RIGHT_ANGLE")
    max_steering_pulse = rospy.get_param("/MAX_STEERING_PULSE")
    min_steering_pulse = rospy.get_param("/MIN_STEERING_PULSE")
    start_recording  = rospy.get_param("/START_RECORDING")
    steering_channel = rospy.get_param("/STEERING_CHANNEL")

    #Throttle constants
    min_throttle = rospy.get_param("/MIN_THROTTLE")
    max_throttle = rospy.get_param("/MAX_THROTTLE")
    zero_pulse = rospy.get_param("/ZERO_PULSE")
    min_throttle_pulse = rospy.get_param("/MIN_THROTTLE_PULSE")
    max_throttle_pulse = rospy.get_param("/MAX_THROTTLE_PULSE")
    throttle_channel = rospy.get_param("/THROTTLE_CHANNEL")
    max_reverse_throttle = rospy.get_param("/MAX_REVERSE_THROTTLE")
    const_throttle_step = rospy.get_param("/CONST_THROTTLE_STEP")

    def __init__(self):
        # Initialize the Servo Motor Controller
        self.const_throttle = rospy.get_param("/CONST_THROTTLE")
        self.smc = ServoMotorController()

    def getActuatorPulseValue(self, joystickValue, joystickMin, joystickMax, actuatorMin, actuatorMax, channel_type='steering'):
        #Linear mapping between two ranges of values
        joystickRange = joystickMax - joystickMin
        actuatorRange = actuatorMax - actuatorMin

        joystickActuatorRatio = float(joystickRange)/float(actuatorRange)
        actuatorValue = int((joystickValue - joystickMin) / joystickActuatorRatio + actuatorMin)	   
        if channel_type == 'steering':
            actuatorValue +=18

        return actuatorValue

    def find_max_throttle(self, throttle_pulse):
        throttle = self.const_throttle
        if throttle_pulse <= self.const_throttle:
            throttle = throttle_pulse
        if throttle_pulse < self.max_reverse_throttle:
            throttle = self.max_reverse_throttle

        return throttle

    def joyStickSubscriberCallback(self, msg):
        rospy.loginfo("Received len(axes):%d", len(msg.axes)) # 8
        rospy.loginfo("Received len(buttons):%d", len(msg.buttons)) #11
        '''
        Received:['__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__getattribute__', '__getstate__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_check_types', '_connection_header', '_full_text', '_get_types', '_has_header', '_md5sum', '_slot_types', '_type', 'axes', 'buttons', 'deserialize', 'deserialize_numpy', 'header', 'serialize', 'serialize_numpy']
        '''
        steering_pulse = self.getActuatorPulseValue(float(msg.axes[0]), self.min_right_angle, self.max_left_angle, self.min_steering_pulse, self.max_steering_pulse, channel_type='steering')
        throttle_pulse = self.find_max_throttle(float(msg.axes[3]))
        throttle_pulse = self.getActuatorPulseValue(throttle_pulse, self.min_throttle, self.max_throttle, self.min_throttle_pulse, self.max_throttle_pulse, channel_type='throttle')
        self.smc.set_channel_pulse(self.steering_channel, pulse=steering_pulse)
        self.smc.set_channel_pulse(self.throttle_channel, pulse=throttle_pulse)
        rospy.loginfo('Steering value: %s', steering_pulse)
        rospy.loginfo('Throttle value: %s', throttle_pulse)
        #rospy.loginfo('Maximum throttle value: %s', self.const_throttle)
        #rospy.loginfo('Joystic throttle value: %s', data.axes[3])

if __name__ == '__main__':
    driver = DonkeyCarManualDriver()
    rospy.init_node('manual_drive_node')
    rospy.loginfo("[ROS manual_drive_node] started.")

    rospy.Subscriber('/joy', Joy, driver.joyStickSubscriberCallback, queue_size=1)

    rospy.spin()

