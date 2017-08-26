#!/bin/bash -eu

# MIT License (C) 2017 Tiryoh<tiryoh@gmail.com>
# https://tiryoh.mit-license.org

[ -e /usr/src/linux-headers-`uname -r` ] || { sudo apt-get update; sudo apt-get install -y raspberrypi-kernel-headers; }
[ -e $HOME/RaspberryPiMouse ] && { cd $HOME/RaspberryPiMouse; git pull; } || { cd $HOME; git clone https://github.com/rt-net/RaspberryPiMouse.git; }
cd $HOME/RaspberryPiMouse/src/drivers
make
sudo make install
