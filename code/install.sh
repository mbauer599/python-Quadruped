#!/bin/bash
# Simple script to install all dependencies and get up and going. 

# Make sure we're root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Update the host system
echo "Updating Package Lists..."
if apt-get update > /dev/null; then
    echo "Done"
else
    echo "Failed Task. Exiting"
    exit 1
fi

# Update the pi
echo "Updating Raspberry Pi..."
if rpi-update > /dev/null; then
    echo "Done"
else
    echo "Failed Task. Exiting"
    exit 1
fi

# Install build-essential
echo "Installing build-essential..."
if apt-get install build-essential -y > /dev/null; then
    echo "Done"
else
    echo "Failed Task. Exiting"
    exit 1
fi

# Install python-dev
echo "python-dev..."
if apt-get install python-dev -y > /dev/null; then
    echo "Done"
else
    echo "Failed Task. Exiting"
    exit 1
fi

# Install python-smbus
echo "python-smbus..."
if apt-get install python-smbus -y > /dev/null; then
    echo "Done"
else
    echo "Failed Task. Exiting"
    exit 1
fi

# Install PWM Expansion Board Requirements
echo "i2c-tools..."
if apt-get install i2c-tools -y > /dev/null; then
    echo "Done"
else
    echo "Failed Task. Exiting"
    exit 1
fi
