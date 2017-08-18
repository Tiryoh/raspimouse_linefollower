#!/bin/bash -eu

[ -e /usr/src/linux-headers-`uname -r` ] || { sudo apt-get update; sudo apt-get install -y raspberrypi-kernel-headers; }
[ -e $HOME/RaspberryPiMouse ] && { cd $HOME/RaspberryPiMouse; git pull; } || { cd $HOME; git clone https://github.com/rt-net/RaspberryPiMouse.git; }
cd $HOME/RaspberryPiMouse/src/drivers
make
sudo make install
