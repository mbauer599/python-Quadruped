# Python-Quadruped
A project to create working python code for a Quadruped with a Raspberry Pi Zero or Zero W as the control board.

The aim is to use a Raspberry Pi Zero (or Zero W), a pwm expansion board and a forward facing distance sensor to program a Quadruped for autonomous movement. The movement will follow the right-hand rule to navigate an entire room (or space), acomplish object avoidance (in the forward facing space), and the intention is to eventually use this data to create a basic text map of a space.

# Hardware
* The frame used for this project is a 3d-printed quadruped, FatKame by Blomdoft, [which may be found on thingiverse](https://www.thingiverse.com/thing:1483635). I do not own nor maintain the Kame projects on thingiverse. There are plenty of re-mixes/re-designes out there, as well as alternatives.
* The control board used is a Raspberry Pi Zero with a WiFi dongle. A Pi 2/3/Zero W could be used interchangably, this is just what I had on hand.
* The pwm expansion board is a [16 channel Adafruit I2C interface module](https://www.adafruit.com/product/815).
