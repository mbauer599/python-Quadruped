#!/bin/python
# Written by Michael Bauer, from examples found around the interwebs.

############################
######### Includes #########
############################

# Library for Raspberry Pi GPIO
import RPi.GPIO as GPIO

from __future__ import division
import time

# Library for I2C control
import Adafruit_PCA9685

############################
##### Global Variables #####
############################
# Ammount of free space to be allowed in the sensor direction in cm
stop_dist = 4

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

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

############################

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Function to return distance
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    return distance
    
# Helper function to take one full step forward.
def one_step_forward():
    pwm.set_pwm(channel_FR1B, 0, servo_max)
    pwm.set_pwm(channel_RL3B, 0, servo_max)
    pwm.set_pwm(channel_FR1A, 0, servo_max)
    pwm.set_pwm(channel_RL3A, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(channel_FR1B, 0, servo_min)
    pwm.set_pwm(channel_RL3B, 0, servo_min)
    pwm.set_pwm(channel_FR1A, 0, servo_min)
    pwm.set_pwm(channel_RL3A, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(channel_FL4B, 0, servo_max)
    pwm.set_pwm(channel_RR2B, 0, servo_max)
    pwm.set_pwm(channel_FL4A, 0, servo_max)
    pwm.set_pwm(channel_RR2A, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(channel_FL4B, 0, servo_min)
    pwm.set_pwm(channel_RR2B, 0, servo_min)
    pwm.set_pwm(channel_FL4A, 0, servo_min)
    pwm.set_pwm(channel_RR2A, 0, servo_min)
    time.sleep(1)
    
print('Walking, press Ctrl-C to quit...')
while True:
    # Determine open distance
    dist = distance()

    # If there's nothing there, take a step forward
    if dist > 4:
        one_step_forward():
        print ("Moving Forward")
    
