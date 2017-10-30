#!/bin/python
# Written by Michael Bauer, from examples found around the interwebs.

############################
######### Includes #########
############################

from __future__ import division
import time

import Adafruit_PCA9685

############################
##### Global Variables #####
############################
# Servo Mappings
# Front Right Servos: 1A/1B Channel: 0/4
channel_FR1A = 0
channel_FR1B = 4
# Rear Right Servos: 2A/2B  Channel: 1/5
channel_RR2A = 1
channel_RR2B = 5
# Rear Left Servos: 3A/3B   Channel: 2/6
channel_RL3A = 2
channel_RL3B = 6
# Front Left Servos: 4A/4B  Channel: 3/7
channel_FL4A = 0
channel_FL4B = 4

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
############################
