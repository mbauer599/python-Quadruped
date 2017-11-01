#!/bin/bash
# Simple script to install all dependencies and get up and going. 

# Make sure we're root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Update the host system
apt-get update > /dev/null

# Update the pi
rpi-update > /dev/null

