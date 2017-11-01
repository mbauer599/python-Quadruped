# Python-Quadruped
A project to create working python code for a Quadruped with a Raspberry Pi Zero or Zero W as the control board.

The aim is to use a Raspberry Pi Zero (or Zero W), a pwm expansion board and a forward facing distance sensor to program a Quadruped for autonomous movement. The movement will follow the right-hand rule to navigate an entire room (or space), acomplish object avoidance (in the forward facing space), and the intention is to eventually use this data to create a basic text map of a space.

# Hardware
* The frame used for this project is a 3d-printed quadruped, FatKame by Blomdoft, [which may be found on thingiverse](https://www.thingiverse.com/thing:1483635). I do not own nor maintain the Kame projects on thingiverse. There are plenty of re-mixes/re-designes out there, as well as alternatives.
* The control board used is a Raspberry Pi Zero with a WiFi dongle. A Pi 2/3/Zero W could be used interchangably, this is just what I had on hand.
* The pwm expansion board is a [16 channel Adafruit I2C interface module](https://www.adafruit.com/product/815).
* The distance sensor used is a [Ultrasonic Module HC-SR04](https://www.sparkfun.com/products/13959).
* The servos user are [SG90 Micro Servo Motor 9G](https://www.amazon.com/gp/product/B00X7CJZWM/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1). Two per leg for a total of 8 servos.

# Servo Mapping
* The Servos are mapped in a clock pattern, with 12'oclock facing forward with the quadruped. The primary servo is designated as 'A' while the secondary (leg) servo is designated as 'B'.
* Front Right Servos: 1A/1B
* Rear Right Servos: 2A/2B
* Rear Left Servos: 3A/3B
* Front Left Servos: 4A/4B

# Credits and Resources


