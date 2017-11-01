#!/bin/bash
# Simple script to install all dependencies and get up and going. 

# Make sure we're root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Update the host system
echo "Updating Package Lists.."
if apt-get update > /dev/null; then
    echo "Done"
else
    echo "Failed Task. Exiting"
    exit 1
fi

echo "Updating Package Lists.."
apt-get update > /dev/null

# Update the pi
rpi-update > /dev/null

