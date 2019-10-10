#!/usr/bin/env python

#
# Copyright (C) 2018-2019 Maruthi Seshidhar Inukonda - All Rights Reserved.
# maruthi.inukonda@gmail.com
#
# This file is released under the Affero GPLv3 License.
#

import rospy
import Adafruit_PCA9685

class ServoMotorController:
    def __init__(self):
        # Initialize the Servo Motor Controller hardware
        self.freq = 60
        self.channel = 1
        self.pulse = 420
        self.pwm = Adafruit_PCA9685.PCA9685()

        self.pwm.set_pwm_freq(self.freq)

    def set_frequency(self, freq=60):
        self.freq = freq
        self.pwm.set_pwm_freq(freq)

    def set_channel_pulse(self, channel=1, pulse=420):
        self.channel = channel
        self.pulse = pulse
        self.pwm.set_pwm(channel, 0, pulse)

if __name__ == '__main__':
    smc = ServoMotorController()
    
