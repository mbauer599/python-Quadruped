# Python-Quadruped
A project to create working python code for a eight servo Quadruped (two servos per leg) with a Raspberry Pi Zero or Zero W as the control board. This project is not complete and has not been tested.

The aim is to use a Raspberry Pi Zero (or Zero W), a pwm expansion board and a forward facing distance sensor to program a Quadruped for autonomous movement. The movement will follow the right-hand rule to navigate an entire room (or space), acomplish object avoidance (in the forward facing space), and the intention is to eventually use this data to create a basic text map of a space.

If you're new to drones or coding, I would highly encourage the research before you get into a project like this, although it's a lot of fun and a good chance to learn. Personally, I would highly recommend against a quadcopter or flying vehicle as a first project. While it may look more fun and exciting, you do sacrifice stability and longevity for maneuverability so just keep that in mind. It’s also a lot easier to crash a flying vehicle :P.

# Hardware
* The frame used for this project is a 3d-printed quadruped, FatKame by Blomdoft, [which may be found on thingiverse](https://www.thingiverse.com/thing:1483635). I do not own nor maintain the Kame projects on thingiverse. There are plenty of re-mixes/re-designes out there, as well as alternatives if this specific project isn't your cup of nice warm tea.
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
* [Adafruit Python Project](https://github.com/adafruit/Adafruit_Python_PCA9685)
* [FatKame by Blomdoft](https://github.com/Blomdoft/fatKame)
* [16 channel Adafruit Tutorial](https://cdn-learn.adafruit.com/downloads/pdf/16-channel-pwm-servo-driver.pdf)
* [Ultrasonic Sensor Tutorial](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)

# Disclaimer
This project comes with no waranty and the owners do not claim to own or maintain any refrenced projects. Use at your own risk.
